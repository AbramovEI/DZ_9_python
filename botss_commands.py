from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    print(msg)
    await update.message.reply_text(f'вы написали {msg}')

async def fam(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    last_name = update.message.text
    print(last_name)
    await update.message.reply_text(f'Фамилия {last_name}')


async def name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    first_name = update.message.text
    print(first_name)
    await update.message.reply_text(f'имя {first_name}')


async def tel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    number = update.message.text
    print(number)
    await update.message.reply_text(f'телефон {number}')


async def printer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'новый контакт {fam} , {name} , {tel}')


# async def new (update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await context.bot.send_message(chat_id=update.effective_chat.id, text= get_info(update.message.text))