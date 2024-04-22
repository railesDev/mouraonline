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
  if not " @" in message.text or len(str(message.text)[4:]) < 4:
    await message.answer('Введи "/q @свойюзернейм"')
  else:
    await state.set_state(Interactive.id)
    question = dboper.get_question(conn, c, message.from_user.id, str(message.text)[3:])
    await message.answer('Вот твой вопрос: '+question+'Отвечай нормально, пожалуйста')
  

@router.message(
    Interactive.id,
    F.text.len() > 10
)
async def save_answer(message: types.Message, state: FSMContext):
  dboper.update_answer(conn, c, message.from_user.id, message.text)
  await message.answer('Ждем, когда другой ответит на тот же вопрос!')
  await state.clear()
  while True:
    resp = dboper.search_pair(conn, c, message.from_user.id)
    if resp is not None:
      username, ans = resp
      await message.answer(username+' '+ans)
      break
    else:
      await asyncio.sleep(200)
      


@router.message(
    Interactive.id,
    F.text.len() <= 10
)
async def try_again(message: types.Message, state: FSMContext):
  await message.answer('Твой ответ слишком короткий, попробуй еще раз!')


# executed in the end. real end.
@router.message(F.text.startswith('/railes_check_outsider'))
async def outsider(message: types.Message, state: FSMContext):
  outsider_id = dboper.check_outsider(conn, c)
  if outsider_id is not None:
    await moura.send_message(chat_id=outsider_id, text="В интерактиве поучаствовало нечетное количество человек, поэтому пары для тебя не нашлось. Хотя погоди, нет!\nТвой контакт на сегодня - мой! - @railesv)\nМожем покушать и поговорить за жизнь)")


@router.message(F.text.startswith('/railes_restart_interactive'))
async def restart(message: types.Message, state: FSMContext):
  dboper.reset_interactive(conn, c)
  dboper.fill_questions_table(conn, c, 'questions.txt')
  await moura.send_message(chat_id=6319974658, text="Successfully restarted interactive. Ask users to /start")
