from bot import router, F, types, FSMContext
import keyboards
from states import User
import consts
import logging


@router.message(
    User.program,
    F.text.in_(consts.program_options)
)
async def program(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    try:
        prog = data["program"]
    except KeyError:
        await state.update_data(program=message.text)

    # Log updated data
    sdata = ", ".join([f"{key} - {value}" for key, value in data.items()])
    logging.info("User data for id " + str(message.from_user.id) + " is set to " + sdata)

    # ask for course
    # await state.update_data(program=message.text)
    await message.reply_photo(consts.course_photo,
                              consts.course_caption(message.text),
                              reply_markup=keyboards.course_keyboard(message.text))
    # TODO: Oriental Studies have 5 courses
    await state.set_state(User.course)
