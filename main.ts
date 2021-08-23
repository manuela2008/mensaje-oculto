basic.forever(function () {
    basic.showLeds(`
        . # . . .
        . # . . .
        # # . . .
        . . . . .
        . . . . .
        `)
    basic.pause(1000)
    basic.showLeds(`
        # . . . .
        . . . . .
        # . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(3000)
    basic.showLeds(`
        . # . . .
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(4000)
    basic.showLeds(`
        # . . . .
        # # . . .
        # . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(3000)
    basic.showLeds(`
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(1000)
    basic.showLeds(`
        . # . . .
        . # . . .
        # # . . .
        . . . . .
        . . . . .
        `)
    basic.pause(1000)
})
