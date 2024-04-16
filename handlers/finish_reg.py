from bot import moura
from bot import dp, router, types, FSMContext, F
import keyboards
from states import User
import consts
from handlers import parse_ad
import re


@router.message(
    User.ad_text,
)
async def finish_reg(message: types.Message, state: FSMContext):
    # MouraCensor
    suitable = True
    stop_words = ' '
    m = message.text.lower()
    p = re.compile(r'(ук([раинаеойцы]{3,}))|(putin)|(пися\s)|(попа\s)|(россия)|(рашка)|(раися)|(путин[уа]*)|(навальн[ыйому]+)|(укропы)|(\sлох)|(\sсука)|(ебал)|(ебать)|(ху[йея])|(хер)|(пизд)|(пидор)|(пидар)|(гандон)|(твар[иь])|(\sненави)|(суицид)|(гнида)|(сос[ауёеи])|(\sсекс)|(\sпереспать)|(\sтрахну)|(ебу)|(еб\s)|(ёб\s)|(войду)|(куни)|(член)|(пенис)|(сиськи)|(za\s)|(лизать)|(дурак)|(идиот)|(жирный)|(урод)|(говно)|(дерьмо)|(параша)|(хохл)|(бля)|(тво[яюе] мат)|(твой батя)|(иди\s)')
    suitable = not bool(len(p.findall(m))) & message.text.len() > 10 & message.text.contains(' ') & message.text.len() < 750
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

'''
# Ad is too short
@router.message(
    User.ad_text,
    F.text.len() <= 10 
)
async def adshort(message: types.Message, state: FSMContext):
    await message.reply(consts.ad_short_caption)


# Ad is too short
@router.message(
    User.ad_text,
    F.text.len() > 750 
)
async def adlong(message: types.Message, state: FSMContext):
    await message.reply(consts.ad_long_caption)

'''
