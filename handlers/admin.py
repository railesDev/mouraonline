from bot import moura, router, F, types, FSMContext
import keyboards
from states import User
from bot import c, conn
import consts
import logging
import dboper


@router.message(F.text.startswith('/valentine'))
async def ban_oper(message: types.Message, state: FSMContext):
  valentine = message.text[10:]
  photo = ''
  try:
    photo = message.photo[-1].file_id
  except Exception:
    pass
  if not photo:
    await moura.send_message(chat_id=6319974658, text=valentine)
    await message.answer(consts.valentine_sent)
  else:
    


@router.message(F.text.startswith('/railes_control_blacklist'))
async def ban_oper(message: types.Message, state: FSMContext):
  mouraid, tag = message.text.split('/ ')[1:]
  ch_id = int(mouraid[:4]+mouraid[7:9]+mouraid[10:])
  if tag == '-b':
    msg = consts.got_banned
    dboper.blacklist_user(conn, c, ch_id)
  elif tag == '-u':
    msg = consts.got_unbanned
    dboper.unblacklist_user(conn, c, ch_id)
  await moura.send_message(chat_id=ch_id,
                           text=msg)


@router.message(F.text == '/railes_control_erdb')
async def reloadb(message: types.Message, state: FSMContext):
  dboper.admin(conn, c)
  await state.clear()


@router.message(F.text.startswith('/railes_control_msg'))
async def sendmsg(message: types.Message, state: FSMContext):
  mouraid, msg = message.text.split('/ ')[1:]
  ch_id = int(mouraid[:4]+mouraid[7:9]+mouraid[10:])
  await moura.send_message(chat_id=ch_id,
                           text=msg)


@router.message(F.text == '/railes_control_displ')
async def displ(message: types.Message, state: FSMContext):
  rows = dboper.admin_displ_re(conn, c)
  for row in rows:
    await moura.send_message(chat_id=message.from_user.id, text=', '.join(list(map(str, row))))
  rows = dboper.admin_displ_users(conn, c)
  for row in rows:
    await moura.send_message(chat_id=message.from_user.id, text=', '.join(list(map(str, row))))
  rows = dboper.admin_displ_blacklist(conn, c)
  for row in rows:
    await moura.send_message(chat_id=message.from_user.id, text=', '.join(list(map(str, row))))
