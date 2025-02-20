# Mouse Clicker 3000

A Python-based UI testing utility for automating mouse clicks at regular intervals. This tool is designed for testing application behavior and UI component responsiveness.

## Features

- Automated mouse clicking at configurable intervals
- Random timing variation to simulate realistic testing scenarios
- Simple console-based interface with activity logging
- Configurable click intervals (default: 5-10 seconds)

## Requirements

- Python 3.6+
- PyAutoGUI library
- threading (standard library)
- datetime (standard library)
- random (standard library)

## Installation

1. Clone this repository
2. Install required packages:
```bash
pip install pyautogui
```

## Usage

Run the script:
```bash
python clicker.py
```

To stop the program, press `Ctrl+C` in the terminal.

## Configuration

You can modify these parameters in the script:
- Click interval range: Change `random.uniform(5, 10)` values
- Failsafe: Set `pyautogui.FAILSAFE = True` to enable emergency stop

## Important Notes

- This tool is intended for testing purposes only
- Always use with caution and be aware of your system's security policies
- It's recommended to enable PyAutoGUI's failsafe during development
- Test in a controlled environment first