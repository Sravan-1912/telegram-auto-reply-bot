from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler

BOT_TOKEN = '7592383381:AAE59Mz_d-5Kclf8jRXtYHtE7EwaaerFGL8'  # 🔥 Put your token here!

is_offline = True  # Assume offline when bot starts

def start(update: Update, context: CallbackContext):
    global is_offline
    is_offline = False
    update.message.reply_text("✅ Bot is now ONLINE. Auto-replies are OFF.")

def offline(update: Update, context: CallbackContext):
    global is_offline
    is_offline = True
    update.message.reply_text("🛑 Bot is now OFFLINE. Auto-replies are ON.")

def auto_reply(update: Update, context: CallbackContext):
    if is_offline:
        chat_id = update.effective_chat.id
        user_first_name = update.message.from_user.first_name
        user_message = update.message.text
        print(f"Received message from {user_first_name}: {user_message}")
        
        reply_text = f"Hey {user_first_name}! 👋 I'm currently offline. I'll reply soon!"
        context.bot.send_message(chat_id=chat_id, text=reply_text)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))    
    dp.add_handler(CommandHandler('offline', offline)) 
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, auto_reply))

    print("🚀 Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
