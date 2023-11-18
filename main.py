def mover_gota():
    # Variables
    x = 2
    y = 2

    # Bucle principal
    while True:
        # Enciende el LED en la posición x, y
        display.set_pixel(x, y, 1)
        # Espera 50 ms
        sleep(50)
        # Apaga el LED en la posición x, y
        display.set_pixel(x, y, 0)

        # Lee la aceleración en los ejes X e Y
        accX = accelerometer.get_x()
        accY = accelerometer.get_y()

        # Actualiza la posición del LED
        if accX <= 150 and x > 0:
            x -= 1
        elif accX > 150 and x < 4:
            x += 1
        if accY <= 150 and y > 0:
            y -= 1
        elif accY > 150 and y < 4:
            y += 1

# Llamamos a la función
mover_gota()
