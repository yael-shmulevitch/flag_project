from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.cmd_l:
        try:
            print('- Started recording -'.format(key))
        except IOError:
            print ("Error")
    else:
        print('incorrect character {0}, press cmd_l'.format(key))


def on_release(key):

    print('{0} released'.format(key))
    if key == keyboard.Key.cmd_l:
        print('{0} stop'.format(key))
        keyboard.Listener.stop
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()