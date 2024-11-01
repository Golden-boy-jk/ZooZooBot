from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot_instance import bot  # Импортируем bot из bot_instance
import random



router = Router()

# Список тотемных животных и их изображения
animals = {

    "Волк": {
    "image": "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/a26086b0-53a3-452a-8552-5f5cef835879.jpg",
    "info_url": "https://moscowzoo.ru/animals/kinds/evropeyskiy_volk"
    },

    "Медведь": {
    "image": "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/22c1783b-0644-434d-9b35-2143c5505033.jpeg",
    "info_url": "https://moscowzoo.ru/about/articles/belye_medvedicy_moskovskogo_zooparka"
    },

    "Сова": {
    "image": "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/e2f19554-2ab4-453e-b796-a2e975d8090d.jpg",
    "info_url": "https://moscowzoo.ru/animals/kinds/belaya_sova"
    },

    "Амурский тигр":{
    "image": "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/71062cdc-ae27-432a-84ed-d3743afd903b.jpeg",
    "info_url": "https://moscowzoo.ru/animals/kinds/amurskiy_tigr"
    },

    "Азиатский слон":{
    "image": "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/61108d03-9845-4183-97a0-2c6c74c29fbb.jpeg",
    "info_url": "https://moscowzoo.ru/animals/kinds/aziatskiy_slon"
    },

    "Александрийский попугай":{
    "image": "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/3d4b82db-4161-421c-8f50-902b0f3b0240.jpg",
    "info_url": "https://moscowzoo.ru/animals/kinds/aleksandriyskiy_popugay"
    },

    "Ёж":{
    "image": "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/01029a4c-4998-4104-bddb-de67d21dea54.jpeg",
    "info_url": "https://moscowzoo.ru/animals/kinds/belogrudyy_ezh"
    },

    "Бинтуронг":{
    "image": "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/83e76f49-856e-4330-a472-b6f1c92da16c.jpg",
    "info_url": "https://moscowzoo.ru/animals/kinds/binturong"
    },

    "Бык Хайленд": {
    "image": "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/75633f66-613c-400e-a908-77ae1d58b7ce.jpeg",
    "info_url": "https://moscowzoo.ru/animals/kinds/byk_haylend"
    },

    "Дальневосточный лесной кот":{
    "image": "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/a8f282a3-2f11-4acc-96e0-e6dd998fdc23.png",
    "info_url": "https://moscowzoo.ru/animals/kinds/dalnevostochnyy_lesnoy_kot"
    },

    "Муравьед":{
    "image": "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/1c730d7d-6448-49ad-aa68-d5a7931a50a5.jpg",
    "info_url": "https://moscowzoo.ru/animals/kinds/chetyrehpalyy_muraved_tamandua"
    },

    "Кайман": {
    "image": "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/e59ebce3-d14e-4947-b94c-e2154fc38539.jpeg",
    "info_url": "https://moscowzoo.ru/animals/kinds/gladkolobyy_kayman"
    },
}

last_animal = None
last_result_text = None

# Стартовое сообщение
@router.message(Command(commands=['start']))
async def start_quiz(message: types.Message):
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Начать викторину")]], resize_keyboard=True)
    await message.reply(
        "Добро пожаловать, храбрый защитник нашей планеты! "
        "Готов ли ты узнать, какое тотемное животное скрыто в твоей душе? "
        "Давай погрузимся в удивительный мир Московского зоопарка!",
        reply_markup=keyboard
    )

# Обработка нажатия на "Начать викторину"
@router.message(F.text == "Начать викторину")
async def question_one(message: types.Message):
    question = "Давай раскроем тайны твоего темперамента! Как бы ты описал свою внутреннюю сущность"
    options = ["Спокойный", "Энергичный", "Добрый и немного стеснительный", "Строгий", "Отзывчивый",
               "Общительный", "Дружелюбный", "Жизнерадостный", "Оптимистичный", "Решительный",
               "Настойчивый", "Целеустремлённый", "Терпеливый", "Внимательный", "Тактичный",
               "Мягкий", "Гибкий", "Организованный", "Ответственный", "Надёжный", "Творческий",
               "Изобретательный", "Сообразительный", "Любознательный", "Чувствительный",
               "Эмоциональный", "Впечатлительный"]
    keyboard = []
    for i in range(0, len(options), 2):
        row = []
        row.append(KeyboardButton(text=options[i]))  # Добавляем первую кнопку в строку
        if i + 1 < len(options):  # Проверяем, чтобы не выйти за пределы списка
            row.append(KeyboardButton(text=options[i + 1]))  # Добавляем вторую кнопку в строку
        keyboard.append(row)  # Добавляем строку в клавиатуру

    keyboard_markup = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )

    await message.reply(question, reply_markup=keyboard_markup)

# Обработка первого ответа и переход к следующему вопросу
@router.message(F.text.in_({"Спокойный", "Энергичный", "Добрый и немного стеснительный", "Строгий", "Отзывчивый",
               "Общительный", "Дружелюбный", "Жизнерадостный", "Оптимистичный", "Решительный",
               "Настойчивый", "Целеустремлённый", "Терпеливый", "Внимательный", "Тактичный",
               "Мягкий", "Гибкий", "Организованный", "Ответственный", "Надёжный", "Творческий",
               "Изобретательный", "Сообразительный", "Любознательный", "Чувствительный",
               "Эмоциональный", "Впечатлительный"}))
async def question_two(message: types.Message):
    question = "Представь, что ты в гастрономическом раю! Какие лакомства радуют твой вкус"
    options = ["Сладкие дары тропиков", "Зеленые спутники фруктов" "Мясные наслаждения и морские деликатесы",
               "Сладкие искушения и хрустящие лакомства", "Питаюсь свежестью зеленых просторов",
               "Я не ем, а грызу гранит", "Мое сердце отдано древесным блюдам",
               "Иногда хочется экзотики(жучки и червячки)",
               "Хрум-хрум", "Нежные дары молочного королевства"]
    keyboard = []
    for i in range(0, len(options), 2):
        row = []
        row.append(KeyboardButton(text=options[i]))  # Добавляем первую кнопку в строку
        if i + 1 < len(options):  # Проверяем, чтобы не выйти за пределы списка
            row.append(KeyboardButton(text=options[i + 1]))  # Добавляем вторую кнопку в строку
        keyboard.append(row)  # Добавляем строку в клавиатуру

    keyboard_markup = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )

    await message.reply(question, reply_markup=keyboard_markup)

# Завершение викторины и вывод результата с изображением
@router.message(F.text.in_({"Сладкие дары тропиков", "Зеленые спутники фруктов" "Мясные наслаждения и морские деликатесы",
               "Сладкие искушения и хрустящие лакомства", "Питаюсь свежестью зеленых просторов",
               "Я не ем, а грызу гранит", "Мое сердце отдано древесным блюдам",
               "Иногда хочется экзотики(жучки и червячки)",
               "Хрум-хрум", "Нежные дары молочного королевства"}))
async def show_result(message: types.Message):
    global last_animal, last_result_text
    # Случайный выбор тотемного животного и его изображение и информация
    last_animal, animal_info = random.choice(list(animals.items()))
    image_url = animal_info["image"]
    info_url = animal_info["info_url"]

    last_result_text = (f"Твое тотемное животное – {last_animal}! "
                        f"Вы энергичный и независимый, как {last_animal}. "
                        f"Ты обладаешь энергией и независимостью, словно это великолепное создание. "
                        f"Ты ценишь близость с родными и дружбу, как истинный защитник природы!.\n\n"
                        f"Узнать больше о {last_animal}: {info_url}")

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Поделиться в социальных сетях"),
                KeyboardButton(text="Намекнуть сотруднику Zоопарка")
            ],
            [
                KeyboardButton(text="Попробовать ещё раз?"),
                KeyboardButton(text="Узнать больше о программе опеки")
            ],
            [
                KeyboardButton(text="Оставить отZооВ")
            ]
        ],
        resize_keyboard=True
    )
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=image_url,
        caption=last_result_text,
        reply_markup=keyboard
    )

# Поделиться в социальных сетях
@router.message(F.text == "Поделиться в социальных сетях")
async def share_result(message: types.Message):
    await message.reply(
        "Вы можете поделиться своим результатом, скопировав текст ниже и отправив его в социальных сетях:\n\n"
        "Узнал своё тотемное животное в Московском зоопарке! Присоединяйтесь к викторине @Zoo_parkMoscow_bot!"
    )

# Связаться с сотрудником зоопарка
@router.message(F.text == "Намекнуть сотруднику Zоопарка")
async def contact_staff(message: types.Message):
    global last_result_text
    result_text = last_result_text if last_result_text else "Результат не найден."
    await message.reply(
        "Для связи с сотрудником Московского Zоопарка, "
        "вы можете написать на support@moscowzoo.ru или помяукать по телефону +7 (495) 123-45-67."
        "Рычать и мычать можно, главное найти общий язык "
        f"Ваш результат: {result_text}"
    )

@router.message(F.text == "Оставить отZooВ")
async def collect_feedback(message: types.Message):
    await message.reply(
        "Мы всегда стремимся улучшить ваш опыт! "
        "Пожалуйста, оставьте отзыв на feedback@moscowzoo.ru, поделитесь предложениями или сообщите об ошибках. "
        "Ваш отзыв конфиденциален и используется только для улучшения бота. Напишите ваш отзыв ниже:"
    )

# Команда "Узнать больше"
@router.message(F.text == "Узнать больше о программе опеки")
async def care_info(message: types.Message):
    await message.reply("Программа опеки позволяет стать защитником выбранного вами животного! "
                        "Узнайте больше на сайте: https://moscowzoo.ru/about/guardianship")

# Попробовать ещё раз - перезапуск викторины
@router.message(F.text == "Может ещё разок?")
async def restart_quiz(message: types.Message):
    await start_quiz(message)
