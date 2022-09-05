import telebot

bot = telebot.TeleBot("5607613808:AAEgyqwvJv6SCaoGl6pupeOnWd_F1Yo--Aw")

tests = ['Python', 'Java']

questions_for_python = [
    {'text': 'Вопрос1?', 'all_answers': ['тест', 'тест2', 'тест3'], 'right_answer': 1},
    {'text': 'Вопрос2?', 'all_answers': ['Але', 'зачем'], 'right_answer': 1},
    {'text': 'Вопрос3?', 'all_answers': ['Але', 'зачем'], 'right_answer': 1}
]

right_answ = 0
percent_right_answ = 0
gen_iter = 0
is_started = False

@bot.message_handler(commands=['start'])
def start_chat(message):
    global is_started
    if is_started:
        bot.send_message(message.from_user.id, "Вы уже проходите тест, если хотите начать заново введите 'Начать тест заново'")
    else:
        bot.send_message(message.from_user.id, "Выберите тест для прохождения: \n" + '\n'.join(tests))


@bot.message_handler(func=lambda message: not message.from_user.is_bot)
def on_message(message):
    global gen_iter
    global right_answ
    global percent_right_answ
    global is_started
    if message.text == 'Начать тест заново':
        gen_iter = 0
        is_started = False
        bot.send_message(message.from_user.id, 'Начинаем тест заново')
        bot.send_message(message.from_user.id, "Выберите тест для прохождения: \n" + '\n'.join(tests))
    elif message.text == 'Python':
        if is_started:
            bot.send_message(message.from_user.id, "Вы уже проходите тест, если хотите начать заново введите 'Начать тест заново'")
        else:
            is_started = True
            bot.send_message(message.from_user.id, questions_for_python[0]['text'] + ':\n' + '\n'.join(questions_for_python[0]['all_answers']))
    elif message.text in questions_for_python[gen_iter]['all_answers']:
        if message.text == questions_for_python[gen_iter]['all_answers'][questions_for_python[gen_iter]['right_answer']]:
            right_answ += 1
            bot.send_message(message.from_user.id, "Правильно, переходим к следующему вопросу...")
        else:
            bot.send_message(message.from_user.id, "Неправильно, переходим к следующему вопросу...")
        if gen_iter == len(questions_for_python) - 1:
            percent_right_answ = format((right_answ/len(questions_for_python) * 100), '.2f')
            bot.send_message(message.from_user.id, f'Тест завершён!\n Вы ответили правильно на {right_answ} из {len(questions_for_python)} вопросов, это {percent_right_answ}% от всего теста.')
        else:
            gen_iter += 1
            bot.send_message(message.from_user.id,
                             questions_for_python[gen_iter]['text'] + ':\n' + '\n'.join(questions_for_python[gen_iter]['all_answers']))
    else:
        bot.send_message(message.from_user.id, 'Такого варианта ответа нет')


bot.polling(none_stop=True)
