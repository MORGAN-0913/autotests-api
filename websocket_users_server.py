import asyncio
import websockets
from websockets import ServerConnection

async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        response = f"Сервер получил сообщение от клиента: {message}"
        for _ in range(5):
            await websocket.send(response)

async def main():
    print(f"WebSocketServer успешно запущен!")
    async with websockets.serve(echo, "localhost", 8765) as serever:
        await asyncio.Future()

    await serever.wait_closed()

asyncio.run(main())