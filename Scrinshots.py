import pyautogui
from pynput.mouse import Listener, Button
import sys
import subprocess
import ctypes


save_path = ""  # путь сохранения скриншота

def take_screenshot():
    timestamp = pyautogui.datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    screenshot_name = f"screenshot_{timestamp}.png"
    full_save_path = save_path + screenshot_name
    screenshot = pyautogui.screenshot()
    screenshot.save(full_save_path)
    print(f"Скриншот сохранен в файле {full_save_path}")

def on_click(x, y, button, pressed):
    if pressed and button == Button.middle:
        take_screenshot()

def exit_program():
    print("Программа завершена.")
    sys.exit(0)

def hide_console():
   
    kernel32 = ctypes.windll.kernel32
    user32 = ctypes.windll.user32
    hWnd = kernel32.GetConsoleWindow()
    if hWnd:
        user32.ShowWindow(hWnd, 0)  

def main():
    hide_console()  # Скрыть окно консоли

    with Listener(on_click=on_click) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            exit_program()

if __name__ == "__main__":
    # Создание окно без GUI
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    subprocess.Popen(["python", __file__], startupinfo=startupinfo)

    main()
