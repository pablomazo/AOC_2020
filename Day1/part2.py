import numpy as np

expenses = np.loadtxt('input', dtype='uint32')

for i in range(expenses.shape[0]):
    elem1 = expenses[i]
    diff = 2020 - elem1
    for j in range(i, expenses.shape[0]):
        elem2 = expenses[j]

        elem3 = diff - elem2
        if elem3 in expenses:
            print('Elem1', elem1)
            print('Elem2', elem2)
            print('Elem3', elem3)
            print('Sum:', elem1 + elem2 + elem3)
            print('Prod', elem1 * elem2 * elem3)
