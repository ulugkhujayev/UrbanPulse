import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from apps.transportation.models import Vehicle
from apps.transportation.serializers import VehicleSerializer


class VehicleConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("vehicles", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("vehicles", self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.channel_layer.group_send(
            "vehicles", {"type": "vehicle_update", "message": message}
        )

    async def vehicle_update(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))

    @database_sync_to_async
    def get_vehicles(self):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return serializer.data
