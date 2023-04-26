import db

from aiogram import Dispatcher, Bot, executor, types

from keyboards import get_kb, get_video_cards_ikb, get_profile_kb, get_video_card_ikb


API_TOKEN = '5225759103:AAFMlBh72y_wFVc1nhoCJ9WZ3PXnsNTngGo'
BOT_NICKNAME = 'best_booot_bot'
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


async def on_startup(_):
    print('bot online')
    db.sql_start()

video_cards = ((1, 25), (2, 50), (3, 100), (4, 250), (5, 500), (6, 1000))


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    user_id = message.from_user.id
    if not await db.get_user(user_id):
        referrer_id = str(message.text[7:])
        if referrer_id != '':
            if referrer_id != str(message.from_user.id):
                await db.add_user(user_id, referrer_id)
                try:
                    await bot.send_message(referrer_id, 'По вашей реферальнной ссылке зарегистрировался новый '
                                                        'пользователь!')
                except:
                    pass
            else:
                await db.create_user(user_id)
                await db.add_user(user_id)
                await bot.send_message(message.from_user.id, 'Нельзя регистрироваться по собственной реферальнной '
                                                             'ссылке!')
        else:
            await db.create_user(user_id)
            await db.add_user(user_id)
    await bot.send_message(message.from_user.id, 'ℹ️Вы открыли меню\n\n📢 Новости — @RiseGame_CIS',
                           reply_markup=get_kb())


@dp.message_handler(text='🔙 Меню')
async def cmd_start(message: types.Message) -> None:
    await bot.send_message(message.from_user.id, 'ℹ️Вы открыли меню\n\n📢 Новости — @RiseGame_CIS',
                           reply_markup=get_kb())


@dp.message_handler(text=['📈Инвестировать'])
async def cmd_invest(message: types.Message) -> None:
    await bot.send_message(message.from_user.id, '🗳 <b>Выбирайте нужную вам видеокарту:</b>',
                           reply_markup=get_video_cards_ikb())


@dp.message_handler(text=['💻Мои видеокарты'])
async def cmd_video_card(message: types.Message) -> None:
    await bot.send_message(message.from_user.id, '🗳 <b>Все ваши активные видеокарты:</b>')


@dp.callback_query_handler(lambda c: c.data.startswith('level'))
async def callback_video_cards(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(f'💻 Видеокарта {video_cards[int(callback.data[-1])][0]} <b>LEVEL</b> \n\n'
                                     f'💰 Стоимость: {video_cards[int(callback.data[-1])][1]}$ \n\n'
                                     f'📈 Прибыль: 140%',
                                     reply_markup=get_video_card_ikb())
    await callback.answer()


@dp.callback_query_handler(lambda c: c.data.startswith('video-card'))
async def callback_video_card(callback: types.CallbackQuery) -> None:
    if callback.data == 'video-card_buy':
        await callback.answer('покупка')
    else:
        await callback.message.edit_text('🗳 <b>Выбирайте нужную вам видеокарту:</b>',
                                         reply_markup=get_video_cards_ikb())
        await callback.answer()


@dp.message_handler(text=['💼Профиль'])
async def cmd_profile(message: types.Message) -> None:
    user_data = await db.get_user(message.from_user.id)
    for data in user_data:
        await bot.send_message(message.from_user.id, f'<b>💼 Ваш профиль:</b>\n\n'
                               f'⚡️ <b>ID в боте:</b> {data[0]}\n'
                               f'⚡️ <b>Дата регистрации:</b> {data[1]}\n\n'
                               f'📊 <b>Ваша статистика:</b>\n\n'
                               f'👉🏻 <b>Баланс:</b> {data[2]}$\n'
                               f'👉🏻 <b>Инвестировано всего:</b> {data[3]}$\n'
                               f'👉🏻 <b>Получено прибыли всего:</b> {data[4]}$\n\n'
                               f'По любым вопросам — @risegame_help',
                               reply_markup=get_profile_kb())


@dp.message_handler(text=['💸 Реферальная система'])
async def cmd_referal(message: types.Message):
    count_referals = await db.count_referals(message.from_user.id)
    await bot.send_message(message.from_user.id, f'💸 Реферальная система:\n\n'
                                                 f'⚡️ Кол-во ваших рефералов: {count_referals}\n'
                                                 f'⚡️ Заработано с рефералов: {0}$\n\n'
                                                 f'🔗 Ваша реферальная ссылка:\n'
                                                 f'➖ https://t.me/{BOT_NICKNAME}?start={message.from_user.id}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
