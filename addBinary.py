from typing import List
def addBinary(a: str, b: str) -> str:
    sum = ''
    # write your code here ^_^
    if a == '0' and b == '0':
        return '0'
    else:
        sum = bin((int(a,2)+int(b,2)))
        return str(sum[2:])



print(addBinary('11', '1'))


