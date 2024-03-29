from numpy import *

def act (x):
    return 0 if x < 0.5 else 1

def go (test1, test2, test3):
    x = array([test1, test2, test3])
    w11 = [0.3,0.3,0]
    w12 = [0.4,-0.5,1]
    weigth1 = array([w11,w12])
    weigth2 = array([-1,1])
    sum_hidden = dot(weigth1,x)
    print('Значения сумм на нейронах скрытого слоя:' + str(sum_hidden))

    out_hidden = array([act(x) for x in sum_hidden])
    print('Значения на выходах нейронов скрытого слоя:' + str(out_hidden))

    sum_end = dot(weigth2,out_hidden)
    y = act(sum_end)
    print('Выходное значение HC:' + str(y))

    return y

test1 =int(input())
test2 = int(input())
test3 = int(input())

res = go(test1, test2, test3)
if res == 1: print('1')
else: print('0')

