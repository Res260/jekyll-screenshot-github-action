#!/usr/bin/env python

import subprocess
import time
import asyncio
import logging
import sys
import signal

import pyppeteer

async def main():
    print(1, flush=True)
    browser = await pyppeteer.launch(args=['--no-sandbox'])
    print(2, flush=True)
    page = await browser.newPage()
    print(3, flush=True)
    await page.goto('http://localhost:8000')
    print(4, flush=True)
    await page.screenshot({'path': '/github/home/screenshot.png'})
    print(5, flush=True)
    await browser.close()
    print(6, flush=True)

with subprocess.Popen(['python', '-m', 'http.server'], cwd='/github/workspace/_site', stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as p:
    time.sleep(3.0)
    asyncio.get_event_loop().run_until_complete(main())
    p.kill()
