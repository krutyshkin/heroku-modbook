# 🧩 Примеры модулей

Рабочие шаблоны external-модулей для Heroku Userbot. Каждый файл — самодостаточный
`.py`, ставится одной командой:

```
.dlmod https://github.com/krutyshkin/heroku-modbook/blob/main/examples/<name>.py
```

| Файл | Что показывает |
|---|---|
| [`hello.py`](hello.py) | **Минимум.** Одна команда, переводимые строки, алиас. |
| [`template_full.py`](template_full.py) | **Полный набор.** Конфиг с валидаторами, pointer-БД, watcher с фильтрами, lifecycle-хуки (`client_ready`, `on_unload`), `SelfUnload`. |

## Как тестировать локально

1. Поднять юзербот: см. [CONTRIBUTING.md](../CONTRIBUTING.md#🧪-как-проверить-модуль-локально).
2. Залить модуль в свой fork или дать прямую ссылку на raw.
3. `.dlmod <url>` → проверить `.help <ModName>`.
4. Релоад — повторным `.dlmod` по той же ссылке.

## Анатомия модуля

```
# requires: <pip>      ← автоустановка зависимостей
# meta developer: @x   ← автор
# scope: heroku_min X  ← минимальная версия юзербота

@loader.tds                    ← переводимые докстринги
class MyMod(loader.Module):
    """Описание"""             ← попадёт в .help
    strings = {"name": "..."}  ← имя модуля + строки
    def __init__(self): ...    ← self.config
    async def client_ready(self): ...
    @loader.command() / @loader.watcher(...) / @loader.loop(...)
    async def on_unload(self): ...
```

Подробно — в [docs/writing-a-module.md](../docs/writing-a-module.md).
