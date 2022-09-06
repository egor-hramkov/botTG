import telebot

bot = telebot.TeleBot("5607613808:AAEgyqwvJv6SCaoGl6pupeOnWd_F1Yo--Aw")

tests = ['Python', 'Java']

questions_for_python = [
    {'text': 'Имеется кортеж вида T = (4, 2, 3). Какая из операций приведёт к тому, что имя T будет ссылаться на кортеж (1, 2, 3)?', 'all_answers': ['T[0] = 1', 'T = (1) + T[1:]', 'T = (1,) + T[1:]', 'T.startswith(1)'], 'right_answer': 2},
    {'text': 'Для чего в Python используется встроенная функция enumerate()?', 'all_answers': ['Для определения количества элементов последовательности.', 'Для одновременного итерирования по самим элементам и их индексам.', 'Для сортировки элементов по значениям id.', 'ты мой краш'], 'right_answer': 1},
    {'text': 'Необходимо собрать и вывести все уникальные слова из строки рекламного текста. Какой из перечисленных типов данных Python подходит лучше всего?', 'all_answers': ['кортеж (tuple)', 'список (list)', 'множество (set)', 'словарь (dict)'], 'right_answer': 2},
    {'text': 'Как вывести список методов и атрибутов объекта x?', 'all_answers': ['help(x)', 'info(x)', '?x', 'dir(x)'], 'right_answer': 2},
    {'text': 'Как можно более кратко представить следующую запись?\nif X:\n\tA = Y\nelse:\n\tA = Z', 'all_answers': ['A = Y if Z else Y', 'A = Y if X else Z', 'A = X if Z else Y', 'A = X if Y else Z'], 'right_answer': 1},
    {'text': 'Какая из перечисленных инструкций выполнится быстрее всего, если n = 10**6?', 'all_answers': ['a = list(i for i in range(n))', 'a = [i for i in range(n)]', 'a = (i for i in range(n))', 'a = {i for i in range(n)}'], 'right_answer': 2},
    {'text': 'Что выведет на экран следующий код?\na, *b, c = [1, 2]\nprint(a, b, c)', 'all_answers': ['[1] [] [2]', '1 0 2', '1 [] 2', 'словарь (dict)'], 'right_answer': 2},
    {'text': 'С помощью Python нужно записать данные в файл, но только в том случае, если файла ещё нет. Какой режим указать в инструкции open()?', 'all_answers': ['"x"', '"w"', '"r"', 'Никакой. Нужна предварительная проверка os.path.exists()'], 'right_answer': 0},
    {'text': 'Для чего в пакетах модулей python в файле __init__.py служит список __all__?', 'all_answers': ['Для конструкторов классов, как и всё, что связано с __init__', 'Список определяет, что экспортировать, когда происходит импорт с помощью from *', 'Для перечисления переменных, которые будут скрыты для импортирования.'], 'right_answer': 1},
    {'text': 'При объявлении класса с помощью оператора class что пишется в круглых скобках после имени класса?', 'all_answers': ['Имена аргументов, принимаемых методом __init__.', 'Имена принимаемых классом аргументов.', 'Имена суперклассов, если класс наследуется от одного или нескольких классов.', 'Имена классов, порождаемых данным классом.'], 'right_answer': 2},
    {'text': 'Какую роль в описании метода класса выполняет декоратор @property?', 'all_answers': ['Декорированный метод становится статическим, экземпляр не передаётся.', 'Декорированный метод становится методом класса: метод получает класс, а не экземпляр.', 'Значение, возвращаемое декорированным методом, вычисляется при извлечении. Можно обратиться к методу экземпляра, как к атрибуту.'], 'right_answer': 2}
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
            bot.send_message(message.from_user.id, questions_for_python[0]['text'])
            str_answers = ''
            for i in range(1, 5):
                str_answers += str(i) + '. ' + questions_for_python[gen_iter]['all_answers'][i - 1] + '\n'
            bot.send_message(message.from_user.id, str_answers)

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
                             questions_for_python[gen_iter]['text'])
            str_answers = ''
            for i in range(1, 5):
                str_answers += str(i) + '. ' + questions_for_python[gen_iter]['all_answers'][i-1] + '\n'
            bot.send_message(message.from_user.id, str_answers)

    else:
        bot.send_message(message.from_user.id, 'Такого варианта ответа нет')


bot.polling(none_stop=True)
