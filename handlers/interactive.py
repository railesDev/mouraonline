from bot import moura, router, dp, F, types, FSMContext, ReplyKeyboardRemove, ParseMode
from bot import c, conn
from states import Interactive
import dboper
import consts
import keyboards
import logging
import asyncio
import random

@router.message(F.text.startswith('/q'))
async def give_question(message: types.Message, state: FSMContext):
  if dboper.is_cheater(conn, c, message.from_user.id):
    await message.answer(consts.inter_cheater, reply_markup=ReplyKeyboardRemove())
    return
  if not " @" in message.text or len(str(message.text)[4:]) < 4:
    await message.answer(consts.inter_hint, reply_markup=ReplyKeyboardRemove())
  else:
    await state.set_state(Interactive.id)
    question = dboper.get_question(conn, c, message.from_user.id, str(message.text)[3:])
    await message.answer_photo(consts.inter_intro, consts.inter_question+question+consts.inter_question_, reply_markup=ReplyKeyboardRemove())
  

@router.message(
    Interactive.id,
    F.text.len() > 10,
    ~(F.text.startswith('/q'))
)
async def save_answer(message: types.Message, state: FSMContext):
  dboper.update_answer(conn, c, message.from_user.id, message.text)
  await message.answer(consts.inter_waiting)
  await state.clear()
  while True:
    resp = dboper.search_pair(conn, c, message.from_user.id)
    if resp is not None:
      username, ans = resp
      await message.answer_photo(consts.inter_ending, consts.inter_finish+username+consts.inter_finish_+ans+consts.inter_final)
      break
    else:
      await asyncio.sleep(30)
      


@router.message(
    Interactive.id,
    F.text.len() <= 10
)
async def try_again(message: types.Message, state: FSMContext):
  await message.answer(consts.inter_short)


# executed in the end. real end.
@router.message(F.text.startswith('/railes_check_outsider'))
async def outsider(message: types.Message, state: FSMContext):
  outsider_id = dboper.check_outsider(conn, c)
  if outsider_id is not None:
    await moura.send_message(chat_id=outsider_id, text=consts.inter_exclusive)

