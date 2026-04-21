#!/bin/bash
PID_FILE="/tmp/vid_cam.pid"
VENV_PYTHON="/home/aakashdandekar/Projects/Vid-Cam/.venv/bin/python3"
SCRIPT="/home/aakashdandekar/Projects/Vid-Cam/main.py"

if [ -f "$PID_FILE" ]; then
    PID=$(cat "$PID_FILE")
    if kill -0 "$PID" 2>/dev/null; then
        kill "$PID"
    fi
    rm -f "$PID_FILE"
else
    nohup "$VENV_PYTHON" "$SCRIPT" > /dev/null 2>&1 &
fi