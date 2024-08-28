# list=["abc", 56, False, 56 ,78]


# a=0
# while (a<(len(list))) :
#     print(list[a])
#     a+=1

# print(len(list))

# mult table of a give numb upto 10

# numb = int(input("enter a number to print its table: "))


# for i in range(1,11):

#     pro = numb*i
#     print(pro)

#     i+=1


# greeting people whos ename starts with s; 

# l= ["harry"," sunny", "soham", "sardar" ]

# for i in l:
#     if (i.startswith("s")):
#         print(f"hello {i}")



# i= 1
# n = int(input("enter the number you want to print the table of\n"))

# while(i<11):
#     print(f"{n} x {i} = {i*n} ")
#     i+=1


# to check if a number is prime

n = int(input("enter a number"))
check = False

for i in range (2, n):
    if(n%i == 0):
        print( "the number is not prime")
        check=True
        break
   

if(check == False):
    print (f" {n}  is a prime number")