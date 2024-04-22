from bot import State, StatesGroup


class User(StatesGroup):
    id = State()
    # access = State()
    gender = State()
    campus = State()
    program = State()
    course = State()
    goals = State()
    gender_goals = State()
    photo_id = State()
    ad_text = State()
    finished = State()
    awaiting = State()
    action = State()
    matched = State()

class Interactive(StatesGroup):
    id = State()
    pairing = State()
