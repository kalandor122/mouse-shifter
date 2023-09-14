import pyautogui
import keyboard
# Define the ranges of coordinates
ranges = {
    "1": (0+1920, 0, 350+1920, 350),
    "2": (0+1920, 680, 450+1920, 1080),
    "3": (600+1920, 0, 1200+1920, 200),
    "4": (800+1920, 700, 1300+1920, 1080),
    "5": (1500+1920, 0, 1900+1920, 250),
    "R": (1500+1920, 750, 1910+1920, 1080)
}

last_key_pressed = None

def get_position_label(x, y):
    for label, (x_min, y_min, x_max, y_max) in ranges.items():
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return label
    return None

# Example usage
while True:
    x, y = pyautogui.position()
    position_label = get_position_label(x, y)
    
    if position_label and position_label != last_key_pressed:
        keyboard.press_and_release(position_label)
        last_key_pressed = position_label
    elif not position_label and last_key_pressed != 'N':
        keyboard.press_and_release('N')
        last_key_pressed = 'N'


