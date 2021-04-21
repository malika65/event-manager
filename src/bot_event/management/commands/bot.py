from django.core.management.base import BaseCommand
from django.conf import settings
from telegram.ext import *
from telegram.utils.request import Request
from telegram import Bot, Update
from .buttons import keyboard_1, keyboard_2
from bot_event.views import sample_response


def start_command(update, context):
    update.message.reply_text(
        "Type smth random to start", reply_markup=keyboard_1)


def help_command(update, context):
    update.message.reply_text("Help command is work)")


def who_are_you(update, context):
    txt = str(update.message.text).lower()
    print(txt)
    if txt == '🤠 пользователь':
        update.message.reply_text("User", reply_markup=keyboard_2)
    elif txt == '💸 спонсор':
        update.message.reply_text("Sponsor")
    else:
        response = sample_response(txt)

        update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    # This will define which button the user tapped on (from what you assigned to "callback_data". As I assigned them "1" and "2"):
    choose = query.data

    # Now u can define what choice ("callback_data") do what like this:
    if choose == 'see':
        print("See")

    if choose == 'eat':
        print("Eat")

    if choose == 'enjoy':
        print("Enjoy")

    if choose == 'know':
        print("Know")

    if choose == 'active':
        print("Active")

    if choose == 'buy':
        print("Buy")

    if choose == 'top':
        print("Top")


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
        dp.add_error_handler(error)

        # запустить бесконечную обработку сообщений
        updater.start_polling()
        updater.idle()

# ======== Webhook setting up ========
@server.route("/")
def webhook():
    bot.remove_webhook()
    s = bot.set_webhook(url='https://api.telegram.org/bot' +
                        '1614749492:AAHcfFo3nNnLI4A27lk27Q7a6s0rDWhOG1E')
    if s:
        return print("webhook setup ok")
    else:
        return print("webhook setup failed")
