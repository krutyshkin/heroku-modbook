# requires: aiohttp
# meta developer: @your_username
# scope: heroku_min 1.5.0
# Полный шаблон external-модуля: конфиг, БД, watcher, lifecycle, on_unload.

from herokutl.tl.types import Message

from heroku import loader, utils


@loader.tds
class TemplateMod(loader.Module):
    """Шаблон модуля со всем набором фичей"""

    strings = {
        "name": "TemplateMod",
        "started": "✅ Модуль запущен",
        "count": "Счётчик: <b>{n}</b>",
        "unloaded": "👋 Модуль выгружен",
    }

    def __init__(self):
        self._counter = 0
        self._users = None  # будет pointer'ом

        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "enabled",
                True,
                "Включить модуль",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "prefix",
                "[TM]",
                "Префикс для логов в watcher'е",
                validator=loader.validators.String(),
            ),
            loader.ConfigValue(
                "auto_inc",
                False,
                "Авто-инкремент счётчика на каждое твоё сообщение",
                validator=loader.validators.Boolean(),
            ),
        )

    async def client_ready(self):
        # pointer на список в БД — авто-персист при .append / .remove
        self._users = self.pointer("users", [])

        if not self.config["enabled"]:
            raise loader.SelfUnload("Модуль выключен в конфиге")

        await self.client.send_message(self.tg_id, self.strings("started"))

    @loader.command()
    async def count(self, message: Message):
        """- показать счётчик"""
        self._counter += 1
        self.set("counter", self._counter)
        await utils.answer(message, self.strings("count").format(n=self._counter))

    @loader.command()
    async def adduser(self, message: Message):
        """<reply> - добавить пользователя в локальный список"""
        if not (reply := message.reply_to_msg_id):
            await utils.answer(message, "Ответь на сообщение пользователя")
            return

        if reply not in self._users:
            self._users.append(reply)
            await utils.answer(message, "Добавлен ✅")
        else:
            await utils.answer(message, "Уже в списке")

    @loader.watcher("out", "only_messages")
    async def watcher(self, message: Message):
        """Логирует твои исходящие сообщения, если включён auto_inc"""
        if not self.config["auto_inc"]:
            return

        self._counter += 1
        # не отвечаем тут — watcher просто считает

    async def on_unload(self):
        # Чистим ресурсы перед выгрузкой / релоадом.
        # Здесь можно закрыть соединения, остановить свои таски и т.п.
        self._counter = 0
