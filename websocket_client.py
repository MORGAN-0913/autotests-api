# import asyncio
# import websockets
#
# async def client():
#     uri = "ws://localhost:8000"
#     async with websockets.connect(uri) as websocket:
#         message = f"Привет, сервер!"
#         print(f"Серверу доставлено сообщение: {message}")
#         await websocket.send(message)
#         for _ in range(3):
#             response = await websocket.recv()
#             print(f"Результат: {response}")
#
# asyncio.run(client())