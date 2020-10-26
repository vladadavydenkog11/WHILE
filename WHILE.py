a = int(input('Put A: '))
b = int(input('Put B: '))
c = int(input('Additional: '))

def compare(a,b,c):
    while a < b:
        a+=c
        if a < b:
            print('Added', c , ', but A is not bigger than B yet: ', a)
        else:
            a > b
            print('Result =', a , 'Excellent. This result we have been required!' )
compare(a,b,c)

