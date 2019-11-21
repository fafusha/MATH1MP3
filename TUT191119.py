# Blackjack
# we know that each card has a value between 1-10
# jack queen king are all worth 10
# np.random.randint(lbound, ubound)
# bust where if your count value is above 21 then you have to return bust
# stay where if ypur count between 16 inclusive and 21 non inclusive
# if you get 21 you have return blackjack

import numpy as np

def blackjack():
    count = 0
    while True:
        card = np.random.randint(1,11)
        count += card
        if count > 21:
            return "bust"
        elif 16 <= count < 21:
            return "stay"
        elif count == 21:
            return "blackjacK"



