from aiogram import types, Router, F
from keyboards.button import *
from config import db, bot
from datetime import datetime
from month.month import month
from aiogram.utils.markdown import hlink


router = Router()


@router.callback_query(F.data == 'back_profile')
@router.callback_query(F.data == 'profile')
async def profile(call: types.CallbackQuery):
    month_user_check = db.fetchone("SELECT registration FROM users WHERE user_id=?", (int(call.from_user.id),))
    date_object = datetime.strptime(month_user_check[0], '%Y-%m-%d %H:%M:%S.%f')
    month_check = str(date_object.date())[5:7]
    data_check = str(date_object.date())[8:10]
    time_check = str(date_object)[11:16]
    subscribe = db.fetchone("SELECT type_subscripion FROM users WHERE user_id=?", (int(call.from_user.id),))
    subscribe_date = db.fetchone("SELECT end_subscription FROM users WHERE user_id=?",
                                 (call.from_user.id,))
    check_subscr = datetime.strptime(subscribe_date[0], '%Y-%m-%d %H:%M:%S.%f')
    hours_minutes = check_subscr.strftime('%H:%M')
    date = check_subscr.strftime('%Y-%m-%d')
    if month_check in month:
        if subscribe[0] == 'trial':
            await call.message.edit_text(f"☀️ В боте с <b>{data_check}</b> {month[month_check]} <b>{time_check}</b>\n"
                                         f"\n"
                                         f"🔑 <b>Подписка на бота</b>\n"
                                         f"— Подписка закончится завтра в <b>{hours_minutes}</b> МСК\n"
                                         f"\n"
                                         f"В профиле вы можете настроить отслеживаемых, свои токены VK и получить "
                                         f"бонусы за приведённого друга.", reply_markup=profile_button(),
                                         parse_mode="html")
        else:
            await call.message.edit_text(f"☀️ В боте с <b>{data_check}</b> {month[month_check]} <b>{time_check}</b>\n"
                                         f"\n"
                                         f"🔑 <b>Подписка на бота</b>\n"
                                         f"— Подписка закончится {date} <b>{hours_minutes}</b> МСК\n"
                                         f"\n"
                                         f"В профиле вы можете настроить отслеживаемых, свои токены VK и получить "
                                         f"бонусы за приведённого друга.", reply_markup=profile_button(),
                                         parse_mode="html")


@router.callback_query(F.data == 'referal')
async def referal_programm(call: types.CallbackQuery):
    bot_info = await bot.get_me()
    bot_username = bot_info.username
    link = hlink("НАЖМИ СЮДА", f'https://t.me/{bot_username}?start={call.from_user.id}')
    await call.message.edit_text(f"🚀 <b>Пригласительная ссылка</b>\n"
                                 f"— Ссылка: {link}\n"
                                 f"— Перешло по ссылке 0 чел.\n"
                                 f"\n"
                                 f"👥 <b>Последние перешедшие</b>\n"
                                 f"— Вы ещё никого не приглашали.\n"
                                 f"\n"
                                 f"<b>Если привели друга ↓</b>\n"
                                 f"— Получаете +10 поисков.\n"
                                 f"— За каждого пятого +25 поисков.\n"
                                 f"\n"
                                 f"<b>Друг сделал покупку ↓</b>\n"
                                 f"— Получаете 1/3 дней от каждой покупки.\n"
                                 f"— Если подписка навсегда, то 180 дней.", reply_markup=referal_keyboard(),
                                 parse_mode='html')

