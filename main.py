led.plot_brightness(0 + 2, 0 + 2, 100)
led.plot(0, 0)
led.plot(1, 1)
A = 0
B = 0
def on_button_pressed_a():
    global A, B
    A = 1
    B = 1
    while A == 1:
        basic.clear_screen()
        led.plot_brightness(0 + 2, 0 + 2, 100)
        led.plot(0, 2)
        led.plot(1,2)
        basic.pause(500)

        basic.clear_screen()
        led.plot_brightness(0 + 2, 0 + 2, 100)
        led.plot(0, 4)
        led.plot(1,3)
        basic.pause(500)

        basic.clear_screen()
        led.plot_brightness(0 + 2, 0 + 2, 100)
        led.plot(2, 4)
        led.plot(2, 3)
        basic.pause(500)

        basic.clear_screen()
        led.plot_brightness(0 + 2, 0 + 2, 100)
        led.plot(4, 4)
        led.plot(3, 3)
        basic.pause(500)

        basic.clear_screen()
        led.plot_brightness(0 + 2, 0 + 2, 100)
        led.plot(4, 2)
        led.plot(3, 2)
        basic.pause(500)

        basic.clear_screen()
        led.plot_brightness(0 + 2, 0 + 2, 100)
        led.plot(4, 0)
        led.plot(3, 1)
        basic.pause(500)

        basic.clear_screen()
        led.plot_brightness(0 + 2, 0 + 2, 100)
        led.plot(2, 0)
        led.plot(2, 1)
        basic.pause(500)

        basic.clear_screen()
        led.plot_brightness(0 + 2, 0 + 2, 100)
        led.plot(0, 0)
        led.plot(1, 1)
        basic.pause(500)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global A, B
    A = 0
    B = 0
    while B == 0:
        basic.clear_screen()
        led.plot_brightness(0 + 2, 0 + 2, 100)
        led.plot(2, 0)
        led.plot(2, 1)
        basic.pause(500)

        basic.clear_screen()
        led.plot_brightness(0 + 2, 0 + 2, 100)
        led.plot(4, 0)
        led.plot(3, 1)
        basic.pause(500)

        basic.clear_screen()
        led.plot_brightness(0 + 2, 0 + 2, 100)
        led.plot(4, 2)
        led.plot(3, 2)
        basic.pause(500)

        basic.clear_screen()
        led.plot_brightness(0 + 2, 0 + 2, 100)
        led.plot(4, 4)
        led.plot(3, 3)
        basic.pause(500)

        basic.clear_screen()
        led.plot_brightness(0 + 2, 0 + 2, 100)
        led.plot(2, 4)
        led.plot(2, 3)
        basic.pause(500)

        basic.clear_screen()
        led.plot_brightness(0 + 2, 0 + 2, 100)
        led.plot(0, 4)
        led.plot(1,3)
        basic.pause(500)

        basic.clear_screen()
        led.plot_brightness(0 + 2, 0 + 2, 100)
        led.plot(0, 2)
        led.plot(1, 2)
        basic.pause(500)

        basic.clear_screen()
        led.plot_brightness(0 + 2, 0 + 2, 100)
        led.plot(0, 0)
        led.plot(1, 1)
        basic.pause(500)
input.on_button_pressed(Button.B, on_button_pressed_b)