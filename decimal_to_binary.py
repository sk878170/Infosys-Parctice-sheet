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


dec=int(input("Enter a binary number: "))
print(decimal_to_binary_conversion(dec))


