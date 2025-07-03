from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, CallbackContext

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("пн", callback_data="button_1"),
            InlineKeyboardButton("вт", callback_data="button_2"),
            InlineKeyboardButton("ср", callback_data="button_3"),
            InlineKeyboardButton("чт", callback_data="button_4"),
            InlineKeyboardButton("пт", callback_data="button_5"),
            InlineKeyboardButton("сб", callback_data="button_6"),
        ],
        [InlineKeyboardButton("воскресенье", callback_data="button_7")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("на какой день вы хотите узнать расписание?", reply_markup=reply_markup)


async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer() 

    if query.data == "button_1":
        await query.edit_message_text(text="""*1 урок|английский язык*
*2 урок|информатика*
*3 урок|биология*
*4 урок|история*
*5 урок|физика*
*6 урок|русский язык*""")
    elif query.data == "button_2":
        await query.edit_message_text(text="""*1 урок|алгебра*
*2 урок|ИЗО*
*3 урок|русский язык*
*4 урок|литература*
*5 урок|труд*
*6 урок|труд*""")
    elif query.data == "button_3":
        await query.edit_message_text(text="""*1 урок|геометрия*
*2 урок|физкультура*
*3 урок|история*
*4 урок|обществознание*
*5 урок|русский язык*
*6 урок|география*
*7 урок|английский язык*""")
    elif query.data == "button_4":
        await query.edit_message_text(text="""*1 урок|география*
*2 урок|русский язык*
*3 урок|литература*
*4 урок|физкультура*
*5 урок|музыка*
*6 урок|алгебра*
*7урок|английский язык*""")
    elif query.data == "button_5":
        await query.edit_message_text(text="""*1 урок|физкультура*
*2 урок|алгебра*
*3 урок|физика*
*4 урок|русский язык*
*5 урок|биология*
*6 урок|геометрия*
*7 урок|ОБЖ*""")
    elif query.data == "button_6":
        await query.edit_message_text(text="""в этот день нету уроков, ураааа!!!""")
    elif query.data == "button_7":
        await query.edit_message_text(text="""в этот день нету уроков, ураааа!!!""")
    else:
        await query.edit_message_text(text="Неизвестная кнопка!")


async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Используйте /start для получения кнопок.")


def main():
    application = Application.builder().token("7449751312:AAGSLQvN9zXzOoe7Et6gRs6is0TsbzBIfg8").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()


if __name__ == "__main__":
    main()
