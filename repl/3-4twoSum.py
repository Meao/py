'''
Krivtson Marina IVT2.3
'''

def sumtwo(lst, target):
    for index, value in enumerate(lst):
        for index2, value2 in enumerate(lst):
            if index!=index2:
                if value2==target-value:
                    couple = [index, index2]
                    return couple
    return None

lst = [1, 0, 0, 5, 0, 0]
target = 5
myset = sumtwo(lst, target)
print(myset)
'''
if __name__ == '__main__':
 assert main(3,2,1,49,0)  ==  [0,1,2,3,49], 
 '''
def sumtw(lst, target):
    for index in range (len(lst)):
        for index2 in range (len(lst)):
            if lst[index2]==target-lst[index]:
                couple = [index, index2]
                return couple       
    return None

myset = sumtw(lst, target)
print(myset)

assert sumtw(lst, 6) == [0, 3], 'There\'s an error in your maths!'
assert myset != None, 'Nothing found!'
assert sumtw(lst, 3) == None, 'There\'s an error in your maths!'

def suminhash(lst, target):
    hasht = list(enumerate(lst, 0))
    print(hasht)
    hashd = dict{enumerate(lst, 0)}
    print(hashd)
    return None
suminhash(lst, target)
