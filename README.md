<div align="center">

# 🪐 Heroku Userbot — Module Development Docs

**Неофициальная рабочая документация по разработке кастомных модулей для
[Heroku Userbot](https://github.com/coddrago/Heroku)**

Продвинутый Telegram-юзербот на Python (форк Hikka, слой Telethon → `herokutl`).
Здесь собрана выверенная по официальной dev-доке SunnexGB и исходникам ядра информация
о том, как писать, конфигурить и публиковать собственные модули.

</div>

---

<p align="center">
  <a href="#-быстрый-старт">Быстрый старт</a> •
  <a href="#-структура-репозитория">Структура</a> •
  <a href="#-документация">Документация</a> •
  <a href="#-примеры">Примеры</a> •
  <a href="#-статус-источника">Статус доки</a>
</p>

---

## ✨ О чём это

`coddrago/Heroku` — юзербот с повышенной безопасностью и современными функциями.
Модульная архитектура позволяет расширять его одной командой `.dlmod` без правки
ядра. Этот репозиторий — **шпаргалка и справочник для разработчиков модулей**:
декораторы, lifecycle-хуки, конфиг, БД, inline, sandbox, полный референс core-модулей
и готовые шаблоны.

> ⚠️ Дока — неофициальная. Основана на dev-доке
> [sunnexgb.github.io/Heroku-documentations-md](https://sunnexgb.github.io/Heroku-documentations-md/)
> и сверенa с исходным кодом ядра `coddrago/Heroku`.

## 🚀 Быстрый старт

Минимальный модуль — это Python-файл с классом-наследником `loader.Module`:

```python
# requires: aiohttp
# meta developer: @your_username
# scope: heroku_min 1.5.0

from herokutl.tl.types import Message
from heroku import loader, utils


@loader.tds
class HelloMod(loader.Module):
    """Привет-модуль"""

    strings = {"name": "HelloMod", "hi": "Привет, 🌍"}

    @loader.command(alias="h")
    async def hello(self, message: Message):
        """- поздороваться"""
        await utils.answer(message, self.strings("hi"))
```

Загрузка в юзербот:
```
.dlmod https://github.com/krutyshkin/heroku-modbook/blob/main/examples/hello.py
```

Релоад — повторным `.dlmod` по той же ссылке. Готовые шаблоны — в [`examples/`](examples).

## 📂 Структура репозитория

```
heroku-modbook/
├── README.md              ← этот файл
├── CONTRIBUTING.md        ← как контрибьютить / обновлять доку
├── LICENSE                ← AGPL-3.0 (как и сам Heroku)
├── .gitignore
├── docs/                   ← документация
│   ├── writing-a-module.md    📘 главный мануал: как написать модуль
│   ├── core-modules.md         🧩 референс всех встроенных модулей и команд
│   ├── api-reference.md        ⚡ быстрый референс декораторов/API
│   ├── customization.md        🎨 плейсхолдеры для info/ping/help
│   ├── creds.md                🔑 создание api_id и api_hash
│   ├── digital-garden.md       🌿 модуль DigitalGarden + dg-теги
│   ├── status.md               📡 статус источников дока-сайта
│   └── heroku-readme-ru.md     README_RU самого юзербота (референс)
├── examples/               ← рабочие шаблоны external-модулей
│   ├── README.md               оглавление + анатомия модуля
│   ├── hello.py                минимальный модуль
│   └── template_full.py       полный: конфиг + БД + watcher + lifecycle
└── source/                ← исходники ядра (первоисточник, только для чтения)
    ├── loader.py             декораторы, Modules, InfiniteLoop, sandbox
    ├── types.py              Module, Library, ModuleConfig, ConfigValue, Safe-прокси
    ├── validators.py         все валидаторы конфига
    ├── database.py           БД: get/set/pointer/save
    ├── modules_loader.py     LoaderMod: .dlmod/.loadmod/load_module
    ├── modules_test.py       TestMod — эталонный пример модуля
    ├── modules_inline_stuff.py  watchers + inline-галерея
    └── utils_messages.py     utils.answer и хелперы
```

## 📚 Документация

| Документ | Что внутри |
|---|---|
| [docs/writing-a-module.md](docs/writing-a-module.md) | 📘 **Главный мануал** — скелет, декораторы, теги, валидаторы, БД, lifecycle, чеклист |
| [docs/core-modules.md](docs/core-modules.md) | 🧩 **Core Modules** — все встроенные модули и команды (Loader, Tester, Updater, Security …) |
| [docs/api-reference.md](docs/api-reference.md) | ⚡ Быстрый референс — сигнатуры декораторов/API под рукой |
| [docs/customization.md](docs/customization.md) | 🎨 Кастомизация info/ping/help через плейсхолдеры |
| [docs/creds.md](docs/creds.md) | 🔑 Создание api_id и api_hash |
| [docs/digital-garden.md](docs/digital-garden.md) | 🌿 Модуль DigitalGarden + dg-теги |
| [docs/status.md](docs/status.md) | 📡 Статус источников дока-сайта |

## 🧩 Примеры

| Пример | Что показывает |
|---|---|
| [examples/hello.py](examples/hello.py) | Минимум: одна команда + переводимые строки |
| [examples/template_full.py](examples/template_full.py) | Полный набор: конфиг, pointer-БД, watcher, lifecycle, `on_unload` |

## 📡 Статус источников

- ✅ **[sunnexgb.github.io/Heroku-documentations-md](https://sunnexgb.github.io/Heroku-documentations-md/)**
  — рабочая статическая дока, на ней основаны все мануалы этого репо.
- ⚠️ **dev.heroku-ub.xyz** — SPA (пустой HTML, JS-рендер, защита от ботов), фетчерами
  не достаётся. Подробности — в [docs/status.md](docs/status.md).
- 🔧 **Исходный код ядра** `coddrago/Heroku` — первичный источник верификации.

## 🔗 Ссылки

- **Ядро юзербота:** https://github.com/coddrago/Heroku
- **Оригинал dev-доки (рабочая):** https://sunnexgb.github.io/Heroku-documentations-md/
- **Дока-сайт (SPA):** https://dev.heroku-ub.xyz/
- **Пользовательская дока:** https://heroku-ub.xyz/
- **Чат:** https://t.me/heroku_talks

## 📄 Лицензия

Распространяется под **AGPL-3.0** (как и сам Heroku Userbot). См. [LICENSE](LICENSE).

<div align="center">
<sub>Неофициальная документация. Все товарные знаки принадлежат их владельцам.</sub>
</div>
