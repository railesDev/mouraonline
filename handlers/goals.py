from bot import moura
from bot import dp, types, FSMContext
import keyboards
from states import User
import consts

from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress


@dp.callback_query()
async def goals(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    chosen_goals = data["goals"]
    if call.data in consts.goals:
        if call.data in chosen_goals:
            chosen_goals.remove(call.data)
            await state.update_data(goals=chosen_goals)
        else:
            chosen_goals.append(call.data)
            await state.update_data(goals=chosen_goals)
        if chosen_goals:
            with suppress(TelegramBadRequest):
                await moura.edit_message_text(chat_id=call.message.chat.id,
                                              message_id=call.message.message_id,
                                              text=consts.goals_chosen_caption(chosen_goals),
                                              reply_markup=keyboards.goals_keyboard().as_markup())
        else:
            with suppress(TelegramBadRequest):
                await moura.edit_message_text(chat_id=call.message.chat.id,
                                              message_id=call.message.message_id,
                                              text=consts.goals_caption,
                                              reply_markup=keyboards.goals_keyboard().as_markup())
    elif call.data == 'save':
        if chosen_goals:
            await state.update_data(goals=chosen_goals)
            with suppress(TelegramBadRequest):
                await moura.edit_message_text(chat_id=call.message.chat.id,
                                              message_id=call.message.message_id,
                                              text=consts.goals_saved_caption(chosen_goals))

            # asking for gender goals
            await state.set_state(User.gender_goals)
            await moura.send_photo(chat_id=call.message.chat.id,
                                   photo=consts.gender_goals_photo,
                                   caption=consts.gender_goals_caption,
                                   reply_markup=keyboards.gendergoals_keyboard)
        else:
            with suppress(TelegramBadRequest):
                await moura.edit_message_text(chat_id=call.message.chat.id,
                                              message_id=call.message.message_id,
                                              text=consts.no_goals_caption,
                                              reply_markup=keyboards.goals_keyboard().as_markup())
