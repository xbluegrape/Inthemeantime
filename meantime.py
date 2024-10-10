import pyautogui
import time

pyautogui.FAILSAFE = False

def no_lock(button):
    try:
        print ('CTRL+C para interrumpir.')
        while True:
            pyautogui.press(button)     # Key pressed
            time.sleep(2)

    except Exception as ex:
        print ('no_lock | Error: ', ex)

def main():
    try:
        print ('\nPrevent Windows screenlock')
        kb_button = str(input('Tecla a presionar: '))
        
        print ('\nRuning')
        no_lock(kb_button)

    except KeyboardInterrupt:
        print('\nStopped')

    except Exception as ex:
        print ('main | Error: ', ex)


if __name__ == "__main__":
    main()