import asyncio
import aiohttp

async def fetch_url(session, url, retries=3):
    for attempt in range(retries):
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    print(f"SUCCESS {url}")
                    return
                else:
                    print(f"Attempt {attempt+1} failed → {response.status}")
        except Exception as e:
            print(f"Error: {e}")

        await asyncio.sleep(1)

async def main():
    urls = ["https://httpbin.org/delay/2"] * 3
    timeout = aiohttp.ClientTimeout(total=5)

    async with aiohttp.ClientSession(timeout=timeout) as session:
        await asyncio.gather(*(fetch_url(session, url) for url in urls))

asyncio.run(main())
