female_anon_photo_id = 'AgACAgIAAxkBAAIGJmVNcnV831dIx07HTQQayc5tk8bnAAI01DEb0oFxSvQ-2w8nblOoAQADAgADeQADMwQ'
male_anon_photo_id = 'AgACAgIAAxkBAAIQxGVQA6sCMjjYnNgsUaCdusBZB4xyAAITzjEb7JSASjy2e7xU6PkMAQADAgADeQADMwQ'

inactivity_caption = ["Are you there? Many people in Moura are awaiting for you!",
                      "Let's get back to the world of Moura!",
                      "Do you still want to match with someone?",
                      "I am ready to show you many people from your university! "
                      "If you don't want to respond, just deactivate the profile"]

start_over = 'Start over 🔄'

publish_ad = 'Publish 🏹!'
publish_placeholder = 'Ready to go?'

no_photo = 'No photo ❌'
show_ad = '🔮Show me an ad!🔮'
save_goals = 'Save💾'
deactivate_profile = 'Deactivate Moura 😴'
deactivate_sure = 'Yes, I am sure ☠️'
deactivate_no = 'No, it is a mistake!'
deactivate_profile_caption = "Are you sure you want to leave us?"
deactivate_profile_placeholder = "Maybe no?)"
deactivate_sure_caption = ("Sorry to seeing you go😞\nYour ad and data have been deleted from us!\n"
                              "But you can always get back by typing /start or clicking on a button👇!")

reactivate_profile = '🔮Return to Moura!🔮'
reactivate_profile_placeholder = "Return?"
reactivate_caption = "Let's start from scratch!🔄"


intro_photo = 'https://cutt.ly/jwOeCQYf'
# 'https://cutt.ly/LwYgpImT'
intro_caption = ("<b>Hey!👋 Announcements channel: @mourahse</b>\n\nWe care about HSE students' security and privacy, so bot is inactive until you enter the access code:\n"
                 "<i>*hint: you can find it in the posters and ads</i>")

restart_caption = "Okay, let's restart filling your profile!🔮"
start_caption = ("🧞Our digital minds say that you have been in Moura recently.\nHappy to see you going back!\n"
                 "We deleted your data from us and you shall start over!🔮")


access_code = "HSEMR"


gender_photo = 'https://cutt.ly/cwTbybUB'
gender_caption = 'Welcome to the world of Moura!🫰\n\n<b>STEP 1/8📝</b>\nTell us about yourself:'
gender_options = ['I am a Guy ‍👨‍💼', 'I am a Lady ‍👩‍💼']
gender_placeholder = 'Your gender?'


campus_photo = 'https://cutt.ly/3wYopqmz'
campus_alias = lambda gender: 'bro' if gender == 'I am a Guy ‍👨‍💼' else 'lady'
campus_placeholder = 'Choose a campus'


def campus_caption(gender):
    return (f'Okay, {campus_alias(gender)}!\n\n<b>STEP 2/8📝</b>\nThen we determine your HSE campus. '
            f'Choose one of yours below:👇')


campus_options = ['Kantemirovskaya 🏭', 'Griboedova 🏨', 'Promyshlennaya 🏫', 'Sedova 🏠']
kanta_photo = 'https://cutt.ly/awYogHta'
griba_photo = 'https://cutt.ly/MwYogMg4'
proma_photo = 'https://cutt.ly/CwYog9ZH'
sedova_photo = 'https://cutt.ly/0wYog5yQ'


def campus_reaction_photo(campus):
    return kanta_photo if campus == 'Kantemirovskaya 🏭'\
        else (griba_photo if campus == 'Griboedova 🏨'
              else (proma_photo if campus == 'Promyshlennaya 🏫'
                    else (sedova_photo if campus == 'Sedova 🏠'
                          else None)))


campus_reaction_caption = 'Each building of HSE is unique🫶\nWe in Moura admire all the campuses and their students!'

program_options = ['Logistics 🚚', 'InterBusiness 💼', 'Economics 📈', 'InterBac 🤹‍', 'PMI 💻', 'Data Analytics 📊',
                   'Physics 🌌', 'Law ⚖️', 'History 📜', 'Mediacommunications 📱', 'Philology 📚', 'Politology 🏛️',
                   'Vostokovedenie ⛩️', 'Design 🎨', 'UAGS 🏢']
program_photo = 'https://cutt.ly/owYoxOJt'
program_caption = '<b>STEP 3/8📝</b>\nWhich program do you study at?👀'
program_placeholder = 'Choose a program'

course_options = ['1 👶', '2 🧒', '3 🧔', '4 👴', '5 😎']
course_photo = 'https://cutt.ly/bwYoxLwG'
course_placeholder = 'Choose course #'


def course_caption(message):
    return (f'So, you study <b>{message if message != "Sedova 🏠" else "Sociology 👥, so skipping the 3rd step"}!</b>\n'
            f'\n<b>STEP 4/8📝</b>\nWhat is your course?')


goals = ['Dates 👫', 'Networking 🤝', 'Friendship 🤙']
goals_photo = 'https://cutt.ly/SwOn6OND'
# 'https://cutt.ly/HwYox0Yv'
basic_done_caption = "So, we are done with your basic information!\n<b>Let's go for a next step!😎</b>"
goals_caption = ("<b>STEP 5/8📝</b>\nWhat are your boundaries and goals?\n\nAre you into dates, "
                 "networking (co-projects) or just friendship?")
no_goals_caption = ("<b>Choose any goal first!</b>\n\n<b>STEP 5/8📝</b>\nWhat are your boundaries and goals?\n"
                    "Your choice will affect which people you will see")


def goals_chosen_caption(chosen_goals):
    return ("<b>STEP 5/8📝</b>\nYour chosen goals:\n<b>" + ', '.join(chosen_goals) +
            "</b>\n\nThey will affect which people you will see\n<b>Don't forget to click Save💾!</b>\n\n" +
            "<i>*to cancel selection, click on a button again</i>")


def goals_saved_caption(chosen_goals):
    return ("<b>STEP 5/8📝</b>\nYour goals have been saved!\n\n<b>" +
            ', '.join(chosen_goals) + "</b>\n\nThis will help Moura to find more suitable people for you!")


gender_goals_photo = 'https://cutt.ly/NwYocqmG'
gender_goals_caption = "<b>STEP 6/8📝</b>\nWhat about your gender preferences? Who should Moura show you?"
gender_goals_options = ['Ladies ‍👩', 'Guys 👨', 'Both 🤷']
gender_goals_placeholder = 'Choose preferences'

photo_id_photo = 'https://cutt.ly/BwYocaLZ'
photo_id_caption = ("<b>STEP 7/8📝</b>\nNow, if you wish, you can attach a photo to your ad! "
                    "It will increase your chance to match!\nOr... refuse and stay anonymous🦹!")
photo_id_placeholder = 'Upload photo/refuse'

ad_text_photo = 'https://cutt.ly/LwYoclfw'
ad_text_caption = ('As we are done with photos,...\n\n<b>STEP 8/8📝</b>\nFinally, create a description!\n'
                   'This is the most important part in your ad.\n\n<b>Describe your desires or offer something</b>')
ad_text_placeholder = 'See it as your Twitter'


def finish_caption(ad):
    return f"<b>✅ WE ARE ALL DONE! Look at your ad:</b>\n\n{ad}\nIs everything correct? <b>If yes, click Publish!</b>"


published_ad_caption = f"<b>Your ad is published!🤩</b>\nNow let's start matching!"

no_ads_caption = "For now no more ads:(\nWait for it, I will send you a new one as soon as it appears!"

got_like_caption = "You have a new like!"
got_like = 'Look at my likes!💟'
got_like_placeholder = 'Wanna look?'

actions = ['Like 💟', 'Next ⏩️', 'Complain ‼️']
actions_placeholder = 'What do you think?'

like_actions = ['Match 💟', 'No 🚫', 'Complain ‼️']
no_likes_caption = "No more likes, wish to continue?"
like_caption = "Like was sent!"
dislike_caption = "Okay, next one!"

complain_caption = "Please forward this ad to @heliumwer, he will deal with this person!"
