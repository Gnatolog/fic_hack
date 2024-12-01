# Используем официальный образ Python
FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /app_fic

# Копируем файлы зависимостей
COPY requirements.txt /app_fic/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в рабочую директорию
COPY  fic/ /app_fic/

# Открываем порт 50000
EXPOSE 50000

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:50000"]
