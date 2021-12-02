from src.telegram_api import updater, dispatcher


def  main():
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
