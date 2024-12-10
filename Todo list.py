def display_menu():
    print("1. Show the tasks ")
    print("2. Add a tasks ")
    print("3. Remove the task ")
    print("4. Exit.")
    
def show_task(task):
    if not task:
        print("There is no tasks to show.")
    else:
        print("Tasks which are their are: ")
        for i in task:
            print(i)
        
def add_task(task):
    tasks=input("Enter the task: ")
    task.append(tasks)
    print("Task added.")
    
def remove_task(task):
    show_task(task)
    n=int(input("Enter the task number have remove: "))
    if 0<n<=len(task):
        remove=task.pop(n-1)
        print("Removed task is: ", remove)
    else:
        print("cannot remove.")
        
def main():
    task=[]
    while True:
        display_menu()
        a=int(input("Enter your choice: "))
        if(a==1):
            show_task(task)
        elif(a==2):
            add_task(task)
        elif(a==3):
            remove_task(task)
        elif(a==4):
            print("Good Byee..")
            break
        else:
            print("Enter the valid number.")
            
if __name__=="__main__":
    main()