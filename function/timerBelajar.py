import time
from plyer import notification
import utils.helper as helper

def countdown(seconds, pomodoro):
    pom = 0 # menit yang dilalui
    helper.clear()
    helper.send_notification("⏰ Timer Belajar ⏰", "Timer Dimulai!")
    print("Timer Dimulai")
    while seconds: 
        hours = seconds // 3600
        mins = (seconds % 3600) // 60
        secs = seconds % 60
        print(f"Waktu belajar [{hours:02}:{mins:02}:{secs:02}]   ", end="\r")
        if pomodoro: 
            if pom == 25: # Setiap 25 menit
                print("Waktunya istirahat 5 menit!", end="\r")
                helper.send_notification("⏰ Pomodoro Timer ⏰", "Waktunya Istirahat 5 Menit!")
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
                helper.send_notification("⏰ Pomodoro Timer ⏰", "Istirahat Selesai! Saatnya FOKUS kembali")
                time.sleep(5)
                continue
        time.sleep(1)
        seconds -= 1
        if seconds % 60 == 0 and pomodoro:
            pom += 1
    
    helper.clear()
    print("Waktu Belajar Habis!    ")
    helper.send_notification("⏰ Timer Belajar ⏰", "Timer Selesai!")
    time.sleep(5)
    return

def timerSetup():
    print("Tentukan waktu timer (Interval 10 menit)")
    jam = int(input("Jam: "))
    menit = round((int(input("Menit: "))) / 10) * 10 # Pembulatan menit ke puluhan terdekat (e.g. 46 -> 50; 33 -> 30)
    jam += menit // 60 # Jika menit lebih dari 60, tambahkan ke jam
    menit = menit % 60 # sisa menit
    print(f"Timer akan di set dengan waktu {jam} jam {menit} menit\n")
    
    while True:
        pomodoro = input("Gunakan pomodoro timer (setiap 25 menit istirahat 5 menit)? [Y/n] ")
        if pomodoro.lower() == "y":
            countdown((menit*60) + (jam*3600), True) # Convert jam dan menit menjadi detik
            return
        elif pomodoro.lower() == "n":
            countdown((menit*60) + (jam*3600), False) # Convert jam dan menit menjadi detik
            return
        else:
            print("Input salah!")