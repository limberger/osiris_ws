import asyncio
import websockets

clients = []


async def hello(websocket, path):
    global clients
    global fastest_time
    message = await websocket.recv()
    if message == "buzz":
        response_time = asyncio.get_event_loop().time()
        clients.append([websocket, response_time])
        if len(clients) == 1:
            await websocket.send("First place!!!!")
            fastest_time = response_time
        else:
            t = round(response_time - fastest_time, 2)
            await websocket.send(f"Response time {t} sec slower.")


async def main():
    async with websockets.serve(hello, "localhost", 8765):
        print("Websockets server Started")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
