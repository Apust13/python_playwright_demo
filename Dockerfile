FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    wget gnupg curl libnss3 libxss1 libasound2 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxcomposite1 libxrandr2 libgbm1 libxdamage1 libxfixes3 libx11-xcb1 libxinerama1 libxext6 libxkbcommon0 libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

ENV PLAYWRIGHT_BROWSERS_PATH=0
RUN playwright install --with-deps

COPY . .

CMD ["pytest", "-m", "regression", "--alluredir=./allure-results"]
