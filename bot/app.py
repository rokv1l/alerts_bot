from src.telegram_api import updater, dispatcher


if __name__ == '__main__':

    updater.start_polling()
    updater.idle()
