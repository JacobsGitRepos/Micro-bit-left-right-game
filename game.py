from microbit import *
import random
import time

score = 0
game_over = False

while not game_over:
    display.show(Image('00900:' * 5))
    time.sleep(1)

    side = random.randint(1, 2)

    if side == 1:
        display.show(Image('00900:00900:90900:00900:00900'))
        time.sleep(1)
        if button_a.was_pressed():
            score += 1
        else:
            game_over = True  # End the game on incorrect or missed input
    else:
        display.show(Image('00900:00900:00909:00900:00900'))
        time.sleep(1)
        if button_b.was_pressed():
            score += 1
        else:
            game_over = True  # End the game on incorrect or missed input
        display.clear()

# Show the final score at the end of the game
display.show(score)
