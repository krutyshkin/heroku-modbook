# 🎨 Кастомизация info/ping/help (плейсхолдеры)

> 📍 [README](../README.md) → **Документация** → Кастомизация
> · соседние: [Core Modules](core-modules.md) · [Как написать модуль](writing-a-module.md)

> По официальной dev-доке `sunnexgb.github.io/Heroku-documentations-md`
> (Guide for custom your Heroku).

Гайд для кастомизации info/ping/help и вообще всего, что угодно. Помогут
**плейсхолдеры** — ключевые слова, которые подставляются в `custom_message`.

## Дефолтные плейсхолдеры

| Плейсхолдер | Что отображает |
|---|---|
| `{me}` | ваш ник в ТГ |
| `{version}` | текущая версия юзербота |
| `{build}` | номер билда (номер коммита) |
| `{prefix}` | префикс команд (например `.` или `!`) |
| `{platform}` | хост (wds / userland / docker) |
| `{upd}` | информация об обновлениях |
| `{uptime}` | время непрерывной работы юзербота |
| `{cpu_usage}` | текущая нагрузка на процессор (%) |
| `{ram_usage}` | объём занятой оперативной памяти |
| `{branch}` | текущая ветка (например `main` или `dev`) |
| `{hostname}` | сетевое имя сервера |
| `{user}` | имя пользователя в системе |
| `{os}` | название ОС (например `Ubuntu`) |
| `{kernel}` | версия ядра дистрибутива |
| `{cpu}` | данные о процессоре (например `6 (12) core(-s); 11.9% total`) |
| `{ping}` | ваш текущий пинг |

## Как применить

1. Обычным сообщением напишите в **Избранное** шаблон, например:

   ```
   {user}@debian
   ━━━━━━━━━━━━━━━━━━━━━━━━
   OS : {os}
   Ver : {version} ({branch}@{build})
   Up : {uptime}
   RAM : {ram_usage}
   Load : {cpu_usage}%
   Ping : {ping}ms
   ━━━━━━━━━━━━━━━━━━━━━━━━
   ⚙️| CPU : {cpu}
   ⚪️| Update : {upd}
   ```

2. Скиньте это сообщение в чат и в ответ на него напишите `.e r.text` — получите
   текст с HTML-разметкой:
   ```
   {user}@debian
   ━━━━━━━━━━━━━━━━━━━━━━━━
   OS     : {os}
   Ver    : {version} ({branch}@{build})
   Up     : {uptime}
   RAM    : {ram_usage}
   Load   : {cpu_usage}%
   Ping   : {ping}ms
   ━━━━━━━━━━━━━━━━━━━━━━━━
   ⚙️| CPU : {cpu}
   ⚪️| Update : {upd}
   ```

3. Примените через `.fconfig <модуль> <параметр> <текст>`:
   - для info: `.fcfg HerokuInfo custom_message <шаблон>`
   - для ping: `.fcfg Tester custom_message <шаблон>`

## Пример применения

```
.fcfg HerokuInfo custom_message {user}@debian ━━━━━━━━━━━━━━━━━━━━━━━━ OS : {os} Ver : {version} ({branch}@{build}) Up : {uptime} RAM : {ram_usage} Load : {cpu_usage}% Ping : {ping}ms ━━━━━━━━━━━━━━━━━━━━━━━━ ⚙️ | CPU : {cpu} ⚪️ | Update : {upd}
```

> Плейсхолдеры работают в `custom_message` модулей **HerokuInfo**, **Tester** (ping)
> и других, где поддерживается этот параметр.

*Гайд по официальной dev-доке SunnexGB.*
