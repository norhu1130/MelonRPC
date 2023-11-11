import discordrpc
import win32gui
import time


melon = f"""\033[38;5;155m
                      !!(       
                    !!!!!!!        
                    /!!!!!         
          !!!!!!!!!                 __  __   ______   _         ____    _   _         _____    _____     _____ 
       !!!!!!!!!!!!!!!             |  \/  | |  ____| | |       / __ \  | \ | |       |  __ \  |  __ \   / ____|
      !!!!!/     *!!!!!            | \  / | | |__    | |      | |  | | |  \| |       | |__) | | |__) | | |
      !!!!!       !!!!!            | |\/| | |  __|   | |      | |  | | | . ` |       |  _  /  |  ___/  | |
      !!!!!.     .!!!!!            | |  | | | |____  | |____  | |__| | | |\  |       | | \ \  | |      | |____
       !!!!!!!!!!!!!!!             |_|  |_| |______| |______|  \____/  |_| \_|       |_|  \_\ |_|       \_____|
          !!!!!!!!!             
"""

print(f"{melon}")
rpc = discordrpc.RPC.set_id(app_id=1154790088295841912)

def info(string):
    print(f"\033[38;5;122m[ℹ️] {string}")

def error(string):
    print(f"\033[38;5;196m[❌] {string}")

def warning(string):
    print(f"\033[38;5;208m[⚠️] {string}")

def success(string):
    print(f"\033[38;5;46m[✅] {string}")

def get_window_hwnd_list():
    def callback(_hwnd, _result: list):
        title = win32gui.GetWindowText(_hwnd)
        if win32gui.IsWindowEnabled(_hwnd) and win32gui.IsWindowVisible(_hwnd) and title is not None and len(title) > 0:
            _result.append(_hwnd)
        return True

    result = []
    win32gui.EnumWindows(callback, result)
    return result

def wait_for_window_hwnd():
    result = None
    info("Looking for Melon Player . . .")

    while result is None:
        hwnd_list = get_window_hwnd_list()

        for hwnd in hwnd_list:
            classname = win32gui.GetClassName(hwnd)
            if classname == "Chrome_WidgetWin_1":
                title = win32gui.GetWindowText(hwnd)
                if title.find("멜론 PC 플레이어") != -1:
                    result = hwnd
                    break


    success("Found Melon App Player!")
    return result

info("프로젝트 문의 : melon@norhu1130.dev")
print()

info("카카오엔터테이먼트사의 공식 제품/서비스가 아닙니다.")
info("멜론 또는 카카오엔터테이먼트사와 승인되지 않았으며, 관련이 없습니다.")
print()

warning("본 프로젝트는 무료로 배포되며, 상업적 이용을 금합니다.")
warning("본 프로그램을 유료로 구입하셨다면, 연락 부탁드립니다.")
print()

hwnd = wait_for_window_hwnd()

cache = None

while True:
    title = win32gui.GetWindowText(hwnd)

    if title == cache:
        continue

    cache = title

    if title == "멜론 PC 플레이어":
        rpc.set_activity(
            state=f"노래를 고르는 중 . . .",
            details="",
            large_image="melon",
            large_text="멜론 PC 플레이어",
            timestamp=time.mktime(time.localtime())
        )
        continue

    split = title.split(" - ")

    song = split[0]
    try:
        # Seven (feat. Latto) - Clean ver - 정국 같은 경우, Clean ver이 아티스트가 되기에 이렇게 처리.
        for i in range(0,100):
            artist = split[i]
    except:
        pass
    if song is None and artist is None:
        error("Failed to get song info. Are you closed Melon Player?")
        continue
    info(f"Playing {song} - {artist}")

    rpc.set_activity(
        state=f"{artist}",
        details=song,
        large_image="melon",
        large_text="멜론 PC 플레이어",
        timestamp=time.mktime(time.localtime())
    )