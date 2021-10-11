import ctypes  # An included library with Python install.


def show():
    ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
