from telegram import  KeyboardButton, ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup


keyboard = [
    [
        KeyboardButton('🤠 Пользователь',callback_data='user'),
        KeyboardButton('💸 Спонсор',callback_data='sponsor'),
    ]
    
]

keyboard_1 = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)


kb = [
    [
        InlineKeyboardButton('🎦 Посмотреть',callback_data='1'),
        InlineKeyboardButton('🍽️ Покушать',callback_data='2'),
    ],
    [   InlineKeyboardButton('🎡 Развлекательное',callback_data='3'),
        InlineKeyboardButton('🖼️ Познавательное',callback_data='4'),
        ] ,   
    [
        InlineKeyboardButton('🧗 Активный отдых',callback_data='5'),
        InlineKeyboardButton('🛍️ Что купить?',callback_data='6'),
    ],
    [
        InlineKeyboardButton('🔝 Топ 10',callback_data='top'),
    ]
]

keyboard_2 = InlineKeyboardMarkup(kb,resize_keyboard=True)

btn_like = [
    [
        InlineKeyboardButton('👍',callback_data='like'),
        InlineKeyboardButton('👎',callback_data='dislike'),
    ]
]

keyboard_like = InlineKeyboardMarkup(btn_like,resize_keyboard=True)



# kb_1 = [
#     [
#         InlineKeyboardButton('📆 Скоро',callback_data='soon')
#     ],
#     [
#         InlineKeyboardButton('🛒 Скидки',callback_data='sale')
#     ],
#     [   InlineKeyboardButton('📒 Посмотреть все',callback_data='see')
#     ],
#     [
#         InlineKeyboardButton('📝 Выбрать по названию',callback_data='name')
#         ] ,   
#     [
#         InlineKeyboardButton('🗺️ Рядом',callback_data='near')
#     ],
#     [
#         InlineKeyboardButton('🔝 Топ 10',callback_data='top')
#     ],
#     [
#         InlineKeyboardButton('⬅️ Назад',callback_data='7')
#     ]
# ]

# keyboard_3 = InlineKeyboardMarkup(kb_1,resize_keyboard=True)