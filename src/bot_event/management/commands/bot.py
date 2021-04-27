import os

from django.core.management.base import BaseCommand
from django.conf import settings
from telegram.ext import *
from telegram.utils.request import Request
from telegram import Bot, Update
from .buttons import keyboard_1, keyboard_2,get_keyboard
from telegram import  KeyboardButton, ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
from bot_event.views import sample_response
from event_app.models import Post,PostImage
from telebot.types import InputMediaPhoto, InputMediaVideo
from datetime import date
import sys
import locale


def start_command(update,context):
    update.message.reply_text("Если заинтересованы в сотрудничестве ,то жмите кнопку 💸 Спонсор \nЕсли вы в поисках новых ощущений или просто не знаете куда сходить , то жмите кнопку 🤠 Пользователь и забудьте об этих проблемах", reply_markup = keyboard_1)

def start_command(update, context):
    update.message.reply_text(
        "Type smth random to start", reply_markup=keyboard_1)


def help_command(update, context):
    update.message.reply_text("Help command is work)")


def who_are_you(update, context):
    txt = str(update.message.text).lower()
    print(txt)
    if txt == '🤠 пользователь':
        update.message.reply_text("Выберите чем хотите заняться",reply_markup = keyboard_2)
    elif txt == '💸 спонсор':
        update.message.reply_text("Для регистрации перейдите на следующий сайт google.com . \nТут вы сможете опубликовать вашу информацию")
    elif txt == 'главное меню':
        update.message.reply_text("Главное меню",reply_markup=keyboard_2)
    else:
        response = sample_response(txt)
        update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")

def choose_by_name(post):
    kb_1 = []
    for i in post:
        kb_1.append([InlineKeyboardButton(f'{i.title}',callback_data=f'{i.id}-posts')])
        
    keyboard_name = InlineKeyboardMarkup(kb_1,resize_keyboard=True)

    return keyboard_name


def print_posts(post,bot,choose,query,true_choose):
    for pop in post:
        image = pop.images.all()
        image = PostImage.objects.filter(post=pop)
        img_list= []
        listToStr = ',\n '.join([str(elem) for elem in pop.link_list])

        for i in image:
            img_list.append(str(i.images))
            
        media_group = list()
        for number, url in enumerate(img_list):
            if number == 1 :
                media_group.append(InputMediaPhoto(media=url))
            else:
                media_group.append(InputMediaPhoto(media=url))

        bot.send_media_group(query.message.chat_id, media=media_group)
        
        bot.send_message(chat_id=query.message.chat_id,
        text=f"Название : {pop.title}\nОписание : {pop.description}\nКонтакты: {pop.phone} \nМы в соц.сетях : {listToStr}")
    btn_more = [
        [
            InlineKeyboardButton('More',callback_data=f'{true_choose}'),
            ]
        ]
    keyboard_more = InlineKeyboardMarkup(btn_more,resize_keyboard=False)

    bot.send_message(chat_id=query.message.chat_id,text="Чтобы посмотреть больше нажмите кнопку ниже",reply_markup=keyboard_more)

def print_one_post(post,bot,query):
    image = post.images.all()
    image = PostImage.objects.filter(post=post)
    img_list= []
    listToStr = ',\n '.join([str(elem) for elem in post.link_list])

    for i in image:
        img_list.append(str(i.images))
        
    media_group = list()
    for number, url in enumerate(img_list):
        if number == 1 :
            media_group.append(InputMediaPhoto(media=url))
        else:
            media_group.append(InputMediaPhoto(media=url))

    bot.send_media_group(query.message.chat_id, media=media_group)
    
    bot.send_message(chat_id=query.message.chat_id,
    text=f"Название : {post.title}\nОписание : {post.description}\nКонтакты: {post.phone} \nМы в соц.сетях : {listToStr}")

     


def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    bot = context.bot
    # This will define which button the user tapped on (from what you assigned to "callback_data". As I assigned them "1" and "2"):
    choose = query.data

    # Now u can define what choice ("callback_data") do what like this:
    if choose == 'back':
        bot.editMessageReplyMarkup(chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=keyboard_2
        )
    
    elif '_' in choose:
        true_choose = choose[0:-1]
        choose = choose.split('_')
        more = int(choose[2])
        subchoose = choose[1]
        choose = choose[0]
        true_choose = true_choose + str(more + 2)
        post = Post()
        if subchoose == 'sale':
            post = Post.objects.filter(category=choose,sale=True)[more-1:more+1]
            print_posts(post,bot,choose,query,true_choose)
        elif subchoose == 'all':
            post = Post.objects.filter(category=choose)[more-1:more+1]
            print_posts(post,bot,choose,query,true_choose)
        elif subchoose == 'name':
            post = Post.objects.filter(category=choose)
            keyboard_name = choose_by_name(post)

            bot.editMessageReplyMarkup(chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            reply_markup=keyboard_name)

        elif subchoose == 'near':
            print("Near")
            # Добавим в будущем карту
        elif subchoose == 'top':
            # Топ 
            print("Top")
    elif 'posts' in choose:
        post_id = choose.split('-')[0]
        post = Post.objects.get(id=post_id)
        print_one_post(post,bot,query)
    # Add submenu
    else:
        keyboard_3 = get_keyboard(choose)
        
        bot.editMessageReplyMarkup(chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=keyboard_3
        )

      

# def likes_handler(update: Update, context: CallbackContext) -> None:
#     query = update.callback_query
#     query.answer()
#     bot = context.bot

#     choose = query.data



class Command(BaseCommand):
    help = 'Telegram bot'

    def handle(self, *args, **options):
        # подключение
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
            base_url=settings.PROXY_URL,  # Proxy нужен для обхода блокировок телеграма
        )
        print(bot.get_me())

        # обработчики сообщений
        updater = Updater(
            bot=bot,
            use_context=True,
        )
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", start_command))
        dp.add_handler(CommandHandler("help", help_command))
        dp.add_handler(MessageHandler(Filters.text, who_are_you))
        # dp.add_handler(MessageHandler(Filters.text, handle_message))
        dp.add_handler(CallbackQueryHandler(button_handler))
        # dp.add_handler(CallbackQueryHandler(options_filter))
        dp.add_error_handler(error)

        # запустить бесконечную обработку сообщений
        
        updater.start_polling()
        updater.idle()

        # updater.start_webhook(listen="0.0.0.0",
        #               port=int(os.environ.get("PORT", 8443)),
        #               url_path=settings.TOKEN )
        # updater.bot.setWebhook(settings.PROXY_URL + settings.TOKEN)

        # updater.idle()
