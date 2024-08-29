def add_item(sh_list):
    item=input("enter the item to insert:")
    sh_list.append(item)
    
def search_item(sh_list):
    item=input("enter the item to search:")
    if(item in sh_list):
        print("Item present")
        return True
    
    else:
        print("item does not exist")
        return False
def display_list(sh_list):
    for i in range(len(sh_list)):
        print(sh_list[i])
        print("\n")
def remove_item(sh_list):
    item=input("enter the item to delete:")
    if(item in sh_list):
        sh_list.remove(item)
    else:
        print("already not there")
def binary_search(sh_list,dict1):
    item=input("enter the item to find:")
    for i in range(len(sh_list)):
        p=str(i)
        dict1[p]=sh_list[i]
    values=dict1.values()
    if(item in values):
        print(item[::-1])
    else:
        print("item not found")
flag=True
shopping_list=[]
dict1={}
while(flag):
    print("Which operation do you wish to perform:")
    print("1:For adding an item to the list \n")
    print("2:searching an item in the list \n")
    print("3:displaying  the list \n")
    print("4:removing an item in the list \n")
    print("5:biinary search \n")
    resp=int(input("enter your response:")) 
    if(resp==1):
        add_item(shopping_list)
    elif(resp==2):
        search_item(shopping_list)
    elif(resp==3):
        display_list(shopping_list)
    elif(resp==4):
        remove_item(shopping_list)
    elif(resp==5):
        binary_search(shopping_list,dict1)
    else:
        print("invalid choice")
    ch=input("do you want to perform more actions:Y/N")
    if((ch=='Y')or(ch=='y')):
        flag=True
    else:
        flag=False
            

