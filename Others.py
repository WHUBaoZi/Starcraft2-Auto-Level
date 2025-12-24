
import script_util
import mss
import time
import pyautogui
import sys

def OthersScript():
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
        
        # Back to menu
        print("准备返回主菜单")
        while True:
            time.sleep(1)
            leave = script_util.find_template_on_screen(sct, "./pics/leave.png")
            if leave is not None:
                pyautogui.click(leave)
                time.sleep(1)
                print("主菜单返回成功，当前战斗轮次结束")
                print("=" * 40)
                break

        # press yes if 15 level
        time.sleep(1)
        pyautogui.click((1270, 910))


        
if __name__ == "__main__":
    loop_num = 1
    print("本机为需要刷级的指挥官")
    print("=" * 40)
    while True:
        print(f"当前战斗次数: {loop_num}")
        OthersScript()
        loop_num = loop_num + 1