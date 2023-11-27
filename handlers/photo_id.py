from bot import moura
from bot import dp, router, F, types, FSMContext
import keyboards
from states import User
import consts


@router.message(
   User.photo_id, (F.photo | F.text == consts.no_photo)
)
async def photo_sent(message: types.Message, state: FSMContext) -> None:
    try:
        if message.text == consts.no_photo:
            data = await state.get_data()
            await state.update_data(photo_id=(consts.female_anon_photo_id
                                              if data["gender"] == 0 else consts.male_anon_photo_id))
    except Exception:
        pass
    try:
        await state.update_data(photo_id=message.photo[-1].file_id)
    except Exception:
        pass
    # ask for ad text
    await state.set_state(User.ad_text)
    await message.answer_photo(consts.ad_text_photo,
                               consts.ad_text_caption,
                               reply_markup=keyboards.ad_text_keyboard)
