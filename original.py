import telebot
from telebot import types

bot = telebot.TeleBot("5607613808:AAEgyqwvJv6SCaoGl6pupeOnWd_F1Yo--Aw")

tests = ['Технологии программирования(Python)', 'Основы ООП']

questions_for_python = [
    {'text': 'Имеется кортеж вида T = (4, 2, 3). Какая из операций приведёт к тому, что имя T будет ссылаться на кортеж (1, 2, 3)?', 'all_answers': ['T[0] = 1', 'T = (1) + T[1:]', 'T = (1,) + T[1:]', 'T.startswith(1)'], 'right_answer': 2},
    {'text': 'Для чего в Python используется встроенная функция enumerate()?', 'all_answers': ['Для определения количества элементов последовательности.', 'Для одновременного итерирования по самим элементам и их индексам.', 'Для сортировки элементов по значениям id.', 'Чтобы узнать длину объекта.'], 'right_answer': 1},
    {'text': 'Необходимо собрать и вывести все уникальные слова из строки рекламного текста. Какой из перечисленных типов данных Python подходит лучше всего?', 'all_answers': ['кортеж (tuple)', 'список (list)', 'множество (set)', 'словарь (dict)'], 'right_answer': 2},
    {'text': 'Как вывести список методов и атрибутов объекта x?', 'all_answers': ['help(x)', 'info(x)', '?x', 'dir(x)'], 'right_answer': 2},
    {'text': 'Как можно более кратко представить следующую запись?\nif X:\n\tA = Y\nelse:\n\tA = Z', 'all_answers': ['A = Y if Z else Y', 'A = Y if X else Z', 'A = X if Z else Y', 'A = X if Y else Z'], 'right_answer': 1},
    {'text': 'Какая из перечисленных инструкций выполнится быстрее всего, если n = 10**6?', 'all_answers': ['a = list(i for i in range(n))', 'a = [i for i in range(n)]', 'a = (i for i in range(n))', 'a = {i for i in range(n)}'], 'right_answer': 2},
    {'text': 'Что выведет на экран следующий код?\na, *b, c = [1, 2]\nprint(a, b, c)', 'all_answers': ['[1] [] [2]', '1 0 2', '1 [] 2', 'словарь (dict)'], 'right_answer': 2},
    {'text': 'С помощью Python нужно записать данные в файл, но только в том случае, если файла ещё нет. Какой режим указать в инструкции open()?', 'all_answers': ['"x"', '"w"', '"r"', 'Никакой. Нужна предварительная проверка os.path.exists()'], 'right_answer': 0},
    {'text': 'Для чего в пакетах модулей python в файле __init__.py служит список __all__?', 'all_answers': ['Для конструкторов классов, как и всё, что связано с __init__', 'Список определяет, что экспортировать, когда происходит импорт с помощью from *', 'Для перечисления переменных, которые будут скрыты для импортирования.', 'Для удобного хранения всех переменных'], 'right_answer': 1},
    {'text': 'При объявлении класса с помощью оператора class что пишется в круглых скобках после имени класса?', 'all_answers': ['Имена аргументов, принимаемых методом __init__.', 'Имена принимаемых классом аргументов.', 'Имена суперклассов, если класс наследуется от одного или нескольких классов.', 'Имена классов, порождаемых данным классом.'], 'right_answer': 2},
    {'text': 'Какую роль в описании метода класса выполняет декоратор @property?', 'all_answers': ['Декорированный метод становится статическим, экземпляр не передаётся.', 'Декорированный метод становится методом класса: метод получает класс, а не экземпляр.', 'Значение, возвращаемое декорированным методом, вычисляется при извлечении. Можно обратиться к методу экземпляра, как к атрибуту.', 'Значение, возвращаемое декорированным методом, подлежит дополнительной проверке'], 'right_answer': 2}
]

questions_for_OOP = [
    {'text': 'Что такое класс в Java?', 'all_answers': ['Уровень сложности программы. Все операторы делятся на классы в зависимости от сложности их использования.', 'Базовый элемент объектно-ориентирован­ного программирования в языке Java.', 'Просто одно из возможных названий переменной.', 'Такое понятие есть только в C++, в Java такого понятия нет.'], 'right_answer': 1},
    {'text': 'Как объявить класс в коде?', 'all_answers': ['class MyClass {}', 'new class MyClass {}', 'select * from class MyClass {}', 'MyClass extends class {}'], 'right_answer': 0},
    {'text': 'Для чего используется оператор NEW?', 'all_answers': ['Для создания новой переменной.', 'Для объявления нового класса.', 'Для создания экземпляра класса.', 'Это антагонист оператора OLD.'], 'right_answer': 2},
    {'text': 'Что означает ключевое слово extends?', 'all_answers': ['Что данный класс наследуется от другого.', 'Что это дополнительный модуль класса, который расширяет его свойства.', 'Что два класса делают одно и то же.', 'Что это самый большой класс в программе.'], 'right_answer': 0},
    {'text': 'Что означает перегрузка метода в Java (overload).', 'all_answers': ['Изменение поведения метода класса относительно родительского.', 'Изменение поведения метода класса относительно дочернего.', 'Несколько методов с одинаковым названием, но разным набором параметров.', 'Несколько разных классов с одинаковым методом.'], 'right_answer': 2},
    {'text': 'Что означает переопределение метода в Java (override).', 'all_answers': ['Изменение поведения метода класса относительно родительского.', 'Изменение поведения метода класса относительно дочернего.', 'Несколько методов с одинаковым названием, но разным набором параметров.', 'Несколько разных классов с одинаковым методом.'], 'right_answer': 0},
    {'text': 'Чем отличаются static-метод класса от обычного метода класса.', 'all_answers': ['Поведение обычного метода класса можно изменить в классе-наследнике, а поведение static-метода нельзя.', 'Обычный метод класса можно переопределить, а static-метод нельзя.', 'Обычный метод класса работает от объекта класса, а static-метод от всего класса.', 'Static-метод класса можно вызывать только внутри класса, а обычный - в любой части кода.'], 'right_answer': 2},
    {'text': 'Как вызвать static-метод внутри обычного?', 'all_answers': ['Никак, static-метод можно вызвать только от объекта класса.', 'Можно, надо перед этим перегрузить обычный метод класса.', 'Можно, надо перед этим переопределить обычный метод класса.', 'Можно, ничего дополнительно делать не надо.'], 'right_answer': 3},
    {'text': 'Как вызвать обычный метод класса внутри static-метода?', 'all_answers': ['Никак, static-метод не работает с объектом класса.', 'Можно, надо перед этим перегрузить обычный метод класса.', 'Можно, надо перед этим переопределить обычный метод класса.', 'Можно, ничего дополнительно делать не надо.'], 'right_answer': 0},
    {'text': 'Для чего необходимо ключевое слово this', 'all_answers': ['Это указатель на переопределенный метод класса. Его нельзя опускать при вызове, иначе переопределение не сработает.', 'Это указатель на текущий объект класса внутри самого класса. Его можно опускать при вызове метода класса, но лучше этого не делать.', 'Это не ключевое слово.', 'Это ключевое слово для вызова обычного метода внутри static-метода. Его нельзя опускать, иначе вызов не сработает и будет ошибка.'], 'right_answer': 1},
    {'text': 'Что вернет метод, объявленный следующим образом:\npublic static int getAmount()', 'all_answers': ['Не ясно, надо смотреть код метода.', 'Вернет static-поле класса.', 'Вернет ссылку на объект класса this.', 'Вернет целочисленное значение.'], 'right_answer': 3}
]

questions_test = [
    {'text': 'Имеется кортеж вида T = (4, 2, 3). Какая из операций приведёт к тому, что имя T будет ссылаться на кортеж (1, 2, 3)?', 'all_answers': ['T[0] = 1', 'T = (1) + T[1:]', 'T = (1,) + T[1:]', 'T.startswith(1)'], 'right_answer': 2}
]

right_answ = 0
percent_right_answ = 0
gen_iter = 0
is_started = False

@bot.message_handler(commands=['start'])
def start_chat(message):
    global is_started
    if is_started:
        bot.send_message(message.from_user.id, "Вы уже проходите тест, если хотите начать заново выберите 'Начать тест заново'")
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Технологии программирования(Python)")
        item2 = types.KeyboardButton("Основы ООП")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Выберите тест для прохождения:', reply_markup=markup)



@bot.message_handler(func=lambda message: not message.from_user.is_bot)
def on_message(message):
    global gen_iter
    global right_answ
    global percent_right_answ
    global is_started
    global questions_test
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1")
    item2 = types.KeyboardButton("2")
    item3 = types.KeyboardButton("3")
    item4 = types.KeyboardButton("4")
    item5 = types.KeyboardButton("Начать тест заново")
    items = [item1, item2, item3, item4]
    #Проверка на динамику кнопок
    if questions_test:
        for i in range(len(questions_test[gen_iter]['all_answers'])):
            markup.add(items[i])
    else:
        for i in range(4):
            markup.add(items[i])
    markup.add(item5)
    if message.text == 'Начать тест заново':
        questions_test = []
        gen_iter = 0
        is_started = False
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item11 = types.KeyboardButton("Технологии программирования(Python)")
        item12 = types.KeyboardButton("Основы ООП")
        markup1.add(item11, item12)
        bot.send_message(message.chat.id, 'Выберите тест для прохождения:', reply_markup=markup1)
    elif message.text == 'Технологии программирования(Python)':
        if is_started:
            bot.send_message(message.from_user.id, "Вы уже проходите тест, если хотите начать заново введите 'Начать тест заново'")
        else:
            is_started = True
            questions_test = questions_for_python
            bot.send_message(message.from_user.id, questions_test[0]['text'])
            bot.send_message(message.chat.id, 'Выберите вариант ответа:', reply_markup=markup)
            str_answers = ''
            for i in range(1, 5):
                str_answers += str(i) + '. ' + questions_test[gen_iter]['all_answers'][i - 1] + '\n'
            bot.send_message(message.from_user.id, str_answers)
    elif message.text == 'Основы ООП':
        if is_started:
            bot.send_message(message.from_user.id, "Вы уже проходите тест, если хотите начать заново введите 'Начать тест заново'")
        else:
            is_started = True
            questions_test = questions_for_OOP
            bot.send_message(message.from_user.id, questions_test[0]['text'])
            bot.send_message(message.chat.id, 'Выберите вариант ответа:', reply_markup=markup)
            str_answers = ''
            for i in range(1, len(questions_test[gen_iter]['all_answers']) + 1):
                str_answers += str(i) + '. ' + questions_test[gen_iter]['all_answers'][i - 1] + '\n'
            bot.send_message(message.from_user.id, str_answers)

    elif message.text in ('1', '2', '3', '4'):
        if int(message.text) - 1 == int(questions_test[gen_iter]['right_answer']):
            right_answ += 1
            bot.send_message(message.from_user.id, "Правильно, переходим к следующему вопросу...")
        else:
            bot.send_message(message.from_user.id, f"Неправильно, правильным ответом было {questions_test[gen_iter]['right_answer'] + 1}, переходим к следующему вопросу...")
        if gen_iter == len(questions_test) - 1:
            percent_right_answ = format((right_answ/len(questions_test) * 100), '.2f')
            bot.send_message(message.from_user.id, f'Тест завершён!\n Вы ответили правильно на {right_answ} из {len(questions_test)} вопросов, это {percent_right_answ}% от всего теста.')
        else:
            gen_iter += 1
            bot.send_message(message.from_user.id,
                             questions_test[gen_iter]['text'])
            str_answers = ''
            for i in range(1, len(questions_test[gen_iter]['all_answers']) + 1):
                str_answers += str(i) + '. ' + questions_test[gen_iter]['all_answers'][i-1] + '\n'
            bot.send_message(message.from_user.id, str_answers)

    else:
        bot.send_message(message.from_user.id, 'Такого варианта ответа нет')


bot.polling(none_stop=True)
