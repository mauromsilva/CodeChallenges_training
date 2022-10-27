import time
import random 

def waiting_game():
    target = random.randint(2,4)
    input()
    start = time.perf_counter()
    input('press enter again after '+str(target)+' seconds')
    elapsed = time.perf_counter()

    print(elapsed)
    print(target)


waiting_game()
