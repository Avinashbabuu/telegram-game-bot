#!/bin/bash
echo "Starting Flask server..."
nohup python3 server/app.py &

echo "Starting Telegram bot..."
nohup python3 bot/bot.py &
