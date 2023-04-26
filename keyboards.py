from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def get_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton('📈Инвестировать')
    btn2 = KeyboardButton('💻Мои видеокарты')
    btn3 = KeyboardButton('💼Профиль')
    kb.add(btn1).add(btn2).add(btn3)
    return kb


def get_profile_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton('💸 Реферальная система')
    btn2 = KeyboardButton('⚙️ Настройки')
    btn3 = KeyboardButton('💳 Вывести деньги')
    btn4 = KeyboardButton('💳 Пополнить баланс')
    btn5 = KeyboardButton('🔙 Меню')
    kb.add(btn1).add(btn2).add(btn3, btn4).add(btn5)
    return kb


def get_video_cards_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=4)
    ibtn1 = InlineKeyboardButton(text='💻1 LEVEL | 25$ | 140%',
                                 callback_data='level_0')
    ibtn2 = InlineKeyboardButton(text='💻2 LEVEL | 50$ | 140%',
                                 callback_data='level_1')
    ibtn3 = InlineKeyboardButton(text='💻3 LEVEL | 100$ | 140%',
                                 callback_data='level_2')
    ibtn4 = InlineKeyboardButton(text='💻4 LEVEL | 250$ | 140%',
                                 callback_data='level_3')
    ibtn5 = InlineKeyboardButton(text='💻5 LEVEL | 500$ | 140%',
                                 callback_data='level_4')
    ibtn6 = InlineKeyboardButton(text='💻6 LEVEL | 1000$ | 140%',
                                 callback_data='level_5')
    ikb.add(ibtn1).add(ibtn2).add(ibtn3).add(ibtn4).add(ibtn5).add(ibtn6)
    return ikb


def get_video_card_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    ibtn1 = InlineKeyboardButton(text='🛍Купить', callback_data='video-card_buy')
    ibtn2 = InlineKeyboardButton(text='🔙Назад', callback_data='video-card_back')
    ikb.add(ibtn1).add(ibtn2)
    return ikb
