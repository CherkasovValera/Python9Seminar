# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
print("U+1F982")
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name} -  вах  генацвали!')


app = ApplicationBuilder().token("5466100628:AAF6NEj5TVg-6ZDBTNhfH_5CH_5sLR_e8bI").build()

app.add_handler(CommandHandler("hello", hello))
print("Gut")
app.run_polling()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
