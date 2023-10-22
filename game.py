from microbit import *
import random
import time
score = 0

while True:
    display.show(Image('00900:'
                       '00900:'
                       '00900:'
                       '00900:'
                       '00900'))
    side = random.randint(1,2)
    time.sleep(1)
    if side == 1:
        display.show(Image('00900:'
                           '00900:'
                           '90900:'
                           '00900:'
                           '00900'))
        time.sleep(1)
        if button_a.was_pressed():
           display.show(Image('00900:'
                              '00900:'
                              '00900:'
                              '00900:'
                              '00900'))
           score += 1
        else:
            display.show(score)
    else:
        display.show(Image('00900:'
                           '00900:'
                           '00909:'
                           '00900:'
                           '00900'))
        time.sleep(1)
        if button_b.was_pressed():
           display.show(Image('00900:'
                              '00900:'
                              '00900:'
                              '00900:'
                              '00900'))
           score += 1
        else:
            display.scroll(score)
