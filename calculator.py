a=float(input("enter 1st number"))
b=float(input("enter 2nd number"))
c=str(input("enter opertor"))
if c=='+':
    print(float(a)+float(b))
elif c=='-':
    print(float(a)-float(b))
elif c=='*':
    print(float(a)*float(b))
elif c=='/':
    print(float(a)/float(b))
elif c=='%':
    print(float(a)%float(b))
elif c=='**':
    print(float(a)**float(b))
else:
    print("enter valid oprator")
print("Have a Good Day.....")
    