# 📡 Статус источника `dev.heroku-ub.xyz` и `sunnexgb.github.io`

> 📍 [README](../README.md) → **Документация** → Статус источника
> · соседние: [Core Modules](core-modules.md) · [Как написать модуль](writing-a-module.md)

## Что здесь

Дока и сниппеты для разработки кастомного модуля под **Heroku Userbot**
(`coddrago/Heroku` — форк Hikka, Python, Telethon-стек `herokutl`).

## Источники документации

### 1. `dev.heroku-ub.xyz` (официальная dev-дока)

Сайт — это **SPA** (пустой HTML, контент рендерится через JS + защита от ботов).
Ни один фетчер не пробил:
- `WebFetch` → `TLSV1_ALERT_UNRECOGNIZED_NAME` (SNI режется).
- 9Router `tavily` / `exa` → пустой контент на всех подстраницах.
- Прямой `curl` с браузерным UA → 0 байт.
- Wayback Machine — снимок есть, но пустая SPA-оболочка (4кб).

### 2. `sunnexgb.github.io/Heroku-documentations-md` ✅ доступна

Рабочая статическая дока (mkdocs/material), фетчится нормально. На ней основаны
все мануалы в этом репозитории:

| Страница оригинала | Документ в репо |
|---|---|
| [Quickstart Development](https://sunnexgb.github.io/Heroku-documentations-md/quickstart-development/) | [writing-a-module.md](writing-a-module.md) |
| [Heroku Core Modules](https://sunnexgb.github.io/Heroku-documentations-md/heroku-core-modules/) | [core-modules.md](core-modules.md) |
| [Как создать свои CREDS](https://sunnexgb.github.io/Heroku-documentations-md/kak-sozdat-svoi-creds/) | [creds.md](creds.md) |
| [Guide for custom your Heroku](https://sunnexgb.github.io/Heroku-documentations-md/guide-for-custom-your-heroku/) | [customization.md](customization.md) |
| [Guide for DigitalGarden module](https://sunnexgb.github.io/Heroku-documentations-md/guide-for-digital-garden-module/) | [digital-garden.md](digital-garden.md) |

### 3. Исходный код ядра `coddrago/Heroku`

Первичный источник для верификации — клон репозитория. Все спорные места
(импорт `Message`, сигнатуры валидаторов, декораторы) сверены с кодом ядра.

## Верификация

- **Импорт `Message`**: в доке `from herokutl.types import Message` (без `.tl`),
  но все core-модули ядра пишут `from herokutl.tl.types import Message` (с `.tl`).
  Оба работают (re-export), но канон — с `.tl`. В мануалах репо — каноничный вариант.
- **Валидатор `Integer`**: принимает `minimum`, `maximum`, `digits` — свёрено с
  `heroku/validators.py`.
- **Команды core-модулей**: свёрены с `heroku/modules/*.py` (LoaderMod, Tester,
  Updater и т.д.) — см. [core-modules.md](core-modules.md).

## Ссылки

- Репо ядра: https://github.com/coddrago/Heroku
- Польз. дока: https://heroku-ub.xyz/
- Дев-дока (SPA, фетчерами не достаётся): https://dev.heroku-ub.xyz/
- Dev-docs (рабочая): https://sunnexgb.github.io/Heroku-documentations-md/quickstart-development/
- Чат: https://t.me/heroku_talks
