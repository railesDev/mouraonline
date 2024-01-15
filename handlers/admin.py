from bot import router, F, types, FSMContext
import keyboards
from states import User
import consts
import logging

@router.message(F.text == '/railes_control_erdb')
async def reloadb(message: Message, cont
