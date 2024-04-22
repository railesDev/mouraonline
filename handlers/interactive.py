from bot import moura, router, dp, F, types, FSMContext, ReplyKeyboardRemove, ParseMode
from bot import c, conn
from states import Interactive
import dboper
import consts
import keyboards
import logging
import asyncio
import random
from inact import InactivityChecker

@router.message(F.text.startswith('/q'))
async def give_question(message: Message, state: FSMContext):
  state.set_state(Interactive.id)
  
  
