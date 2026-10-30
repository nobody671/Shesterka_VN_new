# --- НАСТРОЙКИ ---
define config.default_text_cps = 40
define flash = Fade(0.25, 0.0, 0.75, color="#ffffff")

# --- ПЕРСОНАЖИ ---
define semen = Character('Семён', color="#c8ffc8")
define danil = Character('Данил (Бибизян)', color="#ffffff")
define vova = Character('Вова', color="#ffcc00")
define zhenya = Character('Женя', color="#00ccff")
define vanya = Character('Ваня', color="#66ff66")
define sasha = Character('Саша', color="#ff6666")
define inspector = Character('Инспектор ГАИ', color="#0a0404")
define child = Character('Детский голос', color="#ffffff")
define boy = Character('Мальчишка', color="#ffffff")
define grandma = Character('Бабушка', color="#ffffff")
define man = Character('Мужчина в спецовке', color="#ffffff")
define ilya = Character('Илья', color="#ffffff")
define man_in_cap = Character('Мужчина в кепке', color="#ffffff")
define volodya = Character('Володя', color="#ffffff")
define military1 = Character('Военный 1', color="#ffffff")
define military2 = Character('Военный 2', color="#ffffff")
define volodya_p1 = Character('Парень Володи 1', color="#ffffff")
define volodya_p2 = Character('Парень Володи 2', color="#ffffff")
define kostya = Character('Костя', color="#ffffff")
define storozh = Character('Сторож', color="#ffffff")
define old_man = Character('Старик', color="#ffffff")

# --- ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ (ШКАЛЫ) ---
default friend = 0
default ego = 0
default absurd = 0

# --- СТАРТ ИГРЫ ---
label start:
    # Отправляем игрока в самое начало
    jump p0_intro