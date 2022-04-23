"""
    Celery tasks. Some of them will be launched periodically from admin panel via django-celery-beat
"""
import re
import traceback
from typing import List
from urllib.parse import urljoin

import asyncio
import aiohttp
from app.celery import app
from celery.utils.log import get_task_logger
from bs4 import BeautifulSoup

logger = get_task_logger(__name__)
NESTED_LINKS_LEVEL = 2


@app.task()
def crawl_task(url: str) -> List[str]:
    return asyncio.get_event_loop().run_until_complete(crawl(url))


async def crawl(url: str) -> List[str]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE '
    }
    timeout = aiohttp.ClientTimeout(total=3)
    async with aiohttp.ClientSession(timeout=timeout, headers=headers) as session:
        queue = [url]
        res: set[str] = set()

        async def parse_url(u):
            try:
                async with session.get(u) as resp:
                    if not resp or resp.status != 200:
                        return
                    content = await resp.text()
                    soup = BeautifulSoup(content, 'lxml')
                    anchors = soup.find_all('a', attrs={'href': re.compile("^(/|https?://)")})

                    for anchor in anchors:
                        href = anchor['href']
                        if href[0] == '/':
                            href = urljoin(u, href)
                        if href not in res:
                            res.add(href)
                            queue.append(href)
            except Exception as e:
                print(f'{u}: Get URL error. {e}')
                print(traceback.format_exc())

        level = 0
        while queue and level < NESTED_LINKS_LEVEL:
            tasks = [asyncio.ensure_future(parse_url(u)) for u in queue]
            queue = []
            await asyncio.gather(*tasks)
            level += 1

        return list(res)
