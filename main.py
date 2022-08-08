import sys
import pyautogui
import tkinter as tk
import threading


def find_image(img):
    img_pos = None
    while img_pos is None:
        try:
            img_pos = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        except pyautogui.ImageNotFoundException:
            return False
    pyautogui.moveTo(img_pos)
    pyautogui.leftClick()
    return True


def open_all_chests():
    find_image('chest.png')
    while True:
        try:
            use_btn_exists = find_image('use.png')
            if not use_btn_exists:
                break
            pyautogui.time.sleep(5)
        except pyautogui.FailSafeException:
            break


def open_all_chests_t():
    open_thread = threading.Thread(target=open_all_chests)
    open_thread.daemon = True
    open_thread.start()


def destroy():
    sys.exit()


def create_gui():
    root = tk.Tk()
    root.title("DI Chest Opener")
    root.geometry("200x100")
    open_button = tk.Button(root, text="Open Chests", command=open_all_chests_t)
    open_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    stop_button = tk.Button(root, text="Stop", command=root.destroy)
    stop_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    root.mainloop()


if __name__ == '__main__':
    pyautogui.FAILSAFE = True
    # create_gui()      # uncomment to create a gui
    open_all_chests()   # and comment this line out if you want to use the gui
