import asyncio

import websockets



async def client():
    url = "ws://localhost:8765"
    async with websockets.connect(url) as websocket:
        message = "Привет, сервер!"
        print(f"Отправка:{message}")
        await websocket.send(message)

        for i in range(5):    
            response = await websocket.recv()
            print(f"{i+1} {response}")



asyncio.run(client())

