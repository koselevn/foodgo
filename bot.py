from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import asyncio
import logging
import pymysql
from aiogram.types import ParseMode

bot = Bot(token="6949035753:AAGF7-9NPJxkUbR8tpihp77IBRcYIRKRbCs")
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


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


from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import pymysql

# Стан
class OrderStates(StatesGroup):
    choosing_order = State()

# Виведення списку замовлень
@dp.message_handler(lambda message: message.text == 'Подивитись замовлення', state="*")
async def show_orders(message: types.Message, state: FSMContext):
    chat_id = message.from_user.id
    try:
        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            database='test-foodgo',
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT * FROM couriers 
            JOIN couriers_drive USING(courier_id) 
            JOIN orders USING(order_id) 
            WHERE courier_tg_id = {chat_id} AND order_status = 'On the way' 
            ORDER BY drive_id;"""
        )
        orders = cursor.fetchall()
        if not orders:
            await message.answer("Замовлень немає", reply_markup=kb1)
            return

        await state.update_data(orders=orders)
        await OrderStates.choosing_order.set()

        for order in orders:
            text = (
                f"📦 Замовлення #{order['order_id']}\n"
                f"👤 Клієнт: {order['order_client_name']}\n"
                f"📍 Адреса: {order['order_client_adress']}\n"
                f"📞 Телефон: {order['order_client_phone']}\n"
                f"💵 Оплата: {order['order_client_pay_method']}\n"
                f"💬 Коментар: {order['order_client_comment']}\n"
                f"💰 Ціна: {order['order_pice']} zł\n"
            )
            keyboard = InlineKeyboardMarkup().add(
                InlineKeyboardButton(f"✅ Завершити #{order['order_id']}", callback_data=f"select_order_{order['order_id']}")
            )
            await bot.send_message(chat_id, text, reply_markup=keyboard)

    except Exception as ex:
        print("DB Error:", ex)
        await message.answer("Помилка при з'єднанні з базою даних.")

# Обробка вибору замовлення
@dp.callback_query_handler(lambda c: c.data.startswith('select_order_'), state=OrderStates.choosing_order)
async def finish_order(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()

    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    order_id = int(callback_query.data.replace("select_order_", ""))

    try:
        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            database='test-foodgo',
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE orders SET order_status = 'Delivered' WHERE order_id = {order_id};"
        )
        connection.commit()

        # 🔄 РЕДАГУЄМО повідомлення замовлення — замість нього буде текст завершення
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=f"✅ Замовлення #{order_id} завершено"
        )

        await OrderStates.choosing_order.set()

    except Exception as ex:
        print("DB Error:", ex)
        await bot.send_message(chat_id, "❌ Помилка при оновленні замовлення.")


if __name__ == '__main__':
    executor.start_polling(dp)
