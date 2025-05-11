from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    ConversationHandler, ContextTypes
)
MENU, SUBMENU1, SUBMENU2, SUBMENU3, SUBMENU4 = range(5)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    keyboard = [
        [InlineKeyboardButton("Fruits", callback_data="submenu1")],
        [InlineKeyboardButton("Animals", callback_data="submenu2")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Main Menu", reply_markup=reply_markup)
    return MENU

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    if query.data == "submenu1":
        keyboard = [
            [InlineKeyboardButton("Apple", callback_data="item_apple")],
            [InlineKeyboardButton("Banana", callback_data="item_banana")],
            [InlineKeyboardButton("Back", callback_data="back_main")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="Fruits Submenu",
            reply_markup=reply_markup
        )
        return SUBMENU1
    elif query.data == "submenu2":
        keyboard = [
            [InlineKeyboardButton("Cat", callback_data="item_cat")],
            [InlineKeyboardButton("Dog", callback_data="item_dog")],
            [InlineKeyboardButton("Back", callback_data="back_main")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="Animals Submenu",
            reply_markup=reply_markup
        )
        return SUBMENU2

async def submenu1_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    if query.data == "back_main":
        keyboard = [
            [InlineKeyboardButton("Fruits", callback_data="submenu1")],
            [InlineKeyboardButton("Animals", callback_data="submenu2")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="Main Menu",
            reply_markup=reply_markup
        )
        return MENU
    elif query.data == "item_apple":
        await query.answer(text="You selected Apple.")
        return SUBMENU1
    elif query.data == "item_banana":
        await query.answer(text="You selected Banana.")
        return SUBMENU1

async def submenu2_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    if query.data == "back_main":
        keyboard = [
            [InlineKeyboardButton("Fruits", callback_data="submenu1")],
            [InlineKeyboardButton("Animals", callback_data="submenu2")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="Main Menu",
            reply_markup=reply_markup
        )
        return MENU
    elif query.data == "item_cat":
        await query.answer(text="You selected Cat.")
        return SUBMENU2
    elif query.data == "item_dog":
        await query.answer(text="You selected Dog.")
        return SUBMENU2
async def submenu3_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    if query.data == "back_main":
        keyboard = [
            [InlineKeyboardButton("Fruits", callback_data="submenu1")],
            [InlineKeyboardButton("Animals", callback_data="submenu2")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="Main Menu",
            reply_markup=reply_markup
        )
        return MENU
    elif query.data == "item_cat":
        await query.answer(text="You selected Cat.")
        return SUBMENU3
    elif query.data == "item_dog":
        await query.answer(text="You selected Dog.")
        return SUBMENU3

async def submenu4_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    if query.data == "back_main":
        keyboard = [
            [InlineKeyboardButton("Fruits", callback_data="submenu1")],
            [InlineKeyboardButton("Animals", callback_data="submenu2")]
            
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="Main Menu",
            reply_markup=reply_markup
        )
        return MENU
    elif query.data == "item_cat":
        await query.answer(text="You selected Cat.")
        return SUBMENU4
    elif query.data == "item_dog":
        await query.answer(text="You selected Dog.")
        return SUBMENU4
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Goodbye.")
    return ConversationHandler.END

def main():
    app = Application.builder().token("7223998996:AAEp_2McFFA59tJ3QFZrSonONDUW1XDcXRM").build()
    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MENU: [CallbackQueryHandler(menu_handler)],
            SUBMENU1: [CallbackQueryHandler(submenu1_handler)],
            SUBMENU2: [CallbackQueryHandler(submenu2_handler)],
            SUBMENU3: [CallbackQueryHandler(submenu3_handler)],
            SUBMENU4: [CallbackQueryHandler(submenu4_handler)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    app.add_handler(conv)
    app.run_polling()

if __name__ == "__main__":
    main()
