#!/usr/bin/env python

import subprocess
import time
from playwright.sync_api import sync_playwright

with subprocess.Popen(['python', '-m', 'http.server'], cwd='/github/workspace/_site', stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as p:
    time.sleep(3.0)
    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            executable_path='/usr/bin/google-chrome-stable',
            args=['--no-sandbox']
        )
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        page.goto('http://localhost:8000')
        page.screenshot(path='/github/home/screenshot.png', full_page=True)
        browser.close()
    p.kill()
