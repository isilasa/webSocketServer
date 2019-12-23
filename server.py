import asyncio
import websockets
import json


async def hello(websocket, path):
    jsonData = await websocket.recv()

    try:
        data = json.loads(jsonData)
        print("Client name " + data["name"])
        print("Number from Client: " + str(data["port"]))
        data["port"] = data["port"] * 2
        print(data)
    except KeyError:
        data["name"] = data["name"]
        data["port"] = 0
        print(data)

    greeting = ("Hello " + data["name"])
    await websocket.send(greeting)
    print(greeting)


start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
