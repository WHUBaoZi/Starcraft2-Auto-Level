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

        # Attack targets
        print("准备攻击目标点...")
        while True:
            time.sleep(1)
            target1 = script_util.find_template_on_screen(sct, "./pics/target1.png")
            if target1 is not None:
                pyautogui.hotkey('ctrl', 'z')
                pyautogui.keyDown('shift')
                # Attack target1
                for i in range(10):
                    pyautogui.click(target1)
                    time.sleep(0.1)
                time.sleep(3)
                # Attack target2
                target2 = script_util.find_template_on_screen(sct, "./pics/target2.png")
                if target2 is not None:
                    for i in range(10):
                        pyautogui.click(target2)
                        time.sleep(0.1)
                    time.sleep(5)
                else:
                    # error
                    print("目标点2寻找失败")
                    sys.exit()
                # Attack target3
                target3 = script_util.find_template_on_screen(sct, "./pics/target3.png")
                if target3 is not None:
                    for i in range(10):
                        pyautogui.click(target3)
                        time.sleep(0.1)
                    time.sleep(7)
                else:
                    # error
                    print("目标点3寻找失败")
                    sys.exit()
                # Attack target4
                target4 = script_util.find_template_on_screen(sct, "./pics/target4.png")
                if target4 is not None:
                    for i in range(10):
                        pyautogui.click(target4)
                        time.sleep(0.1)
                    time.sleep(9)
                else:
                    # error
                    print("目标点4寻找失败")
                    sys.exit()
                # Attack target5
                target5 = script_util.find_template_on_screen(sct, "./pics/target5.png")
                if target4 is not None:
                    for i in range(10):
                        pyautogui.click(target5)
                        time.sleep(0.1)
                else:
                    # error
                    print("目标点5寻找失败")
                    sys.exit()
                print("目标点进攻完毕")
                break

        # Exit level
        print("等待退出关卡...")
        while True:
            time.sleep(1)
            score = None
            score_p = script_util.find_template_on_screen(sct, "./pics/score_p.png")
            score_t = script_util.find_template_on_screen(sct, "./pics/score_t.png")
            score_z = script_util.find_template_on_screen(sct, "./pics/score_z.png")
            if score_p is not None:
                score = score_p
            if score_t is not None:
                score = score_t
            if score_z is not None:
                score = score_z
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