from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контакты'),
                                      KeyboardButton(text='О нас')]],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню...')


catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Коврики для йоги', callback_data='mat')],
    [InlineKeyboardButton(text='Одежда', callback_data='clothes')],
    [InlineKeyboardButton(text='Книги', callback_data='books')],
    [InlineKeyboardButton(text='Подарочные сертификаты', callback_data='certificate')]])


get_numder = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
                                                           request_contact=True)]], 
                            resize_keyboard=True)
