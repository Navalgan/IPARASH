import random
from aiogram.utils import executor

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = '5674494549:AAGBjydRKDmSjrwre9uzTvdPbh-ZeCOrIM4'

bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn0 = types.KeyboardButton("/help")
    btn1 = types.KeyboardButton("/rat_test")
    btn2 = types.KeyboardButton("/who")
    btn3 = types.KeyboardButton("/look_at_me")
    btn4 = types.KeyboardButton("/azaza")
    btn5 = types.KeyboardButton("/Nutry_or_Kris")
    markup.add(btn0, btn1, btn2, btn3, btn4, btn5)
    await bot.send_message(message.chat.id,
                           text="Добрый вечер, {0.first_name}! Напиши /help для помощи!".format(message.from_user),
                           reply_markup=markup)


@dp.message_handler(commands=['azaza'])
async def azaza(message):
    await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG_A5jpwfVT5ktMibQGSqTxq_M5zdLGwAClksAAulVBRgn7Dw-I_hQPywE')


@dp.message_handler(content_types=['sticker'])
async def sticker(message):
    await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG_A5jpwfVT5ktMibQGSqTxq_M5zdLGwAClksAAulVBRgn7Dw-I_hQPywE')


@dp.message_handler(commands=['help'])
async def help(message):
    text = [
        'Я сделяль: ',
        '/start - старт?',
        '/help - помогите',
        '/rat_test - тест на крысу',
        '/who - тест на то, какая ты крыса',
        '/look_at_me - похож ли ты на крысу',
        '/azaza - эмуляция ответов Ажажа',
        '/Nutry_or_Kris - какая крыса тебе подходит лучше'
    ]
    await message.reply('\n'.join(text))


@dp.message_handler(commands=['rat_test'])
async def rat_test(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.InlineKeyboardButton("Крысинство")
    btn2 = types.InlineKeyboardButton("Крысасилие")
    btn3 = types.InlineKeyboardButton("Репост Крысиного")
    btn4 = types.InlineKeyboardButton("Нет, я крыса")
    btn5 = types.InlineKeyboardButton("Да, я крыса")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    await bot.send_message(message.chat.id, "Какая из этих статей уважается крысами?", reply_markup=markup)


@dp.message_handler(commands=['who'])
async def rat_test(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.InlineKeyboardButton("Мдуа")
    btn2 = types.InlineKeyboardButton("Блнет")
    markup.add(btn1, btn2)
    await bot.send_message(message.chat.id, "Ты был на КР по матану?", reply_markup=markup)


@dp.message_handler(commands=['look_at_me'])
async def rat_test(message):
    await bot.send_message(message.chat.id, "Отправь мне своё фото")


@dp.message_handler(commands=['Nutry_or_Kris'])
async def rat_test(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.InlineKeyboardButton("Нутри")
    btn2 = types.InlineKeyboardButton("Крис")
    markup.add(btn1, btn2)
    await bot.send_message(message.chat.id, "Выбери свою сторону!", reply_markup=markup)

@dp.message_handler(content_types=['photo'])
async def photo(message):
    photo = open('rat.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo)


@dp.message_handler(content_types=['text'])
async def func(message):
    no_ans = ["Крысинство", "Крысасилие", "Нет, я крыса", "Да, я крыса", "Сажают в клетку", "Нет такого понятия"]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn0 = types.KeyboardButton("/help")
    btn1 = types.KeyboardButton("/rat_test")
    btn2 = types.KeyboardButton("/who")
    btn3 = types.KeyboardButton("/look_at_me")
    btn4 = types.KeyboardButton("/azaza")
    btn5 = types.KeyboardButton("/Nutry_or_Kris")
    btn6 = types.KeyboardButton("крыса!")
    markup.add(btn0, btn1, btn2, btn3, btn4, btn5, btn6)

    if (message.text in no_ans):
        await bot.send_message(message.chat.id,
                               text="Нет, ты крыса!".format(message.from_user),
                               reply_markup=markup)
    elif (message.text == "Нутри"):
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEG_A5jpwfVT5ktMibQGSqTxq_M5zdLGwAClksAAulVBRgn7Dw-I_hQPywE',
                               reply_markup=markup)
    elif (message.text == "Крис"):
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEG_CljpxeGTkLeTpmBMTx0gr674NGM2wACXCEAAkNDeEqkPsa3adYiviwE',
                               reply_markup=markup)
    elif (message.text == "Мдуа"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton("А")
        btn2 = types.InlineKeyboardButton("Ве")
        btn3 = types.InlineKeyboardButton("Ма")
        btn4 = types.InlineKeyboardButton("Ри")
        btn5 = types.InlineKeyboardButton("Я")
        btn6 = types.InlineKeyboardButton("Да")
        btn7 = types.InlineKeyboardButton("Нет")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        await bot.send_message(message.chat.id,
                               text="А по терверу?".format(message.from_user),
                               reply_markup=markup)
    elif (message.text == "Да"):
        await bot.send_message(message.chat.id,
                               text="Такую крысу яб завёл, чтоб на кр ходила".format(message.from_user),
                               reply_markup=markup)
    elif (message.text == "Блнет" or message.text == "Нет"):
        await bot.send_message(message.chat.id,
                               text="Ты самая проедливая крыса, которая ещё и забыла про настолки...".format(
                                   message.from_user),
                               reply_markup=markup)
    elif (message.text == "Репост Крысиного"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton("Сажают в клетку")
        btn2 = types.InlineKeyboardButton("Крысовят")
        btn3 = types.InlineKeyboardButton("Делают их смотрящими в хате")
        btn4 = types.InlineKeyboardButton("Нет, я крыса")
        btn5 = types.InlineKeyboardButton("Да, я крыса")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        await bot.send_message(message.chat.id, "Что делают с крысами?", reply_markup=markup)
    elif (message.text == 'Репост Крысиного'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton("Сажают в клетку")
        btn2 = types.InlineKeyboardButton("Крысовят")
        btn3 = types.InlineKeyboardButton("Делают их смотрящими в хате")
        btn4 = types.InlineKeyboardButton("Нет, я крыса")
        btn5 = types.InlineKeyboardButton("Да, я крыса")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        await bot.send_message(message.chat.id, "Что делают с крысами?", reply_markup=markup)
    elif (message.text == 'Крысовят' or message == 'Делают их смотрящими в хате'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton("Что крыса петух")
        btn2 = types.InlineKeyboardButton("Что крыса тервер")
        btn3 = types.InlineKeyboardButton("Что крыса матан")
        btn4 = types.InlineKeyboardButton("Нет, я крыса")
        btn5 = types.InlineKeyboardButton("Да, я крыса")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        await bot.send_message(message.chat.id, "Что означает дырявая миска?", reply_markup=markup)
    elif (message.text == 'Что крыса петух' or message == 'Что крыса тервер' or message == 'Что крыса матан'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton("Нет такого понятия")
        btn2 = types.InlineKeyboardButton("Крысы, не ходящие на кр")
        btn3 = types.InlineKeyboardButton("Все крысы")
        btn4 = types.InlineKeyboardButton("Нет, я крыса")
        btn5 = types.InlineKeyboardButton("Да, я крыса")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        await bot.send_message(message.chat.id, "Кто такие крысы?", reply_markup=markup)
    elif (message.text == 'Крысы, не ходящие на кр' or message == 'Все крысы'):
        await bot.send_message(message.chat.id,
                               text="ЯМы крыса!".format(message.from_user),
                               reply_markup=markup)
    else:
        stickers = [
            'CAACAgIAAxkBAAEG_A5jpwfVT5ktMibQGSqTxq_M5zdLGwAClksAAulVBRgn7Dw-I_hQPywE',
            'CAACAgIAAxkBAAEG_AxjpwfMXe7_uxEpD6nYqLdOQPEiHAACkksAAulVBRjY4xwvKQuEOiwE',
            'CAACAgIAAxkBAAEG_AhjpwetBAr-w0GxxYlJ4EH1irr0wAAC9SAAAmFpgErcB7wSCqWK7iwE',
            'CAACAgIAAxkBAAEG_CFjpxdRj-G6U1LqHBwpr6RRkdmz4gACsB8AAq7AeUqS1xi8YJAgGywE',
            'CAACAgIAAxkBAAEG_CNjpxde7rJsSTmv1WxFlYXXSMi6GgACSx0AAk1PgEpkl0kDWNfxAiwE',
            'CAACAgIAAxkBAAEG_CVjpxdwpLEHRIHTedB7Yp_HLEuaFAACwSEAAo0kgUqL4Xn4j3FFJCwE',
            'CAACAgIAAxkBAAEG_Cdjpxd8skjHZKMe5z3mm_8SEawspAACRSAAAqRUeUpWWm1f0rX_qywE',
            'CAACAgIAAxkBAAEG_CljpxeGTkLeTpmBMTx0gr674NGM2wACXCEAAkNDeEqkPsa3adYiviwE'
        ]
        await bot.send_sticker(message.chat.id, stickers[random.randint(0, len(stickers) - 1)])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
