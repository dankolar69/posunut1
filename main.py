a = [0, 0]
b = [1, 0]
c = [2, 0]
d = [3, 0]
e = [4, 0]

led.plot(a[0], a[1])
led.plot(b[0], b[1])
led.plot(c[0], c[1])
led.plot(d[0], d[1])
led.plot(e[0], e[1])


def on_button_pressed_a():
    y = 0
    while y < 5:
        a[1] += 1
        b[1] += 1
        c[1] += 1
        d[1] += 1
        e[1] += 1
        y += 1
        
        if y >= 5:
            y = 0
            a[1] = 0
            b[1] = 0
            c[1] = 0
            d[1] = 0
            e[1] = 0
        basic.clear_screen()
        led.plot(a[0], a[1])
        led.plot(b[0], b[1])
        led.plot(c[0], c[1])
        led.plot(d[0], d[1])
        led.plot(e[0], e[1])
        basic.pause(3000)

input.on_button_pressed(Button.A, on_button_pressed_a)