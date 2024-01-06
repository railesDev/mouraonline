from bot import moura
from bot import dp, router, types, FSMContext, F
import keyboards
from states import User
import consts
from handlers import parse_ad


@router.message(
    User.ad_text,
    F.text.len() > 10
)
async def finish_reg(message: types.Message, state: FSMContext):
    await state.update_data(ad_text=message.text)
    data = await state.get_data()
    sdata = parse_ad.parse_ad(data)
    await message.answer_photo(sdata[1],
                               caption=consts.finish_caption(sdata[0]),
                               reply_markup=keyboards.last_keyboard
                               )
    await state.set_state(User.finished)


# Ad is too short
@router.message(
    User.ad_text,
    F.text.len() <= 10
)
async def not_finished(message: types.Message, state: FSMContext):
    await message.reply(consts.ad_short_caption)
