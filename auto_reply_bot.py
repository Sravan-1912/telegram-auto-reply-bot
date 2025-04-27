from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Your Telegram Bot Token
TOKEN = '7592383381:AAE59Mz_d-5Kclf8jRXtYHtE7EwaaerFGL8'

# Create the application
app = ApplicationBuilder().token(TOKEN).build()

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your auto-reply bot. I will answer when Sravan is offline!')

# Auto reply when user sends any text
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name  # Get sender's name
    reply_text = f"Hi {user_name}, Sravan is currently offline 🚫. He'll get back to you soon!"
    await update.message.reply_text(reply_text)

# Add handlers
app.add_handler(CommandHandler('start', start))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), auto_reply))

# Start polling
app.run_polling()
