from bot import router, F, types, FSMContext, ReplyKeyboardRemove
import keyboards
from states import User
import consts
import logging


@router.message(
    User.course,
    F.text.in_(consts.course_options)
)
async def course(message: types.Message, state: FSMContext) -> None:
    # setting course
    await state.update_data(course=message.text)

    # Log updated data
    data = await state.get_data()
    sdata = ", ".join([f"{key} - {value}" for key, value in data.items()])
    logging.info("User data for id " + str(message.from_user.id) + " is set to " + sdata)

    # ask for goals
    await message.answer_photo(consts.goals_photo,
                               consts.basic_done_caption,
                               reply_markup=ReplyKeyboardRemove())
    await message.answer(consts.goals_caption,
                         reply_markup=keyboards.goals_keyboard().as_markup())
    await state.set_state(User.goals)
    await state.update_data(goals=[])
