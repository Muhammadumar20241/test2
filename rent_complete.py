






import telebot
from telebot import types
import pymysql
import io
from io import BytesIO
from telebot.types import InputMediaPhoto
import ast  # Importing the ast module to safely evaluate the string representation of the list


bot = telebot.TeleBot("7760779689:AAGIxP8oRaVqAvKqUs_hL5FyZoP5HV7_phs")

b =""
tell =""
full_nam =""
house_id =""
descrioption =""
permission =int(0)
status ="Unsold"
media = []
q =""
q2 =""
@bot.message_handler(commands=['start'])
def main(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📜Listings")
    btn2 = types.KeyboardButton("🏠Housing")
    markup1.row(btn1)
    markup1.row(btn2)
    
    bot.send_message(message.chat.id, "Hello world", reply_markup=markup1)

@bot.message_handler(func=lambda message: True)
def main2(message):
    if message.text.lower().strip() == "🏠housing":
                
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("📱Register with Tell")
        markup1.row(btn1)
  
        btn2 = types.KeyboardButton("🏠List of housing(personal)")
        btn3 =types.KeyboardButton("📜Listings")
        
        markup1.row(btn2,btn3)        
        
        btn5 =types.KeyboardButton("⛔️Reject")
        btn6 =types.KeyboardButton("✅Accept")
        markup1.row(btn5,btn6)
        
        
        btn7 =types.KeyboardButton("🔙Back")
        btn4 =types.KeyboardButton("➕Add")
        markup1.row(btn4,btn7)
        
        
        
        
        bot.send_message(message.chat.id, "Pls choose from following",reply_markup=markup1)
    elif message.text.lower().strip() =="🔙back":
        
        
        
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("📜Listings")
        btn2 = types.KeyboardButton("🏠Housing")
        markup1.row(btn1)
        markup1.row(btn2)
        bot.send_message(message.chat.id, "Main page",reply_markup=markup1)

    elif message.text.lower().strip() =="📱register with tell":
        
        
        def tell_num(message):
            global tell
            tell =message.text.strip()
            bot.send_message(message.chat.id, "Pls write your full name")
            bot.register_next_step_handler(message, full_name)
            
            
        
        def full_name(message):
            global full_nam, tell
            
            full_nam =message.text.lower().strip()
            
            a =message.chat.id
            
            try:
                connection = pymysql.connect(
                    host='localhost',
                    user='muhamm37_zebo',
                    password='umar022004',
                    database='muhamm37_zebo',
                    port=3306,
                    cursorclass=pymysql.cursors.DictCursor
                )
                print("successfully connected...")
                print('#' * 20)
                try:
                    with connection.cursor() as cursor:
                        create_table_query = f"CREATE TABLE IF NOT EXISTS list_renters(id int AUTO_INCREMENT,chat_id varchar(50), tell varchar(100), name varchar(50), PRIMARY KEY(id));"
                        cursor.execute(create_table_query)
                        print("table created....")

                        select_query = f"SELECT * FROM list_renters WHERE chat_id = %s"
                        cursor.execute(select_query, (a,))
                        result = cursor.fetchone()

                        if result:
                            bot.send_message(message.chat.id, "You have already registered")
                        else:
                            insert_query = f"INSERT INTO list_renters(chat_id, tell, name) VALUES (%s, %s, %s)"
                            cursor.execute(insert_query, (a, tell, full_nam))
                            connection.commit()
                            bot.send_message(message.chat.id, "Success")

                finally:
                    connection.close()

            except Exception as ex:
                print("connection refused...")
                print(ex)
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        bot.send_message(message.chat.id,"📲Pls send your phone number !")
        bot.register_next_step_handler(message, tell_num)




    elif message.text.lower().strip() =="➕add":
        
        a =message.chat.id
        try:
            connection = pymysql.connect(
                host='localhost',
                user='muhamm37_zebo',
                password='umar022004',
                database='muhamm37_zebo',
                port=3306,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("successfully connected...")
            print('#' * 20)
            try:
                with connection.cursor() as cursor:
                    create_table_query = f"CREATE TABLE IF NOT EXISTS list_renters(id int AUTO_INCREMENT,chat_id varchar(50), tell varchar(100), name varchar(50), PRIMARY KEY(id));"
                    cursor.execute(create_table_query)
                    print("table created....")

                    select_query = f"SELECT * FROM list_renters WHERE chat_id = %s"
                    cursor.execute(select_query, (a,))
                    result = cursor.fetchone()

                    if result:
                        
    
                        def user_desc(message):
                            global descrioption, permission
                            
                            descrioption =message.text.lower().strip()
                            bot.send_message(message.chat.id, "Pls send pic")
                            permission +=1
                            
                        
                        
                        
                        
                        
                        
                        
                        def user_id(message):
                            global house_id, b, permission
                            
                            
                            house_id =message.text.strip().lower()
                            b =message.text.strip().lower()
                            a =message.chat.id
                            
                            
                            try:
                                connection = pymysql.connect(
                                    host='localhost',
                                    user='muhamm37_zebo',
                                    password='umar022004',
                                    database='muhamm37_zebo',
                                    port=3306,
                                    cursorclass=pymysql.cursors.DictCursor
                                )
                                print("successfully connected...")
                                print('#' * 20)
                                try:
                                    with connection.cursor() as cursor:
                                        create_table_query = f"CREATE TABLE IF NOT EXISTS id_list_house(id int AUTO_INCREMENT,chat_id varchar(50), house_id varchar(50), PRIMARY KEY(id));"
                                        cursor.execute(create_table_query)
                                        print("table created....")
                
                                        select_query = f"SELECT * FROM id_list_house WHERE house_id = %s"
                                        cursor.execute(select_query, (house_id,))
                                        result = cursor.fetchone()
                
                                        if result:
                                            bot.send_message(message.chat.id, "Sorry this id is taken try another!")
                                            
                                            
                                        else:
                                            
                                            
                                            
                                            # def user_desc(message):
                                            #     global descrioption, permission
                                                
                                            #     descrioption =message.text.lower().strip()
                                            #     permission +=1
                                                
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            insert_query = f"INSERT INTO id_list_house(chat_id, house_id) VALUES (%s, %s)"
                                            cursor.execute(insert_query, (a, house_id))
                                            connection.commit()
                                            
                                            
                                            
                                            bot.send_message(message.chat.id, "Write descrioption for your house.\nEx:\nClient: +998901228929\nRoom: 3\nCost: 200-200$\nLocation: Chilonzor")
                                            bot.register_next_step_handler(message, user_desc)
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                
                                finally:
                                    connection.close()
                
                            except Exception as ex:
                                print("connection refused...")
                                print(ex)
                            
                            
                            
                        
                        
                        
                        
                        
                        
                        
                        bot.send_message(message.chat.id, "Pls write id for a house\nEx:u15090")
                        bot.register_next_step_handler(message, user_id)
                        
                    else:
                        
                        bot.send_message(message.chat.id, "Sorry, you have to register first")

            finally:
                connection.close()

        except Exception as ex:
            print("connection refused...")
            print(ex)
      
    

    elif message.text.lower().strip() == "📜listings":
        global permission, q, q2, b  # Declare all global variables here
        id_house_rent = []  # Initialize as a list
    
        try:
            connection = pymysql.connect(
                host='localhost',
                user='muhamm37_zebo',
                password='umar022004',
                database='muhamm37_zebo',
                port=3306,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Successfully connected...")
            print('#' * 20)
    
            with connection.cursor() as cursor:
                query = f"SELECT * FROM id_list_house"
                cursor.execute(query)
                users = cursor.fetchall()
    
                for user in users:
                    id_house_rent.append(user['house_id'])  # Append house_id to the list
    
        except Exception as ex:
            print("Connection failed ....")
            print(ex)
    
        finally:
            if connection:
                connection.close()
        
        
            
        r = len(id_house_rent)
        q3 = [q2]
    
        place = 0
        counter = 0
    
        for i in id_house_rent:
            counter += 1
            if i == q:
                place = counter
                break  # Stop when the item is found to avoid redundant checks
    
        # Handle index out of range by resetting place to 0 if it exceeds r
        if place >= r:
            place = 0

        q2 = id_house_rent[place]  # q2 assignment should occur after the loop
        print("q2: ",q2)
        print("Id_house",id_house_rent)
            
        print("Place: ",place)
        print("Counter: ",counter)
        
        
        # print("q1: ",q)
        place = int(-1)
        counter = int(0)
        
        
        try:
            connection = pymysql.connect(
                host='localhost',
                user='muhamm37_zebo',
                password='umar022004',
                database='muhamm37_zebo',
                port=3306,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Successfully connected...")
            print('#' * 20)
    
            with connection.cursor() as cursor:
                for table in id_house_rent:
                    # Fetch data from each table
                    query = f"SELECT description, status, photo, callback FROM {table}"
                    cursor.execute(query)
                    users = cursor.fetchall()
    
                    info = ""  # Accumulate description and status
                    media = []  # To store InputMediaPhoto objects
                    call2 = ""  # To store unique callbacks
                    info4 = ""
    
                    for user in users:
                        info2 = f"☑️Description:\n{user['description']}\n"
                        info3 = f"{user['status']}\n"
                        call = f"{user['callback']}\n"
    
                        # Check if the callback is unique
                        for single_call in call.splitlines():
                            if single_call not in call2.splitlines():
                                call2 += f"{single_call}\n"
    
                        # Accumulate description and status in the info string
                        if info2 not in info:
                            info += info2
    
                        if info3 != info4:
                            for i in info3.split():
                                if i.lower().strip() == "sold":
                                    info3 = ""  # Clear info3 if sold
                                else:
                                    pass
    
                            info4 += info3  # Append info3 to info4
                            info += f"☑️Status: {info3}\n"  # Add updated info4 to info with a newline
    
                        # Handle photo if it exists
                        if user['photo'] is not None:
                            photo_data = user['photo']
                            if len(photo_data) > 0:
                                photo_file = BytesIO(photo_data)
                                media.append(InputMediaPhoto(photo_file))
                            else:
                                print("Photo data is empty.")
                        else:
                            print("No photo data available for this entry.")
    
                    # Send media group only if there are photos
                    if media:
                        try:
                            # Use the global q variable
                            q = call2.strip()
    
                            markup1 = types.InlineKeyboardMarkup()
                            btn1 = types.InlineKeyboardButton("Cancel", callback_data="back")
                            btn2 = types.InlineKeyboardButton("Accept", callback_data=f"{q}")
                            markup1.row(btn1, btn2)
                            btn3 = types.InlineKeyboardButton("Next", callback_data=f"{q2}")
                            markup1.row(btn3)
    
                            bot.send_media_group(message.chat.id, media)
                            bot.send_message(message.chat.id, info, reply_markup=markup1)
                            # bot.send_message(message.chat.id, call2.strip())
                            print("q1: ",q)

                            break  # Exit the loop after sending the first media group
                        except Exception as e:
                            print(f"Failed to send media group: {e}")
                    else:
                        print("No photos to send.")
    
                    # Reset for the next table
                    info = ""
                    media = []
                    call2 = ""
    
        except Exception as ex:
            print("Connection failed ....")
            print(ex)
    
        finally:
            if connection:
                connection.close()


    elif message.text.lower().strip() == "🏠list of housing(personal)":
        a = str(message.chat.id)
        id_house_rent = []
    
        try:
            connection = pymysql.connect(
                host='localhost',
                user='muhamm37_zebo',
                password='umar022004',
                database='muhamm37_zebo',
                port=3306,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Successfully connected for personal listings...")
            print('#' * 20)
    
            with connection.cursor() as cursor:
                cursor.execute("SELECT chat_id, house_id FROM id_list_house")
                users = cursor.fetchall()
                id_house_rent = [user['house_id'] for user in users if user['chat_id'].strip().lower() == a]
    
        except Exception as ex:
            print("Connection failed while fetching personal house IDs...")
            print(ex)
        finally:
            if connection:
                connection.close()
        
        
        if not id_house_rent:
            bot.send_message(message.chat.id, "You have no personal listings.")
            return  # Exit if there are no listings
        
        
        
        # Fetch listings for each personal house ID
        for table in id_house_rent:
            try:
                connection = pymysql.connect(
                    host='localhost',
                    user='muhamm37_zebo',
                    password='umar022004',
                    database='muhamm37_zebo',
                    port=3306,
                    cursorclass=pymysql.cursors.DictCursor
                )
                print("Successfully connected for personal listings details...")
                print('#' * 20)
    
                with connection.cursor() as cursor:
                    cursor.execute(f"SELECT description, status, photo, callback FROM {table}")
                    users = cursor.fetchall()
    
                    info = ""
                    media = []
                    call2 = ""
                    info4 = ""
    
                    for user in users:
                        info2 = f"☑️Description:\n{user['description']}\n"
                        info3 = f"☑️Status: {user['status']}\n"
                        call = f"{user['callback']}\n"
    
                        for single_call in call.splitlines():
                            if single_call not in call2.splitlines():
                                call2 += f"{single_call}\n"
    
                        if info2 not in info:
                            info += info2
                        if info3 != info4 and "sold" not in info4:
                            info4 += "☑️Status: sold\n"
                            info += info4
    
                        if user['photo']:
                            photo_file = BytesIO(user['photo'])
                            media.append(InputMediaPhoto(photo_file))
    
                    if media:
                        
                        # global q
                    
                        q =call2.strip()
                        
                        markup1 = types.InlineKeyboardMarkup()
                        btn1 = types.InlineKeyboardButton("Cancel", callback_data="back")
                        btn2 = types.InlineKeyboardButton("Accept", callback_data=f"{q}")
                        markup1.row(btn1, btn2)
                        # btn3 =types.InlineKeyboardButton("Next",callback_data =f"{q}")
                        # markup1.row(btn3)
                        
                        bot.send_media_group(message.chat.id, media)
                        bot.send_message(message.chat.id, f"{call2}"+info)
                        # bot.send_message(message.chat.id, call2.strip())
                        
                        
                        # markup1 = types.InlineKeyboardMarkup()
                        # btn1 = types.InlineKeyboardButton("Cancel", callback_data="back")
                        # btn2 = types.InlineKeyboardButton("Accept", callback_data=f"{call2.strip()}")
                        # markup1.row(btn1, btn2)
    
                        # bot.send_media_group(message.chat.id, media)
                        # bot.send_message(message.chat.id, info, reply_markup=markup1)
                    else:
                        bot.send_message(message.chat.id, "Sorryan bro")
    
            except Exception as ex:
                print("Connection failed while fetching personal listings details...")
                print(ex)
            finally:
                if connection:
                    connection.close()


    elif message.text.lower().strip() == "✅accept":
        
        
        def user_house(message):
            w = message.text.lower().strip()  # House ID
            e = "sold"  # Value to insert
            print(w)
            id_house_rent = []  # Initialize as a list
        
            try:
                connection = pymysql.connect(
                    host='localhost',
                    user='muhamm37_zebo',
                    password='umar022004',
                    database='muhamm37_zebo',
                    port=3306,
                    cursorclass=pymysql.cursors.DictCursor
                )
                print("Successfully connected...")
                print('#' * 20)
        
                with connection.cursor() as cursor:
                    query = f"SELECT * FROM id_list_house"
                    cursor.execute(query)
                    users = cursor.fetchall()
        
                    for user in users:
                        id_house_rent.append(user['house_id'])  # Append house_id to the list
        
            except Exception as ex:
                print("Connection failed ....")
                print(ex)
        
            finally:
                if connection:
                    connection.close()
                        
                        
            # a =['u16090','u15080','u15067']
            
            # w ="u15080"
            
            found =False
            
            
            for i in id_house_rent:
                if i.lower().strip() ==w.lower().strip():
                    found =True
                else:
                    pass
                
                # print(i)
            
            if not found:
                bot.send_message(message.chat.id, "Sorry id not found!")
                # b ="m*"
            
            
            # print(b)

            
            
            
            
            
            
            
            
            
                
            try:
                connection = pymysql.connect(
                    host='localhost',
                    user='muhamm37_zebo',
                    password='umar022004',
                    database='muhamm37_zebo',
                    port=3306,
                    cursorclass=pymysql.cursors.DictCursor
                )
                print("Successfully connected...")
                print('#' * 20)
        
                with connection.cursor() as cursor:
                    for table in w:
                        # Fetch data from each table
                        query = f"SELECT description, status, photo, callback FROM {w}"
                        cursor.execute(query)
                        users = cursor.fetchall()
        
                        info = ""  # Accumulate description and status
                        media = []  # To store InputMediaPhoto objects
                        call2 = ""  # To store unique callbacks
                        info4 = ""
        
                        for user in users:
                            info2 = f"☑️Description:\n{user['description']}\n"
                            info3 = f"{user['status']}\n"
                            call = f"{user['callback']}\n"
        
                            # Check if the callback is unique
                            for single_call in call.splitlines():
                                if single_call not in call2.splitlines():
                                    call2 += f"{single_call}\n"
        
                            # Accumulate description and status in the info string
                            if info2 not in info:
                                info += info2
        
                            if info3 != info4:
                                for i in info3.split():
                                    if i.lower().strip() == "sold":
                                        info3 = ""  # Clear info3 if sold
                                        info3 ="Sold"
                                    else:
                                        pass
        
                                info4 += info3  # Append info3 to info4
                                info += f"☑️Status: {info3}\n"  # Add updated info4 to info with a newline
        
                            # Handle photo if it exists
                            
                        # bot.send_message(message.chat.id, info4)
                        # bot.send_message(message.chat.id, info)
                        
                            
                            
                        
                        # Reset for the next table
                        # info = ""
                        media = []
                        call2 = ""
                    # bot.send_message(message.chat.id, info4)
                    # bot.send_message(message.chat.id, info)
                    
                    # Find the position of the word "Description:"
                    b = info.find("Description:")

                    # Create a new string starting after "Description:" (i.e., b + length of "Description:")
                    info = info[b + len("Description:"):].strip()

                    
                    
                    insert_query = f"INSERT INTO {w}(description,status) VALUES (%s,%s)"
                    cursor.execute(insert_query, (info,e))
                    connection.commit()
                    bot.send_message(message.chat.id, "Success!")
                                                    
                    
        
            except Exception as ex:
                print("Connection failed ....")
                print(ex)
        
            finally:
                if connection:
                    connection.close()

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            # id_house =[]
            # decs =[]
            # callback =[]
            # status2 =[]
            # status =[]
            # try:
            #     connection = pymysql.connect(
            #         host='localhost',
            #         user='muhamm37_zebo',
            #         password='umar022004',
            #         database='muhamm37_zebo',
            #         port=3306,
            #         cursorclass=pymysql.cursors.DictCursor
            #     )
            #     print("Successfully connected...")
            #     print('#' * 20)
        
            #     with connection.cursor() as cursor:
            #         query = f"SELECT * FROM {w}"
            #         cursor.execute(query)
            #         users = cursor.fetchall()
                    
            #         for user in users:
            #             decs.append(user['description'])
            #             status2.append(user['status'])
                    
                    
            #         status =str(status)
            #         status2 =str(status)
                    
                    
            #         if status2 not in status:
            #             info += info2

            #         if info3 != info4:
            #             for i in info3.split():
            #                 if i.lower().strip() == "sold":
            #                     info3 = ""  # Clear info3 if sold
            #                 else:
            #                     pass

            #             info4 += info3  # Append info3 to info4
            #             info += f"☑️Status: {info3}\n"  # Add updated info4 to info with a newline

                    
                    
                    
                    
            #         insert_query = f"INSERT INTO {w}(status) VALUES (%s)"
            #         cursor.execute(insert_query, (e))
            #         connection.commit()
            #         bot.send_message(message.chat.id, "A'lo !")
                                            
                    
        
            # except Exception as ex:
            #     print("Connection failed ....")
            #     print(ex)
        
            # finally:
            #     if connection:
            #         connection.close()
            
        bot.send_message(message.chat.id, "Write the house_ID: ")
        bot.register_next_step_handler(message, user_house)
 
    elif message.text.lower().strip() == "⛔️reject":
        
        
        
        def user_rej(message):
            w =message.text.strip()
            bot.send_message(message.chat.id, "Your reject has accepted")
        
        
        
        
        
        
        
        bot.send_message(message.chat.id, "Write your house_ID: ")
        bot.register_next_step_handler(message, user_rej)








@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    global permission
    if permission ==1:
            
        
        try:
            global b, descrioption, status, media
            
            # MySQL connection and cursor setup inside the handle_photo function
            db = pymysql.connect(
                host="localhost",  
                user="muhamm37_zebo",  
                password="umar022004",  
                database="muhamm37_zebo"  
            )
            cursor = db.cursor()
    
            # Create a table for storing images if not exists
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS {b} (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                user_id BIGINT,
                                photo LONGBLOB,description varchar(300),status varchar(300),callback varchar(200)
                            )''')
            db.commit()
    
            # Get photo ID and download the file
            file_info = bot.get_file(message.photo[-1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            
            # Insert the photo into the MySQL database
            sql = f"INSERT INTO {b} (user_id, photo, description, status, callback) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (message.chat.id, downloaded_file, descrioption, status, b))
            db.commit()
    
            bot.send_message(message.chat.id, "Success")
            
            
            # # Retrieve all photos from the database for the user
            # cursor.execute(f"SELECT photo FROM {b} WHERE user_id = %s", (message.chat.id,))
            # results = cursor.fetchall()
                
            # if results:
            #     media = []
            #     for result in results:
            #         # Create an InputMediaPhoto object from the binary data and add it to the media list
            #         media.append(types.InputMediaPhoto(io.BytesIO(result[0])))
            
            #     try:
            #         connection = pymysql.connect(
            #             host='localhost',
            #             user='muhamm37_zebo',
            #             password='umar022004',
            #             database='muhamm37_zebo',
            #             port=3306,
            #             cursorclass=pymysql.cursors.DictCursor
            #         )
            #         print("Successfully connected...")
            #         print('#' * 20)
            
            #         with connection.cursor() as cursor:
            #             query = f"SELECT * FROM {b}"
            #             cursor.execute(query)
            #             users = cursor.fetchall()
            
            #             info = ""
            #             info2 =""
            #             for user in users:
            #                 info += f"☑️Description:\n{user['description']}\n☑️Status:\n{user['status']}\n"
            #                 if info.lower().strip() ==info2.lower():
            #                     pass
            #                 else:
            #                     info2 += f"☑️Description:\n{user['description']}\n☑️Status:\n{user['status']}\n"
                            
            #     except Exception as ex:
            #         print("Connection failed ....")
            #         print(ex)
            
            #     finally:
            #         if connection:
            #             connection.close()
            #     # Send the media group (all images simultaneously)
            #     bot.send_media_group(message.chat.id, media)
            
            #     # Send the text information after sending the photos
            #     bot.send_message(message.chat.id, info2)
            
            
            # else:
            #     bot.send_message(message.chat.id, "No pictures found.")
            #     permission -=1
                
        except Exception as e:
            bot.send_message(message.chat.id, "Error occurred: " + str(e))
            permission -=1

        finally:
            cursor.close()
            db.close()







    
    
@bot.callback_query_handler(func=lambda callback: True)
def callback(callback):
    global q2, q
    if callback.data ==f"{q2}":
            
        q = q2
    
        id_house_rent = []  # Initialize as a list
    
        try:
            connection = pymysql.connect(
                host='localhost',
                user='muhamm37_zebo',
                password='umar022004',
                database='muhamm37_zebo',
                port=3306,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Successfully connected...")
            print('#' * 20)
    
            with connection.cursor() as cursor:
                query = "SELECT * FROM id_list_house"
                cursor.execute(query)
                users = cursor.fetchall()
    
                for user in users:
                    id_house_rent.append(user['house_id'])
    
        except Exception as ex:
            print("Connection failed ....")
            print(ex)
    
        finally:
            if connection:
                connection.close()
        
        r = len(id_house_rent)
        q3 = [q2]
    
        place = 0
        counter = 0
    
        for i in id_house_rent:
            counter += 1
            if i == q:
                place = counter
                break  
    
        if place >= r:
            place = 0
    
        q2 = id_house_rent[place] if place < r else id_house_rent[0]
        print("q2:", q2)
        print("Place:", place)
        print("Counter:", counter)
    
        try:
            connection = pymysql.connect(
                host='localhost',
                user='muhamm37_zebo',
                password='umar022004',
                database='muhamm37_zebo',
                port=3306,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Successfully connected...")
            print('#' * 20)
    
            with connection.cursor() as cursor:
                for table in q3:
                    query = f"SELECT description, status, photo, callback FROM {table}"
                    cursor.execute(query)
                    users = cursor.fetchall()
    
                    info = ""
                    media = []
                    call2 = ""
                    info4 = ""
    
                    for user in users:
                        info2 = f"☑️Description:\n{user['description']}\n"
                        info3 = f"{user['status']}\n"
                        call = f"{user['callback']}\n"
    
                        if call.strip() not in call2.splitlines():
                            call2 += call.strip() + "\n"
    
                        if info2 not in info:
                            info += info2
    
                        if info3 != info4:
                            for i in info3.split():
                                if i.lower().strip() == "sold":
                                    info3 = ""  # Clear info3 if sold
                                    info3 = "Sold"
                                else:
                                    pass
    
                            info4 += info3  # Append info3 to info4
                            info += f"☑️Status: {info3}\n"  # Add updated info4 to info with a newline
    
        
                        if user['photo']:
                            photo_data = user['photo']
                            if photo_data:
                                photo_file = BytesIO(photo_data)
                                media.append(InputMediaPhoto(photo_file))
    
                    if media:
                        try:
                            q = call2.strip()
    
                            markup1 = types.InlineKeyboardMarkup()
                            btn1 = types.InlineKeyboardButton("Cancel", callback_data="back")
                            btn2 = types.InlineKeyboardButton("Accept", callback_data=f"{q}")
                            btn3 = types.InlineKeyboardButton("Next", callback_data=f"{q2}")
                            markup1.row(btn1, btn2)
                            markup1.row(btn3)
                            bot.send_media_group(callback.message.chat.id, media)
                            bot.send_message(callback.message.chat.id, info, reply_markup=markup1)
                            # bot.send_message(callback.message.chat.id, call2.strip())
                            print("q:", q)
    
                            break
                        except Exception as e:
                            print(f"Failed to send media group: {e}")
    
        except Exception as ex:
            print("Connection failed ....")
            print(ex)
    
        finally:
            if connection:
                connection.close()
    
        
        
    elif callback.data == f"{q}":
    
        id_house_rent = []  # Initialize as a list
    
        try:
            connection = pymysql.connect(
                host='localhost',
                user='muhamm37_zebo',
                password='umar022004',
                database='muhamm37_zebo',
                port=3306,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Successfully connected...")
            print('#' * 20)
    
            with connection.cursor() as cursor:
                query = "SELECT * FROM id_list_house"
                cursor.execute(query)
                users = cursor.fetchall()
    
                for user in users:
                    id_house_rent.append(f"{user['chat_id']}, {user['house_id']}")  # Append formatted string to the list
    
        except Exception as ex:
            print("Connection failed ....")
            print(ex)
    
        finally:
            if connection:
                connection.close()
    
        
        b =str(callback.message.chat.id)
        # id_house_rent =str(id_house_rent)
        # id_house_rent = id_house_rent.replace("[", "").replace("]", "")
        
        # id_house_rent =id_house_rent.split()
        
        
        
        # a = ['1271233612, u15053', '1271233612, u16090', '71233612, u17079', '33612, u13087', '1271212, u98078']
        # b = "u16090"
        id_house_list2 = []

        for item in id_house_rent:
            # Split each element by comma and strip spaces
            item_id, item_code = item.split(',')
            item_id = item_id.strip()
            item_code = item_code.strip()
            
            # Check if item_code matches b
            if item_code == q:
                id_house_list2.append(item_id)  # Add the matching id to id_house_list2




        
        
        
        
        # # a = ['1271233612, u15053', '1271233612, u16090', '71233612, u17079', '33612, u13087', '1271212, u98078']
        # id_house_list2 = []

        # for item in id_house_rent:
        #     # Split each element by comma and strip spaces
        #     item_id, item_code = item.split(',')
        #     item_id = item_id.strip()
        #     item_code = item_code.strip()
            
        #     # Check if item_id matches b
        #     if item_id == b:
        #         id_house_list2.append(item_code)  # Add the matching code to id_house_list2

        # print(id_house_list2)
        # id_house_list2 ="1271233612"
        
        # bot.send_message(id_house_list2, "hello world")
        # bot.send_message(callback.message.chat.id, "message sent")
                
        # id_house_list2 = "1271233612"  # Assign the chat ID here directly if known
                
        # Attempt to send the message and catch any errors
        
    
    
        
        # Assuming id_house_list2 is originally in the format of a string that looks like "['1271233612']"
        id_house_list2 = str(id_house_list2)
        
        # Convert the string representation of the list to an actual list
        try:
            id_list = ast.literal_eval(id_house_list2)  # Safely evaluate the string to a list
            chat_id = int(id_list[0])  # Get the first element and convert it to an integer
        except (ValueError, SyntaxError) as e:
            print(f"Error converting id_house_list2 to int: {e}")
            chat_id = None  # Handle the error case
        
        if chat_id is not None:  # Proceed only if chat_id is valid
            msg = f"{q}\nYour house is proposed to a client!"
            try:
                bot.send_message(chat_id, msg)
                bot.send_message(callback.message.chat.id, "Message sent")
                print(f"Message sent to {chat_id}: {msg}")
            except telebot.apihelper.ApiTelegramException as e:
                print(f"Failed to send message to {chat_id}: {e}")
    
        
    
    
    
    
    
    
    
    
    

















bot.polling(none_stop=True)
















































