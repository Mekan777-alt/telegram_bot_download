from aiogram import types, Router, F
from aiogram.filters import Command
from keyboards.button import *
from config import db
from datetime import datetime, timedelta
from month.month import month

router = Router()


@router.callback_query(F.data == 'help')
async def help(call: types.CallbackQuery):
    await call.message.edit_text("Вы можете пройти краткое обучение по использованию бота,"
                                 " либо связаться с <b>поддежкой</b> напрямую, чтобы задать вопрос.\n"
                                 "\n"
                                 "У вас остались вопросы по использованию бота? Нажмите кнопку "
                                 "<b>«Поддержка»</b>, чтобы написать нам 👩🏼‍💻", reply_markup=help_keyboard(),
                                 parse_mode='html')


@router.callback_query(F.data == 'back_list_1')
@router.callback_query(F.data == 'education')
async def education(call: types.CallbackQuery):
    await call.message.edit_text('Бот умеет смотреть <b>анонимно</b> сторис в Инстаграм и Вконтакте. '
                                 'Для этого нужно боту отправить ссылку на профиль 🤫\n\n <b>Внимание!</b> '
                                 'У пользователя в списке просмотренных никто не отобразится, максимально анонимно.\n\n'
                                 '📄 Страница: <b>1/6</b>', parse_mode='html', reply_markup=list1_keyboard())


@router.callback_query(F.data == 'back_list_2')
@router.callback_query(F.data == 'list_1')
async def list_1(call: types.CallbackQuery):
    await call.message.edit_text("Помимо анонимного просмотра можно скачать любое медиа в максимальном качестве "
                                 "из Инстаграм. \n\nФото, видео, Hightlight, Reels и т.п.\n\n 📄 Страница: <b>2/6</b>",
                                 reply_markup=list2_keyboard(), parse_mode='html')


@router.callback_query(F.data == 'back_list_3')
@router.callback_query(F.data == 'list_2')
async def list_2(call: types.CallbackQuery):
    await call.message.edit_text("<b>Отслеживание</b> — регулярное получение новых историй пользователя Вконтакте или"
                                 " Инстаграм. "
                                 "Подключить отслеживание вы сможете отправив боту ссылку на профиль ВК или Инсты.\n"
                                 "\n"
                                 "Бот будет постоянно <b>следить</b> за профилем и при появлении новых историй "
                                 "отправит вам в чат.\n"
                                 "\n"
                                 "📄 Страница: <b>3/6</b>", parse_mode='html', reply_markup=list3_keyboard())


@router.callback_query(F.data == 'back_list_4')
@router.callback_query(F.data == 'list_3')
async def list3(call: types.CallbackQuery):
    await call.message.edit_text("Бот может скачать VK Клипы, Insagram Reels, YouTube Shorts <b>без водного знака</b> "
                                 "в "
                                 "максимальном качестве.\n\nПросто отправьте ссылку!\n\n"
                                 "📄 Страница: <b>4/6</b>", parse_mode='html', reply_markup=list4_keyboard())


@router.callback_query(F.data == 'back_list_5')
@router.callback_query(F.data == 'list_4')
async def list4(call: types.CallbackQuery):
    await call.message.edit_text("Бота можно <b>добавить в чат</b> и вместе с друзьями смотреть анонимно "
                                 "сторисы, скачивать "
                                 "через бота видео, чтобы ваши товарищи их оценили.\n\n"
                                 "Также вы можете настроить в разделе <b>«Профиль»</b> чаты, в которые будут "
                                 "отправляться отслеживаемые истории.\n\n"
                                 "📄 Страница: <b>5/6</b>", parse_mode='html', reply_markup=list5_keyboard())


@router.callback_query(F.data == 'back_list_6')
@router.callback_query(F.data == 'list_5')
async def list5(call: types.CallbackQuery):
    await call.message.edit_text(f"Бот является <b>лучшим</b> в Телеграм для отслеживания Инстаграм и Вконтакте. "
                                 f"Стабильная работа, удобный интерфейс и самые демократичные цены.\n"
                                 f"\n"
                                 f"Подпишитесь на канал, чтобы не пропускать информацию об обновлениях, "
                                 f"акциях и бонусах @sdasas\n\n"
                                 f"Подробнее про все <b>возможности</b> бота можно узнать в /faq (нажмите на команду)\n"
                                 f"\n"
                                 f"📄 Страница: <b>6/6</b>", reply_markup=list6_keyboard(), parse_mode='html')


@router.callback_query(F.data == 'done')
async def done(call: types.CallbackQuery):
    markup = main_keyboard()
    await call.message.edit_text("👋🏻 Бот умеет <b>анонимно</b> смотреть любой контент в Инстаграм и Вконтакте.\n"
                                 "\n"
                                 "👀 Просто отправь ссылку на <b>ВК, Инсту, Ютуб</b> или <b>TikTok</b>. "
                                 "Всё что умеет бот можно прочитать "
                                 "в /faq (нажми)\n"
                                 "\n"
                                 "🤔 Лучший бот по цене за подписку, кол-ву функций и стабильности работы.",
                                 reply_markup=markup, parse_mode='html')
