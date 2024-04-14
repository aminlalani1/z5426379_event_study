def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return tic


res = qan_tic()
print(res)

test_list = [0,1,2,3,4,5,6,7,8,9,10,20, 22, 23, 25,29, 30, 31]

def is_even_num(lis):
    evennum = []
    for n in lis:
        if n % 2 == 0:
            evennum.append(n)
    return evennum

print(is_even_num(test_list))

def add(a,b):
    """ Returns the sum of numbers, created on March 5, 2024"""
    return a + b
help(add)