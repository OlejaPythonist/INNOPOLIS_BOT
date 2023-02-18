from aiogram import Dispatcher  # type: ignore
from aiogram import types
from keyboards.user import commands_keyboard
from parsing.parse_info import (
    get_bachelor_text,
    get_master_text,
    get_postgraduate_text,
    parse
)


async def start(message: types.Message) -> None:
    await message.reply(
        "Привет)",
        reply_markup=commands_keyboard
    )  # текст нужно придумать


async def bachelor(call: types.CallbackQuery) -> None:
    await call.message.answer("ПОИСК ИНФОРМАЦИИ НАЧАЛСЯ")
    url = "https://apply.innopolis.university/bachelor/"\
          "?lang=ru&id=12&site=s1&template=university24&landing_mode=edit"
    texts = await parse(url, get_bachelor_text)
    for text in texts:
        await call.message.answer(text)


async def master(call: types.CallbackQuery) -> None:
    await call.message.answer("ПОИСК ИНФОРМАЦИИ НАЧАЛСЯ")
    url = "https://apply.innopolis.university/master/datascience/"\
          "?lang=ru&id=12&site=s1&template=university24&landing_mode=edit"
    texts = await parse(url, get_master_text)
    for text in texts:
        await call.message.answer(text)


async def postgraduate(call: types.CallbackQuery) -> None:
    await call.message.answer("ПОИСК ИНФОРМАЦИИ НАЧАЛСЯ")
    url = "https://apply.innopolis.university/postgraduate-study/"\
          "?lang=ru&id=12&site=s1&template=university24&landing_mode=edit"
    texts = await parse(url, get_postgraduate_text)
    for text in texts:
        await call.message.answer(text)


async def trash(message: types.Message) -> None:
    await message.answer(
        "Вы ввели неправильную комманду.\nУзнать условия поступления:",
        reply_markup=commands_keyboard
    )


def register_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(
        start,
        commands=["start", "help"]
    )
    dp.register_message_handler(trash)
    dp.register_callback_query_handler(
        bachelor,
        lambda c: c.data == "bachelor"
    )
    dp.register_callback_query_handler(
        master,
        lambda c: c.data == "master"
    )
    dp.register_callback_query_handler(
        postgraduate,
        lambda c: c.data == "postgraduate"
    )
