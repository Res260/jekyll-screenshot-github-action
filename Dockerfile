FROM python

RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
    fonts-noto-color-emoji \
    gnupg \
    --no-install-recommends \
    && curl -sSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /etc/apt/trusted.gpg.d/google-chrome.gpg \
    && echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y \
    google-chrome-stable \
    --no-install-recommends

RUN apt install -y libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgdk-pixbuf-xlib-2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libnss3 lsb-release xdg-utils wget

# Google Chrome doesn't run from the root user.
RUN groupadd chrome && useradd --uid=1001 -g chrome -s /bin/bash -G audio,video chrome \
    && mkdir -p /home/chrome && chown -R chrome:chrome /home/chrome

ADD ./requirements.txt .
RUN python -m pip install -r requirements.txt

USER chrome

ENV HOME /home/chrome
WORKDIR /home/chrome

ADD ./screenshot.py .
ADD ./start.sh .

WORKDIR /home/chrome

CMD ["/bin/sh", "/home/chrome/start.sh"]
