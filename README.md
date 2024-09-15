# Визуализация Баллистического Движения

Данный проект моделирует и визуализирует баллистическое движение тела, брошенного под углом. Программа использует библиотеку `matplotlib` для создания графиков траектории движения, а также зависимости скорости и координат от времени.

## 📄 Содержание

- [Обзор](#обзор)
- [Функции](#функции)
- [Установка](#установка)
- [Использование](#использование)
- [Пример](#пример)
- [Создание исполняемого файла](#создание-исполняемого-файла)
- [Зависимости](#зависимости)
- [Лицензия](#лицензия)

## 📌 Обзор

Программа моделирует движение тела, брошенного с определенной высоты с заданной начальной скоростью и углом. Она игнорирует сопротивление воздуха и следует основным уравнениям движения по параболе.

### Входные данные:
- Высота, с которой брошено тело.
- Начальная скорость.
- Угол броска (в градусах).

### Вывод программы:
1. График траектории движения тела.
2. Графики зависимости скорости от времени, а также координат X и Y от времени.

## 🚀 Функции

- Моделирование баллистического движения в 2D.
- Визуализация графиков:
  - Траектории тела.
  - Скорости по времени.
  - Координат X и Y по времени.
- Простой интерфейс для ввода данных.

## ⚙️ Установка

Для запуска программы на вашем компьютере выполните следующие шаги:

1. **Клонирование репозитория**:
    ```bash
    git clone <ссылка_на_репозиторий>
    cd ballistic_motion_visualizer
    ```

2. **Установка необходимых библиотек**:
    Убедитесь, что у вас установлен Python 3. Для установки зависимостей используйте `pip`:
    ```bash
    pip install -r requirements.txt
    ```

    Если файл `requirements.txt` отсутствует, установите библиотеки вручную:
    ```bash
    pip install matplotlib numpy
    ```

3. **Запуск программы**:
    ```bash
    python main.py
    ```

## 💻 Использование

После запуска программы вам будет предложено ввести следующие параметры:
- **Начальная высота** (в метрах) – высота
