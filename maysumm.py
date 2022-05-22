a= [1,2,3]
b=0
for i in a:
    b=b+i
print(b)




a= [1,3,3]
multiply=1
for i in a:
    multiply=multiply*i
print(multiply)


n=int(input("enter any positive number"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not a prime number")
            break
    else:
        print("prime number")
        
        
for i in range (2):
    print("outer loop",i)
    for j in range(3):
        print("inner loop",j)
print("rest of the code")
            



    