import asyncio

import websockets
from websockets import ServerConnection



async def echo(websocket: ServerConnection):
    async for message in websocket: 
        print(f'Получено сообщение {message}')
        response = f'Сервер получил: {message}'
       
        for _ in range(5):
            await websocket.send(response)


async def keep_alive():
    try: 
        while True:
            await asyncio.sleep(3600)
    except asyncio.CancelledError: 
        print("Dead")


async def main():
    async with websockets.serve(echo, "localhost", 8765):
        print("WebSocket сервер запущен на ws://localhost:8765")
        await asyncio.Future()
    await keep_alive()

asyncio.run(main())