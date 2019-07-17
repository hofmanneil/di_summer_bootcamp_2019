import json
##################################################
# Function definition
def convert_name_into_capital(name):
    name_list = name.split(' ')
    name_capital = name_list[0].capitalize() + ' ' + name_list[1].capitalize()
    return name_capital


def get_birthday_date():
    print("Here we have the list of the people into your birthday dictionnary")
    for k in birthday_dic.keys():
        printed_name = convert_name_into_capital(k)
        print(printed_name)
    print("=====================================")
    # retrieve birthdate from a name
    search_name = input("Who 's birthday do you want to look up ? ")
    search_name = search_name.lower()
    while (search_name not in birthday_dic):
        print("This name does not exist. Please insert a new name:")
        search_name = input("Who 's birthday do you want to look up ? ")
        search_name = search_name.lower()

    birthday_date = birthday_dic[search_name]
    # change the name into capital letter to print out
    printed_name = convert_name_into_capital(search_name)

    # print the name
    print("{}'s birthday is {}".format(printed_name, birthday_dic[search_name]))

def add_birthday_date():
    name = input("Insert a name:")
    name = name.lower()
    birthday_date = input("Insert a date (DD/MM/YYYY):")
    birthday_dic[name] = birthday_date

    printed_name = convert_name_into_capital(name)

    # print the name
    print("{}'s birthday is {}".format(printed_name, birthday_dic[name]))

def delete_birthday_date():
    print("Here we have the list of the people into your birthday dictionnary")
    for k in birthday_dic.keys():
        printed_name=convert_name_into_capital(k)
        print(printed_name)
    print("=====================================")
    name_delete = input("Insert the name you want to delete:")
    name_delete = name_delete.lower()
    while name_delete not in birthday_dic:
        print("This name does not exist.")
        name_delete = input("Insert the name you want to delete:")
        name_delete = name_delete.lower()
    birthday_dic.pop(name_delete)
    print("{} has been deleted".format(name_delete))

def save_to_json():
    updated_dic_json = json.dumps(birthday_dic)
    f = open('birthday.json', 'w')
    f.write(updated_dic_json)
    f.close()

def load_from_json():
    file = open('birthday.json', 'r')
    content_json = file.read()
    file.close()
    b = json.loads(content_json)
    return b

################################################
#step 1 : load the json files into python
birthday_dic=load_from_json()

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
        get_birthday_date()
    #2 - Add a birthday date==========================================
    elif menu_selected==2:
        add_birthday_date()
    #3 - Delete birthday date=========================================
    elif menu_selected==3:
        delete_birthday_date()
    #4 - Exit=============================================================
    elif menu_selected==4:
        save_to_json()
        break
    else:
        print("You insert a wrong value please try again.")









