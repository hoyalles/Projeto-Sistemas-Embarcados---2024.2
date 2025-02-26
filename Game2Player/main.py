from machine import Pin
import time
import random

led = Pin(4, Pin.OUT)
player_1 = Pin(2, Pin.IN, Pin.PULL_UP)
player_2 = Pin(3, Pin.IN, Pin.PULL_UP)

print("Preparem-se! O jogo vai começar em breve...")


for _ in range(3):
    led.value(1)
    time.sleep(0.3)
    led.value(0)
    time.sleep(0.3)


delay_time = random.uniform(3, 7)  
print("Esperem... Apertem assim que o Led Acender")
time.sleep(delay_time)


led.value(1)
print("🔥 Pressione o botão o mais rápido possível!")


while True:
    if player_1.value() == 0:  
        print("🥇 Player 1 venceu!")
        break
    if player_2.value() == 0:
        print("🥇 Player 2 venceu!")
        break
    time.sleep(0.01) 

led.value(0)
