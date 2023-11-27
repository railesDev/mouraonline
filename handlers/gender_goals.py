from bot import router, F, types, FSMContext
import keyboards
from states import User
import consts


@router.message(
    User.gender_goals,
    F.text.in_(consts.gender_goals_options)
)
async def gender_goals(message: types.Message, state: FSMContext) -> None:
    await state.update_data(gender_goals=(consts.gender_goals_options.index(message.text)))
    # ask for a photo
    await state.set_state(User.photo_id)
    await message.answer_photo(consts.photo_id_photo,
                               consts.photo_id_caption,
                               reply_markup=keyboards.photo_keyboard)
