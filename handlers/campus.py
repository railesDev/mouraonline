from bot import router, F, types, FSMContext
import keyboards
from states import User
import consts
import logging

from handlers import program


@router.message(
    User.campus,
    F.text.in_(consts.campus_options)
)
async def campus(message: types.Message, state: FSMContext):
    await state.update_data(campus=message.text)

    # Log updated data
    data = await state.get_data()
    sdata = ", ".join([f"{key} - {value}" for key, value in data.items()])
    logging.info("User data for id " + str(message.from_user.id) + " is set to " + sdata)

    await message.answer_photo(consts.campus_reaction_photo(message.text),
                               caption=consts.campus_reaction_caption)

    # process individual case with Sedova
    if message.text == 'Sedova 🏠':
        await state.update_data(campus=message.text)
        await state.set_state(User.program)
        await state.update_data(program='Sociology 👥')
        await state.set_state(User.course)
        await program.program(message, state)
        return

    # ask for program
    await state.update_data(campus=message.text)
    await message.answer_photo(consts.program_photo,
                               consts.program_caption,
                               reply_markup=keyboards.keyboard_programs(message.text))
    await state.set_state(User.program)
