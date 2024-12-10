def default_view():
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply numbers")
    print("4. Divide numbers")

def add():
    sum=0
    n=input("Enter your values: ").split()
    for i in n:
        sum+=float(i)
    print("Sum: ", sum)
    
def sub():
    a,b=input("Enter yor values: ").split()
    diff=float(a)-float(b)
    print("Subtraction: ", diff)
    
def multi():
    mul=1
    n=input("Enter your values: ").split()
    for i in n:
        mul*=float(i)
    print("Multiplication output: ", mul)

def divide():
    a,b=input("Enter your values: ").split()
    if(b==0.0,0):
        print("Invalid!!")
    else:
        print("Division output: ", float(a)/float(b))

    
def main():
    while True:
        default_view()
        n=int(input("Enter the task you want to do:"))
        if(n==1):
            add()
        elif(n==2):
            sub()
        elif(n==3):
            multi()
        elif(n==4):
            divide()
        else:
            print("Please type a valid number!!")
         
if __name__=="__main__":
    main()