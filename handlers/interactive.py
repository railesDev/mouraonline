import blablabla

@router.message(F.text.startswith('/q'))
async def give_question(message: Message, state: FSMContext):
  
