import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print("Mensaje recibido:", message)
        await websocket.send("Servidor recibió: " + message)

async def main():
    async with websockets.serve(echo, "0.0.0.0", 8000):
        print("Servidor WebSocket escuchando en ws://0.0.0.0:8000")
        await asyncio.Future()  # Mantener servidor corriendo

if __name__ == "__main__":
    asyncio.run(main())
