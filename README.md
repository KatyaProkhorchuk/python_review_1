# Bash <br>
>***Клонировать репозиторий*** git clone git@github.com:KatyaProkhorchuk/python_review_1.git<br>
cd python_review_1 <br>
pip freeze -r requirements.txt <br>
***Для запуска программы*** python3 main.py<br>
***Для запуска тестов*** PYTHONPATH=src python -m pytest --cov=shell --cov-report=html tests.py
# 
> **Функционал**<br>
* ls. Вывести список файлов и директорий для текущей директории <br>
* pwd. Вывести полный путь для текущей директории <br>
* cd <путь>. Переход по относительному или абсолютному пути <br>
* cp <имя файла> <имя файла>. Скопировать файл <br>
* mv <имя файла> <имя файла>. Переместить файл <br>
* rm <имя файла>. Удалить файл <br>
* rmdir <имя директории>. Удалить директорию в случае, если она пуста <br>
* mkdir <имя директории>. Создать директорию, если ее не было <br>
* run <путь к исполняемому файлу> <аргументы> <br>
  **Example:** run echo 'hello' <br>
* exit Выход
