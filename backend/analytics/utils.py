"""Shared analytics computation utilities."""
from datetime import timedelta

from django.db.models import Sum
from django.utils import timezone
from rest_framework.exceptions import ValidationError


def parse_days_param(request, default=30, max_days=365):
    """Parse and validate the 'days' query parameter."""
    raw = request.query_params.get("days", default)
    try:
        days = max(1, min(int(raw), max_days))
    except (ValueError, TypeError):
        raise ValidationError({"days": "Must be a positive integer."})
    return days


def aggregate_metrics(queryset):
    """Aggregate metric snapshots into a summary dict."""
    agg = queryset.aggregate(
        impressions=Sum("impressions"),
        clicks=Sum("clicks"),
        conversions=Sum("conversions"),
        spend=Sum("spend"),
        revenue=Sum("revenue"),
    )
    return {
        "impressions": int(agg["impressions"] or 0),
        "clicks": int(agg["clicks"] or 0),
        "conversions": int(agg["conversions"] or 0),
        "spend": float(agg["spend"] or 0),
        "revenue": float(agg["revenue"] or 0),
    }


def calculate_trend(current, previous):
    """Calculate trend direction and percentage change between two values."""
    if current is None or previous is None:
        return {"direction": "neutral", "change_pct": 0.0}
    if previous == 0:
        return {"direction": "up" if current > 0 else "neutral", "change_pct": 0.0}
    pct = round(((current - previous) / abs(previous)) * 100, 1)
    if pct > 0:
        direction = "up"
    elif pct < 0:
        direction = "down"
    else:
        direction = "neutral"
    return {"direction": direction, "change_pct": pct}


def compute_derived_metrics(metrics):
    """Compute CTR, CPA, ROAS, CPC, conversion_rate from raw aggregates."""
    imp = metrics["impressions"]
    clicks = metrics["clicks"]
    conv = metrics["conversions"]
    spend = metrics["spend"]
    revenue = metrics["revenue"]

    return {
        "ctr": round((clicks / imp) * 100, 2) if imp else None,
        "cpa": round(spend / conv, 2) if conv else None,
        "roas": round(revenue / spend, 2) if spend else None,
        "cpc": round(spend / clicks, 2) if clicks else None,
        "conversion_rate": round((conv / clicks) * 100, 2) if clicks else None,
    }


def compute_analytics_with_trends(current, previous=None):
    """Compute full analytics result with optional trend comparison."""
    derived = compute_derived_metrics(current)
    result = {**current, **derived}

    if previous and any(v for v in previous.values()):
        prev_derived = compute_derived_metrics(previous)
        result["trends"] = {
            "ctr": calculate_trend(derived["ctr"], prev_derived["ctr"]),
            "cpa": calculate_trend(derived["cpa"], prev_derived["cpa"]),
            "roas": calculate_trend(derived["roas"], prev_derived["roas"]),
            "cpc": calculate_trend(derived["cpc"], prev_derived["cpc"]),
            "conversion_rate": calculate_trend(derived["conversion_rate"], prev_derived["conversion_rate"]),
            "spend": calculate_trend(current["spend"], previous["spend"]),
            "revenue": calculate_trend(current["revenue"], previous["revenue"]),
            "impressions": calculate_trend(current["impressions"], previous["impressions"]),
            "clicks": calculate_trend(current["clicks"], previous["clicks"]),
        }
    else:
        result["trends"] = None

    return result


def get_period_querysets(queryset, days=30):
    """Return (current_qs, previous_qs) for a given number of days."""
    now = timezone.now().date()
    current_start = now - timedelta(days=days)
    previous_start = current_start - timedelta(days=days)

    current_qs = queryset.filter(date__gte=current_start, date__lte=now)
    previous_qs = queryset.filter(date__gte=previous_start, date__lt=current_start)

    return current_qs, previous_qs
