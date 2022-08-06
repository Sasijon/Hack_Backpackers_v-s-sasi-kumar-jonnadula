
def bit_compr(s):
    x = int(s)
    binary = x
    decimal, i, n = 0, 0, 0
    while(x != 0):
        dec = x % 10
        decimal = decimal + dec * pow(2, i)
        x = x//10
        i += 1
    return decimal
    
    
'''
BitCompress(“0101100000”)	If mylink.mynumber1 contains the string “0101100000”, then the following two functions are equivalent, and return the number 352
'''

s = '0101100000'
print(bit_compr(s))
        