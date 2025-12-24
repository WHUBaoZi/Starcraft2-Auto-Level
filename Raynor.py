import script_util
import mss
import time
import pyautogui
import sys


def RaynorScript():
    with mss.mss() as sct:
        # Check prestige
        print("检查威望中...")
        while True:
            time.sleep(1)
            custom = script_util.find_template_on_screen(sct, "./pics/custom.png")
            if custom is not None:
                pyautogui.click(custom)
                time.sleep(1)
                activate = script_util.find_template_on_screen(sct, "./pics/activate.png")
                if activate is not None:
                    pyautogui.click(activate)
                    time.sleep(1)
                    yes = script_util.find_template_on_screen(sct, "./pics/yes.png")
                    if yes is not None:
                        pyautogui.click(yes)
                        time.sleep(0.5)
                        pyautogui.click(yes)
                        print("威望已开启")
                        pyautogui.press('esc')
                    else:
                        pyautogui.press('esc')
                else:
                    pyautogui.press('esc')
                print("威望检查完毕")
                time.sleep(1)
                break
        
        # Press ready
        print("准备中...")
        ready = script_util.find_template_on_screen(sct, "./pics/ready.png")
        if ready is not None:
            pyautogui.click(ready)
        else:
            # error
            print("准备失败")
            sys.exit()

        # Ready to attack targets
        print("正在寻找初始目标点...")
        target1 = target2 = target3 = target4 = target5 = None
        while True:
            time.sleep(1)
            target1 = script_util.find_template_on_screen(sct, "./pics/first_target.png")
            if target1 is not None:
                pyautogui.keyDown('shift')
                # Attack target1
                print("开始攻击...")
                for i in range(10):
                    pyautogui.hotkey('ctrl', 'z')
                    pyautogui.click(target1)
                    time.sleep(0.1)
                for i in range(10):
                    pyautogui.hotkey('ctrl', 'x')
                    pyautogui.click(target1)
                    time.sleep(0.1)
                break
        time.sleep(5)
        target2 = (target1[0] + 21, target1[1] - 151)
        target3 = (target1[0] + 102, target1[1] - 46)
        target4 = (target1[0] - 113, target1[1] - 37)
        target5 = (target1[0] - 112, target1[1] - 159)
        # Attack other targets
        for i in range(10):
            pyautogui.hotkey('ctrl', 'z')
            pyautogui.click(target2)
            time.sleep(0.1)
        for i in range(10):
            pyautogui.hotkey('ctrl', 'x')
            pyautogui.click(target2)
            time.sleep(0.1)
        time.sleep(7)

        for i in range(10):
            pyautogui.hotkey('ctrl', 'z')
            pyautogui.click(target3)
            time.sleep(0.1)
        for i in range(10):
            pyautogui.hotkey('ctrl', 'x')
            pyautogui.click(target3)
            time.sleep(0.1)
        time.sleep(9)

        for i in range(10):
            pyautogui.hotkey('ctrl', 'z')
            pyautogui.click(target4)
            time.sleep(0.1)
        for i in range(10):
            pyautogui.hotkey('ctrl', 'x')
            pyautogui.click(target4)
            time.sleep(0.1)
        time.sleep(11)

        for i in range(10):
            pyautogui.hotkey('ctrl', 'z')
            pyautogui.click(target5)
            time.sleep(0.1)
        for i in range(10):
            pyautogui.hotkey('ctrl', 'x')
            pyautogui.click(target5)
            time.sleep(0.1)
        pyautogui.keyUp('shift')

        # Exit level
        print("等待退出关卡...")
        while True:
            time.sleep(1)
            score = None
            score = script_util.find_template_on_screen(sct, "./pics/score.png")
            if score is not None:
                pyautogui.click(score)
                print("关卡退出完成")
                break
        
        # back to menu
        print("准备返回主菜单")
        while True:
            time.sleep(1)
            leave = script_util.find_template_on_screen(sct, "./pics/leave.png")
            if leave is not None:
                pyautogui.click(leave)
                time.sleep(1)
                print("主菜单返回成功，当前战斗轮次结束")
                break


if __name__ == "__main__":
    loop_num = 1
    print("本机为雷诺")
    print("=" * 40)
    while True:
        print(f"当前战斗次数: {loop_num}")
        RaynorScript()
        loop_num = loop_num + 1