from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler


key_token = "6868024717:AAGgiwlBcENXrLLFSUzI4etP4GK0LhFWQkA" #Masukkan KEY-TOKEN BOT 
user_bot = "ClassX_igs_bot" #Masukkan @user bot


async def  start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Gunakan /help untuk menampilkan apa yang dapat saya berikan..")
    
async def  help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kirim pesan, bot akan membalas pesan..")


async def  text_massage(update: Update, context:ContextTypes.DEFAULT_TYPE):
    text_diterima : str = update.message.text
    print(f"Pesan diterima : {text_diterima}")
    text_lwr_diterima = text_diterima.lower()
    if 'perangkat kelas' in text_lwr_diterima:
        await update.message.reply_text("Hallo!\n1. Ketua kelas: Wylseen\n2. Wakil ketua: Halimah\n3. Sekretaris: Via")
    elif 'tugas dari guru' in text_lwr_diterima:
        await update.message.reply_text("1. Tugas bahasa inggris halaman 122.\n2. Tugas coding pyhton\n3. Tugas Matematika hal 34")
    elif 'siapa kamu ?' in text_lwr_diterima:
        await update.message.reply_text(f"saya adalah {user_bot}, asisten kelas anda yg akan membantu mengurus tugas kelas.")
    elif 'tenggat waktu tugas' in text_lwr_diterima:
        await update.message.reply_text(f"1. Tugas bahasa inggris: 29/01/2024\n2. Tugas coding pyhton: 28/11/2023\n3. Tugas Matematika: 1/12/2023")
    else:
        await update.message.reply_text("Tidak termasuk dalam kelas.")


async def photo_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("Gambar kamu bagus")
        
async def  error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"error... : {context.error}")


if __name__ == '__main__':
    print("Mulai")
    app = Application.builder().token(key_token).build()
    #COMMAND :
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    #MESSAGE:
    app.add_handler(MessageHandler(filters.TEXT, text_massage))
    app.add_handler(MessageHandler(filters.PHOTO, photo_message))
    #error :
    app.add_error_handler(error)
    #polling :
    app.run_polling(poll_interval=1)
