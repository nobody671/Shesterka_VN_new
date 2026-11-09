# --- НАСТРОЙКИ ---
define config.default_text_cps = 40
define flash = Fade(0.25, 0.0, 0.75, color="#ffffff")

# --- ПЕРСОНАЖИ ---
define semen = Character('Семён', color="#1e361e")
define danil = Character('Данил', color="#2c2c2c")
define vova = Character('Вова', color="#493b00")
define zhenya = Character('Женя', color="#004152")
define vanya = Character('Ваня', color="#2d742d")
define sasha = Character('Саша', color="#4d1e1e")
define inspector = Character('Инспектор ГАИ', color="#0a0404")
define child = Character('Детский голос', color="#793a3a")
define boy = Character('Мальчишка', color="#793a3a")
define grandma = Character('Бабушка', color="#5d7700")
define man = Character('Мужчина в спецовке', color="#1a0252")
define ilya = Character('Илья', color="#2C2C2C")
define man_in_cap = Character('Мужчина в кепке', color="#1a0252")
define volodya = Character('Володя', color="#241616")
define military1 = Character('Военный 1', color="#002e1b")
define military2 = Character('Военный 2', color="#002e1b")
define volodya_p1 = Character('Парень в зелёном комбинезоне', color="#004770")
define volodya_p2 = Character('Парень в синем комбинезоне', color="#004770")
define kostya = Character('Костя', color="#5c7000")
define storozh = Character('Сторож', color="#690202")
define old_man = Character('Старик', color="#690202")

# --- ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ (ШКАЛЫ) ---
default friend = 0
default ego = 0
default absurd = 0

# Специальный стиль для текста концовок: белый текст с чёрной обводкой в 3 пикселя
define ending_text = Character(None, kind=centered, what_outlines=[(3, "#FAE1E1", 0, 0)], what_color="#ffffff")

# --- Пользовательские позиции для спрайтов ---
transform pos_1: # Крайний левый
    xalign 0.0
    yalign 1.0
    zoom 0.66

transform pos_2: # Левый
    xalign 0.25
    yalign 1.0
    zoom 0.66

transform pos_3: # Центр
    xalign 0.5
    yalign 1.0
    zoom 0.66

transform pos_4: # Правый
    xalign 0.75
    yalign 1.0
    zoom 0.66

transform pos_5: # Крайний правый
    xalign 1.0
    yalign 1.0
    zoom 0.66


# --- СТАРТ ИГРЫ ---
label start:
    # Отправляем игрока в самое начало
    jump p0_intro