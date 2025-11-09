import random
import matplotlib.pyplot as plt
import numpy as np

def coin_flip(dollars, tries):
    for i in range(tries): # runs through every try
        if random.randint(0, 1): # if its one then add one if not subtract one
            dollars +=  1
        else:
            dollars -= 1
    return dollars

output = {}
flips = [5, 50, 100, 500, 5000, 10000]
for flip in flips:
    temp = []
    for gambler in range(1000): # number of gamblers
        temp.append(coin_flip(100, flip))
    output[flip] = np.array(temp)

    print('--------------------')
    print(f'{flip} flips: ')
    print(f'\tAverage flips: {np.mean(output[flip])}$')
    print(f'\tHighest final money: {np.max(output[flip])}$')
    print(f'\tLowest final money: {np.min(output[flip])}$')

    plt.hist(output[flip], bins=32, color='skyblue', edgecolor='black')

    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title(f'{flip} flips')

    plt.show()
plt.savefig('Lab8_P1_JohnTan-Aristy.png')