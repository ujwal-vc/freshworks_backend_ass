import data_store_lib


x=1

user=data_store_lib.sad()
while(x!=0):
    user_wish=input("Choose one of the below operations : \n1.Create \n2.Read \n3.Delete \n")

    if(user_wish=='1'):
        user.create()

    if(user_wish=='2'):
        user.read()
    
    if(user_wish=='3'):
        user.delete()

    x=int(input("EXIT= 0 ,RUN AGAIN= 1 :\n"))


