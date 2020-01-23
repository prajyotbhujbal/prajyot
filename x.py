case=int(input("enter no of test cases"))
while(case>0):
    nv=int(input("enter the number of villegers"))
    print("enter the cost")
    cost = map(int,input().split()[:nv])
    mylist=list(cost)
    totalcost=0
    goingtovillage=0

    z=0
    print(mylist)
    for i in range(0,len(mylist)):
        mincost=mylist[0]
        break
    mylist.sort(reverse=True)
    for i in(0,len(mylist)):
        maxcost=mylist[0]
        break

    if(len(mylist)==2):
        print("minium total cost=",maxcost)
    else:
        totalcost=maxcost
        goingtovillage=mincost
        totalcost=maxcost+goingtovillage
        
        p=0

    for i in range(0,len(mylist)):
        mincost=mylist[i]
        maxcost=mylist[i+1]
        break
    totalcost=maxcost
    goingttovillage=mincost
    totalcost=maxcost+goingtovillage
    p=0
    for i in range(2,len(mylist)):

        if(goingtovillage>mylist[i]):
            p=goingtovillage
        else:
            p=mylist[i]
            totalcost=totalcost+p
        totalcost=totalcost+goingttovillage    
    print(totalcost)
    case=case-1
    
    






