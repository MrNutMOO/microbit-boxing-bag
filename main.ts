input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    
    Punched += 1
    basic.showNumber(Punched)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    sped = 0
    basic.pause(randint(250, 2500))
    basic.showLeds(`
        # # . # #
                # . # . #
                . # # # .
                # . # . #
                # # . # #
    `)
    while (!input.pinIsPressed(TouchPin.P0)) {
        sped += 1
        basic.pause(1)
    }
    basic.showNumber(sped)
    basic.showNumber(sped)
    basic.showNumber(sped)
    basic.showLeds(`
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    `)
    basic.pause(100)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showNumber(5)
    basic.pause(100)
    basic.showNumber(4)
    basic.pause(100)
    basic.showNumber(3)
    basic.pause(100)
    basic.showNumber(2)
    basic.pause(100)
    basic.showNumber(1)
    basic.pause(100)
    basic.showLeds(`
        # # . # #
                # . # . #
                . # # # .
                # . # . #
                # # . # #
    `)
    led.plotBarGraph(input.acceleration(Dimension.Strength) / 75, 50)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    seconds = 15
    while (seconds > 0) {
        basic.showNumber(seconds)
        seconds += 0 - 1
    }
    basic.showLeds(`
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    `)
    music.playMelody("C5 B A G G A B C5 ", 329)
    basic.pause(100)
    index = randint(0, text_list.length - 1)
    basic.showString("" + text_list[index])
})
let index = 0
let seconds = 0
let text_list : string[] = []
let sped = 0
let Punched = 0
basic.showString("Hi")
Punched = 0
sped = 0
text_list = ["GOOD JOB!", "WELL DONE!", "WOW!", "YEAH!", "NICELY DONE!", "EPIC!"]
seconds = 0
