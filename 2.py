iam=[]
a=True
while a==True:
    for i in range(0,5):
        b=input("inter word or end")
        if b=="end":
            a=False
            ex=",".join(iam)
            print(ex)
            break
        else:
            iam += [b]
    else:
        ex=",".join(iam)
        print(ex)
        a=False
