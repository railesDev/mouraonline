from bot import moura, router, F, types, FSMContext, ReplyKeyboardRemove
from bot import c, conn
from states import User
import dboper
import consts
import keyboards
import random
import asyncio
from inact import InactivityChecker


@router.message(
    User.action,
    F.text.in_(consts.actions)
)
async def perform_action(message: types.Message, state: FSMContext):
    blacklisted = dboper.check_blacklist(conn, c, message.from_user.id)
    if blacklisted:
        await message.answer(consts.blacklisted_caption)
        await state.clear()
        return
    data = await state.get_data()
    if message.text == consts.actions[2]:
        dboper.react(conn, c, message.from_user.id, data["awaiting"], 1)
        await moura.send_message(chat_id=data["awaiting"],
                                 text=consts.got_like_caption,
                                 reply_markup=keyboards.see_likes_keyboard)
        await message.answer(consts.like_caption,
                             reply_markup=keyboards.awaiting_keyboard)
        await state.set_state(User.awaiting)
        await state.update_data(awaiting=-1)

        # SPECIAL LINES TO CHECK INACTIVITY EACH 24 HOURS
        '''while True:
            await asyncio.sleep(86400)
            try:
                data = await state.get_data()
                if data['awaiting'] > 0:
                    break
            except KeyError:
                await message.answer(random.choice(consts.inactivity_caption))'''
        checker = InactivityChecker(state, message)
        await checker.start()

    elif message.text == consts.actions[1]:
        dboper.react(conn, c, message.from_user.id, data["awaiting"], 0)
        await message.answer(consts.dislike_caption,
                             reply_markup=keyboards.awaiting_keyboard)
        # TODO: 100% NEXT AD WILL BE SENT
        await state.set_state(User.awaiting)
        await state.update_data(awaiting=-1)

        # SPECIAL LINES TO CHECK INACTIVITY EACH 24 HOURS
        checker = InactivityChecker(state, message)
        await checker.start()
        
        '''while True:
            await asyncio.sleep(86400)
            try:
                data = await state.get_data()
                if data['awaiting'] > 0:
                    break
            except KeyError:
                await message.answer(random.choice(consts.inactivity_caption))'''

    elif message.text == consts.actions[0]:
        dboper.react(conn, c, message.from_user.id, data["awaiting"], 0)
        await message.answer(consts.complain_caption,
                             reply_markup=keyboards.awaiting_keyboard)
        await state.set_state(User.awaiting)
        await state.update_data(awaiting=-1)

        # SPECIAL LINES TO CHECK INACTIVITY EACH 24 HOURS

        checker = InactivityChecker(state, message)
        await checker.start()
        
        '''
        while True:
            await asyncio.sleep(86400)
            try:
                data = await state.get_data()
                if data['awaiting'] > 0:
                    break
            except KeyError:
                await message.answer(random.choice(consts.inactivity_caption))'''
