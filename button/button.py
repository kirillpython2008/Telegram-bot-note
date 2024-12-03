from aiogram import types

# create inline button

inline_kb = [[types.InlineKeyboardButton(text='создать заметку', callback_data='get_user_text')]]

inline_keyboard = types.InlineKeyboardMarkup(inline_keyboard=inline_kb)

# create reply button

reply_kb_1 = [[types.KeyboardButton(text='прочитать заметку'), types.KeyboardButton(text='создать заметку')],
              [types.KeyboardButton(text='Удалить заметку'), types.KeyboardButton(text='Редактировать заметку')]]

reply_keyboard_1 = types.ReplyKeyboardMarkup(keyboard=reply_kb_1, resize_keyboard=True)
