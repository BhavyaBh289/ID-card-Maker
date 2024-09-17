import pyautogui
import time
#
print(pyautogui.position())
with open('python.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

# Initialize an empty list to store the strings
string_array = []

# Process each line
for line in lines:
    # Strip any leading or trailing whitespace characters
    clean_line = line.strip()
    # Append the cleaned line to the string array
    string_array.append(clean_line)
t = string_array
for i in(t):
    pyautogui.moveTo(221,169,0)
    pyautogui.click()
    pyautogui.hotkey("ctrl","a")

    pyautogui.write(i)
    time.sleep(3)
    pyautogui.moveTo(440,229,0)
    pyautogui.click()
    time.sleep(2)

    pyautogui.moveTo(215,553,0)
    pyautogui.click()
