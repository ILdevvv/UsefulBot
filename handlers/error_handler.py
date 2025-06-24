from aiogram.types import ErrorEvent
from aiogram import Router

from config.loader import settings
from config.bot import bot

router = Router()

@router.error()
async def global_error_handler(event: ErrorEvent) -> bool:
    update = event.update
    exception = event.exception

    if hasattr(update, 'message') and update.message:
        user_id = update.message.from_user.id
        first_name = update.message.from_user.first_name
        text = update.message.text
    else:
        user_id = None
        first_name = "Unknown"
        text = None
    tb = f"{type(exception).__name__}: {exception}"

    # Отправка администратору
    await bot.send_message(
        settings.CHAT_ID,
        f"🚨 <b>Ошибка в боте</b>\n"
        f"<b>Пользователь:</b> <a href='tg://user?id={user_id}'>{first_name}</a>\n"
        f"<b>Сообщение:</b> {text}\n"
        f"<b>Трассировка:</b> {tb}",
        parse_mode="HTML"
    )
    # Ответ пользователю
    if hasattr(update, 'message') and update.message:
        await update.message.reply("Произошла ошибка при обработке вашего запроса. Пожалуйста, попробуйте позже.")
    return True
