from time import sleep
from threading import Thread

from telegram import Update
from telegram.ext import CallbackContext

from src.database import session_maker, Alert, User
from src.telegram_api import dispatcher


def alert_handler(update: Update, context: CallbackContext) -> None:
    with session_maker() as session:
        messages = [alert.message for alert in session.query(Alert).filter(not Alert.sent).all()]
        if not messages:
            return
        for user in session.query(User).filter(User.active).all():
            Thread(target=send_alerts, args=(user.id, messages)).start()


def send_alerts(user: int, texts: list) -> None:
    for text in texts:
        dispatcher.bot.send_message(chat_id=user, text=text)

