import asyncio
import os
import websockets

clients = []


async def serverws(websocket, path):
    global clients
    global fastest_time
    message = await websocket.recv()
    response_time = asyncio.get_event_loop().time()
    print(f"{response_time} Received: {message}")
    await websocket.send(f"ok")


async def main():
    port=os.environ.get('PORT','3000')
    print(f"Serving port: {port}")
    async with websockets.serve(serverws, "0.0.0.0", int(port)):
        print("Websockets server Started")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
