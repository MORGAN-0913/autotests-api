# import asyncio
# import websockets
# from websockets import ServerConnection
#
# async def echo(websocket: ServerConnection):
#     async for message in websocket:
#         print(f"Получено сообщение: {message}")
#         response = f"Сервер получил сообщение клиента: {message}"
#         for _ in range(3):
#             await websocket.send(response)
#
# async def main():
#     print(f"WebSocketServer успешно запущен на порту ws://localhost:8000")
#     async with websockets.serve(echo, "localhost", 8000) as server:
#         await asyncio.Future()
#     await server.wait_closed()
#
# asyncio.run(main())