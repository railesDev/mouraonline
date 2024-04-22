from bot import moura, router, dp, F, types, FSMContext, ReplyKeyboardRemove, ParseMode
from bot import c, conn
from states import Interactive
import dboper
import consts
import keyboards
import logging
import asyncio
import random

inter_hint = '👀 Опечатка в команде! Введи "/q @свойюзернейм"'
inter_short = '👀 Твой ответ слишком короткий, попробуй еще раз!'
inter_cheater = 'Извини, но вопрос можно получить только один😌'
inter_question = 'Привет! Спасибо за твой визит на Мура Ток! Давай посмотрим, какой вопрос тебе выпадет...:\n\n<b>'
inter_question_ = '</b>\n\nТвой ответ увидит человек, которому выпадет тот же вопрос🙌'
inter_waiting = 'Принято) Теперь давай подождем, когда твоя секретная пара тоже ответит!🧘‍♀️'
inter_finish = '🏄‍♀️ Прием! Вот юзернейм: '
inter_finish_ = '\n\nА вот ответ на вопрос:\n\n'
inter_exclusive = "В интерактиве поучаствовало нечетное количество человек, поэтому пары для тебя не нашлось...\n\nХотя постой, нет!\n\nТвой контакт на сегодня - мой! - @railesv)\nМожем покушать и поговорить за жизнь)"

@router.message(F.text.startswith('/q'))
async def give_question(message: types.Message, state: FSMContext):
  if dboper.is_cheater(conn, c, message.from_user.id):
    await message.answer(consts.inter_cheater)
    return
  if not " @" in message.text or len(str(message.text)[4:]) < 4:
    await message.answer(consts.inter_hint)
  else:
    await state.set_state(Interactive.id)
    question = dboper.get_question(conn, c, message.from_user.id, str(message.text)[3:])
    await message.answer(consts.inter_question+question+consts.inter_question_)
  

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
      await message.answer(consts.inter_finish+username+consts.inter_finish_+ans)
      break
    else:
      await asyncio.sleep(100)
      


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

