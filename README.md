<div align="center">
    <img src="asset/logo_appium.png" alt="APPIUM">
</div>

---

<h1 align="center"> Appium UI auto-test </h1>

Пример того, как можно автоматизировать тестирование мобильных устройств на Python при помощи фреймворка 
[Appium](https://github.com/appium/appium).
В качестве тестового приложения используется пример приложения 
[todo](https://github.com/android/architecture-samples), доступный GitHub.

---

<h1 align="center">Запуск</h1>

Для начала устанавливаем зависимости: 
* [Appium-Python-Client](https://pypi.org/project/Appium-Python-Client/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)

```
pip install -r requirements.txt
```

Запускаем команду `make start`, чтобы создать файл `.env`, который необходимо заполнить, и файл `settings.json`.

```
make start
```

Запустите тесты следующей командой:
```
python3 main.py
```
Также можно запустить тесты через команду `make run`
```
make run
```


---

<h1 align="center">Структура проекта </h1>

```
SimpleAutoTestUI/
├── asset/
│   └── ...
├── src/
│   ├── locators/
│   │   └── страницы с локаторами 
│   ├── pages/
│   │   └── страницы с экранами приложения 
│   ├── tests/
│   │   └── тесты 
│   └── utils/
│       │── конфиги
│       └── настройки
└── main.py
```

## asset/
Директория, в которой находятся ресурсы (например, изображения).

## src/
Директория, которая содержит исходный код вашего проекта. Она включает в себя несколько поддиректорий:
1. **locators/** - В этой директории содержатся файлы с локаторами элементов интерфейса (например, идентификаторы, имена, пути).
2. **pages/** - Эта директория содержит файлы, которые представляют каждый экран приложения.
3. **tests/** - В этой директории содержатся тесты.
4. **utils/** - Эта директория содержит вспомогательные файлы и модули.

## main.py
Основной файл проекта.
