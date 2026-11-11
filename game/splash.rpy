# Определяем изображение (если оно в папке images, Ren'Py найдёт его сам)
image my_logo = "cryble.png"

label splashscreen:
    # 1. Показываем чёрный экран на 1 секунду
    scene black with Pause(1)
    
    # 2. Плавно показываем ваш логотип
    show my_logo with dissolve
    
    # 3. Держим логотип на экране 2 секунды
    with Pause(2)
    
    # 4. Плавно убираем логотип
    hide my_logo with dissolve
    
    # 5. Небольшая пауза перед главным меню
    scene black with Pause(0.5)
    
    # 6. Возвращаемся (обязательно!)
    return