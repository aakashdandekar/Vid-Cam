#!/usr/bin/env python3
"""
Webcam Recorder for Ubuntu Linux
- Run with 'start' to begin recording
- Run with 'stop' to save and exit
- Called via toggle.sh which handles start/stop logic
"""

import cv2
import time
import sys
import os
import signal
import threading
from datetime import datetime
from pathlib import Path

OUTPUT_DIR   = "/home/aakashdandekar/Projects/Vid-Cam/saves"
FPS          = 20.0
FOURCC       = "mp4v"
PID_FILE     = "/tmp/vid_cam.pid"
TRIGGER_FILE = "/tmp/stop_recording"

stop_event = threading.Event()

def file_watcher():
    if os.path.exists(TRIGGER_FILE):
        os.remove(TRIGGER_FILE)

    while not stop_event.is_set():
        if os.path.exists(TRIGGER_FILE):
            os.remove(TRIGGER_FILE)
            stop_event.set()
            break
        
        time.sleep(0.3)


if __name__ == "__main__":
    with open(PID_FILE, "w") as f:
        f.write(str(os.getpid()))

    t_watcher = threading.Thread(target=file_watcher, daemon=True)
    t_watcher.start()

    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    if not cap.isOpened():
        stop_event.set()
        sys.exit(0)

    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    output_dir = Path(OUTPUT_DIR).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp   = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = output_dir / f"recording_{timestamp}.mp4"

    fourcc = cv2.VideoWriter_fourcc(*FOURCC)
    writer = cv2.VideoWriter(str(output_path), fourcc, FPS, (width, height))

    def handle_signal(sig, frame):
        stop_event.set()

    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGINT, handle_signal)

    while not stop_event.is_set():
        ret, frame = cap.read()
        
        if not ret:
            time.sleep(0.05)
            continue

        writer.write(frame)

    cap.release()
    writer.release()

    if os.path.exists(PID_FILE):
        os.remove(PID_FILE)