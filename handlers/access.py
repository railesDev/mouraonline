from bot import router, F, types, FSMContext, c, conn
import keyboards
from states import User
import consts
import dboper


@router.message(User.id, (F.text.upper() == consts.access_code))
async def access(message: types.Message, state: FSMContext) -> None:
    await state.update_data(id=message.from_user.id)
    # ask for gender
    await message.answer_photo(consts.gender_photo,
                               consts.gender_caption,
                               reply_markup=keyboards.keyboard_gender)
    await state.set_state(User.gender)  # setting state that we wait for gender


@router.message((F.text == consts.start_over))
async def start_over(message: types.Message, state: FSMContext) -> None:
    await message.answer(consts.restart_caption)
    await message.answer_photo(consts.gender_photo,
                               consts.gender_caption,
                               reply_markup=keyboards.keyboard_gender)
    await state.set_state(User.gender)  # setting state that we wait for gender

