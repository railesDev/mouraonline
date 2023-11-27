from bot import moura
from bot import dp, router, F, types, FSMContext
import keyboards
from states import User
from bot import c, conn
import consts
import logging
import dboper


@router.message(
    F.text == consts.deactivate_profile
)
async def deactivate(message: types.Message, state: FSMContext):
    await message.answer(consts.deactivate_profile_caption,
                         reply_markup=keyboards.leaving_sure_keyboard)


@router.message(
    F.text == consts.deactivate_sure
)
async def deactivate(message: types.Message, state: FSMContext):
    dboper.deactivate_user(conn, c, message.from_user.id)
    await message.answer(consts.deactivate_sure_caption,
                         reply_markup=keyboards.return_keyboard)
    await state.clear()
