import cv2
import numpy as np
import os

def find_template_on_screen(sct, template_path, threshold=0.9):
    """
    在指定屏幕区域匹配模板，返回匹配坐标 (x, y) 或 None
    """
    # 读取模板
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"模板图片不存在: {template_path}")
    template = cv2.imread(template_path)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template_gray.shape[::-1]

    monitor = sct.monitors[1]
    screen = sct.grab(monitor)
    screen_np = np.array(screen)
    screen_bgr = screen_np[:, :, :3]
    screen_gray = cv2.cvtColor(screen_bgr, cv2.COLOR_BGR2GRAY)

    # 模板匹配
    res = cv2.matchTemplate(screen_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    points = list(zip(*loc[::-1]))

    if points:
        pt = points[0]  # 只取第一个匹配
        x, y = pt[0] + w // 2, pt[1] + h // 2  # 中心位置
        return (x, y)
    else:
        return None