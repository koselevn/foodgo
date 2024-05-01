from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import asyncio
import logging
import pymysql
from aiogram.types import ParseMode

bot = Bot(token="6949035753:AAGF7-9NPJxkUbR8tpihp77IBRcYIRKRbCs")
dp = Dispatcher(bot)


kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb1.add(KeyboardButton('Подивитись замовлення'))

kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb2.add(KeyboardButton('Завершити замовлення'))

KEY = 'RS95ass'

START = """
Привіт!

Раді бачити тебе курєром в нашому ресторані швидкої їжі FoodGo

Введіть будьласка ключ який був наданий адміністратором

Приклад: /RS95ass
"""

HELP = """
HElP TEXT
"""


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text=START)


@dp.message_handler(commands=['help'])
async def help_message(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text=HELP)


@dp.message_handler(commands=[f'{KEY}'])
async def help_message(message: types.Message):
    chat_id = message.from_user.id
    try:
        conection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            database='test-foodgo',
            cursorclass=pymysql.cursors.DictCursor
        )
        print('Conection')
        try:
            cursor = conection.cursor()
            add_user_query = f"insert into `couriers` (courer_name, courier_tg_id) value ('{message.from_user.first_name}', {message.from_user.id});"
            cursor.execute(add_user_query)
            conection.commit()
            await bot.send_message(chat_id=chat_id, text="Ключь принят!", reply_markup=kb1)
            await bot.send_message(chat_id=chat_id, text="Гловне меню:", reply_markup=kb1)
        finally:
            conection.close()
    except Exception as ex:
        print('No Conection')
        print(ex)
        await bot.send_message(chat_id=chat_id, text='Error!', reply_markup=kb1)
        await bot.send_message(chat_id=chat_id, text=ex, reply_markup=kb1)


@dp.message_handler()
async def balance_message(message: types.Message):
    chat_id = message.from_user.id
    if message.text == 'Подивитись замовлення':
        ORDER_ID = [0]
        # db
        try:
            conection = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                database='test-foodgo',
                cursorclass=pymysql.cursors.DictCursor
            )
            print('Conection')
            try:
                cursor = conection.cursor()
                orderSel_id = f"select * from couriers join couriers_drive using(courier_id) JOIN orders USING(order_id) where courier_tg_id = {message.from_user.id} and order_status = 'On the way' order by drive_id;"
                cursor.execute(orderSel_id)
                order = cursor.fetchall()
                print(order)
                ORDER_ID[0] = order[0]['order_id']
                print(ORDER_ID)
            finally:
                print('And1')
            try:
                cursor = conection.cursor()
                orderSel = f"SELECT * FROM couriers join couriers_drive using(courier_id) JOIN orders USING(order_id) WHERE courier_tg_id = {message.from_user.id} and order_status = 'On the way' order by drive_id;"
                cursor.execute(orderSel)
                order = cursor.fetchall()
                mess_ORDER = f"Order: {order[0]['order_id']}\n\nSTATYS: {order[0]['order_status']}\n\nClient name: {order[0]['order_client_name']}\nAdress: {order[0]['order_client_adress']}\nPhone: {order[0]['order_client_phone']}\nPay method: {order[0]['order_client_pay_method']}\n\nComment: {order[0]['order_client_comment']}\n\n\nPrice: {order[0]['order_pice']} zl"
                print(order)
                await bot.send_message(chat_id=chat_id, text="Замовлення:", reply_markup=kb1)
                await bot.send_message(chat_id=chat_id, text=mess_ORDER, reply_markup=kb2)
            finally:
                conection.close()
                print('And2')
        except Exception as ex:
            print('No Conection')
            print(ex)
            await bot.send_message(chat_id=chat_id, text="Замовлень немає", reply_markup=kb1)
    elif message.text == 'Завершити замовлення':
        ORDER_ID = [0]
        try:
            conection = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                database='test-foodgo',
                cursorclass=pymysql.cursors.DictCursor
            )
            print('Conection')
            try:
                cursor = conection.cursor()
                orderSel_id = f"SELECT * FROM couriers join couriers_drive using(courier_id) JOIN orders USING(order_id) WHERE courier_tg_id = {message.from_user.id} and order_status = 'On the way' order by drive_id;"
                cursor.execute(orderSel_id)
                order = cursor.fetchall()
                print(order)
                ORDER_ID[0] = order[0]['order_id']
                print(ORDER_ID[0])
            finally:
                print('And1')
            try:
                cursor = conection.cursor()
                update_order_ST = f"UPDATE `orders` SET order_status = 'Delivered' where order_id = {int(ORDER_ID[0])};"
                cursor.execute(update_order_ST)
                conection.commit()
            finally:
                print('And2')
                await bot.send_message(chat_id=chat_id, text="Замовлення завершено!", reply_markup=kb1)
        except Exception as ex:
            print('No Conection')
            print(ex)


if __name__ == '__main__':
    executor.start_polling(dp)
