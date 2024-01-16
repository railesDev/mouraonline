from bot import moura, router, F, types, FSMContext
import keyboards
from states import User
from bot import c, conn
import consts
import logging
import dboper

@router.message(F.text == '/railes_control_erdb')
async def reloadb(message: types.Message, state: FSMContext):
  dboper.admin(conn, c)


@router.message(F.text.startswith('/railes_control_msg'))
async def sendmsg(message: types.Message, state: FSMContext):
  mouraid, msg = message.text.split('/ ')[1:]
  ch_id = int(mouraid[:4]+mouraid[7:9]+mouraid[10:])
  await moura.send_message(chat_id=ch_id,
                           text=msg)
