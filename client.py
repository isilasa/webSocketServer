import asyncio
import websockets
import json


async def hello():
    url = "ws://localhost:8765"
    port = 8765
    async with websockets.connect(url) as websocket:
        name = input("What's your name? ")

        data = {
            "name": name,
            "age": age
        }

        jsonData = json.dumps(data)

        await websocket.send(jsonData)
        print(data["name"])

        print(await websocket.recv())


asyncio.get_event_loop().run_until_complete(hello())
