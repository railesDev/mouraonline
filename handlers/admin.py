from bot import moura, router, F, types, FSMContext
import keyboards
from states import User
from bot import c, conn
import consts
import logging
import dboper
import asyncio
import time

@router.message(F.text.startswith('/railes_restart_interactive'))
async def restart(message: types.Message, state: FSMContext):
  dboper.reset_interactive(conn, c)
  dboper.fill_questions_table(conn, c, 'questions.txt')
  await moura.send_message(chat_id=6319974658, text="Successfully restarted interactive. Ask users to /start")

@router.message(F.text.startswith('/railes_control_msgall'))
async def spam(message: types.Message, state: FSMContext):
  text = consts.channel_ad
  ids = dboper.get_all_ids(conn, c)
  await moura.send_photo(chat_id=6319974658,
                         photo=consts.moura_channel_photo_id,
                         caption=text)
  for id in ids:
    try:
      await moura.send_photo(chat_id=id,
                           photo=consts.moura_channel_photo_id,
                           caption=text)
      logging.info(f'Successfully sent a message to {id}')
      time.sleep(70)
    except Exception as e:
      await moura.send_message(chat_id=6319974658, text=f'Error occured while spamming.{str(e)}')
    


@router.message(F.text.startswith('/valentine') | F.content_type.in_({'photo'}))
async def send_valentine(message: types.Message, state: FSMContext):
  ph = ''
  try:
    if not message.caption.startswith("/valentine"):
      return
    if len(message.caption[10:]) < 6:
      await message.answer(consts.short_valentine)
      return
    ph = message.photo[-1].file_id
    valentine = message.caption[10:]
  except Exception:
    if len(message.text[10:]) < 6:
      await message.answer(consts.short_valentine)
      return
    valentine = message.text[10:]
  await message.answer(consts.valentine_sent)
  if not ph:
    await moura.send_message(chat_id=6319974658, text=valentine)
  elif ph:
    await moura.send_photo(chat_id=6319974658, photo=ph, caption=valentine)
    


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

@router.message(F.text.startswith('/railes_control_eraseme'))
async def removeuser(message: types.Message, state: FSMContext):
  dboper.erase_user(conn, c, message.from_user.id)


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
