from states.states import user_state
from button.button import inline_keyboard, reply_keyboard_1
from basedata.basedata import get_db_text, get_db_number, get_all, delete, remake, all_id_1
from aiogram import Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


# command start
async def func_start(message: types.Message):
    await message.answer(f'Здравствуйте, {message.from_user.first_name}\n'
                         f'Я - бот-заметка, я могу принимать, сохранять, отправлять, изменять и удалять ваши заметки',
                         reply_markup=inline_keyboard)


# inline_button
async def get_text_1_inline(query: types.CallbackQuery, state: FSMContext):
    await query.message.answer('Введите текст заметки')
    await state.set_state(user_state.state_get_user_text)


# reply_button
async def get_text_1_reply(message: types.Message, state: FSMContext):
    await message.answer('Введите текст заметки')
    await state.set_state(user_state.state_get_user_text)


# state
async def get_text_2(message: types.Message, state: FSMContext):
    await get_db_text(message.message_id, message.from_user.id, message.text)
    await state.clear()
    await message.answer(
        f'Заметка сохранена id: {message.message_id}(чтобы посмотреть все свои заметки пропишите /all)',
        reply_markup=reply_keyboard_1)


# reply_button
async def get_number_1(message: types.Message, state: FSMContext):
    await message.answer('Введите id заметки')
    await state.set_state(user_state.state_get_user_number)


# state
async def get_number_2(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        if type(int(message.text)) == int:
            try:
                await message.answer(await get_db_number(int(message.text), message.from_user.id))
            except:
                await message.answer('Такого id нет')
    else:
        await message.answer('id заметки это число')
    await state.clear()


# command
async def get_all_1(message: types.Message):
    for i in await get_all(message.from_user.id):
        await message.answer(f"id: {i[0]} текст заметки: {i[-1]}")


# reply_button
async def delete_1(message: types.Message, state: FSMContext):
    await message.answer('Напишите id заметки, которую хотите удалить')
    await state.set_state(user_state.state_delete)


# state
async def delete_2(message: types.Message, state: FSMContext):
    if await delete(int(message.text), message.from_user.id):
        await message.answer('Заметка удалена')
    else:
        await message.answer('Такого id нет')
    await state.clear()


# reply_button
async def remake_1(message: types.Message, state: FSMContext):
    await message.answer('Напишите id заметки, которой хотите изменить')
    await state.set_state(user_state.state_remake_1)


text_id = 0


# state
async def remake_2(message: types.Message, state: FSMContext):
    global text_id
    text_id = message.text
    if await all_id_1(int(text_id), message.from_user.id):
        await state.clear()
        await state.set_state(user_state.state_remake_2)
        await message.answer('Напишите текст для заметки, которую хотите изменить')
    else:
        await message.answer('Такого id нет')


# state
async def remake_3(message: types.Message, state: FSMContext):
    global text_id
    await remake(message.text, text_id, message.from_user.id)
    await message.answer('Заметка изменена')
    await state.clear()
    text_id = 0


def registration(dp: Dispatcher):

    # reply_button
    dp.message.register(get_number_1, F.text == 'прочитать заметку')
    dp.message.register(get_text_1_reply, F.text == 'создать заметку')
    dp.message.register(delete_1, F.text == 'Удалить заметку')
    dp.message.register(remake_1, F.text == 'Редактировать заметку')

    # inline_button
    dp.callback_query.register(get_text_1_inline, F.data == 'get_user_text')

    # command
    dp.message.register(func_start, Command("start"))
    dp.message.register(get_all_1, Command('all'))

    # state
    dp.message.register(get_text_2, user_state.state_get_user_text)
    dp.message.register(get_number_2, user_state.state_get_user_number)
    dp.message.register(delete_2, user_state.state_delete)
    dp.message.register(remake_2, user_state.state_remake_1)
    dp.message.register(remake_3, user_state.state_remake_2)
