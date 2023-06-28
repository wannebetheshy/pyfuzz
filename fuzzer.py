
from decoration import banner, url_banner, Timer
from parseargumets import info
from makerequests import get_send_request
import asyncio
import aiohttp
import sys
import time


URL, WORDLIST, SPECWORD, MAXREQSPERTIME, POST_DATA = info(sys.argv).assign_args
print(URL, WORDLIST, SPECWORD, MAXREQSPERTIME)

async def main():
    url_banner(URL.replace(SPECWORD, '', 1), len(WORDLIST))
    timer = Timer(time.perf_counter())
    tasklist = []
    semaphore = asyncio.Semaphore(value=MAXREQSPERTIME)

    if POST_DATA:
        for word in WORDLIST:
            url = URL.replace(SPECWORD, word, 1)
            tasklist.append(asyncio.create_task(get_send_request(word, url, semaphore)))
        
    else:
        for word in WORDLIST:
            url = URL.replace(SPECWORD, word, 1)
            tasklist.append(asyncio.create_task(get_send_request(word, url, semaphore)))

    await asyncio.gather(*tasklist)
    timer.show_time(time.perf_counter())
    

if __name__ == '__main__':
    banner()
    asyncio.run(main())
