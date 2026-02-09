import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)

load_dotenv()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum!")


async def randomcat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo("https://cataas.com/cat")


async def greet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command, name = update.message.text.split(" ")
    await update.message.reply_text(f"salom {name}")


async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command, operand01, operator, operand02 = update.message.text.split(" ")

    result = "xatolik berdi"

    if operator == "+":
        result = str(int(operand01) + int(operand02))
    elif operator == "-":
        result = str(int(operand01) - int(operand02))
    elif operator == "*":
        result = str(int(operand01) * int(operand02))
    elif operator == "/":
        if int(operand02) == 0:
            result = "nolga bolish mumkin emas"
        else:
            result = str(int(operand01) / int(operand02))

    await update.message.reply_text(result)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)


def main():
    app = ApplicationBuilder().token(os.getenv("TOKEN")).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("randomcat", randomcat))
    app.add_handler(CommandHandler("greet", greet))
    app.add_handler(CommandHandler("calc", calc))

    app.add_handler(MessageHandler(filters.TEXT, echo))

    app.run_polling()


main()
