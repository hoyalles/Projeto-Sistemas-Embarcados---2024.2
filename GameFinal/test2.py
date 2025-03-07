import time
import random
from gpiozero import LED, Button


led = LED(4)  # LED conectado no pino GPIO 4
jogador_1 = Button(2, pull_up=True)  # Botão do jogador 1 no pino GPIO 2
jogador_2 = Button(3, pull_up=True)  # Botão do jogador 2 no pino GPIO 3

print("Preparem-se! O jogo vai começar em breve...")


for _ in range(3):
    led.on()
    time.sleep(0.3)
    led.off()
    time.sleep(0.3)

# Espera um tempo aleatório entre 3 e 7 segundos antes de acender o LED
delay_time = random.uniform(3, 7)
print("Esperem... Apertem assim que o LED acender")
time.sleep(delay_time)


led.on()


print("Pressione o botão o mais rápido possível!")


while True:
    if jogador_1.is_pressed:
        print("Jogador 1 venceu!")
        break
    if jogador_2.is_pressed:  
        print("Jogador 2 venceu!")
        break
    time.sleep(0.01)

led.off()

print("Fim do jogo!")
