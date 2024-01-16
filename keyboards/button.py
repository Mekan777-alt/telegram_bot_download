from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text='💰 Оплатить подписку', callback_data='buy_subscription'),
        ],
        [
            InlineKeyboardButton(text='📓 Профиль', callback_data='profile'),
            InlineKeyboardButton(text='🆘 Помощь', callback_data='help'),
        ],
        [
            InlineKeyboardButton(text='📰 Наш канал', url='http://example.com/channel')
        ]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    return markup


def buy_subscription_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text='7 дней -- 99 руб.', callback_data='7_day')
        ],
        [
            InlineKeyboardButton(text='1 месяц -- 306 руб.', callback_data='1_month')
        ],
        [
            InlineKeyboardButton(text='3 месяца -- 778 руб.', callback_data='3_month')
        ],
        [
            InlineKeyboardButton(text='6 месяцев -- 1332 руб.', callback_data='6_month')
        ],
        [
            InlineKeyboardButton(text='🎇 1 год -- 2403 руб.', callback_data='1_year')
        ],
        [
            InlineKeyboardButton(text='👑 НАВСЕГДА -- 3519 руб.', callback_data='forever')
        ],
        [
            InlineKeyboardButton(text='🔙 Назад', callback_data='back_menu')
        ],
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    return markup


def profile_button():
    keyboard = [
        [
            InlineKeyboardButton(text='👥 Рефералка', callback_data='referal')
        ],
        [
            InlineKeyboardButton(text='👁 Отслеживаемые', callback_data='referal'),
            InlineKeyboardButton(text='👅 Язык бота', callback_data='language')
        ],
        [
            InlineKeyboardButton(text='📩 Мои чаты', callback_data='referal'),
            InlineKeyboardButton(text='🔑 Токены VK', callback_data='referal')
        ],
        [
            InlineKeyboardButton(text='🔙 Назад', callback_data='back_menu')
        ]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    return markup


def buy_carts():
    buttons = [
        [
            InlineKeyboardButton(text='💳 Банк. карта', callback_data='bank_cart')
        ],
        [
            InlineKeyboardButton(text='🔙 Назад', callback_data='back_buy')
        ]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    return markup


def referal_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text='💸 Заработать на боте', callback_data='cash_bot')
        ],
        [
            InlineKeyboardButton(text='🔗 Отправить другу ссылку', callback_data='send_friend')
        ],
        [
            InlineKeyboardButton(text='🔙 Назад', callback_data='back_profile')
        ]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    return markup


def help_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text='📋 Пройти обучение', callback_data='education')
        ],
        [
            InlineKeyboardButton(text='📩 Поддержка', url="hpkzn.ru")
        ],
        [
            InlineKeyboardButton(text='🔙 Назад', callback_data='back_menu')
        ]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    return markup


def list1_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text='▶️ Далее', callback_data='list_1'),
            InlineKeyboardButton(text='🚫 Закончить', callback_data='done')
        ]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    return markup


def list2_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text='◀️ Назад', callback_data='back_list_1'),
            InlineKeyboardButton(text='▶️ Далее', callback_data='list_2')
        ],
        [
            InlineKeyboardButton(text='🚫 Закончить', callback_data='done')
        ]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    return markup


def list3_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text='◀️ Назад', callback_data='back_list_2'),
            InlineKeyboardButton(text='▶️ Далее', callback_data='list_3')
        ],
        [
            InlineKeyboardButton(text='🚫 Закончить', callback_data='done')
        ]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    return markup


def list4_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text='◀️ Назад', callback_data='back_list_3'),
            InlineKeyboardButton(text='▶️ Далее', callback_data='list_4')
        ],
        [
            InlineKeyboardButton(text='🚫 Закончить', callback_data='done')
        ]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    return markup


def list5_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text='◀️ Назад', callback_data='back_list_4'),
            InlineKeyboardButton(text='▶️ Далее', callback_data='list_5')
        ],
        [
            InlineKeyboardButton(text='🚫 Закончить', callback_data='done')
        ]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    return markup


def list6_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text='◀️ Назад', callback_data='back_list_5'),
            InlineKeyboardButton(text='🚫 Закончить', callback_data='done')
        ]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    return markup

