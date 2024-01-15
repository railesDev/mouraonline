female_anon_photo_id = 'AgACAgIAAxkBAAIGJmVNcnV831dIx07HTQQayc5tk8bnAAI01DEb0oFxSvQ-2w8nblOoAQADAgADeQADMwQ'
male_anon_photo_id = 'AgACAgIAAxkBAAIQxGVQA6sCMjjYnNgsUaCdusBZB4xyAAITzjEb7JSASjy2e7xU6PkMAQADAgADeQADMwQ'

inactivity_caption = ["Хэй, ты тут?",
                      "Вернемся в мир Муры?",
                      "Еще хочешь с кем-то мэтчиться?",
                      "Йо, тут еще куча людей, с которыми стоит пообщаться!",
                      "Если не хочешь больше мэтчиться, заморозь профиль!"]

# for future:
no_ad_respond_caption = ["Хэй, ты тут? Отреагируешь на анкету, что я прислал?",
                      "Вернемся в мир Муры? Тут у тебя висит анкета)",
                      "Еще хочешь с кем-то мэтчиться?",
                      "Йо, тут человечек ждет твоей реакции!",
                      "Если не хочешь больше мэтчиться, заморозь профиль!"]


start_over = 'Начать заново 🔄'

publish_ad = 'Опубликовать 🏹!'
publish_placeholder = 'Погнали?'

no_photo = 'Без фото ❌'
show_ad = '🔮 Покажи новую анкету! 🔮'
save_goals = 'Сохранить💾'
deactivate_profile = 'Деактивировать Муру 😴'
deactivate_sure = 'Да, точно ☠️'
deactivate_no = 'Не, я случайно!'
deactivate_profile_caption = "Точно хочешь нас покинуть?"
deactivate_profile_placeholder = "Может, нет?)"
deactivate_sure_caption = ("Грустно, что ты нас покидаешь😞\nТвоя анкета и данные были удалены с наших серверов!\n"
                              "Но ты всегда можешь вернуться, нажав /start или на кнопку ниже👇!")

reactivate_profile = '🔮 Вернуться в Муру! 🔮'
reactivate_profile_placeholder = "Возвращаемся?"
reactivate_caption = "Давай начнем с чистого листа!🔄"


intro_photo = 'https://cutt.ly/jwOeCQYf'
# 'https://cutt.ly/LwYgpImT'
intro_caption = ("<b>Привет!👋 Канал для анонсов: @mourahse</b>\nНе забудь подписаться, чтобы ничего не пропустить!\n\nМы заботимся о безопасности и приватности студентов вышки, поэтому Мура не будет работать, пока ты не введешь код доступа!\n\n<b>Введи его в ответ:</b>\n\n"
                 "<i>*подсказка: ты можешь найти его на постерах</i>")

restart_caption = "Окей, давай заполним твой профиль заново!🔮"
start_caption = "🧞Наша коллегия цифровых старейшин говорит, что у тебя уже был профиль в Муре.\nВся твоя информация сохранена, смотри, какая анкета у тебя была до этого:"

return_start_caption = "Твой профиль был деактивирован, так что время начать с чистого листа!🔮"


access_code = "HSEMR"


gender_photo = 'https://cutt.ly/cwTbybUB'
gender_caption = 'Добро пожаловать в мир Муры!🫰\n\n<b>ШАГ 1/8📝</b>\nРасскажи о себе:'
gender_options = ['Я парень ‍👨‍💼', 'Я девушка ‍👩‍💼']
gender_placeholder = 'Твой пол?'


campus_photo = 'https://cutt.ly/3wYopqmz'
campus_alias = lambda gender: 'бро' if gender == 'Я парень ‍👨‍💼' else 'леди'
campus_placeholder = 'Выбери свой корпус'


def campus_caption(gender):
    return (f'Окей, {campus_alias(gender)}!\n\n<b>ШАГ 2/8📝</b>\nТеперь давай определим корпус, в который ты обычно ходишь на пары.'
            f'Выбери свой ниже:👇')


campus_options = ['Кантемировская 🏭', 'Грибоедова 🏨', 'Промышленная 🏫', 'Седова 🏠']
kanta_photo = 'https://cutt.ly/awYogHta'
griba_photo = 'https://cutt.ly/MwYogMg4'
proma_photo = 'https://cutt.ly/CwYog9ZH'
sedova_photo = 'https://cutt.ly/0wYog5yQ'


def campus_reaction_photo(campus):
    return kanta_photo if campus == 'Кантемировская 🏭'\
        else (griba_photo if campus == 'Грибоедова 🏨'
              else (proma_photo if campus == 'Промышленная 🏫'
                    else (sedova_photo if campus == 'Седова 🏠'
                          else None)))


campus_reaction_caption = 'Согласись, каждое здание вышки обладает своим уникальным и потрясающим вайбом?🫶'

program_options = ['Логистика 🚚', 'МежБиз 💼', 'Экономика 📈', 'МежБак 🤹‍', 'ПМИ 💻', 'Анализ данных 📊',
                   'Физика 🌌', 'Право ⚖️', 'История 📜', 'Медиаком 📱', 'Филология 📚', 'Политология 🏛️',
                   'Востоковедение ⛩️', 'Дизайн 🎨', 'УАГС 🏢']
program_photo = 'https://cutt.ly/owYoxOJt'
program_caption = '<b>ШАГ 3/8📝</b>\nНа какой программе учишься?👀'
program_placeholder = 'Выбери ОП'

course_options = ['1 👶', '2 🧒', '3 🧔', '4 👴', '5 😎']
course_photo = 'https://cutt.ly/bwYoxLwG'
course_placeholder = 'Выбери номер своего курса'


def course_caption(message):
    return (f'Что ж, ты учишься на программе <b>{message if message != "Седова 🏠" else "Социология 👥, так что пропускаем шаг номер 3!"}!</b>\n'
            f'\n<b>ШАГ 4/8📝</b>\nНа каком курсе учишься?')


goals = ['Допускаю дейты 👫', 'Нетворкинг 🤝', 'Дружба 🤙']
goals_photo = 'https://cutt.ly/SwOn6OND'
# 'https://cutt.ly/HwYox0Yv'
basic_done_caption = "Покончили с базовой информацией, теперь перейдем к следующему шагу!😎"
goals_caption = ("<b>ШАГ 5/8📝</b>\nКакие у тебя рамки и цели?\n\nТы допускаешь дейты, "
                 "ищешь возможности для нетворкинга или просто дружбу?")
no_goals_caption = ("<b>Сначала выбери хотя бы одну из целей!</b>\n\n<b>ШАГ 5/8📝</b>\nКакие у тебя рамки и цели?\n"
                    "Твой выбор повлияет на то, каких людей ты увидишь!")


def goals_chosen_caption(chosen_goals):
    return ("<b>ШАГ 5/8📝</b>\nТвои выбранные цели:\n<b>" + ', '.join(chosen_goals) +
            "</b>\n\nТвой выбор повлияет на то, каких людей ты увидишь!\n<b>Не забудь нажать на кнопку Сохранить💾!</b>\n\n" +
            "<i>*чтобы отменить выбор цели, нажми на нее еще раз)</i>")


def goals_saved_caption(chosen_goals):
    return ("<b>ШАГ 5/8📝</b>\nТвои предпочтения сохранены!\n\n<b>" +
            ', '.join(chosen_goals) + "</b>\n\nЭто поможет Муре найти более подходящих тебе людей!")


gender_goals_photo = 'https://cutt.ly/NwYocqmG'
gender_goals_caption = "<b>ШАГ 6/8📝</b>\nЧто по поводу твоих предпочтений? Кого Муре стоит тебе показывать?"
gender_goals_options = ['Девушки ‍👩', 'Парни 👨', 'Без разницы 🤷']
gender_goals_placeholder = 'Выбери предпочтения'

photo_id_photo = 'https://cutt.ly/BwYocaLZ'
photo_id_caption = ("<b>ШАГ 7/8📝</b>\nТеперь, если хочешь, можешь прикрепить фото к анкете! "
                    "Этот шаг увеличит твои шансы на мэтч!\nИли... откажись и оставайся в тени🦹!")
photo_id_placeholder = 'Пришли фото/откажись'

ad_text_photo = 'https://cutt.ly/LwYoclfw'
ad_text_caption = ('Вот мы и разобрались с фото,...\n\n<b>ШАГ 8/8📝</b>\nПоследнее действие - напиши описание!\n'
                   'Эта часть - самая важная.\n\n<b>Опиши, чего хочешь, расскажи о себе, предложи что-то</b>')
ad_text_placeholder = 'Это твой твиттер'

ad_short_caption = 'Слишком короткое описание, попробуй что-то другое!👇'

def finish_caption(ad):
    return f"<b>✅ МЫ СПРАВИЛИСЬ!\nВзгляни на свою анкету:</b>\n\n{ad}\nВсе верно? <b>Если да, кликай на Опубликовать!</b>"


published_ad_caption = f"<b>Твоя анкета опубликована!🤩</b>\nПришло время познакомиться с миром Moura!"

no_ads_caption = "Пока что не нашлось подходящих анкет:(\nПодожди немного, я сам отправлю тебе анкету, как только она появится!"

got_like_caption = "У тебя новый лайк!"
likes = 'Посмотреть мои лайки 💟'
got_like_placeholder = 'Хочешь посмотреть?'

setup = 'Настройки профиля⚙️'
setup_caption = '🪬<b>Ты в основном меню!\n\nТвоя анкета:</b>'
setup_placeholder = 'Выбери действие'
change_ad = 'Обновить анкету 🔄'
backto_ads = '🔮 К просмотру анкет 🔮'


actions = ['Жалоба ‼️', 'Дальше ⏩️', 'Лайк 💟']
actions_placeholder = 'Что думаешь?'

like_actions = ['Жалоба ‼️', 'Нет 🚫', 'Мэтч! 💟']
pause_likes = 'В основное меню 💣'
no_likes_caption = "Больше лайков нет, продолжим?"
like_caption = "Лайк отправлен!"
dislike_caption = "Окей, погнали дальше!"

complain_caption = "Пожалуйста, перешли сообщение с анкетой Рэю - @vwonders, он разберется!"

match_photo = 'https://cutt.ly/ewKuxbOs'
match_letter_caption = 'Поздравляю с мэтчем!🎉\n\nВремя ответного шага с твоей стороны: <b>оставь послание!</b>📨\n\n\n*подсказки смотри выше, изменить послание после отправкибудет уже нельзя!'
matched = '<b>📨Тебе пришло послание от нового мэтча, смотри:</b>'
letter_sent_caption = 'Твое послание успешно отправлено! 📨'
