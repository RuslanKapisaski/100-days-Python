import pyautogui
import time

pyautogui.FAILSAFE = True

DETECTION_REGION = (300, 350, 120, 50)
OBSTACLE_COLOR_LIMIT = 100

print("Open chrome://dino")
print("Click on the game window.")
print("Bot will start in 3 seconds...")

time.sleep(3)

while True:
    screenshot = pyautogui.screenshot(region=DETECTION_REGION)

    pixels = screenshot.load()

    obstacle_found = False

    for x in range(screenshot.width):
        for y in range(screenshot.height):
            r, g, b, а = pixels[x, y]

            if r < OBSTACLE_COLOR_LIMIT and g < OBSTACLE_COLOR_LIMIT and b < OBSTACLE_COLOR_LIMIT:
                obstacle_found = True
                break

        if obstacle_found:
            break

    if obstacle_found:
        pyautogui.press("space")
        time.sleep(0.05)