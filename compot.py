from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Доступные команды:\n"
        "/start — запуск бота\n"
        "/help — показать это сообщение\n"
        "/joke — рассказать тупую шутку\n"
        "/random — показать рандомное число\n"
        "/time — вывести текущее время\n"
        "/guess <число> — попробовать угадать число\n"
    )
    await update.message.reply_text(help_text)

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Как я могу помочь?")

async def random_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = random.randint(1, 100)
    await update.message.reply_text(f"Ваше случайное число: {number}")

import datetime

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.now()
    await update.message.reply_text(f"Текущее время: {now.strftime('%Y-%m-%d %H:%M:%S')}")

target_number = random.randint(1, 10)

async def guess_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        guess = int(context.args[0])
        if guess == target_number:
            await update.message.reply_text("Поздравляю! Вы угадали число 🎉")
        elif guess < target_number:
            await update.message.reply_text("Моё число больше.")
        else:
            await update.message.reply_text("Моё число меньше.")
    except (IndexError, ValueError):
        await update.message.reply_text("Пожалуйста, отправьте команду так: /guess <число>")

async def joke_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jokes = [
        "Однорукий заходит в second hand. Выходит с двумя.",
        "Почему инвалиды не могут попасть в автобус? \nИх не пропускает валидатор! Бадутц!",
        "Колобок повесился!",
        "How do you call a fake pasta? \nAn Impasta! Ohohoho!",
        "Что сказал миллениал, когда выпил ТРЕТЬЮ чашку кофе за день (только он так мог)? \nОх! Моё сердечко щас скажет: ну вот, скоро моя остановочка охохохохохоохохохоохо",
        "суп из одной рыбы это уха, а из 5 рыб это ухахахахахахах",
        "Какой фрукт самый быстрый? Молниевый банан! 🍌⚡",
        "Считаете ли вы, что в скором времени фруктовое желе заменит биткоины? \nСпециалисты по криптовалюте отвечают: ааааааээээщщщлжыьывлту кажется, мы не поняли ваш вопрос.",
        "Что говорит кот, когда хочет есть? Мяу-мау! 🐱",
        "Почему учебник всегда грустный? Потому что у него много страниц... и мало друзей! 📚",
        "Что делает утка в интернете? Крякает онлайн! 🦆",
        "Почему утёнок пошёл на работу? Потому что хотел стать хлебом на закваске! 🦆🥖"
    ]
    joke = random.choice(jokes)
    await update.message.reply_text(joke)



TOKEN = 'тута был мой токен, но он останется при мне:)'
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("random", random_number))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("guess", guess_command))
app.add_handler(CommandHandler("joke", joke_command))

app.run_polling()

