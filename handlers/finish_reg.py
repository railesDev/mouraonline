from bot import moura
from bot import dp, router, types, FSMContext, F
import keyboards
from states import User
import consts
from handlers import parse_ad
import re


@router.message(
    User.ad_text,
    F.text.len() > 10
)
async def finish_reg(message: types.Message, state: FSMContext):
    # MouraCensor
    suitable = True
    stop_words = ' '
    m = message.text.lower()
    p = re.compile(r'(ук([раинаеойцы]{3,}))|(россия)|(рашка)|(раися)|(путин[уа]*)|(навальн[ыйому]+)|(укропы)|(лох)|(сука)|(ебал)|(ебать)|(ху[йея])|(хер)|(пизд)|(пидор)|(пидар)|(гандон)|(твар[иь])|(ненавижу)|(суицид)|(гнида)|(сос[ауёеи])|(секс)|(переспать)|(трахну)|(ебу)|(еб\s)|(ёб\s)|(войду)|(куни)|(член)|(пенис)|(сиськи)|(выбор[ыа])|(лизать)|(дурак)|(идиот)|(жирный)|(урод)|(говно)|(дерьмо)|(параша)|(хохл)|(бля)|(тво[яюе] мат)|(твой батя)|(иди)')
    suitable = not bool(len(p.findall(m)))
    #
    if suitable:
        await state.update_data(ad_text=message.text)
        data = await state.get_data()
        sdata = parse_ad.parse_ad(data)
        await message.answer_photo(sdata[1],
                               caption=consts.finish_caption(sdata[0]),
                               reply_markup=keyboards.last_keyboard
                               )
        await state.set_state(User.finished)
    else:
        await message.reply(consts.ad_incorrect_caption)


# Ad is too short
@router.message(
    User.ad_text,
    F.text.len() <= 10
)
async def not_finished(message: types.Message, state: FSMContext):
    await message.reply(consts.ad_short_caption)
