

import time

def fetch_user(user_id: int)-> str:
    time.sleep(1)
    return f"User {user_id} data"

def main_sync():
    start = time.time()
    results = []
    for i in range(10):
        result = fetch_user(i)
        results.append(result)
    print(f"Time: {time.time()- start:.2f} secodns")
    print(results)

main_sync()

# this is sync so it took 3 secodns but now 
# now using async okay  

import asyncio 

async def fetch_user_asysnc(user_id: int) -> str:
    await asyncio.sleep(1)
    return f"User {user_id} data"

async def main_async():
    start = time.time()
    results = await asyncio.gather(
        *[fetch_user_asysnc(i) for i in range(10)]
    )
    print(f"Time: {time.time() - start:.2f} seconds")
    print(list(results))

asyncio.run(main_async())
