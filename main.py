from data import phone_numbers
from custompywhatkit import custom_py_what_kit
import time
import pyautogui


msg = "test message"

# Step 2 - Enter the custom coordinates here
custom_py_what_kit_instance = custom_py_what_kit(1670, 994)

for phone_number in phone_numbers:
    phone_number = "+91" + str(phone_number)
    print(f'Sending message to {phone_number}')
    custom_py_what_kit_instance.sendwhatmsg_instantly(phone_no=phone_number, message=msg, wait_time=10)
    time.sleep(2)

print('Press Ctrl-C to quit.')

# Step 1 - get the coordinates where message is typed in whatsapp web
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

# Step 4 - run the program