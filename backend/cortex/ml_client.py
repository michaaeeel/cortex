"""Shared ML service client for making requests to the ML microservice."""
import logging

import httpx
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response

logger = logging.getLogger(__name__)

ML_SERVICE_URL = getattr(settings, "ML_SERVICE_URL", "http://ml-services:8001")
ML_INTERNAL_API_KEY = getattr(settings, "ML_INTERNAL_API_KEY", "")


def ml_service_post(path, data, timeout=30.0):
    """Make a POST request to the ML service and return a DRF Response.

    Returns a Response on success, or an error Response on failure.
    """
    headers = {}
    if ML_INTERNAL_API_KEY:
        headers["X-Internal-Key"] = ML_INTERNAL_API_KEY
    try:
        resp = httpx.post(
            f"{ML_SERVICE_URL}{path}",
            json=data,
            headers=headers,
            timeout=timeout,
        )
        resp.raise_for_status()
        return Response(resp.json())
    except httpx.HTTPStatusError as e:
        logger.error("ML service returned %s: %s", e.response.status_code, e.response.text)
        return Response(
            {"error": "Insights service unavailable"},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
    except httpx.ConnectError:
        logger.error("Cannot connect to ML service at %s", ML_SERVICE_URL)
        return Response(
            {"error": "Cannot connect to ML service"},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
