def calculate_ctr(impressions: int, clicks: int) -> float | None:
    """Click-through rate as a percentage."""
    if not impressions:
        return None
    return round((clicks / impressions) * 100, 2)


def calculate_cpa(spend: float, conversions: int) -> float | None:
    """Cost per acquisition."""
    if not conversions:
        return None
    return round(spend / conversions, 2)


def calculate_roas(revenue: float, spend: float) -> float | None:
    """Return on ad spend."""
    if not spend:
        return None
    return round(revenue / spend, 2)


def calculate_cpc(spend: float, clicks: int) -> float | None:
    """Cost per click."""
    if not clicks:
        return None
    return round(spend / clicks, 2)


def calculate_conversion_rate(clicks: int, conversions: int) -> float | None:
    """Conversion rate as a percentage."""
    if not clicks:
        return None
    return round((conversions / clicks) * 100, 2)


def calculate_trend(current: float | None, previous: float | None) -> dict:
    """Compare current vs previous period and return trend info."""
    if current is None or previous is None:
        return {"direction": "neutral", "change_pct": 0.0}
    if previous == 0:
        direction = "up" if current > 0 else "neutral"
        return {"direction": direction, "change_pct": 0.0}
    change_pct = round(((current - previous) / abs(previous)) * 100, 1)
    if change_pct > 0:
        direction = "up"
    elif change_pct < 0:
        direction = "down"
    else:
        direction = "neutral"
    return {"direction": direction, "change_pct": change_pct}


def compute_campaign_analytics(current_period: dict, previous_period: dict | None = None) -> dict:
    """Compute all analytics for a campaign given aggregated metric data.

    Each period dict should have: impressions, clicks, conversions, spend, revenue
    """
    ctr = calculate_ctr(current_period["impressions"], current_period["clicks"])
    cpa = calculate_cpa(current_period["spend"], current_period["conversions"])
    roas = calculate_roas(current_period["revenue"], current_period["spend"])
    cpc = calculate_cpc(current_period["spend"], current_period["clicks"])
    conv_rate = calculate_conversion_rate(current_period["clicks"], current_period["conversions"])

    result = {
        "impressions": current_period["impressions"],
        "clicks": current_period["clicks"],
        "conversions": current_period["conversions"],
        "spend": current_period["spend"],
        "revenue": current_period["revenue"],
        "ctr": ctr,
        "cpa": cpa,
        "roas": roas,
        "cpc": cpc,
        "conversion_rate": conv_rate,
    }

    if previous_period:
        prev_ctr = calculate_ctr(previous_period["impressions"], previous_period["clicks"])
        prev_cpa = calculate_cpa(previous_period["spend"], previous_period["conversions"])
        prev_roas = calculate_roas(previous_period["revenue"], previous_period["spend"])
        prev_cpc = calculate_cpc(previous_period["spend"], previous_period["clicks"])
        prev_conv_rate = calculate_conversion_rate(previous_period["clicks"], previous_period["conversions"])

        result["trends"] = {
            "ctr": calculate_trend(ctr, prev_ctr),
            "cpa": calculate_trend(cpa, prev_cpa),
            "roas": calculate_trend(roas, prev_roas),
            "cpc": calculate_trend(cpc, prev_cpc),
            "conversion_rate": calculate_trend(conv_rate, prev_conv_rate),
            "spend": calculate_trend(current_period["spend"], previous_period["spend"]),
            "revenue": calculate_trend(current_period["revenue"], previous_period["revenue"]),
        }
    else:
        result["trends"] = None

    return result
