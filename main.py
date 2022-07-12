import datetime
import time
import pyautogui
import pyperclip

times_looping = input('times to repeat: ')
msg = input('msg: ')
pyperclip.copy(msg)
time_to_wait = input('time to wait in seconds: ')

print('you got 10 seconds')
time.sleep(10)

st = t = time.time()

for i in range (int(times_looping)):
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("return")
    time.sleep(float(time_to_wait))

et = time.time()

print('done')
print(f"finished in {str(datetime.timedelta(seconds=(et-st)))}")
print(f"{(int(times_looping)/(et-st))} messages per second")