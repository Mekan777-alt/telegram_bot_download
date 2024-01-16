from aiogram import types, Router, F
from aiogram.filters import Command
from keyboards.button import main_keyboard, buy_subscription_keyboard, buy_carts
from config import db
from datetime import datetime, timedelta

router = Router()


@router.message(Command("start"))
async def start_command(message: types.Message):
    user_id = str(message.from_user.id)
    user_id_from_db = db.fetchone("SELECT user_id FROM users WHERE user_id=?", (user_id,))
    if user_id_from_db is not None and str(user_id_from_db[0]) == user_id:
        markup = main_keyboard()
        await message.answer("👋🏻 Бот умеет <b>анонимно</b> смотреть любой контент в Инстаграм и Вконтакте.\n"
                             "\n"
                             "👀 Просто отправь ссылку на <b>ВК, Инсту, Ютуб</b> или <b>TikTok</b>. "
                             "Всё что умеет бот можно прочитать "
                             "в /faq (нажми)\n"
                             "\n"
                             "🤔 Лучший бот по цене за подписку, кол-ву функций и стабильности работы.",
                             reply_markup=markup, parse_mode='html')
    else:
        now = datetime.now()
        one_day = timedelta(days=1)
        new_date = now + one_day
        db.query(
            "INSERT INTO users (user_id, user_name, type_subscripion, start_subscription, end_subscription, sum_buy) "
            "VALUES (?, ?, ?, ?, ?, ?)", (int(message.from_user.id), str(message.from_user.username),
                                          'trial', now, new_date, 0))
        markup = main_keyboard()
        await message.answer("👋🏻 Бот умеет <b>анонимно</b> смотреть любой контент в Инстаграм и Вконтакте.\n"
                             "\n"
                             "👀 Просто отправь ссылку на <b>ВК, Инсту, Ютуб</b> или <b>TikTok</b>. "
                             "Всё что умеет бот можно прочитать "
                             "в /faq (нажми)\n"
                             "\n"
                             "🤔 Лучший бот по цене за подписку, кол-ву функций и стабильности работы.",
                             reply_markup=markup, parse_mode='html')


@router.callback_query(F.data == 'back_buy')
@router.callback_query(F.data == 'buy_subscription')
async def buy(call: types.CallbackQuery):
    user_id = int(call.from_user.id)
    buy_sum = db.fetchone("SELECT sum_buy FROM users WHERE user_id=?", (user_id,))
    subscribe_date = db.fetchone("SELECT end_subscription FROM users WHERE user_id=?",
                                 (user_id,))
    subscribe = db.fetchone("SELECT type_subscripion FROM users WHERE user_id=?", (user_id,))
    markup = buy_subscription_keyboard()
    if subscribe[0] == 'trial':
        date_object = datetime.strptime(subscribe_date[0], '%Y-%m-%d %H:%M:%S.%f')

        hours_minutes = date_object.strftime('%H:%M')
        await call.message.edit_text(f"<b>Условия скидок</b> 💯\n"
                                     f"— Покупок от 2500 руб: 15%\n"
                                     f"— Покупок от 1200 руб: 8%\n"
                                     f"— Покупок от 500 руб: 5%\n"
                                     f"— Для первой покупки: 10%\n"
                                     f"Больше покупок в боте — выше скидка.\n"
                                     f"\n"
                                     f"🏷 Ваша скидка: 10%\n"
                                     f"💳 Сумма покупок: {buy_sum[0]} руб.\n"
                                     f"🔑 Подписка: Закончится завтра в <b>{hours_minutes}</b> (МСК)\n"
                                     f"\n"
                                     f"— Покупая подписку НАВСЕГДА у вас снимаются все лимиты.\n"
                                     f"— Чем дольше подписка, тем выгоднее.", reply_markup=markup, parse_mode="html")
    else:
        await call.message.edit_text(f"<b>Условия скидок</b> 💯\n"
                                     f"— Покупок от 2500 руб: 15%\n"
                                     f"— Покупок от 1200 руб: 8%\n"
                                     f"— Покупок от 500 руб: 5%\n"
                                     f"— Для первой покупки: 10%\n"
                                     f"Больше покупок в боте — выше скидка.\n"
                                     f"\n"
                                     f"🏷 Ваша скидка: 10%\n"
                                     f"💳 Сумма покупок: {buy_sum[0]} руб.\n"
                                     f"🔑 Подписка: Закончится {subscribe_date} (МСК)\n"
                                     f"\n"
                                     f"— Покупая подписку НАВСЕГДА у вас снимаются все лимиты.\n"
                                     f"— Чем дольше подписка, тем выгоднее.", reply_markup=markup, parse_mode="html")


@router.callback_query(F.data == '7_day')
@router.callback_query(F.data == '1_month')
@router.callback_query(F.data == '3_month')
@router.callback_query(F.data == '6_month')
@router.callback_query(F.data == '1_year')
@router.callback_query(F.data == 'forever')
async def seven_days(call: types.CallbackQuery):
    markup = buy_carts()
    await call.message.edit_text("Выберите удобный для вас способ оплаты.\n"
                                 "\n"
                                 "💳 Банк. карта — это сервис RoboКасса.\n"
                                 "— Методы оплаты: Банковская карта, ЮMoney, SberPay, MirPay.", reply_markup=markup)


@router.callback_query(F.data == 'back_menu')
async def back_menu(call: types.CallbackQuery):
    markup = main_keyboard()
    await call.message.edit_text("👋🏻 Бот умеет анонимно смотреть любой контент в Инстаграм и Вконтакте.\n"
                                 "\n"
                                 "👀 Просто отправь ссылку на ВК, Инсту, Ютуб или TikTok. Всё что умеет бот можно "
                                 "прочитать "
                                 "в /faq (нажми)\n"
                                 "\n"
                                 "🤔 Лучший бот по цене за подписку, кол-ву функций и стабильности работы.",
                                 reply_markup=markup)
