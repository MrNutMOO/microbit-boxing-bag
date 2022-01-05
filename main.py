def on_pin_pressed_p0():
    global Punched
    Punched += 1
    basic.show_number(Punched)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global sped
    sped = 0
    basic.pause(randint(250, 2500))
    basic.show_leds("""
        # # . # #
                # . # . #
                . # # # .
                # . # . #
                # # . # #
    """)
    while not (input.pin_is_pressed(TouchPin.P0)):
        sped += 1
        basic.pause(1)
    basic.show_number(sped)
    basic.show_number(sped)
    basic.show_number(sped)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(100)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(5)
    basic.pause(100)
    basic.show_number(4)
    basic.pause(100)
    basic.show_number(3)
    basic.pause(100)
    basic.show_number(2)
    basic.pause(100)
    basic.show_number(1)
    basic.pause(100)
    basic.show_leds("""
        # # . # #
                # . # . #
                . # # # .
                # . # . #
                # # . # #
    """)
    led.plot_bar_graph(input.acceleration(Dimension.STRENGTH) / 75, 50)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global seconds, index
    seconds = 15
    while seconds > 0:
        basic.show_number(seconds)
        seconds += 0 - 1
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    music.play_melody("C5 B A G G A B C5 ", 329)
    basic.pause(100)
    index = randint(0, len(text_list) - 1)
    basic.show_string("" + (text_list[index]))
input.on_button_pressed(Button.B, on_button_pressed_b)

index = 0
seconds = 0
text_list: List[str] = []
sped = 0
Punched = 0
basic.show_string("Hi")
Punched = 0
sped = 0
text_list = ["GOOD JOB!",
    "WELL DONE!",
    "WOW!",
    "YEAH!",
    "NICELY DONE!",
    "EPIC!"]
seconds = 0