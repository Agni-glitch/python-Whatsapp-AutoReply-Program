import pyautogui
import pyperclip
import time
import customeReply
import genai
def copy_text():
    click_x, click_y = 1140, 1055
    start_x, start_y = 690, 200  
    end_x, end_y = 1730, 940  
    pyautogui.moveTo(click_x, click_y)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y)
    pyautogui.mouseUp()
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    copied_text = pyperclip.paste()
    return copied_text
extracted_text = copy_text()
text = extracted_text.split(':')[-1].strip()
print(text)
while True:
    if text in customeReply.replies:
        response_list = customeReply.replies[text]
        pyautogui.moveTo(810, 980)
        pyautogui.click()
        for j in response_list:
            if j == ' ':
                pyautogui.press('space')
            else:
                pyautogui.typewrite(j)
        pyautogui.hotkey('enter')
    else:
        a = genai.res(text)
        pyautogui.moveTo(810, 980)
        pyautogui.click()
        for j in a:
            if j == ' ':
                pyautogui.press('space')
            else:
                pyautogui.typewrite(j)
        pyautogui.hotkey('enter')
    time.sleep(10)