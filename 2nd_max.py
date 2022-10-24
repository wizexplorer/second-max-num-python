print("|-------------------------EXPERIMENT NO.25-----------------------------|")
print("|         FINDING THE SECOND MAXIMUM NUMBER FROM THE LIST              |")
print("|----------------------------------------------------------------------|")
print()
L=eval(input("              Enter the list of number : "))
max_num=max(L)
secondmax=min(L)   # dosn't work, if value less than 0 
for i in range(len(L)):
    # if secondmax<max_num and secondmax<L[i]:
    #     secondmax=secondmax
    if L[i]>secondmax and L[i]<max_num:
        secondmax=L[i]
print()
print("*"*72)
print("    Second maximum element of the list :",secondmax)
print("*"*72)
