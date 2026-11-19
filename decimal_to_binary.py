def decimal_to_binary_conversion(dec):
    rem=0
    s=""
    while dec>0:
        rem=dec%2
        s=s+str(rem)
        dec=dec//2
    return reverse(s)

def reverse(str):
    rev=""
    for i in str:
        rev=i+rev
    return rev

def decimal_to_binary_conversion2(dec):
    s=""
    while dec>0:
        temp = dec & 1
        s=str(temp)+s
        dec = dec >> 1
    return s




dec=int(input("Enter a binary number: "))
print(decimal_to_binary_conversion(dec))
print(decimal_to_binary_conversion2(dec))

