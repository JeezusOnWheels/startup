import csv
import datetime
from dateutil import parser
global ListboxList
def find_item_date_and_name(item_id,items_access_copy,good_food_types):

    i = 0
    arr = []
    for row in items_access_copy:
        #print(row)
        if i == 0:
            i = i + 1
        else:
            if int(row[0]) == item_id and row[2] in good_food_types:#we have found the item, now access the exp date
                exp_date = parser.parse(row[3])
                name = row[1]
                arr.append(exp_date)
                arr.append(name)
    return arr
def start(ID):
    good_food_types = ["Fruit", "Beverages", "Baking", "Vegetables", "Condiments", "Meats","Breads & Cereal", "Entrees","Diary","Snacks","Desserts","Seafood","Candy","snacks","Baby food","Legumes","Soups","Sauces","Sides"]
    ListboxList = []
    items = open("ProductDatabase.csv", "r")
    users = open("users.csv", "r")
    items_access = csv.reader(items)
    items_access_copy = []
    users_access = csv.reader(users)
    user_id = int(ID)#This will depend on the USER!!! CHANGE ME IN THE GUI
    user_items = []
    for row in items_access:
        items_access_copy.append(row)
    i = 0
    for row in users_access:
        if i == 0:
            i = i + 1 #IGNORE THE HEADER
        else:
            if int(row[0]) == user_id:#we have found the user, access their items
                exp_date_and_name = find_item_date_and_name(int(row[1]),items_access_copy,good_food_types)
                current_date = datetime.datetime.now()
                print(exp_date_and_name)
                if exp_date_and_name != []:
                    ListboxList.append(str(exp_date_and_name[1]) + " will expire in " + str((exp_date_and_name[0] - current_date).days) + " days")
                print(ListboxList)

    return ListboxList
