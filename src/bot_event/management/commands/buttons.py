from telegram import  KeyboardButton, ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup


keyboard = [
    [
        KeyboardButton('🤠 Пользователь',callback_data='user'),
        KeyboardButton('💸 Спонсор',callback_data='sponsor'),
    ],
    [
        KeyboardButton('Главное меню',callback_data='menu'),
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



def get_keyboard(choose):
    kb_1 = [
            [
                InlineKeyboardButton('📆 Скоро',callback_data=f'{choose}_soon_2')
            ],
            [
                InlineKeyboardButton('🛒 Скидки',callback_data=f'{choose}_sale_2')
            ],
            [   InlineKeyboardButton('📒 Посмотреть все',callback_data=f'{choose}_all_2')
            ],
            [
                InlineKeyboardButton('📝 Выбрать по названию',callback_data=f'{choose}_name_2')
                ] ,   
            [
                InlineKeyboardButton('🗺️ Рядом',callback_data=f'{choose}_near_2')
            ],
            [
                InlineKeyboardButton('🔝 Топ 10',callback_data=f'{choose}_top_2')
            ],
            [
                InlineKeyboardButton('⬅️ Назад',callback_data='back')
            ]
        ]
    keyboard_3 = InlineKeyboardMarkup(kb_1,resize_keyboard=True)
        
    return keyboard_3
        
