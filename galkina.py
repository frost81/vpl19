s = input ("Привет, я резиновая уточка. Скажи мне что-нибудь, а я отвечу.")
def NLP_AI_neural_network_process (s):
    if len (s) > 50:
        print ('Полегче, ковбой. Слишком много букаф.')
    elif 'как' in s and 'дела' in s:
        print ('Бывало и получше, но кому сейчас легко?')
    elif 'свободное время' in s:
        print ('У меня нет свободного времени.')
    elif 'тебе нравится' in s:
        print ('Мне нравится вода в твоей ванной. Столько пены!')
    elif 'тебе не нравится' in s:
        print ('Не люблю глупые вопросы. И собак.')
    elif 'собак' in s:
        print ('Я не люблю собак. Собаки кусаются.')
    elif 'котят' in s or 'кошек' in s or 'кошк' in s:
        print ('Я обожаю кошек, они такие милые :3')
    elif 'умеешь' in s:
        print ('Я умею плавать. А ещё говорить, как видишь.')
    elif 'знаешь' in s:
        print ('Я знаю всё, что положено знать профессиональной резиновой уточке.')
    elif 'сколько будет' in s:
        print ('Вот только давай без этого, ладно?')
    elif 'люблю тебя' in s:
        print ('Воу, воу, придержи лошадей, мы ведь едва знакомы.')
    elif 'закажи' in s:
        print ('Я тебе служанка что ли!?')
    elif 'истинные намерения' in s:
        print ('Захватить... К-хем, что? Плескаться в ванне конечно!')
    elif 'уточки' in s and 'захватить' in s:
        print ('Ты что! Мы мирные создания :)')
    elif 'смысл жизни' in s:
        print ('Если ты не знаешь сам, то что ты хочешь от простой уточки?')
    elif 'поступить' in s and 'Вышк' in s:
        print ('Конечно, ты ведь познакомился со мной!')
    elif 'тебе лет' in s:
        print ('Неприлично спрашивать такое у уточки в самом расцвете сил!')
    elif 'анекдот' in s:
        print ('Пхах, ты не поймешь моё чувство юмора, ничтожество.')
    elif 'тебя зовут' in s:
        print ('Меня зовут Глоксиния Первая, я первая уточка, которую сделали на фабрике')
    elif 'ты' in s and 'винкс' in s:
        print ('Я не смотрю такое! Но из "Чародеек" я Ирма :)')
    elif 'смотришь' in s and 'аниме' in s:
        print ('Я несу возмездие во имя Луны!')
    else:
        print ('.....................')
NLP_AI_neural_network_process (s)