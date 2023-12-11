print("String Operator\n","Menu\n1.Count Number of Alphabets\n2.Extract String\n3.Check Whether String is Alphanumeric Or Not\n4.Exit\n")
s=str(input("Enter the string:"))
j=1
while j==1:
    x=int(input("Enter Your Choice"))
    if(x==1):
        c=0
        for i in s:
            if(i.isalpha()):
                c+=1
        print("No. of alphabets are:",c,"\n")

    elif(x==2):
        a=int(input("Enter the Starting Range:"))
        b=int(input("Enter the Ending Range:"))
        print(s[a:b+1],"\n")
    elif(x==3):
        if(s.isalnum()):
            print("Given String is Alphanumeric")
        else:
            print("Given String is NOT Alphanumeric")
    elif(x==4):
        exit()
    else:
        print("Invalid Choice")
        

