from bot import moura
from bot import dp, router, F, types, FSMContext
import keyboards
from states import User
from bot import c, conn
import consts
import dboper
import asyncio
import random
import logging
import consts


def goals_encoder(goals_data, decode=False):
    if decode:
        output = goals_data[0]*(consts.goals[0]+', ')+goals_data[1]*(consts.goals[1]+', ')+goals_data[2]*(consts.goals[2])
        return output
    else:
        code = [consts.goals[0] in goals_data, consts.goals[1] in goals_data, consts.goals[2] in goals_data]
        return code


@router.message(
    User.finished,
    F.text == consts.publish_ad
)
async def register_finishing(message: types.Message, state: FSMContext):
    data = await state.get_data()
    sdata = list(data.values())
    sdata[4] = goals_encoder(sdata[4])
    sdata = sdata[:4] + [sdata[4][0], sdata[4][1], sdata[4][2]] + sdata[5:]
    logging.info("FINAL DATA: "+str(sdata))
    await message.answer(
        text=consts.published_ad_caption,
        reply_markup=keyboards.awaiting_keyboard
    )
    # Insert the user data into the table
    dboper.save_user(conn, c, sdata)
    await state.set_state(User.awaiting)

    # SPECIAL LINES TO CHECK INACTIVITY EACH 10 MINUTES
    while True:
        await asyncio.sleep(600)
        try:
            data = await state.get_data()
            if data['awaiting']:
                pass
        except KeyError:
            await message.answer(random.choice(consts.inactivity_caption))
