import telebot
from telebot import types
import mysql.connector
from mysql.connector import pooling
from threading import Lock
import os
from dotenv import load_dotenv

# Variables
load_dotenv('my.env')
user_lock = Lock()
i = {}
j = {}
channel_id = '@elphii'
# Setup bot token
bot = telebot.TeleBot(os.getenv('TOKEN'))

#######################
###### Setup DB ######
#######################

# Create a connection pool
db_pool = pooling.MySQLConnectionPool(
    pool_name='my_pool',
    pool_size=30,
    pool_reset_session=True,
    host=os.getenv('host'),
    database=os.getenv('db'),
    user=os.getenv('user'),
    password=os.getenv('pass')
)

db_poola = pooling.MySQLConnectionPool(
    pool_name='my_poola',
    pool_size=30,
    pool_reset_session=True,
    host=os.getenv('host'),
    database=os.getenv('db'),
    user=os.getenv('user'),
    password=os.getenv('pass')
)

db_poolb = pooling.MySQLConnectionPool(
    pool_name='my_poolb',
    pool_size=30,
    pool_reset_session=True,
    host=os.getenv('host'),
    database=os.getenv('db'),
    user=os.getenv('user'),
    password=os.getenv('pass')
)

db_poolc = pooling.MySQLConnectionPool(
    pool_name='my_poolc',
    pool_size=30,
    pool_reset_session=True,
    host=os.getenv('host'),
    database=os.getenv('db'),
    user=os.getenv('user'),
    password=os.getenv('pass')
)

db_poold = pooling.MySQLConnectionPool(
    pool_name='my_poold',
    pool_size=25,
    pool_reset_session=True,
    host=os.getenv('host'),
    database=os.getenv('db'),
    user=os.getenv('user'),
    password=os.getenv('pass')
)

# Table

# Delete previous table
#connection = db_poolc.get_connection()
#cursor = connection.cursor()
#cursor.execute("DROP TABLE IF EXISTS users")
#connection.commit()

# Creat new bot table
#connection = db_poolc.get_connection()
#cursor = connection.cursor()
#cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, chat_id BIGINT UNIQUE NOT NULL, username VARCHAR(255), name VARCHAR(255), gender VARCHAR(255), age INT, city VARCHAR(255), photo_id VARCHAR(255), partner_id BIGINT, target VARCHAR(255), bio VARCHAR(255), verify VARCHAR(255))")
#connection.commit()

# DB control
# Get user by photo
def get_user(chat_id):
    connection = db_poolc.get_connection()
    try:
        cursor = connection.cursor()
        query = f"SELECT photo_id FROM users WHERE chat_id = {chat_id}"
        cursor.execute(query)
        user = cursor.fetchone()
        return user[0] if user else None
        connection.commit()
    finally:
        cursor.close()
        connection.close()

# Get user by id
def get_userid(chat_id):
    connection = db_poola.get_connection()
    try:
        cursor = connection.cursor()
        query = f"SELECT chat_id FROM users WHERE chat_id = {chat_id}"
        cursor.execute(query)
        user = cursor.fetchone()
        return user[0] if user else None
        connection.commit()
    finally:
        cursor.close()
        connection.close()

# Add user
def add_user(chat_id, username):
    connection = db_poola.get_connection()
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO users (chat_id, username) VALUES ({chat_id}, '{username}')"
        cursor.execute(query)
        connection.commit()
    finally:
        cursor.close()
        connection.close()

# Update verify
def update_verify(chat_id):
    connection = db_poola.get_connection()
    try:
        cursor = connection.cursor()
        query = f"UPDATE users SET verify = 'yes' WHERE chat_id = {chat_id}"
        cursor.execute(query)
        connection.commit()
    finally:
        cursor.close()
        connection.close()

# Delete user
def delete_user(chat_id):
    connection = db_poola.get_connection()
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM users WHERE chat_id = {chat_id}"
        cursor.execute(query)
        connection.commit()
    finally:
        cursor.close()
        connection.close()

# Update name
def update_name(chat_id, name):
    connection = db_poola.get_connection()
    try:
        cursor = connection.cursor()
        query = f"UPDATE users SET name = '{name}' WHERE chat_id = {chat_id}"
        cursor.execute(query)
        connection.commit()
    finally:
        cursor.close()
        connection.close()

# Update age
def update_age(chat_id, age):
    connection = db_poolb.get_connection()
    try:
        cursor = connection.cursor()
        query = f"UPDATE users SET age = {age} WHERE chat_id = {chat_id}"
        cursor.execute(query)
        connection.commit()
    finally:
        cursor.close()
        connection.close()

# Update gender
def update_gender(chat_id, gender):
    connection = db_poolb.get_connection()
    try:
        cursor = connection.cursor()
        query = f"UPDATE users SET gender = '{gender}' WHERE chat_id = {chat_id}"
        cursor.execute(query)
        connection.commit()
    finally:
        cursor.close()
        connection.close()

# Update photo
def update_photo(chat_id, photo_id):
    connection = db_poolb.get_connection()
    try:
        cursor = connection.cursor()
        query = f"UPDATE users SET photo_id = '{photo_id}' WHERE chat_id = {chat_id}"
        cursor.execute(query)
        connection.commit()
    finally:
        cursor.close()
        connection.close()

# Update city
def update_city(chat_id, city):
    connection = db_poolb.get_connection()
    try:
        cursor = connection.cursor()
        query = f"UPDATE users SET city = '{city}' WHERE chat_id = {chat_id}"
        cursor.execute(query)
        connection.commit()
    finally:
        cursor.close()
        connection.close()

# Update target
def update_target(chat_id, target):
    connection = db_poolc.get_connection()
    try:
        cursor = connection.cursor()
        query = f"UPDATE users SET target = '{target}' WHERE chat_id = {chat_id}"
        cursor.execute(query)
        connection.commit()
    finally:
        cursor.close()
        connection.close()

# Update bio
def update_bio(chat_id, bio):
    connection = db_poolc.get_connection()
    try:
        cursor = connection.cursor()
        query = f"UPDATE users SET bio = '{bio}' WHERE chat_id = {chat_id}"
        cursor.execute(query)
        connection.commit()
    finally:
        cursor.close()
        connection.close()

# My profile
def my_profile(chat_id):
    connection = db_poolc.get_connection()
    try:
        cursor = connection.cursor()
        query = f"SELECT name, gender, age, city, photo_id, target, bio, verify FROM users WHERE chat_id = {chat_id}"
        cursor.execute(query)
        result = cursor.fetchone()
        if result[7]:
           profile_text = f"\n وریفای: {'✅'}\n 👤نام: {result[0]}\n ⚧جنسیت: {result[1]}\n 🔢سن: {result[2]}\n 🌇شهر: {result[3]}\n 🎯هدف: {result[5]}\n 🎨بیو: {result[6]}\n"
        else:
           profile_text = f"\n 👤نام: {result[0]}\n ⚧جنسیت: {result[1]}\n 🔢سن: {result[2]}\n 🌇شهر: {result[3]}\n 🎯هدف: {result[5]}\n 🎨بیو: {result[6]}\n"
        bot.send_photo(chat_id, result[4], caption=profile_text)
        connection.commit()
    finally:
        cursor.close()
        connection.close()

# Check gender
def check_gender(chat_id):
    connection = db_poolc.get_connection()
    try:
        cursor = connection.cursor()
        query = f"SELECT gender FROM users WHERE chat_id = {chat_id}"
        cursor.execute(query)
        user = cursor.fetchone()
        return user[0] if user else None
        connection.commit()
    finally:
        cursor.close()
        connection.close()


# show_profiles
# Show boy
def show_profiles_boy(i, chat_id):
    connection = db_pool.get_connection()
    cursor = connection.cursor()
    query = f"SELECT chat_id, name, gender, age, city, photo_id, target, bio, verify FROM users WHERE chat_id != {chat_id} AND gender = 'پسر' AND photo_id IS NOT NULL"
    cursor.execute(query)
    result = cursor.fetchall()
    try:
       r = result[i]
       if r[8]:
          profile_text = f"\n وریفای: {'✅'}\n 👤نام: {r[1]}\n ⚧جنسیت: {r[2]}\n 🔢سن: {r[3]}\n 🌇شهر: {r[4]}\n 🎯هدف: {r[6]}\n 🎨بیو: {r[7]}\n"
       else:
          profile_text = f"\n 👤نام: {r[1]}\n ⚧جنسیت: {r[2]}\n 🔢سن: {r[3]}\n 🌇شهر: {r[4]}\n 🎯هدف: {r[6]}\n 🎨بیو: {r[7]}\n"
       bot.send_photo(chat_id, r[5], caption=profile_text)
       return r[0] if r else None
       connection.commit()
       cursor.close()
       connection.close()
    except IndexError:
       return None
       connection.commit()
       cursor.close()
       connection.close()

# Show girl
def show_profiles_girl(j, chat_id):
    connection = db_pool.get_connection()
    cursor = connection.cursor()
    query = f"SELECT chat_id, name, gender, age, city, photo_id, target, bio, verify FROM users WHERE chat_id != {chat_id} AND gender = 'دختر' AND photo_id IS NOT NULL"
    cursor.execute(query)
    result = cursor.fetchall()
    try:
       r = result[j]
       if r[8]:
          profile_text = f"\n وریفای: {'✅'}\n 👤نام: {r[1]}\n ⚧جنسیت: {r[2]}\n 🔢سن: {r[3]}\n 🌇شهر: {r[4]}\n 🎯هدف: {r[6]}\n 🎨بیو: {r[7]}\n"
       else:
          profile_text = f"\n 👤نام: {r[1]}\n ⚧جنسیت: {r[2]}\n 🔢سن: {r[3]}\n 🌇شهر: {r[4]}\n 🎯هدف: {r[6]}\n 🎨بیو: {r[7]}\n"
       bot.send_photo(chat_id, r[5], caption=profile_text)
       return r[0] if r else None
       connection.commit()
       cursor.close()
       connection.close()
    except IndexError:
       return None
       connection.commit()
       cursor.close()
       connection.close()

# Update partner
def update_partner(chat_id, partner_id):
    connection = db_pool.get_connection()
    try:
        cursor = connection.cursor()
        query = f"UPDATE users SET partner_id = {partner_id} WHERE chat_id = {chat_id}"
        cursor.execute(query)
        connection.commit()
    finally:
        cursor.close()
        connection.close()

def get_partner(chat_id):
    connection = db_pool.get_connection()
    try:
        cursor = connection.cursor()
        query = f"SELECT partner_id FROM users WHERE chat_id = {chat_id}"
        cursor.execute(query)
        user = cursor.fetchone()
        return user[0] if user else None
        connection.commit()
    finally:
        cursor.close()
        connection.close()

# Send profile to
def send_profile_to(chat_id, partner_id):
    connection = db_poold.get_connection()
    try:
        cursor = connection.cursor()
        query = f"SELECT name, gender, age, city, photo_id, target, bio, verify FROM users WHERE chat_id = {chat_id}"
        cursor.execute(query)
        result = cursor.fetchone()
        if result[7]:
           profile_text = f"\n وریفای: {'✅'}\n نام: {result[0]}\n جنسیت: {result[1]}\n سن: {result[2]}\n شهر: {result[3]}\n هدف: {result[5]}\n بیو: {result[6]}\n"
        else:
           profile_text = f"\n نام: {result[0]}\n جنسیت: {result[1]}\n سن: {result[2]}\n شهر: {result[3]}\n هدف: {result[5]}\n بیو: {result[6]}\n"
        bot.send_photo(partner_id, result[4], caption=profile_text)
        connection.commit()
    finally:
        cursor.close()
        connection.close()


#######################
###### Keyboards ######
#######################

# Define main keyboard
def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton('جستجو'))
    keyboard.add(types.KeyboardButton('پروفایل من'))
    keyboard.add(types.KeyboardButton('بازگشت'))
    return keyboard

# Profile keyboard
def profile_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(
        types.InlineKeyboardButton('ویرایش پروفایل', callback_data='edit_profile'),
        types.InlineKeyboardButton('حذف پروفایل', callback_data='delete_profile')
    )
    return markup

# Search keyboard
def search_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(
        types.InlineKeyboardButton('جستجو پسر', callback_data='search_boy'),
        types.InlineKeyboardButton('جستجو دختر', callback_data='search_girl')
    )
    return markup

# In search keyboard
def in_search_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(
        types.InlineKeyboardButton('لایک', callback_data='like'),
        types.InlineKeyboardButton('بعدی', callback_data='next')
    )
    return markup

# Create profile keyboard
def create_profile_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('ساخت پروفایل', callback_data='create_profile'))
    return markup

# Delete profile keyboard
def delete_profile_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('تایید حذف', callback_data='confirm_delete'))
    return markup

# Edit profile keyboard
def edit_profile_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(
        types.InlineKeyboardButton('سن', callback_data='edit_age'),
        types.InlineKeyboardButton('اسم', callback_data='edit_name')
    )
    markup.row(
        types.InlineKeyboardButton('تصویر', callback_data='edit_photo'),
        types.InlineKeyboardButton('جنسیت', callback_data='edit_gender')
    )
    markup.row(
        types.InlineKeyboardButton('هدف', callback_data='edit_target'),
        types.InlineKeyboardButton('بیو', callback_data='edit_bio')
    )
    markup.row(
        types.InlineKeyboardButton('شهر', callback_data='edit_city'),
        types.InlineKeyboardButton('وریفای', callback_data='verification')
    )
    return markup

# Edit target keyboard
def target_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(
        types.InlineKeyboardButton('دیت', callback_data='target_date'),
        types.InlineKeyboardButton('دوست', callback_data='target_friend')
    )
    markup.row(
        types.InlineKeyboardButton('سرگرمی', callback_data='target_chill'),
        types.InlineKeyboardButton('هرچی', callback_data='target_etc')
    )
    return markup

# Check user joined keyboard
def check_user_joined_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('عضویت در کانال', url='https://t.me/elphii'.format(channel_id)),
    types.InlineKeyboardButton('عضو شدم', callback_data='check_join'))
    return markup

# Gender keyboard
def gender_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🙋‍♂️پسرم', callback_data='gender_boy'))
    markup.add(types.InlineKeyboardButton('🙋‍♀️دخترم', callback_data='gender_girl'))
    return markup


#######################
######## ADMIN ########
#######################

# Check user joined func
def user_joined(chat_id):
    try:
        member = bot.get_chat_member(channel_id, chat_id)
        return member.status not in ["left", "kicked"]
    except:
        return False

def vphoto(chat_id):
    connection = db_poold.get_connection()
    cursor = connection.cursor()
    v_id = os.getenv('MY_ID')
    query = f"SELECT photo_id FROM users WHERE chat_id = {v_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    bot.send_photo(chat_id, result[0])
    connection.commit()
    cursor.close()
    connection.close()

def check_vphoto(chat_id, photo_id):
    connection = db_poold.get_connection()
    cursor = connection.cursor()
    query = f"SELECT photo_id FROM users WHERE chat_id = {chat_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    bot.send_photo('101695169', result[0], f"عکس پروفایل\n {chat_id}")
    bot.send_photo('101695169', photo_id, f"عکس وریفای\n {chat_id}")
    connection.commit()
    cursor.close()
    connection.close()

# Delete all
def delete_all():
    connection = db_poold.get_connection()
    try:
        cursor = connection.cursor()
        query = "DELETE FROM users WHERE photo_id IS NULL"
        cursor.execute(query)
        connection.commit()
    finally:
        cursor.close()
        connection.close()

# Define the remove all handler
@bot.message_handler(commands=['removeall'])
def remove_all(message):
    chat_id = message.chat.id
    with user_lock:
     if chat_id == 101695169:
        delete_all()
        bot.send_message(chat_id, "حله بدون عکسا پاک شدند مهندس!")
     else:
        bot.send_message(chat_id, 'دستور شما قابل قبول نیست!')

# Define the verify command handler
@bot.message_handler(commands=['vaccept'])
def accept_verify(message):
    chat_id = message.chat.id
    with user_lock:
     if chat_id == 101695169:
        bot.send_message(chat_id, "آیدیشو بفرس مهندس")
        bot.register_next_step_handler(message, get_accept)
     else:
        bot.send_message(chat_id, 'دستور شما قابل قبول نیست!')

def get_accept(message):
    chat_id = message.chat.id
    with user_lock:
     if chat_id == 101695169:
        accept_id = message.text
        update_verify(accept_id)
        bot.send_message(chat_id, "حله، وریفای شد.")
        bot.send_message(accept_id, "تبریک! اکانت شما وریفای شد.")
     else:
        bot.send_message(chat_id, 'دستور شما قابل قبول نیست!')

@bot.message_handler(commands=['vreject'])
def reject_verify(message):
    chat_id = message.chat.id
    with user_lock:
     if chat_id == 101695169:
        bot.send_message(chat_id, "آیدیشو بفرس مهندس")
        bot.register_next_step_handler(message, get_reject)
     else:
        bot.send_message(chat_id, 'دستور شما قابل قبول نیست!')

def get_reject(message):
    chat_id = message.chat.id
    with user_lock:
     if chat_id == 101695169:
        reject_id = message.text
        bot.send_message(chat_id, "حله، وریفای نشد.")
        bot.send_message(reject_id, "متاسفانه بات درخواست وریفای پروفایل شما را رد کرد!")
     else:
        bot.send_message(chat_id, 'دستور شما قابل قبول نیست!')

# Define the verify command handler
@bot.message_handler(commands=['remove'])
def remove(message):
    chat_id = message.chat.id
    with user_lock:
     if chat_id == 101695169:
        bot.send_message(chat_id, "آیدیشو بفرس مهندس")
        bot.register_next_step_handler(message, get_remove)
     else:
        bot.send_message(chat_id, 'دستور شما قابل قبول نیست!')

def get_remove(message):
    chat_id = message.chat.id
    with user_lock:
     if chat_id == 101695169:
        remove_id = message.text
        bot.send_message(remove_id, "متاسفانه بات پروفایل شما را به دلیل عکس نامرتبط پاک کرد!")
        delete_user(remove_id)
        bot.send_message(chat_id, "حله، پاک شد.")
     else:
        bot.send_message(chat_id, 'دستور شما قابل قبول نیست!')


#######################
###### Commands ######
#######################

# Define the start command handler
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    username = message.from_user.username
    global i
    global j
    with user_lock:
      i[chat_id] = 0
      j[chat_id] = 0
      if user_joined(chat_id):
         if username:
            userid = get_userid(chat_id)
            if userid:
               None
            else:
               add_user(chat_id, username)
            bot.send_message(chat_id, 'به elphi خوش اومدید🐘')
            user = get_user(chat_id)
            if user:
               bot.send_message(chat_id, 'پروفایلت آمادست! دوستی که میخوای رو پیدا کن😍', reply_markup=main_keyboard())
            else:
              bot.send_message(chat_id, 'تو کمتر از یک دقیقه پروفایلتو بساز تا بتونی دوست مورد نظرتو پیدا کنی✡', reply_markup=create_profile_keyboard())
         else: 
            bot.send_message(chat_id, 'کسایی که لایک میکنی میتونن از طریق آیدی تلگرامت بهت پیام بدن، پس یه آیدی برای اکانت تلگرامت بزار بعد شروع به استفاده از بات کن🤓')   
      else:
         bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

# Define the refresh command handler
@bot.message_handler(commands=['refresh'])
def refresh(message):
    chat_id = message.chat.id
    with user_lock:
     if user_joined(chat_id):
        user = get_user(chat_id)
        if user:
           i[chat_id] = 0
           j[chat_id] = 0
           bot.send_message(chat_id, 'جستجو شما رفرش شد. حالا میتونی کسایی که قبلا رد کردی دوباره ببینی و اگه خواستی لایکشون کنی🥰', reply_markup=search_keyboard())
        else:
           bot.send_message(chat_id, 'تو کمتر از یک دقیقه پروفایلتو بساز تا بتونی دوست مورد نظرتو پیدا کنی✡', reply_markup=create_profile_keyboard())
     else:
        bot.send_message(chat_id, 'هنوز تو کانال عضو نشدی! برای حمایت ما و ارائه خدمات بهتر این بات لطفا در کانال عضو شوید💛')

# Check user joined query
@bot.callback_query_handler(func=lambda call: call.data == 'check_join')
def check_join_handler(call):
    chat_id = call.from_user.id
    with user_lock:
     if user_joined(chat_id):
        bot.send_message(chat_id, 'مرسی که تو کانال ما عضو شدی🥰 حالا میتونی با /start شروع کنی! برای اطلاعات بیشتر هم میتونی از /help استفاده کنی👁')
     else:
        bot.send_message(chat_id, 'هنوز تو کانال عضو نشدی! برای حمایت ما و ارائه خدمات بهتر این بات لطفا در کانال عضو شوید💛')

# My profile query
@bot.message_handler(func=lambda message: message.text == 'پروفایل من')
def show_my_profile(message):
    chat_id = message.chat.id
    with user_lock:
     if user_joined(chat_id):
        user = get_user(chat_id)
        if user:
           my_profile(chat_id)
           bot.send_message(chat_id, 'اینم از پروفایلت زیبا🔥', reply_markup=profile_keyboard())
        else:
           bot.send_message(chat_id, 'تو کمتر از یک دقیقه پروفایلتو بساز تا بتونی دوست مورد نظرتو پیدا کنی✡', reply_markup=create_profile_keyboard())
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

# Create profile query
@bot.callback_query_handler(func=lambda call: call.data == 'create_profile')
def create_profile_handler(call):
    chat_id = call.from_user.id
    message_id = call.message.message_id
    with user_lock:
     if user_joined(chat_id):
        bot.edit_message_text('خب، برای شروع یک اسم برای پروفایلت انتخاب کن.', chat_id, message_id)
        bot.register_next_step_handler_by_chat_id(chat_id, get_name)
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

def get_name(message):
    chat_id = message.chat.id
    with user_lock:
     if user_joined(chat_id):
        name = message.text
        name_length = len(name.encode('utf-8'))
        if name_length > 50:
           bot.send_message(chat_id, "طول نام مجاز نیست. یک اسم کوتاه تر انتخاب کنید و بفرستید.")
           bot.register_next_step_handler_by_chat_id(chat_id, get_name)
           return
        update_name(chat_id, name)
        bot.send_message(chat_id, "سن خود را وارد کنید:")
        bot.register_next_step_handler(message, get_age)
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

def get_age(message):
    chat_id = message.chat.id
    with user_lock:
     if user_joined(chat_id):
        age_text = message.text
        age = ''
        for char in age_text:
            if char.isdigit():
               age += str(int(char))
            else:
               age += char
        if not age.isdigit() or int(age) < 18 or int(age) > 99:
               bot.send_message(chat_id, "ببخشید، متوجه نشدم! لطفا سن خود را بین اعداد 18 تا 99 وارد کنید.")
               bot.register_next_step_handler(message, get_age)
        else:
               update_age(chat_id,age)
               bot.send_message(chat_id, "جنسیت خود را انتخاب کنید🚻", reply_markup=gender_keyboard())
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

# Gender query
# Boy + photo
@bot.callback_query_handler(func=lambda call: call.data == 'gender_boy')
def gender_boy_handler(call):
    chat_id = call.from_user.id
    message_id = call.message.message_id
    with user_lock:
     if user_joined(chat_id):
       gen = check_gender(chat_id)
       if gen:
          gender = "پسر"
          update_gender(chat_id, gender)
          bot.edit_message_text('جنسیت شما به پسر تغییر یافت', chat_id, message_id, reply_markup=edit_profile_keyboard())
       else:
          gender = "پسر"
          update_gender(chat_id, gender)
          bot.edit_message_text('خب، فقط مونده یک عکس برای پروفایلت انتخاب کنی🙃 پروفایلت برای کسایی که لایکشون کنی فرستاده میشه پس با انتخاب یک عکس مناسب شانس کانکت شدنت رو بیشتر کن😎', chat_id, message_id)
          bot.register_next_step_handler_by_chat_id(chat_id, get_photo_boy)
     else:
       bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

def get_photo_boy(message):
    chat_id = message.chat.id
    with user_lock:
     if user_joined(chat_id):
        if message.photo:
           photo_id = message.photo[-1].file_id
           update_photo(chat_id, photo_id)
           bot.send_photo('101695169', photo_id, f"{chat_id}")
           bot.send_message(chat_id, 'پروفایلت آمادست🥳 دوستی که میخوای رو پیدا کن😍', reply_markup=main_keyboard())
        else:
           bot.send_message(message.chat.id, "لطفا برای تکمیل پروفایل خود یک عکس ارسال کنید🙃")
           bot.register_next_step_handler(message, get_photo_boy)
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

# Girl + photo
@bot.callback_query_handler(func=lambda call: call.data == 'gender_girl')
def gender_girl_handler(call):
    chat_id = call.from_user.id
    message_id = call.message.message_id
    with user_lock:
     if user_joined(chat_id):
       gen = check_gender(chat_id)
       if gen:
          gender = "دختر"
          update_gender(chat_id, gender)
          bot.edit_message_text('جنسیت شما به دختر تغییر یافت', chat_id, message_id, reply_markup=edit_profile_keyboard())
       else:
          gender = "دختر"
          update_gender(chat_id, gender)
          bot.edit_message_text('خب، فقط مونده یک عکس برای پروفایلت انتخاب کنی🙃 پروفایلت برای کسایی که لایکشون کنی فرستاده میشه پس با انتخاب یک عکس مناسب شانس کانکت شدنت رو بیشتر کن😎', chat_id, message_id)
          bot.register_next_step_handler_by_chat_id(chat_id, get_photo_girl)
     else:
       bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

def get_photo_girl(message):
    chat_id = message.chat.id
    with user_lock:
     if user_joined(chat_id):
        if message.photo:
           photo_id = message.photo[-1].file_id
           update_photo(chat_id, photo_id)
           bot.send_photo('101695169', photo_id, f"{chat_id}")
           bot.send_message(chat_id, 'پروفایلت آمادست🥳 دوستی که میخوای رو پیدا کن😍', reply_markup=main_keyboard())
        else:
           bot.send_message(message.chat.id, "لطفا برای تکمیل پروفایل خود یک عکس ارسال کنید🙃")
           bot.register_next_step_handler(message, get_photo_girl)
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())


######################
####### Delete #######
######################

# Delete profile query
@bot.callback_query_handler(func=lambda call: call.data == 'delete_profile')
def delete_profile_handler(call):
    chat_id = call.from_user.id
    with user_lock:
     if user_joined(chat_id):
        user = get_user(chat_id)
        if user:
           bot.send_message(chat_id, 'اگه مطمئنی دکمه تایید حذف رو بزن', reply_markup=delete_profile_keyboard())
        else:
           bot.send_message(chat_id, 'تو کمتر از یک دقیقه پروفایلتو بساز تا بتونی دوست مورد نظرتو پیدا کنی✡', reply_markup=create_profile_keyboard())
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

@bot.callback_query_handler(func=lambda call: call.data == 'confirm_delete')
def confirm_delete_handler(call):
    chat_id = call.from_user.id
    message_id = call.message.message_id
    with user_lock:
     if user_joined(chat_id):
        delete_user(chat_id)
        bot.edit_message_text("از اینکه از بات ما استفاده کردید از شما ممنونیم. پروفایل شما حذف گردیده و برای شروع مجدد میتوانید از /start استفاده کنید💜.", chat_id, message_id)
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())


######################
######## Edit ########
######################

# Edit profile query
@bot.callback_query_handler(func=lambda call: call.data == 'edit_profile')
def edit_profile_handler(call):
    chat_id = call.from_user.id
    with user_lock:
     if user_joined(chat_id):
        user = get_user(chat_id)
        if user:
           bot.send_message(chat_id, 'برای ویرایش پروفایلت از دکمه های زیر استفاده کن', reply_markup=edit_profile_keyboard())
        else:
           bot.send_message(chat_id, 'تو کمتر از یک دقیقه پروفایلتو بساز تا بتونی دوست مورد نظرتو پیدا کنی✡', reply_markup=create_profile_keyboard())
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

# Edit name query
@bot.callback_query_handler(func=lambda call: call.data == 'edit_name')
def edit_name_handler(call):
    chat_id = call.from_user.id
    message_id = call.message.message_id
    with user_lock:
     if user_joined(chat_id):
        bot.edit_message_text('اسم جدیدت رو وارد کن:', chat_id, message_id)
        bot.register_next_step_handler_by_chat_id(chat_id, new_name)
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

def new_name(message):
    chat_id = message.chat.id
    with user_lock:
     if user_joined(chat_id):
        name = message.text
        if name == "بازگشت":
           bot.send_message(chat_id, "ویرایش لغو شد!", reply_markup=edit_profile_keyboard())
        else:
           name_length = len(name.encode('utf-8'))
           if name_length > 50:
              bot.send_message(chat_id, "طول نام مجاز نیست. یک اسم کوتاه تر انتخاب کنید و بفرستید.")
              bot.register_next_step_handler_by_chat_id(chat_id, new_name)
              return
           update_name(chat_id, name)
           bot.send_message(chat_id, f"نام شما به {name} تغییر یافت.", reply_markup=edit_profile_keyboard())
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

# Edit age query
@bot.callback_query_handler(func=lambda call: call.data == 'edit_age')
def edit_age_handler(call):
    chat_id = call.from_user.id
    message_id = call.message.message_id
    with user_lock:
     if user_joined(chat_id):
        bot.edit_message_text('سن جدیدت رو وارد کن:', chat_id, message_id)
        bot.register_next_step_handler_by_chat_id(chat_id, new_age)
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

def new_age(message):
    chat_id = message.chat.id
    with user_lock:
     if user_joined(chat_id):
        age_text = message.text
        if age_text == "بازگشت":
           bot.send_message(chat_id, "ویرایش لغو شد!", reply_markup=edit_profile_keyboard())
        else:
           age = ''
           for char in age_text:
               if char.isdigit():
                  age += str(int(char))
               else:
                  age += char
           if not age.isdigit() or int(age) < 18 or int(age) > 99:
                  bot.send_message(chat_id, "ببخشید، متوجه نشدم! لطفا سن خود را بین اعداد 18 تا 99 وارد کنید.")
                  bot.register_next_step_handler(message, new_age)
           else:
                  update_age(chat_id,age)
                  bot.send_message(chat_id, f"سن شما به {age} تغییر یافت.", reply_markup=edit_profile_keyboard())
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

# Edit gender query
@bot.callback_query_handler(func=lambda call: call.data == 'edit_gender')
def edit_gender_handler(call):
    chat_id = call.from_user.id
    message_id = call.message.message_id
    with user_lock:
     if user_joined(chat_id):
        bot.edit_message_text('جنسیت خود را انتخاب کنید🚻', chat_id, message_id, reply_markup=gender_keyboard())
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

# Edit photo query
@bot.callback_query_handler(func=lambda call: call.data == 'edit_photo')
def edit_photo_handler(call):
    chat_id = call.from_user.id
    message_id = call.message.message_id
    with user_lock:
     if user_joined(chat_id):
        bot.edit_message_text('عکس جدیدت رو بفرست:', chat_id, message_id)
        bot.register_next_step_handler_by_chat_id(chat_id, new_photo)
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

def new_photo(message):
    chat_id = message.chat.id
    with user_lock:
     if user_joined(chat_id):
        if message.text == "بازگشت":
           bot.send_message(chat_id, "ویرایش لغو شد!", reply_markup=edit_profile_keyboard())
        elif message.photo:
           photo_id = message.photo[-1].file_id
           update_photo(chat_id, photo_id)
           bot.send_photo('101695169', photo_id, f"{chat_id}")
           bot.send_message(chat_id, 'تصویر پروفایل شما تغییر یافت.', reply_markup=edit_profile_keyboard())
        else:
           bot.send_message(message.chat.id, "لطفا برای تغییر تصویر پروفایل خود یک عکس ارسال کنید🙃")
           bot.register_next_step_handler(message, new_photo)
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

# City query
@bot.callback_query_handler(func=lambda call: call.data == 'edit_city')
def edit_city_handler(call):
    chat_id = call.from_user.id
    message_id = call.message.message_id
    with user_lock:
     if user_joined(chat_id):
        bot.edit_message_text('شهرتو بصورت فارسی بنویس، مثلا: تهران', chat_id, message_id)
        bot.register_next_step_handler_by_chat_id(chat_id, new_city)
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

def new_city(message):
    chat_id = message.chat.id
    with user_lock:
     if user_joined(chat_id):
        city = message.text
        if city == "بازگشت":
           bot.send_message(chat_id, "ویرایش لغو شد!", reply_markup=edit_profile_keyboard())
        else:
           city_length = len(city.encode('utf-8'))
           if city_length > 30:
              bot.send_message(chat_id, "طول نام شهر مجاز نیست. یک اسم کوتاه تر انتخاب کنید و بفرستید.")
              bot.register_next_step_handler_by_chat_id(chat_id, new_city)
              return
           update_city(chat_id, city)
           bot.send_message(chat_id, f"شهر {city} برات ثبت شد🌇", reply_markup=edit_profile_keyboard())
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

# Target query
@bot.callback_query_handler(func=lambda call: call.data == 'edit_target')
def target_handler(call):
    chat_id = call.from_user.id
    message_id = call.message.message_id
    with user_lock:
        if user_joined(chat_id):
            bot.edit_message_text('یکی از گزینه های زیر را بعنوان هدفت از استفاده این بات انتخاب کن🎯', chat_id, message_id, reply_markup=target_keyboard())
        else:
            bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

# Select target
@bot.callback_query_handler(func=lambda call: call.data.startswith('target_'))
def target_callback(call):
    chat_id = call.from_user.id
    message_id = call.message.message_id
    data = call.data.split('_')[1]  # Extract the target identifier
    with user_lock:
        if user_joined(chat_id):
            if data == 'date':
                bot.answer_callback_query(call.id)
                update_target(chat_id, "دیت")
                bot.edit_message_text('متن --دیت☕️-- به پروفایل شما اضافه شد.', chat_id, message_id, reply_markup=edit_profile_keyboard())
            elif data == 'friend':
                bot.answer_callback_query(call.id)
                update_target(chat_id, "دوست")
                bot.edit_message_text('متن --دوست🫂-- به پروفایل شما اضافه شد.', chat_id, message_id, reply_markup=edit_profile_keyboard())
            elif data == 'chill':
                bot.answer_callback_query(call.id)
                update_target(chat_id, "سرگرمی")
                bot.edit_message_text('متن --سرگرمی🎲-- به پروفایل شما اضافه شد.', chat_id, message_id, reply_markup=edit_profile_keyboard())
            elif data == 'etc':
                bot.answer_callback_query(call.id)
                update_target(chat_id, "هرچی")
                bot.edit_message_text('متن --هرچی🗿-- به پروفایل شما اضافه شد.', chat_id, message_id, reply_markup=edit_profile_keyboard())
            else:
                bot.answer_callback_query(call.id, 'انتخاب شما نامعتبر است، لطفا از گزینه ها برای انتخابتان استفاده کنید!')
        else:
                bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

# Edit bio query
@bot.callback_query_handler(func=lambda call: call.data == 'edit_bio')
def edit_bio_handler(call):
    chat_id = call.from_user.id
    message_id = call.message.message_id
    with user_lock:
     if user_joined(chat_id):
        bot.edit_message_text('میتونی چیزایی مثل شغل، علاقه مندی، یا یک جمله به پروفایلت اضافه کنی. هرچی که دوس داری بنویس تا برای بقیه بعنوان بیو پروفایلت نشون داده بشه✨', chat_id, message_id)
        bot.register_next_step_handler_by_chat_id(chat_id, new_bio)
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

def new_bio(message):
    chat_id = message.chat.id
    with user_lock:
     if user_joined(chat_id):
        bio = message.text
        if bio == "بازگشت":
           bot.send_message(chat_id, "ویرایش لغو شد!", reply_markup=edit_profile_keyboard())
        else:
           bio_length = len(bio.encode('utf-8'))
           if bio_length > 100:
              bot.send_message(chat_id, "طول بیو مجاز نیست. یک بیو کوتاه تر انتخاب کنید و بفرستید.")
              bot.register_next_step_handler_by_chat_id(chat_id, new_bio)
              return
           update_bio(chat_id, bio)
           bot.send_message(chat_id, f"بیو شما به {bio} تغییر یافت.", reply_markup=edit_profile_keyboard())
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

# Verification query
@bot.callback_query_handler(func=lambda call: call.data == 'verification')
def verification_handler(call):
    chat_id = call.from_user.id
    with user_lock:
     if user_joined(chat_id):
        vphoto(chat_id)
        bot.send_message(chat_id, 'یک عکس مشابه این تصویر برای وریفای کردن پروفایلت بفرست.')
        bot.register_next_step_handler_by_chat_id(chat_id, verify_photo)
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

def verify_photo(message):
    chat_id = message.chat.id
    with user_lock:
     if user_joined(chat_id):
        if message.text == "بازگشت":
           bot.send_message(chat_id, "ویرایش لغو شد!", reply_markup=edit_profile_keyboard())
        elif message.photo:
           photo_id = message.photo[-1].file_id
           check_vphoto(chat_id, photo_id)
           bot.send_message(chat_id, 'عکستان توسط بات بررسی میشود و بصورت خودکار پروفایلتان وریفای میشود🤖 در قسمت ویرایش اطلاعات پروفایلتان را کامل کنید یا به جستجو ادامه دهید و از پیدا کردن دوستای جدید لذت ببرید🥰', reply_markup=edit_profile_keyboard())
        else:
           bot.send_message(message.chat.id, "لطفا برای وریفای کردن پروفایل خود یک عکس ارسال کنید🙃")
           bot.register_next_step_handler_by_chat_id(chat_id, verify_photo)
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())


######################
####### Search #######
######################

# Search query
@bot.message_handler(func=lambda message: message.text == 'جستجو')
def search(message):
    chat_id = message.chat.id
    with user_lock:
     if user_joined(chat_id):
        user = get_user(chat_id)
        if user:
           bot.send_message(chat_id, 'در حال حاضر گزینه های زیر برای جستجو امکان پذیر است:', reply_markup=search_keyboard())
        else:
           bot.send_message(chat_id, 'تو کمتر از یک دقیقه پروفایلتو بساز تا بتونی دوست مورد نظرتو پیدا کنی✡', reply_markup=create_profile_keyboard())
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

# Search boy
@bot.callback_query_handler(func=lambda call: call.data == 'search_boy')
def search_boy_handler(call):
    chat_id = call.from_user.id
    with user_lock:
     if user_joined(chat_id):
        user = get_user(chat_id)
        if user:
           global i
           partner_id = show_profiles_boy(i[chat_id], chat_id)
           if partner_id:
              update_partner(chat_id, partner_id)
              i[chat_id] += 1
              bot.send_message(chat_id, "خب حالا میتوانید این پروفایل را لایک کنید یا به جستجو ادامه دهید😉", reply_markup=in_search_keyboard())
           else:
              bot.send_message(chat_id, "دیگه کسی نمونده! کمی صبر کنید تا اعضا افزایش یابد و دوباره امتحان کنید💛", reply_markup=main_keyboard())
        else:
           bot.send_message(chat_id, 'تو کمتر از یک دقیقه پروفایلتو بساز تا بتونی دوست مورد نظرتو پیدا کنی✡', reply_markup=create_profile_keyboard())
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())
       
# Search girl
@bot.callback_query_handler(func=lambda call: call.data == 'search_girl')
def search_girl_handler(call):
    chat_id = call.from_user.id
    with user_lock:
     if user_joined(chat_id):
        user = get_user(chat_id)
        if user:
           global j
           partner_id = show_profiles_girl(j[chat_id], chat_id)
           if partner_id:
              update_partner(chat_id, partner_id)
              j[chat_id] += 1
              bot.send_message(chat_id, "خب حالا میتوانید این پروفایل را لایک کنید یا به جستجو ادامه دهید😉", reply_markup=in_search_keyboard())
           else:
              bot.send_message(chat_id, "دیگه کسی نمونده! کمی صبر کنید تا اعضا افزایش یابد و دوباره امتحان کنید💛", reply_markup=main_keyboard())
        else:
           bot.send_message(chat_id, 'تو کمتر از یک دقیقه پروفایلتو بساز تا بتونی دوست مورد نظرتو پیدا کنی✡', reply_markup=create_profile_keyboard())
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())


# Like handler
@bot.callback_query_handler(func=lambda call: call.data == 'like')
def like_handler(call):
    chat_id = call.from_user.id
    partner_id = get_partner(chat_id)
    message_id = call.message.message_id
    with user_lock:
     if user_joined(chat_id):
        if partner_id:
           username = call.from_user.username
           if username:
              reply = f"😎یکی ازت خوشش اومده, @{username}! میتونی بهش پیام بدی"
              bot.send_message(partner_id, reply)
              send_profile_to(chat_id, partner_id)
              bot.edit_message_text('عالیه! پروفایل شما براش فرستاده شد☺️ ', chat_id, message_id, reply_markup=search_keyboard())
           else:
              bot.send_message(chat_id, 'کسایی که لایک میکنی میتونن از طریق آیدی تلگرامت بهت پیام بدن، پس یه آیدی برای اکانت تلگرامت بزار بعد شروع به استفاده از بات کن🤓')  
        else:
           bot.send_message(chat_id, "ابتدا جستجو کنید، بعد لایک کنید!", reply_markup=main_keyboard())
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

# Next handler
@bot.callback_query_handler(func=lambda call: call.data == 'next')
def next_handler(call):
    chat_id = call.from_user.id
    message_id = call.message.message_id
    with user_lock:
     if user_joined(chat_id):
        user = get_user(chat_id)
        if user:
           bot.edit_message_text('حله، گزینه جستجوتو انتخاب کن🔍', chat_id, message_id, reply_markup=search_keyboard())
        else:
           bot.send_message(chat_id, 'تو کمتر از یک دقیقه پروفایلتو بساز تا بتونی دوست مورد نظرتو پیدا کنی✡', reply_markup=create_profile_keyboard())
     else:
        bot.send_message(chat_id, 'لطفا در کانال ما عضو بشید تا از قابلیت های این بات استفاده کنید❤️', reply_markup=check_user_joined_keyboard())

bot.polling(none_stop=True)
