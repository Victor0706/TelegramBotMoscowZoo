import telebot
from Config import TOKEN, token
from telebot import types
from social_spam import Vkontakte


vk = Vkontakte()
vk.connect_user(token)


bot = telebot.TeleBot(TOKEN)

summ = 0


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = 'Приветствую Вас уважаемый пользователь! Здесь вы можете посмотреть всех животных и выбрать свое тотемное животное. \
    \nЧтобы начать работу введите команду боту в следущем формате: \
    \nПосмотреть отряды имеющихся животных: /animals \
    \nОпределить ваше тотемное животное /victorina \
    \nСвязаться с сотрудником для получения необходимой информации /contact'
    bot.reply_to(message, text)


@bot.message_handler(commands=['animals'])
def animals(message: telebot.types.Message):
    text = 'Классы животных в зоопарке: \nМлекопитающие: /mammals \nПтицы: /birds \
    \nРептилии: /reptiles \nАмфибии: /amphibians'
    bot.reply_to(message, text)


@bot.message_handler(commands=['mammals'])
def mammals(message: telebot.types.Message):
    text = 'Отряды млекопитающих в зоопарке: \nПриматы \nНасекомоядные \nРукокрылые \nГрызуны \nЛастоногие \nДаманы \
    \nТрубкозубовые \nНеполнозубые \nХищники \nНепарнокопытные \nПарнокопытные \nХоботные \nДвурезцовые сумчатые \
    \nКитопарнокопытные \nМозоленогие'
    bot.reply_to(message, text)


@bot.message_handler(commands=['birds'])
def birds(message: telebot.types.Message):
    text = 'Отряды птиц в зоопарке: \nГусеобразные \nЖуравлеобразные \nКазуарообразные \nСовообразные \nВоробьинообразные \
    \nСоколообразные \nРакшеобразные \nКурообразные \nПопугаеобразные \nПингвинообразные \
    \nГолубеобразные \nРжанкообразные \nФламингообразные \nДятлообразные \nТураковые \nАистообразные \nКукушкообразные'
    bot.reply_to(message, text)


@bot.message_handler(commands=['reptiles'])
def reptiles(message: telebot.types.Message):
    text = 'Отряды рептилий в зоопарке: \nЧешуйчатые \nКрокодилы \nЧерепахи'
    bot.reply_to(message, text)


@bot.message_handler(commands=['amphibians'])
def amphibians(message: telebot.types.Message):
    text = 'Отряды амфибий в зоопарке: \nБесхвостые земноводные \nХвостатые земноводные'
    bot.reply_to(message, text)


@bot.message_handler(commands=['contact'])
def contact(message: telebot.types.Message):
    bot.send_contact(message.chat.id, phone_number=89672902384, first_name='Victor', last_name='https://vk.com/id339279540')


@bot.message_handler(commands=['victorina'])
def victorina_start(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Готовы к викторине? Начнем. Просто напишите: викторина')


@bot.message_handler(commands=['review'])
def review(message: telebot.types.Message):
    bot.send_poll(message.chat.id, question='Как Вам наша викторина?', options=['Отлично', 'Удовлетворительно', 'Не понравилось'], is_anonymous=True, allows_multiple_answers=False)


@bot.message_handler(commands=['guardianship'])
def guardianship(message: telebot.types.Message):
    text = 'Возьмите животное под опеку! \
    \nУчастие в программе «Клуб друзей зоопарка» — это помощь в содержании наших обитателей, а также ваш личный вклад в дело сохранения биоразнообразия Земли и \
    \nразвитие нашего зоопарка. \
    \nОсновная задача Московского зоопарка с самого начала его существования это — сохранение биоразнообразия планеты. Когда вы берете под опеку животное, вы помогаете нам в \
    \nэтом благородном деле. При нынешних темпах развития цивилизации к 2050 году с лица Земли могут исчезнуть около 10 000 биологических видов. Московский зоопарк \
    \nвместе с другими зоопарками мира делает все возможное, чтобы сохранить их. \
    \nТрадиция опекать животных в Московском зоопарке возникло с момента его создания в 1864г. Такая практика есть и в других зоопарках по всему миру. \
    \nВ настоящее время опекуны объединились в неформальное сообщество — Клуб друзей Московского зоопарка. Программа «Клуб друзей» дает возможность опекунам \
    \nощутить свою причастность к делу сохранения природы, участвовать в жизни Московского зоопарка и его обитателей, видеть конкретные результаты своей деятельности. \
    \nОпекать – значит помогать любимым животным. Можно взять под крыло любого обитателя Московского зоопарка, в том числе и того, кто живет за городом – в Центре \
    \nвоспроизводства редких видов животных под Волоколамском. Там живут и размножаются виды, которых нет в городской части зоопарка: величественные журавли стерхи, забавные дрофы, исчезнувшая в природе\
    \nлошадь Пржевальского, изящные антилопы бонго и многие другие. Можете съездить на экскурсию в Центр и познакомиться с обитателями.'
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def victorina(message: telebot.types.Message):
    global summ
    if message.text == 'викторина' or message.text == 'Попробовать еще раз?':
        summ = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('да на первый вопрос')
        item2 = types.KeyboardButton('нет на первый вопрос')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Вы любите больших животных?', reply_markup=markup)
    elif message.text == 'икторина' or message.text == 'виктрина':
        raise SyntaxError('ошибка ввода')

    if message.text == 'да на первый вопрос':
        summ = summ + 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('да на второй вопрос')
        item2 = types.KeyboardButton('нет на второй вопрос')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Вам нравятся крупные хищники?', reply_markup=markup)
    elif message.text == 'нет на первый вопрос':
        summ = summ
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('да на второй вопрос')
        item2 = types.KeyboardButton('нет на второй вопрос')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Вам нравятся крупные хищники?', reply_markup=markup)

    if message.text == 'да на второй вопрос':
        summ = summ + 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('да на третий вопрос')
        item2 = types.KeyboardButton('нет на третий вопрос')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Вам нравятся крупные, но добрые животные?', reply_markup=markup)
    elif message.text == 'нет на второй вопрос':
        summ = summ
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('да на третий вопрос')
        item2 = types.KeyboardButton('нет на третий вопрос')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Вам нравятся крупные, но добрые животные?', reply_markup=markup)

    if message.text == 'да на третий вопрос':
        summ = summ + 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('да на четвертый вопрос')
        item2 = types.KeyboardButton('нет на четвертый вопрос')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Вам интересуют маленькие и проворные животные?', reply_markup=markup)
    elif message.text == 'нет на третий вопрос':
        summ = summ
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('да на четвертый вопрос')
        item2 = types.KeyboardButton('нет на четвертый вопрос')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Вас интересуют маленькие и проворные животные?', reply_markup=markup)

    if message.text == 'да на четвертый вопрос':
        summ = summ + 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('да на пятый вопрос')
        item2 = types.KeyboardButton('нет на пятый вопрос')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Понравится, когда встретите развоворчиго друга в перьях?', reply_markup=markup)
    elif message.text == 'нет на четвертый вопрос':
        summ = summ
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('да на пятый вопрос')
        item2 = types.KeyboardButton('нет на пятый вопрос')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Понравится, когда встретите развоворчиго друга в перьях?', reply_markup=markup)

    if message.text == 'да на пятый вопрос':
        summ = summ + 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('да на шестой вопрос')
        item2 = types.KeyboardButton('нет на шестой вопрос')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'А как Вам хищники в панцире?', reply_markup=markup)
    elif message.text == 'нет на пятый вопрос':
        summ = summ
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('да на шестой вопрос')
        item2 = types.KeyboardButton('нет на шестой вопрос')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'А как Вам хищники в панцире?', reply_markup=markup)

    if message.text == 'да на шестой вопрос':
        summ = summ + 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('да на седьмой вопрос')
        item2 = types.KeyboardButton('нет на седьмой вопрос')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Как насчет экзотики?', reply_markup=markup)
    elif message.text == 'нет на шестой вопрос':
        summ = summ
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('да на седьмой вопрос')
        item2 = types.KeyboardButton('нет на седьмой вопрос')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Как насчет экзотики?', reply_markup=markup)

    if message.text == 'да на седьмой вопрос':
        summ = summ + 1
        bot.send_message(message.chat.id, f'Вы набрали {summ} баллов')
        if summ == 7:
            text = 'Амурский тигр - ваш выбор.'
            image = 'amur_tiger.png'
        elif summ == 6:
            text = 'Слон - то, что вам нужно.'
            image = 'asian_elephant.png'
        elif summ == 5:
            text = 'Тамарин - маленький примат.'
            image = 'red-handed_tamarin.png'
        elif summ == 4:
            text = 'Вы выбрали какаду Гоффина. Будет с кем поговорить.'
            image = 'goffin_cockatoo.png'
        elif summ == 3:
            text = 'Грозный нильский крокодил. Вот кто ваш друг.'
            image = 'nile_crocodile.png'
        else:
            text = 'Полная экзотика. Подружитесь с голубым древолазом?'
            image = 'blue_drew_frog.png'
        bot.reply_to(message, text)
        file = open(image, 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('Попробовать еще раз?')
        markup.add(item)
        bot.reply_to(message, text)
        bot.send_message(message.chat.id, 'Не устроил результат? Тогда пройдем викторину еще раз.', reply_markup=markup)
        text = 'Чтобы поделиться результатом загрузите и перетащите фото в строку. \
        \nТакже просим Вас оценить интерес с которым Вы проходили викторину: /review \
        \nДля вашего удобства отправим результат викторины на вашу страничку Вконтакте \
        \nТеперь самое время подробнее ознакомиться с программой опекунства: /guardianship'
        bot.reply_to(message, text)
        vk.send_message(339279540, message='По итогам викторины мне посоветовали стать опекуном этой очаровашки:' f'<a href="https://t.me/MoscowZooAnimalBot"</a>',
                        image=image)

    elif message.text == 'нет на седьмой вопрос':
        summ = summ
        bot.send_message(message.chat.id, f'Вы набрали {summ} баллов')
        if summ == 7:
            text = 'Амурский тигр - ваш выбор.'
            image = 'amur_tiger.png'
        elif summ == 6:
            text = 'Слон - то, что вам нужно.'
            image = 'asian_elephant.png'
        elif summ == 5:
            text = 'Тамарин - маленький примат.'
            image = 'red-handed_tamarin.png'
        elif summ == 4:
            text = 'Вы выбрали какаду Гоффина. Будет с кем поговорить.'
            image = 'goffin_cockatoo.png'
        elif summ == 3:
            text = 'Грозный нильский крокодил. Вот кто ваш друг.'
            image = 'nile_crocodile.png'
        else:
            text = 'Полная экзотика. Подружитесь с голубым древолазом?'
            image = 'blue_drew_frog.png'
        bot.reply_to(message, text)
        file = open(image, 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('Попробовать еще раз?')
        markup.add(item)
        bot.reply_to(message, text)
        bot.send_message(message.chat.id, 'Не устроил результат? Тогда пройдем викторину еще раз.', reply_markup=markup)
        text = 'Чтобы поделиться результатом загрузите и перетащите фото в строку. \
        \nТакже просим Вас оценить интерес с которым Вы проходили викторину: /review \
        \nДля вашего удобства отправим результат викторины на вашу страничку Вконтакте \
        \nТеперь самое время подробнее ознакомиться с программой опекунства: /guardianship'
        bot.reply_to(message, text)
        vk.send_message(339279540, message='По итогам викторины мне посоветовали стать опекуном этой очаровашки:' f'<a href="https://t.me/MoscowZooAnimalBot"</a>',
        image=image)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message, 'Ваш результат принят')


bot.polling()