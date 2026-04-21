# Vid-Cam

A lightweight webcam recorder for Ubuntu Linux, controlled via a single toggle script. One run starts recording; another run stops it and saves the file.

---

## How It Works

`launch.sh` acts as a toggle. If no recording is active, it launches `main.py` in the background. If a recording is already running, it sends a signal to stop it. The output is saved as a timestamped `.mp4` file.

---

## Requirements

- Ubuntu Linux
- Python 3
- OpenCV (`opencv-python`)
- A V4L2-compatible webcam

Install dependencies:

```bash
pip install opencv-python
```

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/Vid-Cam.git
cd Vid-Cam
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install opencv-python
```

3. Update the paths in `launch.sh` and `main.py` to match your system:

```bash
# In launch.sh
VENV_PYTHON="/path/to/Vid-Cam/.venv/bin/python3"
SCRIPT="/path/to/Vid-Cam/main.py"

# In main.py
OUTPUT_DIR = "/path/to/Vid-Cam/saves"
```

4. Make the script executable:

```bash
chmod +x launch.sh
```

---

## Usage

**Start recording:**

```bash
./launch.sh
```

**Stop recording and save:**

```bash
./launch.sh
```

Running the script a second time sends a stop signal. The recording is saved to the `saves/` directory with a filename like `recording_20250421_143500.mp4`.

---

## Output

Recordings are saved to the `saves/` directory by default. Each file is named with a timestamp:

```
saves/
  recording_20250421_143500.mp4
  recording_20250421_150012.mp4
```

---

## Configuration

The following constants can be adjusted in `main.py`:

| Variable | Default | Description |
|---|---|---|
| `OUTPUT_DIR` | `./saves` | Directory where recordings are saved |
| `FPS` | `20.0` | Frames per second |
| `FOURCC` | `mp4v` | Video codec |

---

## Binding to a Keyboard Shortcut

For quick access, bind `launch.sh` to a keyboard shortcut via your desktop environment's settings. This lets you start and stop recording without opening a terminal.

**Example (GNOME):** Settings > Keyboard > Custom Shortcuts > add the full path to `launch.sh`.

---

## License

MIT
