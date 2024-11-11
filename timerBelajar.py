import time
from plyer import notification

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Helper Mahasiswa",  # Optional: specify the app name
        timeout=5  # Duration in seconds
    )

def countdown(seconds, pomodoro):
    pom = 0 # menit yang dilalui
    send_notification("⏰ Timer Belajar ⏰", "Timer Dimulai!")
    print("Timer Dimulai")
    while seconds: 
        hours = seconds // 3600
        mins = (seconds % 3600) // 60
        secs = seconds % 60
        print(f"Waktu belajar [{hours:02}:{mins:02}:{secs:02}]   ", end="\r")
        if pomodoro: 
            if pom == 25: # Setiap 25 menit
                print("Waktunya istirahat 5 menit!", end="\r")
                send_notification("⏰ Pomodoro Timer ⏰", "Waktunya Istirahat 5 Menit!")
                time.sleep(5)
                pomTimer = 295 # 5 menit istirahat
                while pomTimer:
                    pomMins = pomTimer // 60
                    pomSecs = pomTimer % 60
                    print(f"Waktu istirahat [{pomMins:02}:{pomSecs:02}]    ", end="\r")
                    time.sleep(1)
                    pomTimer -= 1
                pom = 0
                print("Istirahat selesai!         ", end="\r")
                send_notification("⏰ Pomodoro Timer ⏰", "Istirahat Selesai! Saatnya FOCUS kembali")
                time.sleep(5)
                continue
        time.sleep(1)
        seconds -= 1
        if seconds % 60 == 0 and pomodoro:
            pom += 1
    
    print("Waktu Belajar Habis!    ")
    send_notification("⏰ Timer Belajar ⏰", "Timer Selesai!")
    return True

print("Tentukan waktu timer (Interval 10 menit)")
jam = int(input("Jam: "))
menit = (round((int(input("Menit: "))) / 10) * 10)
jam += menit // 60
menit = menit % 60

print(f"Timer akan di set dengan waktu {jam} jam {menit} menit\n")
while True:
    pomodoro = input("Gunakan pomodoro timer (setiap 25 menit istirahat 5 menit)? [Y/n] ")
    if pomodoro.lower() == "y":
        countdown((menit*60) + (jam*3600), True)
    elif pomodoro.lower() == "n":
        countdown((menit*60) + (jam*3600), False)
    else:
        print("Input salah!")
