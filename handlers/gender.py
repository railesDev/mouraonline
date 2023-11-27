from bot import router, F, types, FSMContext
import keyboards
from states import User
import consts
import logging


@router.message(
    (F.text.in_(consts.gender_options))
)
async def gender(message: types.Message, state: FSMContext) -> None:
    await state.update_data(gender=1 if message.text == consts.gender_options[0] else 0)

    # Log updated data
    data = await state.get_data()
    sdata = ", ".join([f"{key} - {value}" for key, value in data.items()])
    logging.info("User data for id "+str(message.from_user.id)+" is set to "+sdata)

    # ask for campus
    await message.answer_photo(consts.campus_photo,
                               consts.campus_caption(message.text),
                               reply_markup=keyboards.keyboard_campus)
    await state.set_state(User.campus)