import json
#step 1 : load the json files into python
file=open('birthday.json','r')
content_json=file.read()
file.close()
birthday_dic =json.loads(content_json)

#step 2: display the menu
while True:
    print("""
    Welcome to the birthday dictionary
    ==================================
    1 - Get a birthday date
    2 - Add a birthday date
    3 - Delete birthday date
    4 - Exit birthday dictionnary
    """)
    menu_selected=int(input("Type a number:"))
    #1 - Get a birthday date==========================================
    if menu_selected==1:
        # retrieve birthdate from a name
        search_name = input("Who 's birthday do you want to look up ? ")
        search_name = search_name.lower()
        while(search_name not in birthday_dic):
                print("This name does not exist. Please insert a new name:")
                search_name = input("Who 's birthday do you want to look up ? ")
                search_name = search_name.lower()


        birthday_date = birthday_dic[search_name]
        #change the name into capital letter to print out
        printed_name_list = search_name.split(' ')
        printed_name = printed_name_list[0].capitalize() + ' ' + printed_name_list[1].capitalize()

        #print the name
        print("{}'s birthday is {}".format(printed_name, birthday_dic[search_name]))
    #2 - Add a birthday date==========================================
    elif menu_selected==2:
        name=input("Insert a name:")
        birthday_date=input("Insert a date:")
        birthday_dic[name]=birthday_date
    #3 - Delete birthday date=========================================
    elif menu_selected==3:
        print("Here we have the list of the people into your birthday dictionnary")
        for k in birthday_dic.keys():
            printed_name_list = k.split(' ')
            printed_name = printed_name_list[0].capitalize() + ' ' + printed_name_list[1].capitalize()
            print(printed_name)
        print("=====================================")
        name_delete=input("Insert the name you want to delete")
        name_delete=name_delete.lower()
        while name_delete not in birthday_dic:
            print("This name does not exist. Please insert a new one")
            name_delete = input("Insert the name you want to delete")
            name_delete = name_delete.lower()
        birthday_dic.pop("name_delete")
    #4 - Exit=============================================================
    elif menu_selected==4:
        updated_dic_json=json.dumps(birthday_dic)
        f=open('birthday.json','w')
        f.write(updated_dic_json)
        f.close()
        break
    else:
        print("You insert a wrong value please try again.")









