from pynput import keyboard

def on_press(key):
    try:
        # Използвайте key.char само ако key е обект от тип keyboard.KeyCode
        if hasattr(key, 'char'):
            print(f'Key {key.char} pressed')
        else:
            print(f'Special key {key} pressed')
    except AttributeError:
        pass
    except Exception:
        
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        # Спиране на програмата при натискане на ESC
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


