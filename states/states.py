from aiogram.fsm.state import StatesGroup, State


class user_state(StatesGroup):
    state_get_user_text = State()  # enter new note
    state_get_user_number = State()  # enter id note
    state_delete = State()  # delete note
    state_remake_1 = State()  # id note remake
    state_remake_2 = State()  # new text note remake
