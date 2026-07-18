# requires: aiohttp
# meta developer: @your_username
# scope: heroku_min 1.5.0
# Демонстрационный external-модуль. Поставить: .dlmod https://github.com/krutyshkin/heroku-modbook/blob/main/examples/hello.py

from herokutl.tl.types import Message

from heroku import loader, utils


@loader.tds
class HelloMod(loader.Module):
    """Минимальный модуль-пример: одна команда и переводимые строки"""

    strings = {
        "name": "HelloMod",
        "hello_msg": "Привет, мир! 🌍",
        "hello_user": "Привет, <b>{name}</b>!",
    }

    strings_ru = {"hello_msg": "Привет, мир! 🌍"}

    @loader.command(alias="hi")
    async def hello(self, message: Message):
        """- поздороваться"""
        args = utils.get_args(message)

        if args:
            await utils.answer(
                message, self.strings("hello_user").format(name=" ".join(args))
            )
        else:
            await utils.answer(message, self.strings("hello_msg"))
