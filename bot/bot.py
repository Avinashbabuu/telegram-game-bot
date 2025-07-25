import os
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")
WEB_URL = os.getenv("WEB_URL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("✅ I’ve Joined", callback_data="check_join")
    ]])
    await update.message.reply_text(
        f"🎮 Please join {CHANNEL_USERNAME} to play the game.",
        reply_markup=keyboard
    )

async def check_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
    query = update.callback_query

    if member.status in ["member", "administrator", "creator"]:
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton("▶️ Play Now", web_app=WebAppInfo(url=f"{WEB_URL}?uid={user_id}"))
        ]])
        await query.edit_message_text("✅ Channel joined! Click below to play.", reply_markup=keyboard)
    else:
        await query.answer("❌ You haven’t joined the channel yet.", show_alert=True)

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(check_join, pattern="check_join"))

if __name__ == "__main__":
    app.run_polling()
