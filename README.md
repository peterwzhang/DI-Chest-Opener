# DI-Chest-Opener
A simple python script to open blessed chests on Diablo Immortal since they have a 5-second cooldown per chest and tend to stack up quickly.

## Setup
You need python3 to run this, you can get this [here](https://www.python.org/downloads/)

Once you have the items above, you can follow the instructions below:
1. Clone the repository
2. Go into the new cloned directory
3. [Optional] Make a virtual environment and activate it ([click here for help](https://docs.python.org/3/library/venv.html))
4. Install requirements: `$ pip install -r requirements.txt`
5. Run: `$ python main.py`

## Notes
- This has only been tested on Windows 10, with a 1920x1080 resolution. If you use a different resolution, you may have to supply your own images.
- There is a failsafe to stop before all of your chests have been opened, just move your cursor to any corner of your screen.
- There is a GUI version, however it was quickly made and not tested. If you would like to try it you can call the `create_gui()` function instead of `open_all_chests()`.
- Although I highly doubt this will cause anything to happen to your account, I am not responsible for anything that happens to your account from using this script.
