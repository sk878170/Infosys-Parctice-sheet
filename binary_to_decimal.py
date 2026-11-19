def binary_to_decimal(bin):
    temp=str(bin)
    rev=temp[-1::-1]
    j=0
    result=0
    for i in rev:
        result=result+(int(i)*(2**j))
        j+=1
    return result

bin=int(input("Enter the binary number: "))
print(binary_to_decimal(bin))

