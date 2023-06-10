import time

def start_focus_timer(minutes):
    seconds = minutes * 60
    print(f"专注时钟已开始，将持续 {minutes} 分钟。")
    time.sleep(seconds)
    print("时间到！")

focus_minutes = int(input("请输入专注时钟的分钟数："))
start_focus_timer(focus_minutes)
