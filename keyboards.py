from bot import types, InlineKeyboardBuilder
import consts


kb_gender = [
        [types.KeyboardButton(text=consts.gender_options[0])],
        [types.KeyboardButton(text=consts.gender_options[1])],
        [types.KeyboardButton(text=consts.start_over)],
    ]
keyboard_gender = types.ReplyKeyboardMarkup(keyboard=kb_gender,
                                            resize_keyboard=True,
                                            input_field_placeholder=consts.gender_placeholder
                                            )

kb_campus = [
        [types.KeyboardButton(text=consts.campus_options[0])],
        [types.KeyboardButton(text=consts.campus_options[1])],
        [types.KeyboardButton(text=consts.campus_options[2])],
        [types.KeyboardButton(text=consts.campus_options[3])],
        [types.KeyboardButton(text=consts.start_over)],
    ]
keyboard_campus = types.ReplyKeyboardMarkup(keyboard=kb_campus,
                                            resize_keyboard=True,
                                            input_field_placeholder=consts.campus_placeholder
                                            )

kb_kanta = [
            [types.KeyboardButton(text=consts.program_options[0])],
            [types.KeyboardButton(text=consts.program_options[1])],
            [types.KeyboardButton(text=consts.program_options[2])],
            [types.KeyboardButton(text=consts.program_options[3])],
            [types.KeyboardButton(text=consts.program_options[4])],
            [types.KeyboardButton(text=consts.program_options[5])],
            [types.KeyboardButton(text=consts.program_options[6])],
            [types.KeyboardButton(text=consts.program_options[7])],
            [types.KeyboardButton(text=consts.start_over)],
        ]

kb_griba = [
            [types.KeyboardButton(text=consts.program_options[8])],
            [types.KeyboardButton(text=consts.program_options[9])],
            [types.KeyboardButton(text=consts.program_options[10])],
            [types.KeyboardButton(text=consts.program_options[11])],
            [types.KeyboardButton(text=consts.program_options[12])],
            [types.KeyboardButton(text=consts.start_over)],
        ]

kb_proma = [
            [types.KeyboardButton(text=consts.program_options[13])],
            [types.KeyboardButton(text=consts.program_options[14])],
            [types.KeyboardButton(text=consts.start_over)],
        ]


def keyboard_programs(campus):
    return types.ReplyKeyboardMarkup(keyboard=(kb_kanta if campus == consts.campus_options[0]
                                               else (kb_griba if campus == consts.campus_options[1]
                                                     else (kb_proma if campus == consts.campus_options[2]
                                                           else None))),
                                     resize_keyboard=True,
                                     input_field_placeholder=consts.program_placeholder)


course_kb = [
        [types.KeyboardButton(text=consts.course_options[0])],
        [types.KeyboardButton(text=consts.course_options[1])],
        [types.KeyboardButton(text=consts.course_options[2])],
        [types.KeyboardButton(text=consts.course_options[3])],
        [types.KeyboardButton(text=consts.start_over)],
    ]

five_course_kb = [
        [types.KeyboardButton(text=consts.course_options[0])],
        [types.KeyboardButton(text=consts.course_options[1])],
        [types.KeyboardButton(text=consts.course_options[2])],
        [types.KeyboardButton(text=consts.course_options[3])],
        [types.KeyboardButton(text=consts.course_options[4])],
        [types.KeyboardButton(text=consts.start_over)],
    ]

def course_keyboard(program):
    return types.ReplyKeyboardMarkup(keyboard=(five_course_kb
                                               if program in [consts.program_options[7],
                                                              consts.program_options[8],
                                                              consts.program_options[12]]
                                               else course_kb),
                                     resize_keyboard=True,
                                     input_field_placeholder=consts.course_placeholder)


def goals_keyboard():
    goals_builder = InlineKeyboardBuilder()
    for goal in consts.goals:
        goals_builder.add(types.InlineKeyboardButton(text=goal, callback_data=goal))
    goals_builder.add(types.InlineKeyboardButton(text=consts.save_goals, callback_data='save'))
    goals_builder.adjust(1, 2, 1, repeat=True)
    return goals_builder


gendergoals_kb = [
        [types.KeyboardButton(text=consts.gender_goals_options[0])],
        [types.KeyboardButton(text=consts.gender_goals_options[1])],
        [types.KeyboardButton(text=consts.gender_goals_options[2])],
        [types.KeyboardButton(text=consts.start_over)],
    ]

gendergoals_keyboard = types.ReplyKeyboardMarkup(keyboard=gendergoals_kb,
                                                 resize_keyboard=True,
                                                 input_field_placeholder=consts.gender_goals_placeholder
                                                 )

photo_kb = [
        [types.KeyboardButton(text=consts.no_photo)],
        [types.KeyboardButton(text=consts.start_over)],
    ]

photo_keyboard = types.ReplyKeyboardMarkup(keyboard=photo_kb,
                                           resize_keyboard=True,
                                           input_field_placeholder=consts.photo_id_placeholder
                                           )

ad_text_keyboard = types.ForceReply(input_field_placeholder=consts.ad_text_placeholder)


last_kb = [
        [types.KeyboardButton(text=consts.publish_ad)],
        [types.KeyboardButton(text=consts.start_over)],
    ]

last_keyboard = types.ReplyKeyboardMarkup(keyboard=last_kb,
                                          resize_keyboard=True,
                                          input_field_placeholder=consts.publish_placeholder
                                          )

awaiting_kb = [
        [types.KeyboardButton(text=consts.show_ad)],
        [types.KeyboardButton(text=consts.setup)],
    ]

awaiting_keyboard = types.ReplyKeyboardMarkup(keyboard=awaiting_kb,
                                              resize_keyboard=True,
                                              input_field_placeholder=consts.publish_placeholder
                                              )

settings_kb = [
        [types.KeyboardButton(text=consts.change_ad)],
        [types.KeyboardButton(text=consts.backto_ads)],
        [types.KeyboardButton(text=consts.likes)],
        [types.KeyboardButton(text=consts.deactivate_profile)],
    ]


settings_keyboard = types.ReplyKeyboardMarkup(keyboard=settings_kb,
                                              resize_keyboard=True,
                                              input_field_placeholder=consts.setup_placeholder
                                              )


leaving_sure_kb = [
        [types.KeyboardButton(text=consts.deactivate_sure)],
        [types.KeyboardButton(text=consts.deactivate_no)],
    ]

leaving_sure_keyboard = types.ReplyKeyboardMarkup(keyboard=leaving_sure_kb,
                                              resize_keyboard=True,
                                              input_field_placeholder=consts.deactivate_profile_placeholder
                                              )

return_kb = [
        [types.KeyboardButton(text=consts.reactivate_profile)],
    ]

return_keyboard = types.ReplyKeyboardMarkup(keyboard=return_kb,
                                            resize_keyboard=True,
                                            input_field_placeholder=consts.reactivate_profile_placeholder
                                            )


tinder_kb = [
    [types.KeyboardButton(text=consts.actions[1]),
     types.KeyboardButton(text=consts.actions[2])],
    [types.KeyboardButton(text=consts.actions[0])],
    ]

tinder_keyboard = types.ReplyKeyboardMarkup(keyboard=tinder_kb,
                                            resize_keyboard=True,
                                            input_field_placeholder=consts.actions_placeholder
                                            )

see_likes_kb = [
    [types.KeyboardButton(text=consts.likes)],
    [types.KeyboardButton(text=consts.setup)],
    ]

see_likes_keyboard = types.ReplyKeyboardMarkup(keyboard=see_likes_kb,
                                               resize_keyboard=True,
                                               input_field_placeholder=consts.got_like_placeholder
                                               )


likes_kb = [
    [types.KeyboardButton(text=consts.like_actions[1]),
     types.KeyboardButton(text=consts.like_actions[2])],
    [types.KeyboardButton(text=consts.like_actions[0])],
    [types.KeyboardButton(text=consts.pause_likes)],
    ]

likes_keyboard = types.ReplyKeyboardMarkup(keyboard=likes_kb,
                                           resize_keyboard=True,
                                           input_field_placeholder=consts.actions_placeholder
                                           )
