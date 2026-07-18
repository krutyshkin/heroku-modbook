# ⚡ Карта API (быстрый референс)

> 📍 [README](../README.md) → **Документация** → Карта API
> · соседние: [Как написать модуль](writing-a-module.md) · [Core Modules](core-modules.md)

Форк `Hikka` → `coddrago/Heroku`. Telethon-слои переименованы: `telethon` → `herokutl`,
`hikka` → `heroku`. Лоадер патчит `__import__`, так что в core-модулях можно писать
`from telethon...` / `from hikka...` — автоматически перепишется. Но чище — сразу
`from herokutl...` / `from heroku...`.

## Импорты

```python
# Core-модуль (в heroku/modules/):
from herokutl.tl.types import Message
from .. import loader, main, utils
from ..inline.types import InlineCall

# External-модуль (.dlmod):
from herokutl.tl.types import Message
from heroku import loader, utils
from heroku.inline.types import InlineCall
```

## Декораторы (`loader.*`)

| Декоратор | Назначение |
|---|---|
| `@loader.tds` | На классе. Делает докстринги переводимыми. |
| `@loader.command(alias=..., aliases=[...])` | Команда. Имя = имя метода. Поддерживает [теги фильтрации](writing-a-module.md#полный-список-тегов) (`only_pm`, `only_photos`, `from_id`, …). |
| `@loader.watcher(*tags, **kw)` | Ватчер сообщений. Имя метода любое, регистрируется под ключом из имени. |
| `@loader.inline_handler()` | Inline-хендлер. Имя `*_inline_handler`. |
| `@loader.callback_handler()` | Callback кнопки. Имя `*_callback_handler`. |
| `@loader.raw_handler(*UpdateType)` | Сырые Telethon-апдейты. |
| `@loader.loop(interval, autostart, wait_before, stop_clause)` | Бесконечный цикл. |
| `@loader.tag(*tags, **kw)` | Тегирование (в основном для watcher). |
| `@loader.ratelimit` | Ужесточить рейд-лимит команды. |
| `@loader.debug_method(name)` | Internal Debug Method. |

## Lifecycle

```
__init__  →  config_complete  →  client_ready  →  [работа]  →  on_unload
                (config из БД)     (клиент готов)              (релоад/выгрузка)
                                   ↑ поднимай LoadError / SelfUnload / SelfSuspend
```
`on_dlmod` — только при первой установке через `.dlmod`/`.loadmod`.

## `self.*` (после `internal_init`)

| Атрибут | Тип/назначение |
|---|---|
| `self.client`, `self._client` | Telethon-клиент |
| `self.allclients` | Все клиенты (мультиаккаунт) |
| `self.db`, `self._db` | База данных |
| `self.allmodules` | Реестр модулей |
| `self.inline` | InlineManager |
| `self.tg_id`, `self._tg_id` | Твой ID |
| `self.lookup(name)` | Найти модуль по имени |
| `self.get_prefix()` | Префикс (по умолч. `.`) |
| `self.translator` | Транслятор |
| `self.strings` | Строки: `self.strings("key")` / `self.strings["key"]` |
| `self.is_external` | True если external |

## БД (через `self`)

```python
self.get(key, default=None)              # чтение
self.set(key, value)                     # запись (str/int/float/bool/list/dict/None)
self.pointer(key, default, item_type)   # auto-persist список/словарь
# напрямую:
self._db.get(owner, key, default)
self._db.set(owner, key, value)
self._db.pointer(owner, key, default)
```
Неймспейс для `self.get/set/pointer` — `self.__class__.__name__`.

## Команды

```python
@loader.command(alias="p")
async def ping(self, message: Message):
    """- пинг"""           # докстринг → в .help
    args = utils.get_args(message)          # список аргументов
    raw  = utils.get_args_raw(message)      # строкой
    chat = utils.get_chat_id(message)
    await utils.answer(message, f"pong {args}")
```

## Ответы (`utils.answer`)

```python
await utils.answer(message, "Текст")
await utils.answer(message, "https://x.com/p.jpg", caption="...", asfile=True)
await utils.answer(message, "Текст", reply_markup=[
    {"text": "OK", "callback": self.cb, "args": (1,)},
    {"text": "X", "action": "close"},
])
```
`utils.answer` сам решает: отредактировать твоё сообщение или послать новое.

## Inline (`self.inline`)

```python
await self.inline.form(
    message=message,
    text="Заголовок",
    reply_markup=[[{"text":"OK","callback":self.cb}]],
    photo="...", gif="...", file="...",
    ttl=300, force_me=False, disable_security=False,
    silent=True,
)
# list / gallery / query_gallery — для сложных UI
```

## Конфиг

```python
self.config = loader.ModuleConfig(
    loader.ConfigValue("k", "def", "doc",
        validator=loader.validators.String(),
        on_change=self._cb, folder="Grp"),
)
val = self.config["k"]              # чтение
self.config.set_no_raise("k", "v")  # программная установка
```

## Валидаторы (`loader.validators.*`)

`Boolean`, `Integer(minimum=, maximum=, digits=)`, `Float`, `String`, `Choice([...])`,
`MultiChoice([...])`, `Series`, `Link`, `RegExp(pattern)`, `TelegramID`, `Union(...)`,
`Hidden`, `Emoji`, `EntityLike`, `RandomLink`, `RandomLinkList`.

Свой валидатор — наследник `Validator` (см. [writing-a-module.md](writing-a-module.md#свой-валидатор)).

## Загрузка/выгрузка (команды пользователя)

Полный список — в [core-modules.md → Loader](core-modules.md#loader--загрузка-и-управление-внешними-модулями).
Кратко: `.dlmod`/`.loadmod`/`.unloadmod`/`.addrepo`/`.delrepo`/`.clearmodules`/`.ml`.

## Спецкомментарии шапки

`# requires: <pip pkgs>` · `# packages: <apt pkgs>` · `# meta developer: @x`
· `# scope: heroku_min X.Y.Z` · `# scope: inline` · `# scope: ffmpeg`
· `# scope: no_stats` · `# packurl: <url>`
