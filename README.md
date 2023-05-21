<div align="center">
    <img src="asset/logo_appium.png" alt="APPIUM">
</div>

---

<h1 align="center"> Appium UI auto-test </h1>

An example of how you can automate mobile device testing in Python using a framework
[Appium](https://github.com/appium/appium).
The sample app is being used as a test app
[todo](https://github.com/android/architecture-samples) is available on GitHub.

---

<h1 align="center">Launch</h1>

First, install the dependencies:
* [Appium-Python-Client](https://pypi.org/project/Appium-Python-Client/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)

```
pip install -r requirements.txt
```

We run the `make start` command to create the `.env` file that needs to be populated and the `settings.json` file.

```
make start
```

Run the tests with the following command:
```
python3 main.py
```
You can also run tests with the `make run` command
```
make run
```


---

<h1 align="center">Project structure</h1>

```
SimpleAutoTestUI/
├── asset/
│   └── ...
├── src/
│   ├── locators/
│   │   └── ... 
│   ├── pages/
│   │   └── ...
│   ├── tests/
│   │   └── ... 
│   └── utils/
│       │── ...
│       └── ...
└── main.py
```

## asset/
The directory where the resources (such as images) are located.

## src/
The directory that contains the project's source code. It includes several subdirectories:
1. **locators/** - This directory contains files with interface element locators (for example, identifiers, names, paths).
2. **pages/** - This directory contains files that represent each screen of the application.
3. **tests/** - This directory contains tests.
4. **utils/** - This directory contains auxiliary files and modules.

## main.py
main project file.
