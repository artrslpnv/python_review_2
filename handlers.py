# -*- coding: utf-8 -*-
import telebot
from BD import get_match,add_matches
from app import bot
import sqlite3

conn = dict()
names=dict()
dates=dict()
score=dict()
goals=dict()
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Привет, я телеграм-бот  сообщающий события ,произошедшие в матче,напиши  /help')


@bot.message_handler(commands=['help'])
def handle_reg(message):
    bot.send_message(message.chat.id, "Напиши навзвания двух команд игравших в матче в формате ' Название команды хозяев "
                                      "- Название Команды гостей' " )
    bot.register_next_step_handler(message, get_name)  # следующий шаг – функция get_name


# Handles all text messages that match the regular expression
@bot.message_handler(content_types=['text'], regexp="python")
def handle_python_message(message):
    bot.send_message(message.chat.id, "Я обожаю python!")


@bot.message_handler(content_types=['text'])
def handle_text_message(message):
    bot.send_message(message.chat.id, message.text)


def get_name(message):
    names[message.chat.id] = message.text
    bot.send_message(message.chat.id, 'Когда это было? Дата в формате дд.мм.гггг')
    bot.register_next_step_handler(message, get_date)
def set_score(message):
    score[message.chat.id]=message.text
    bot.send_message(message.chat.id,"Кто забил голы?  в формате  <Фамилия минута, Фамилия минута ...>")
    bot.register_next_step_handler(message,set_goals)
def set_goals(message):
    goals[message.chat.id]= message.text
    add_matches(conn[message.chat.id].cursor(),conn[message.chat.id],names[message.chat.id],dates[message.chat.id],score[message.chat.id],goals[message.chat.id])
    bot.send_message(message.chat.id,"Спасибо , Пока!")
def get_date(message):
    dates[message.chat.id] = message.text
    conn[message.chat.id]=sqlite3.connect('mthcs.db')
    list=get_match(conn[message.chat.id], names[message.chat.id], dates[message.chat.id])
    if len(list)!=0:
        name,score,goals=list[0]
        answer = 'Матч {Name} закончился со счетом {Score} голы забили {Goals}, Вам понравилась моя работа?'.format(Name=name, Score=score, Goals=goals)
        keyboard = telebot.types.InlineKeyboardMarkup()  # наша клавиатура
        key_yes = telebot.types.InlineKeyboardButton(text='Да', callback_data='yes')
        keyboard.add(key_yes)
        key_no = telebot.types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        key_idk = telebot.types.InlineKeyboardButton(text='Не знаю', callback_data='idk')
        keyboard.add(key_idk)
        bot.send_message(message.chat.id, text=answer, reply_markup=keyboard)
    else:
        answer="Данных по этому матчу найти не удалось :( , Не хотели бы вы нам помочь?"
        keyboard = telebot.types.InlineKeyboardMarkup()  # наша клавиатура
        key_yes = telebot.types.InlineKeyboardButton(text='Да', callback_data='Yes')
        keyboard.add(key_yes)
        key_no = telebot.types.InlineKeyboardButton(text='Нет', callback_data='No')
        keyboard.add(key_no)
        key_idk = telebot.types.InlineKeyboardButton(text='Не знаю', callback_data='Idk')
        keyboard.add(key_idk)
        bot.send_message(message.chat.id, text=answer, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, 'Спасибо! : )')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Попрбуйте еще раз или найдите себе другого бота!:(")
        bot.register_next_step_handler(call.message, get_name)
    elif call.data=='idk':
        bot.send_message(call.message.chat.id, ":|")
    elif call.data == "Yes":
        bot.send_message(call.message.chat.id,'Введите счет этого матча')
        bot.register_next_step_handler(call.message,set_score)
    elif call.data == "No":
        bot.send_message(call.message.chat.id,"Прощайте!")
    elif call.data== "Idk":
        bot.send_message(call.message.chat.id , ":|")
