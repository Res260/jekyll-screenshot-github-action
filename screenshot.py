#!/usr/bin/env python

import subprocess
import time
import asyncio
import logging
import sys
import signal

import pyppeteer

async def main():
    browser = await pyppeteer.launch(args=['--no-sandbox', '-size=1920,1080'])
    page = await browser.newPage()
    await page.goto('http://localhost:8000')
    await page.screenshot({'path': '/github/home/screenshot.png', 'fullPage': True})
    await browser.close()

with subprocess.Popen(['python', '-m', 'http.server'], cwd='/github/workspace/_site', stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as p:
    time.sleep(3.0)
    asyncio.get_event_loop().run_until_complete(main())
    p.kill()
