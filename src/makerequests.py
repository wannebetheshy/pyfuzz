import aiohttp
import asyncio

async def get_send_request(word, url, semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                page_size = len(await resp.read())
                print(f"{' '*2}{resp.status}{' '*2*3}{page_size:08d}{' '*2*3}{url}")
        await session.close()

async def post_send_request(word, url, semaphore, post_data):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=post_data) as resp:
                page_size = len(await resp.read())
                print(f"{' '*2}{resp.status}{' '*2*3}{page_size:08d}{' '*2*3}{url}")
        await session.close()