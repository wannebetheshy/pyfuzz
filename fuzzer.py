
from sources.decoration import banner, url_banner, Timer
from sources.parseargumets import info
from sources.makerequests import get_send_request, post_send_request
import asyncio
import aiohttp
import sys
import time

async def main():

    # Getting arguments
    URL, WORDLIST, SPECWORD, MAXREQSPERTIME, POST_DATA = info(sys.argv).assign_args

    # Decoration part
    url_banner(URL.replace(SPECWORD, '', 1), len(WORDLIST))
    timer = Timer(time.perf_counter())
    tasklist = []

    # Restrict requests
    semaphore = asyncio.Semaphore(value=MAXREQSPERTIME)

    if POST_DATA:
        for word in WORDLIST:
            post_data = POST_DATA.replace(SPECWORD, word, 1)
            url = URL.replace(SPECWORD, word, 1)
            tasklist.append(asyncio.create_task(post_send_request(word, url, semaphore, post_data)))
        
    else:
        for word in WORDLIST:
            url = URL.replace(SPECWORD, word, 1)
            tasklist.append(asyncio.create_task(get_send_request(word, url, semaphore)))

    await asyncio.gather(*tasklist)
    timer.show_time(time.perf_counter())
    

if __name__ == '__main__':
    banner()
    asyncio.run(main())
