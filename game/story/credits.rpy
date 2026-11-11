# Метка, которая запускает титры
label credits:
    # Показываем экран с титрами
    show screen credits_screen
    # Ждём 120 секунд (или столько, сколько нужно для прокрутки)
    pause 120
    # Скрываем экран
    hide screen credits_screen
    return

# Экран с титрами
screen credits_screen:
    # Фон (можно использовать изображение)
    add "#000000" # Чёрный фон
    
    # Контейнер для текста, который будет двигаться
    vbox:
        xalign 0.5
        yalign 1.0 # Начинаем с нижнего края
        
        # Анимация движения вверх
        at transform:
            # Движение вверх за 20 секунд (настройте под свой текст)
            linear 20.0 yalign 0.0
        
        # Ваш текст
        text _("ИГРА СОЗДАНА В") size 30
        text _("МОЕЙ КРУТОЙ СТУДИИ") size 60
        null height 50
        
        text _("Руководитель проекта") size 30
        text _("Ваше Имя") size 40
        null height 50
        
        text _("Музыка") size 30
        text _("Композитор") size 40
        null height 50
        
        text _("Спасибо за игру!") size 50