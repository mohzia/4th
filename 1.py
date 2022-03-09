i=0
m=True
mylist=[]
while m==True:
    data=input("enter any things or exit to quit!!  ")
    mylist += [data]
    if mylist[i]=="exit":
        print(mylist*2)
        m=False
    i=i+1