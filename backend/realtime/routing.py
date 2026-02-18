from django.urls import path

from .ws_consumer import MetricsConsumer

websocket_urlpatterns = [
    path("ws/metrics/", MetricsConsumer.as_asgi()),
]
