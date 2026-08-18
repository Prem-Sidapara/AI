

# time.sleep to bas samajhne ke liye tha 

# ab real api 

import asyncio
import httpx 

async def get_joke()-> str:
    async with httpx.AsyncClient(headers={"Accept": "application/json"}) as client:
        response = await client.get("https://icanhazdadjoke.com/")
        data = response.json()
        return data['joke']

async def main():
    jokes = await asyncio.gather(
        get_joke(),
        get_joke(),
        get_joke(),
        get_joke(),
        get_joke(),
    )
    for joke in jokes:
        print(joke)
        print("-------")

asyncio.run(main())