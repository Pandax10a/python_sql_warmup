
import dbcreds
import mariadb

conn = mariadb.connect(
user=dbcreds.user, 
password=dbcreds.password,
host=dbcreds.host, 
port=dbcreds.port, 
database=dbcreds.database)

cursor = conn.cursor()
cursor.execute('CALL sales_persons_list()')
result = cursor.fetchall()
cursor.execute('CALL inventory_list()')
result_inventory = cursor.fetchall()
        
cursor.close()
conn.close()


def show_available_staff():
    for x in result:
        print(x[1].decode("UTF-8"))
    try:
        while True:
            user_answer = input('choose a sales person: ')
            if(user_answer == 'rabbit'):
                print('chosen rabbit')
                return user_answer
            elif(user_answer == 'tiger'):
                print('chosen tiger')
                return user_answer
            elif(user_answer == 'horse'):
                print('chosen horse')
                return user_answer
            else:
                print('choose again, type carefully')
    except:
        print('you have not typed in one of the 3 options')



the_chosen_salesperon = show_available_staff()
print(result_inventory)

def item_for_sale(sales_person_id):
    temp_sales_storage=[]
    temp_sales_storage.append(sales_person_id)
    for x in result_inventory:
        print(x[1].decode("UTF-8"), " ", x[2])
    user_choose_item = input('pick an item: ')
    if(user_choose_item == 'grass'):
        temp_sales_storage.append(user_choose_item)
    elif(user_choose_item == 'hay'):
        temp_sales_storage.append(user_choose_item)
    elif(user_choose_item == 'tofu'):
        temp_sales_storage.append(user_choose_item)
    elif(user_choose_item == 'carrot'):
        temp_sales_storage.append(user_choose_item)
    elif(user_choose_item == 'banana'):
        temp_sales_storage.append(user_choose_item)
    conn = mariadb.connect(
    user=dbcreds.user, 
    password=dbcreds.password,
    host=dbcreds.host, 
    port=dbcreds.port, 
    database=dbcreds.database)

    cursor = conn.cursor()
    cursor.execute('CALL sales_persons_list()')
    result = cursor.fetchall()
    cursor.execute('CALL inventory_list()')
    result_inventory = cursor.fetchall()
        
    cursor.close()
    conn.close()

item_for_sale()

    
