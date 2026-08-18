

import asyncio 
import httpx

async def get_joke() -> str:
    try:
        async with httpx.AsyncClient(headers = {"Accept": "application/json"}) as client:
            response = await client.get("https://icanhazdadjoke.com/", timeout = 5.0 )
            response.raise_for_status()
            data = response.json()
            return data['joke']
    except httpx.TimeoutException:
        return "Error: Request timed out"
    except httpx.HTTPStatusError as e:
        return f"Error: HTTP {e.response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

async def main():
    jokes = await asyncio.gather(
        get_joke(),
        get_joke(),
        get_joke(),
        get_joke(),
        get_joke(),
    )
    print(f"Fetching {len(jokes)} jokes....")
    for joke in jokes:
        print(joke)
        print("-------")

asyncio.run(main())