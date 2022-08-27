import time
import pyautogui

i = 0
n = input('请输入伐木次数：')
n=int(n)

while True:
        about_pos = pyautogui.locateOnScreen('images/icon.png',confidence=0.8)
        if about_pos==None:
            print('未找到')
        else:
            break

goto_pos = pyautogui.center(about_pos)
pyautogui.moveTo(goto_pos, duration=1)
pyautogui.click()


while True:

    time.sleep(1)
    pyautogui.click(clicks=3,interval=0.5)

    time.sleep(2)

    pyautogui.press('esc')



    while True:
        exit_pos = pyautogui.locateOnScreen('images/exit.png',confidence=0.8)
        if exit_pos==None:
            print('未找到')
        else:
            break
    goto_pos = pyautogui.center(exit_pos)
    pyautogui.moveTo(goto_pos,duration=1)
    pyautogui.click()


    while True:
        confirm_pos = pyautogui.locateOnScreen('images/confirm_button.png',confidence=0.8)
        if confirm_pos==None:
            print('未找到')
        else:
            break
    goto_pos = pyautogui.center(confirm_pos)
    pyautogui.moveTo(goto_pos,duration=1)
    pyautogui.click()
    i=i+1
    print('第'+str(i)+'次伐木结束')


    if i==n:
        break

    while True:
        click_enter_pos = pyautogui.locateOnScreen('images/click_enter.png',confidence=0.8)
        if click_enter_pos==None:
            print('未找到')
        else:
            pyautogui.click()
            break
    #延长相应时间，可根据需要进行修改
    time.sleep(30)