from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Начать тестирование')
kb.row(button,button2)

kb_in = InlineKeyboardMarkup(resize_keyboard=True)
button3 = InlineKeyboardButton(text='ДА',callback_data='response_yes')
button4 = InlineKeyboardButton(text='НЕТ',callback_data='response_no')
kb_in.add(button3,button4)

kb_about = InlineKeyboardMarkup(resize_keyboard=True)
button_f = InlineKeyboardButton(text='Флегматика',callback_data='fl')
button_ch = InlineKeyboardButton(text='Холерика',callback_data='ch')
button_mel = InlineKeyboardButton(text='Меланхолика',callback_data='mel')
button_san = InlineKeyboardButton(text='Сангвиника',callback_data='san')
kb_about.add(button_f,button_ch)
kb_about.add(button_mel,button_san)


