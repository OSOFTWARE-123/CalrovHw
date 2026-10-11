import keyboard
import logging

logging.basicConfig(level=logging.INFO, format='')

def readkey():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_UP:
            return event.name

mod = "Stabilize"

"""Logging ile yazdığım kod."""
logging.info("Hoşgeldiniz! Komutlar: \nW: Yukarı\nA: Sol\nS: Aşağı\nD: Sağ\nC: Stabilize'ye geçiş\nH: Depth Hold'a geçiş\nİ: Modu örüntüleme\nQ: Çıkış\n")
while True:
    key = readkey()    
    if key == 'w':
        logging.info("Yukarı hareket ediliyor")
    elif key == 'a':
        logging.info("Sola hareket ediliyor")
    elif key == 's':
        logging.info("Aşağı hareket ediliyor")
    elif key == 'd':
        logging.info("Sağa hareket ediliyor")
    elif key == 'c':
        logging.info("Stabilize moduna geçiliyor")
        mod = "Stabilize"
    elif key == 'h':
        logging.info("Depth Hold moduna geçiliyor")
        mod = "Depth Hold"
    elif key == 'i':
        logging.info(f"Şu anki mod: {mod}")
    elif key == 'q':
        logging.info("Q tuşuna basıldı. Çıkıs yapiliyor")
        break
    else:
        logging.error(f"{key} tuşuna basıldı. Geçersiz komut.")


"""Print ile yazdığım kod."""

# print("Hoşgeldiniz! Komutlar: \nW: Yukarı\nA: Sol\nS: Aşağı\nD: Sağ\nC: Stabilize'ye geçiş\nH: Depth Hold'a geçiş\nİ: Modu örüntüleme\nQ: Çıkış\n")

# while True:
#     key = readkey()    
#     if key == 'w':
#         print("Yukarı hareket ediliyor")
#     elif key == 'a':
#         print("Sola hareket ediliyor")
#     elif key == 's':
#         print("Aşağı hareket ediliyor")
#     elif key == 'd':
#         print("Sağa hareket ediliyor")
#     elif key == 'c':
#         print("Stabilize moduna geçiliyor")
#         mod = "Stabilize"
#     elif key == 'h':
#         print("Depth Hold moduna geçiliyor")
#         mod = "Depth Hold"
#     elif key == 'i':
#         print(f"Şu anki mod: {mod}")
#     elif key == 'q':
#         print("Q tuşuna basıldı. Çıkıs yapiliyor")
#         break
#     else:
#         print(f"{key} tuşuna basıldı. Geçersiz komut.")
