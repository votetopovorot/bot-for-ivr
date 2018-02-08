# -*- coding: utf-8 -*-
import telebot
import sqlite3
import time
import schedule
from telebot import types

conn = sqlite3.connect('users.sqlite') #подключаемся к бд
cursor = conn.cursor()

#____________________ проверяем наличие таблиц ___________
cursor.execute('''
CREATE TABLE IF NOT EXISTS  usersusers(
firstname,
userid,
admin,
theme,
level)
''')


#___________________ ставим значение переменных ____________
token = '   ' # вставьте токен
password = "  " # вставьте пароль
bot = telebot.TeleBot(token, threaded=False) # объект - бот

#________________ создаем списки _____________
login = {}
adminmessageone = {}
adminmessagetwo = {}

#________________ обозначаем глобальные переменные _______
messageintimeadmin = 'Сообщение по таймеру'
sendmessageadmin = 'Срочное сообщение'
endplease = 'Закончить сессию'
toadminmenu = 'В меню администратора'
gotoreg = 'Хорошо'
iwasinreg = 'Я уже есть в базе данных!'
scholar = 'Ученик'
admin = 'Администратор'
research = 'Исследования'
project = 'Проекты'
researchandprojects = 'Исследования и проекты'
whoiam = 'Узнать о сессии'
changemylife = 'Изменить параметры'
backtoadminmenu = 'Назад в меню администратора'
writeme = 'Написать в службу поддержки'
tenlevel = '10'
elevenlevel = '11'
eitherlevels = '10 и 11'
letsdosage = 'Хорошо'


#____________создаем клавиатуры для передачи данных между функциями________________
markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup7 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup8 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

#_______________ создаем переменные для клавиатур _____________
item1 = types.KeyboardButton(messageintimeadmin)    # 'Сообщение по таймеру'
item2 = types.KeyboardButton(sendmessageadmin)      # 'Срочное сообщение'
item3 = types.KeyboardButton(endplease)             # 'Закончить сессию'
item4  = types.KeyboardButton(toadminmenu)          # 'В меню администратора'
item5 = types.KeyboardButton(gotoreg)               # 'Хорошо'
item6 = types.KeyboardButton(iwasinreg)             # 'Я уже есть в базе данных!'
item7 = types.KeyboardButton(scholar)               # 'Ученик'
item8 = types.KeyboardButton(admin)                 # 'Администратор'
item9 = types.KeyboardButton(project)               # 'Исследования'
item10 = types.KeyboardButton(research)             # 'Проекты'
item11 = types.KeyboardButton(researchandprojects)  # 'Исследования и проекты'
item12 = types.KeyboardButton(whoiam)               # 'Узнать о сессии'
item13 = types.KeyboardButton(changemylife)         # 'Изменить параметры'
item14 = types.KeyboardButton(backtoadminmenu)      # 'Назад в меню администратора'
item15 = types.KeyboardButton(writeme)              # 'Написать в службу поддержки'
item16 = types.KeyboardButton(tenlevel)             # '10'
item17 = types.KeyboardButton(elevenlevel)          # '11'
item18 = types.KeyboardButton(eitherlevels)         # '10 и 11'
item19 = types.KeyboardButton(letsdosage)           # 'Хорошо'
#item20

#________________ формируем клавиатуры ___________________
markup1.row(item1, item2)                           # 'Сообщение по таймеру', 'Срочное сообщение',
markup1.row(item12, item3)                          # 'Узнать о сессии', 'Закончить сессию'
markup1.row(item15)                                 # 'Написать в службу поддержки'

markup2.row(item9, item10)                          # 'Исследования', 'Проекты'
markup2.row(item11)                                 # 'Исследования и проекты'

markup3.row(item5, item6)                           # 'Хорошо', 'Я уже есть в базе данных!'

markup4.row(item7, item8)                           # 'Ученик', 'Администратор'

markup5.row(item9, item10)                          # 'Исследования', 'Проекты'
markup5.row(item11)                                 # 'Исследования и проекты'
markup5.row(item14)                                 # 'Назад в меню администратора

markup6.row(item12, item13)                         # 'Узнать о сессии', 'Изменить параметры'
markup6.row(item15)                                 # 'Написать в службу поддержки'
markup6.row(item3)                                  # 'Закончить сессию'

markup7.row(item16, item17)                         # '10', '11'
markup7.row(item18)                                 # '10 и 11'

markup8.row(item19)                                 # 'Хорошо'

#markup9.row(item20, item21)


#__________________ начало функционирования кода
@bot.message_handler(commands=['start']) # процедура, которую запускает команда "/start"

#def id(message): # функция проверки id пользователя в табличке
#    user = message.chat.id # "user" = id пользователя
#    login[user] = message.text # элемент списка наделяем "логином" пользователя
#    userlogin = login[user] # "userlogin" = "логин" пользователя
#    conn = sqlite3.connect('users.sqlite')  # подключаемся к бд
#    cursor = conn.cursor()

#_________проверка id пользователя на существование в базе данных, предложение зарегистрироваться_______
def hello(message): # функция первого ответа
    #print(message.chat.id)
    bot.send_message(message.chat.id, 'Вас приветствует бот кафедры исследований и проектов!')
    time.sleep(2) # подождем 2 секунды
    # проверяем id на существование в таблице
    userid = message.chat.id
    userid = str(userid)
    conn = sqlite3.connect('users.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM usersusers WHERE userid = (?)", (userid,))
    results = str(cursor.fetchall())
    #print(results)
    goodresult = str([(0,)])
    if results == goodresult:
        #print('cool')
        bot.send_message(message.chat.id, 'Вас еще нет в базе данных \n' 
                                          'Пожалуйста, зарегистрируйтесь в ней!', reply_markup=markup3)
        bot.register_next_step_handler(message, tobase)
        conn.commit()
        conn.close()
    else:
        bot.send_message(message.chat.id, 'Вы уже зарегистрированы')
        cursor.execute("SELECT admin FROM usersusers WHERE userid = (?)", (userid,))
        newresults = (cursor.fetchone())
        #print(newresults[0])
        newform = str(newresults[0])
        if newform == 'admin':
            tomenu = bot.send_message(message.chat.id, 'Воспользуйтесь меню администратора, чтобы сообщить информацию',
                                      reply_markup=markup1)
            bot.register_next_step_handler(tomenu, commands)
        elif newform == 'user':
            tousermenu = bot.send_message(message.chat.id, 'Ожидайте уведомлений!', reply_markup=markup6)
            bot.register_next_step_handler(tousermenu, usercommands)
        elif newform == 'None':
            letsdeleteold = bot.send_message(message.chat.id, 'Ваша запись оказалась повреждена :( \n'
                                                'Пожалуйста, пройдите регистрацию ещё раз. \n'
                                              'Для этого сначала нажмите кнопку "Хорошо", \n а затем наберите /start',
                                             reply_markup=markup8)
            bot.register_next_step_handler(letsdeleteold, sage)
        conn.commit()
        conn.close()

#__________________создание логина нового пользователя____________
def tobase(message):
    if message.text == 'Хорошо':
        user = message.chat.id  # переменная "user" = id пользователя
        loginbyuser = bot.send_message(message.chat.id,
                                       'Придумайте логин!')  # получаем от пользователя текст переменной "логин"
        bot.register_next_step_handler(loginbyuser, reply)
    elif message.text == 'Я уже есть в базе данных!':
        bot.send_message(message.chat.id, 'Напишите в службу поддержки!')
        writemeguys(message)

#____________________запись нового логина в базу даных______________
def reply(message):
    conn = sqlite3.connect('users.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM usersusers WHERE firstname = (?)", (message.text,))
    results = str(cursor.fetchall())
    goodresult = str([(0,)])
    if results == goodresult:
        user = message.chat.id  # "user" = id пользователя
        #print(user)
        login[user] = message.text  # элемент списка наделяем "логином" пользователя
        userlogin = login[user]  # "userlogin" = "логин" пользователя
        #print(userlogin)
        # cursor.execute("DELETE FROM usersusers")
        cursor.execute("INSERT INTO usersusers (firstname, userid) VALUES(?,?)",
                       (str(userlogin,), str(user,)))  # execute посылает действие, insert - вставляет
        res = cursor.execute("SELECT firstname, userid FROM usersusers")
        res = cursor.fetchall()
        #print(res)  # выводим логин и id пользователей
        #print(9)
        conn.commit()
        conn.close()
        variants = bot.send_message(message.chat.id, 'Вы ученик или администратор?',
                                    reply_markup=markup4)
        bot.register_next_step_handler(variants, adminornot)  # ждем определение для перехода к следующей функции
    else:
        bot.send_message(message.chat.id, 'Логин занят!')
        time.sleep(1)
        loginbyuser = bot.send_message(message.chat.id,
                                       'Придумайте логин!')  # получаем от пользователя текст переменной "логин"
        bot.register_next_step_handler(loginbyuser, reply)

#________________________регистрация статуса нового пользователя________________
def adminornot(message):
    if message.text == 'Ученик':
        conn = sqlite3.connect('users.sqlite')  # подключаемся к бд
        cursor = conn.cursor()
        cursor.execute("UPDATE usersusers SET admin = 'user' WHERE userid = (?)", (message.chat.id,))
        #print(7)
        conn.commit()
        conn.close()
        variants = bot.send_message(message.chat.id, 'По каким темам вы хотите получать уведомления?',
                                    reply_markup=markup2)
        bot.register_next_step_handler(variants, userthemes)  # ждем определение для перехода к следующей функции
    elif message.text == 'Администратор':
        bot.send_message(message.chat.id, 'Пожалуйста, введите пароль')
        bot.register_next_step_handler(message, passwordtest)

#________________проверка пароля администратора; регистрация админстратора_____________
def passwordtest(message):
    userspassword = str(message.text)
    if userspassword == password:
        bot.send_message(message.chat.id, 'Пароль верный')
        conn = sqlite3.connect('users.sqlite')  # подключаемся к бд
        cursor = conn.cursor()
        cursor.execute("UPDATE usersusers SET admin = 'admin' WHERE userid = (?)", (message.chat.id,))
        cursor.execute("UPDATE usersusers SET theme = 'research and projects' WHERE userid = (?)", (message.chat.id,))
        cursor.execute("UPDATE usersusers SET level = '10 и 11' WHERE userid = (?)", (message.chat.id,))
        conn.commit()
        conn.close()
        #print(8)
        bot.send_message(message.chat.id, 'Вы успешно зарегистрировались!')
        time.sleep(1)
        tomenu = bot.send_message(message.chat.id, 'Воспользуйтесь меню администратора, '
                                                   'чтобы сообщить информацию',
                                  reply_markup=markup1)
        bot.register_next_step_handler(tomenu, commands)
    else:
        bot.send_message(message.chat.id, 'Пароль неверный')
        time.sleep(1)
        bot.send_message(message.chat.id, 'Пожалуйста подождите 5 секунд и введите пароль еще раз')
        time.sleep(5)
        bot.register_next_step_handler(message, passwordtest)

#__________________личный кабинет пользователя_______________
def usercommands(message):
    if message.text == whoiam:
        whoiamfunction(message)
        tomenu = bot.send_message(message.chat.id, 'Продолжить работу?', reply_markup=markup6)
        bot.register_next_step_handler(tomenu, usercommands)
    if message.text == changemylife:
       changetheme(message)
    if message.text == writeme:
        writemeguys(message)
        tomenu = bot.send_message(message.chat.id, 'Продолжить работу?', reply_markup=markup6)
        bot.register_next_step_handler(tomenu, usercommands)
    if message.text == endplease:
        bot.send_message(message.chat.id, 'До свидания! Чтобы возобновить работу, просто напишите /start!')

#________________личный кабинет администратора_______________
def commands(message):
    if message.text == sendmessageadmin:
        letsdomessage(message)
    if message.text == whoiam:
        whoiamfunction(message)
        tomenu = bot.send_message(message.chat.id, 'Продолжить работу?', reply_markup=markup1)
        bot.register_next_step_handler(tomenu, commands)
    if message.text == messageintimeadmin:
        messageintimefunction(message)
    if message.text == endplease:
        bot.send_message(message.chat.id, 'До свидания! Чтобы возобновить работу, просто напишите /start!')
    if message.text == writeme:
        writemeguys(message)
        tomenu = bot.send_message(message.chat.id, 'Продолжить работу?', reply_markup=markup1)
        bot.register_next_step_handler(tomenu, commands)

#_______________ссылка на личные контакты__________________
def writemeguys(message):
    bot.send_message(message.chat.id, 'Пожалуйста, пишите по адресу: @yuurochka. \n'
                                      'Помогу решить любые проблемы, отвечу на любые вопросы')

#________________отправка сообщения по таймеру_____________
def messageintimefunction(message):
    tomenu = bot.send_message(message.chat.id, 'Пока что данная функция находится в разработке. '
                                               'Скоро она появится!\n '
                                               'Продолжить работу?', reply_markup=markup1)
    bot.register_next_step_handler(tomenu, commands)

#________________информация пользователю о нем самом_____________
def whoiamfunction(message):
    userid = str((message.chat.id))
    conn = sqlite3.connect('users.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT userid, firstname, theme, admin, level FROM usersusers")
    rows = cursor.fetchall()
    for row in rows:
        anotherid = str(row[0])
        if userid == anotherid:
            bot.send_message(message.chat.id, 'Ваш логин: ' + row[1])
            if row[2] == 'research':
                bot.send_message(message.chat.id, 'Ваши уведомления: Исследования')
            elif row[2] == 'projects':
                bot.send_message(message.chat.id, 'Ваши уведомления: Проекты')
            elif row[2] == 'research and projects':
                bot.send_message(message.chat.id, 'Ваши уведомления: Исследования и проекты')
            time.sleep(1)
            if row[4] == '10':
                bot.send_message(message.chat.id, 'Ваш выбранный класс: 10')
            elif row[4] == '11':
                bot.send_message(message.chat.id, 'Ваш выбранный класс: 11')
            elif row[4] == '10 и 11':
                bot.send_message(message.chat.id, 'Ваш выбранный класс: 10 и 11')
            time.sleep(1)
            if row[3] == 0:
                bot.send_message(message.chat.id, 'Ваш статус: ученик')
            elif row[3] == 1:
                bot.send_message(message.chat.id, 'Ваш статус: администратор')
    conn.commit()
    conn.close()

#___________________предложение пользователю изменить свои темы______________
def changetheme(message):
    where = bot.send_message(message.chat.id, 'По каким темам вы хотите получать уведомления?',
                             reply_markup=markup2)
    bot.register_next_step_handler(where, userthemes)  # ждем определение для перехода к следующей функции

#______________предложение администратору отправить сообщение; узнаем куда______________
def letsdomessage(message):
    whom = bot.send_message(message.chat.id, 'Куда вы хотите отправить сообщение?', reply_markup=markup5)
    bot.register_next_step_handler(whom, messageto)

#________________отправление сообщения от администратора; узнаем кому______________
def messageto(message):
    userid = message.chat.id
    if message.text == backtoadminmenu:
        back = bot.send_message(message.chat.id, 'Выберите действие!', reply_markup=markup1)
        bot.register_next_step_handler(back, commands)
    else:
        if message.text == 'Исследования':
            adminmessageone[userid] = 'research'
        elif message.text == 'Проекты':
            adminmessageone[userid] = 'projects'
        elif message.text == 'Исследования и проекты':
            adminmessageone[userid] = 'research and projects'
        whatlevel = bot.send_message(message.chat.id, 'Какому классу вы хотите отправить сообщение?',
                                     reply_markup=markup7)
        bot.register_next_step_handler(whatlevel, levelto)

#_________________все еще отправление сообщения от администратора; узнаем что отправлять___________
def levelto(message):
    userid = message.chat.id
    if message.text == '10':
        adminmessagetwo[userid] = '10'
    elif message.text == '11':
        adminmessagetwo[userid] = '11'
    elif message.text == '10 и 11':
        adminmessagetwo[userid] = '10 и 11'
    bot.send_message(message.chat.id, 'Введите сообщение для рассылки. \n'
                                      'Чтобы вернуться в меню администратора, '
                                      'введите слово "back"')
    bot.register_next_step_handler(message, breakingnews)

#____________предлагаем одуматься; отправляем сообщение и выходим в личный кабинет____________
def breakingnews(message):
    if message.text == 'back':
        back = bot.send_message(message.chat.id, 'Выберите действие!', reply_markup=markup1)
        bot.register_next_step_handler(back, commands)
    else:
        if message.content_type == 'text':
            userid = message.chat.id
            whom = str(adminmessageone[userid])
            where = str(adminmessagetwo[userid])
            conn = sqlite3.connect('users.sqlite')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usersusers")
            rows = cursor.fetchall()
            if whom == 'research':
                for row in rows:
                    if row[3] == 'research':
                        if where == '10':
                            if row[4] == '10':
                                chatid = str(row[1])
                                bot.send_message(int(chatid), message.text)
                        if where == '11':
                            if row[4] == '11':
                                chatid = str(row[1])
                                bot.send_message(int(chatid), message.text)
                        if where == '10 и 11':
                            if row[4] == '10 и 11':
                                chatid = str(row[1])
                                bot.send_message(int(chatid), message.text)
            elif whom == 'projects':
                for row in rows:
                    if where == '10':
                        if row[4] == '10':
                            chatid = str(row[1])
                            bot.send_message(int(chatid), message.text)
                    if where == '11':
                        if row[4] == '11':
                            chatid = str(row[1])
                            bot.send_message(int(chatid), message.text)
                    if where == '10 и 11':
                        if row[4] == '10 и 11':
                            chatid = str(row[1])
                            bot.send_message(int(chatid), message.text)
            elif whom == 'research and projects':
                for row in rows:
                    if row[3] == 'research':
                        if where == '10':
                            if row[4] == '10':
                                chatid = str(row[1])
                                bot.send_message(int(chatid), message.text)
                        if where == '11':
                            if row[4] == '11':
                                chatid = str(row[1])
                                bot.send_message(int(chatid), message.text)
                        if where == '10 и 11':
                            if row[4] == '10 и 11':
                                chatid = str(row[1])
                                bot.send_message(int(chatid), message.text)
                    if row[3] == 'projects':
                        if where == '10':
                            if row[4] == '10':
                                chatid = str(row[1])
                                bot.send_message(int(chatid), message.text)
                        if where == '11':
                            if row[4] == '11':
                                chatid = str(row[1])
                                bot.send_message(int(chatid), message.text)
                        if where == '10 и 11':
                            if row[4] == '10 и 11':
                                chatid = str(row[1])
                                bot.send_message(int(chatid), message.text)
                    if row[3] == 'research and projects':
                        if where == '10':
                            if row[4] == '10':
                                chatid = str(row[1])
                                bot.send_message(int(chatid), message.text)
                        if where == '11':
                            if row[4] == '11':
                                chatid = str(row[1])
                                bot.send_message(int(chatid), message.text)
                        if where == '10 и 11':
                            if row[4] == '10 и 11':
                                chatid = str(row[1])
                                bot.send_message(int(chatid), message.text)
            cursor.close()
            conn.close()
            back = bot.send_message(message.chat.id, 'Сообщение разослано!', reply_markup=markup1)
            bot.register_next_step_handler(back, commands)
        else:
            again = bot.send_message(message.chat.id, 'Принимается только текст')
            bot.register_next_step_handler(again, commands)

#___________________изменяем профиль пользователя____________________
def userthemes(message):
    conn = sqlite3.connect('users.sqlite')  # подключаемся к бд
    cursor = conn.cursor()
    # cursor.execute("DELETE FROM usersusers")
    if message.text == 'Исследования':
        cursor.execute("UPDATE usersusers SET theme = 'research' WHERE userid = (?)", (message.chat.id,))
        #print(8.1)
    elif message.text == 'Проекты':
        cursor.execute("UPDATE usersusers SET theme = 'projects' WHERE userid = (?)", (message.chat.id,))
        #print(8.2)
    elif message.text == 'Исследования и проекты':
        cursor.execute("UPDATE usersusers SET theme = 'research and projects' WHERE userid = (?)", (message.chat.id,))
        #print(8.3)
    conn.commit()
    conn.close()
    year = bot.send_message(message.chat.id, 'Уведомления какого класса вы хотите получать?', reply_markup=markup7)
    bot.register_next_step_handler(year, letsdoyear)  # ждем определение для перехода к следующей функции

#_____________________изменяем год пользователя________________________
def letsdoyear(message):
    conn = sqlite3.connect('users.sqlite')  # подключаемся к бд
    cursor = conn.cursor()
    # cursor.execute("DELETE FROM usersusers")
    if message.text == '10':
        cursor.execute("UPDATE usersusers SET level = '10' WHERE userid = (?)", (message.chat.id,))
        # print(8.1)
    elif message.text == '11':
        cursor.execute("UPDATE usersusers SET level = '11' WHERE userid = (?)", (message.chat.id,))
        # print(8.2)
    elif message.text == '10 и 11':
        cursor.execute("UPDATE usersusers SET level = '10 и 11' WHERE userid = (?)", (message.chat.id,))
        # print(8.3)
    conn.commit()
    conn.close()
    backto = bot.send_message(message.chat.id, 'Готово! Ожидайте уведомлений!', reply_markup=markup6)
    bot.register_next_step_handler(backto, usercommands)

#_______________________удаляем старые данные о пользователе________________
def sage(message):
    if message.text == 'Хорошо':
        conn = sqlite3.connect('users.sqlite')  # подключаемся к бд
        cursor = conn.cursor()
        deleteme = "DELETE FROM usersusers WHERE userid = ?"
        cursor.execute(deleteme, (message.chat.id,))
        bot.send_message(message.chat.id, 'Старые данные успешно удалены. \n'
                                          'Пожалуйста, пройдите процедуру регистрации еще раз')
        conn.commit()
        conn.close()
    else:
        well = bot.send_message(message.chat.id, 'Пожалуйста, нажмите "Хорошо", чтобы удалить прошлые данные',
                                reply_markup=markup8)
        bot.register_next_step_handler(well, sage)

conn.commit()

#___________________получаем поток данных от серверов Телеграмм_____________

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=2, timeout=10)
        except Exception as e:
            print(e)
            time.sleep(15)
            @bot.message_handler(content_types=["text"])
            def again_please(message):
                bot.send_message(message.chat.id, 'Сервер Телеграмм остановил работу бота. \n'
                                                  'Пожалуйста, нажмите /start для возобновления')