from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton # type: ignore


commands_keyboard = InlineKeyboardMarkup()

bachelor = InlineKeyboardButton("Бакалавриат", callback_data="bachelor")
master = InlineKeyboardButton("Магистратура", callback_data="master")
postgraduate = InlineKeyboardButton("Аспирантура", callback_data="postgraduate")

commands_keyboard.add(bachelor, master, postgraduate)
