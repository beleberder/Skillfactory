import numpy as np
np.random.seed(0)
number = np.random.randint(1,101)

count = 0 #счётчик угадываний
while True:
    count+=1
    guess = np.random.randint(1,101)
    
    if guess == number:
        print("Guess number = ", count)
        break
