import numpy as np

expenses = np.loadtxt('input', dtype='uint32')

for i in range(expenses.shape[0]):
    elem1 = expenses[i]
    for j in range(i, expenses.shape[0]):
        elem2 = expenses[j]

        if elem1 + elem2 == 2020:
            print('Elem1', elem1)
            print('Elem2', elem2)
            print('Prod', elem1 * elem2)
