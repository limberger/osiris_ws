import asyncio
import websockets


async def hello():
    uri = "wss://osiris-ws-69795ccd37bb.herokuapp.com/ws"
    async with websockets.connect(uri) as websocket:
        name = input("Whats you name?")
        await websocket.send(name)
        print(f"Client setn: {name}")

        greeting = await websocket.recv()
        print(f"Client received: {greeting}")


if __name__ == "__main__":
    asyncio.run(hello())
