import telebot
import psycopg2
import datetime
from telebot import types

token = '5900669666:AAENjMchhx-VVG8M5jHRSdQZ3-9w3Ai2J3g'

bot = telebot.TeleBot(token)
start_time=datetime.date(2023,1,31)
today=datetime.date.today()
week=int(datetime.date.today().strftime("%V"))-int(datetime.date(2023,1,31).strftime("%V"))+1
conn=psycopg2.connect(database='postgres',
                      user='postgres',
                      password='postgres',
                      host='localhost',
                      port='5432')
cursor= conn.cursor()

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help",'/shedule','/mtuci')
    bot.send_message(message.chat.id, 'Привет! Хотите узнать расписание?', reply_markup=keyboard)

@bot.message_handler(commands=['mtuci'])
def start(message):
    bot.send_message(message.chat.id, 'https://mtuci.ru/')

@bot.message_handler(commands=['week'])
def start(message):
    bot.send_message(message.chat.id, (f'Сейчас идет{week} неделя'))

@bot.message_handler(commands=['shedule'])
def test(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('/Понед', '/Вторн', '/Среда', '/Четв','/Пятн','/Суб','/Текущая','/След','/start')
    bot.send_message(message.chat.id, "Выберите день", reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def answer(message):
    bot.send_message(message.chat.id, 'Я умею выводить расписание на определённый день недели, на всю неделю и на последующую-/shedule и определять какая идет неделя-/week')

@bot.message_handler(commands=['Понед','Вторн','Среда','Четв','Пятн','Суб'])
def answer(message):
    ans=''
    if week%2==0:
        wk=2
    else:
        wk=1
    if message.text=="/Понед":
        wd=1
    elif message.text=="/Вторн":
        wd=2
    elif message.text == "/Среда":
        wd = 3
    elif message.text == "/Четв":
        wd = 4
    elif message.text == "/Пятн":
        wd = 5
    elif message.text == "/Суб":
        wd = 6


    cursor.execute(f"SELECT subject,room,start_time FROM timetable WHERE id_days='{wd}_{wk}'")
    records = list(cursor.fetchall())
    if len(records)==0:
        bot.send_message(message.chat.id, 'Занятий нет')
        return
    for i in records:
        #cursor.execute("SELECT full_name from teacher WHERE subject='{i[0]}'")
        cursor.execute(f"SELECT full_name FROM teacher WHERE subject='{i[0]}'")
        teacher=cursor.fetchone()
        subj=i+teacher
        ans+=(f"{str(subj)}\n")
    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, ans)

@bot.message_handler(commands=['Текущая','След'])
def answer(message):
    global week
    weekday=['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота']
    ans=''
    if message.text == "/След":
        if (week+1)%2==0:
            wk=2
        else:
            wk=1
    else:
        if week%2==0:
            wk=2
        else:
            wk=1
    for i in range(1,7):
        ans+=(f"{weekday[i-1]}\n")
        cursor.execute(f"SELECT subject,room,start_time FROM timetable WHERE id_days='{i}_{wk}'")
        records = list(cursor.fetchall())
        if len(records) == 0:
            ans+=(f"Занятий нет\n")
        for i in records:
            # cursor.execute("SELECT full_name from teacher WHERE subject='{i[0]}'")
            cursor.execute(f"SELECT full_name FROM teacher WHERE subject='{i[0]}'")
            teacher = cursor.fetchone()
            subj = i + teacher
            ans += (f"{str(subj)}\n")
    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, ans)



@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда введите команду /shedule')
    else:
        bot.send_message(message.chat.id, 'Извините, я вас не понял')




bot.polling(none_stop=True)