import numpy as np
np.random.seed(0)

number_of_guesses=[]

for i in range(1000):
    number = np.random.randint(1,101)

    left_border = 0
    rigth_border = 100
    guesses = []
    count = 0

    while True:
        count+=1
        if (rigth_border-left_border)%2==0:
            my_guess = left_border + int((rigth_border-left_border)/2)
        else:    
            my_guess = left_border + int((rigth_border-left_border+1)/2)
        guesses.append(my_guess)
        
        if my_guess == number:
            #print(f"Correct, counter ={count}")
            #print(*guesses)
            number_of_guesses.append(tuple([number, count]))
            print(i)
            break
        elif my_guess<number:
            #print("number should be greater than", my_guess)
            left_border = my_guess
        else:
            rigth_border = my_guess
            #print("number should be less than", my_guess)
    
average_score = sum(list(map(lambda x: x[1],number_of_guesses)))/len(number_of_guesses)
min_score = min(list(map(lambda x: x[1], number_of_guesses)))
max_score = max(list(map(lambda x: x[1], number_of_guesses)))
min_value = filter(lambda x: x[1]==min_score, number_of_guesses)
min_value = set(map(lambda x: x[0], min_value))
max_value = filter(lambda x: x[1]==max_score, number_of_guesses)
max_value = set(map(lambda x: x[0], max_value))
    
print("average_score =", average_score)
print("min score =",min_score)
print("max score =",max_score)
print("values for min score = ", *min_value)
print("values for max score size = ", len(max_value))
print("values for max score = ", *max_value, '\n')