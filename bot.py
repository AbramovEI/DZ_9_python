from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from botss_commands import *

app = ApplicationBuilder().token("5809695533:AAE6V66t5gY-NQVugBCRJhU5YiUEZuiDVLo").build()

print('server start')

app.add_handler(CommandHandler("hello", hello))

app.add_handler(CommandHandler("hi", bot))

app.add_handler(CommandHandler("fam", fam))

app.add_handler(CommandHandler("name", name))

app.add_handler(CommandHandler("tel", tel))

app.add_handler(CommandHandler("print", printer))

app.run_polling()