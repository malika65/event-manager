from telegram import  KeyboardButton, ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup


keyboard = [
    [
        KeyboardButton('🤠 Пользователь',callback_data='see'),
        KeyboardButton('💸 Спонсор',callback_data='eat'),
    ]
]

keyboard_1 = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)


kb = [
    [
        InlineKeyboardButton('🎦 Посмотреть',callback_data='see'),
        InlineKeyboardButton('🍽️ Покушать',callback_data='eat'),
    ],
    [   InlineKeyboardButton('🎡 Развлекательное',callback_data='enjoy'),
        InlineKeyboardButton('🖼️ Познавательное',callback_data='know'),
        ] ,   
    [
        InlineKeyboardButton('🧗 Активный отдых',callback_data='active'),
        InlineKeyboardButton('🛍️ Что купить?',callback_data='buy'),
    ],
    [
        InlineKeyboardButton('🔝 Топ 10',callback_data='top'),
    ]
]

keyboard_2 = InlineKeyboardMarkup(kb,resize_keyboard=True)
