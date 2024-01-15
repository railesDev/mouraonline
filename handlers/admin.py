from bot import router, F, types, FSMContext
import keyboards
from states import User
from bot import c, conn
import consts
import logging

@router.message(F.text == '/railes_control_erdb')
async def reloadb(message: types.Message, state: FSMContext):
  dboper.admin(conn, c)
