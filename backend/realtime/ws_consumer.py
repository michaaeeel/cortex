import json

from channels.generic.websocket import AsyncWebsocketConsumer


class MetricsConsumer(AsyncWebsocketConsumer):
    """WebSocket consumer that broadcasts live metric updates to connected clients."""

    async def connect(self):
        if not self.scope["user"].is_authenticated:
            await self.close()
            return
        self.group_name = "live_metrics"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, "group_name"):
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def metrics_update(self, event):
        """Handle metrics_update messages from the channel layer."""
        await self.send(text_data=json.dumps(event["data"]))
