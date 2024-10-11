

import asyncio

def main():
    try:
        from osiris_ws import server_ws
    except ImportError as exc:
        raise ImportError(
            "Couldn't importServer."
        ) from exc
    
    asyncio.run(server_ws.main())


if __name__ == "__main__":
    main()