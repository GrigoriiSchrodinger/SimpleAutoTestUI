start:
	@CREATED=false; \
    if [ -e .env ]; then \
        echo "File .env already exists"; \
    else \
        echo "# appium server settings" > .env; \
        echo "APPIUM_HOST=127.0.0.1" >> .env; \
        echo "APPIUM_PORT=4723" >> .env; \
        echo "" >> .env; \
        echo "# device settings" >> .env; \
        echo "VERSION=Версия_устройства" >> .env; \
        echo "NAME_DEVICE='Название вашего устройства'" >> .env; \
        CREATED=true; \
    fi >/dev/null; \
    if [ "$$CREATED" = true ]; then \
        echo "\033[0;33mВнимание! был создан .env файл. Заполните его пожалуйста перед запускам тестов\033[0m"; \
    fi
