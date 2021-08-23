def on_forever():
    basic.show_leds("""
        . # . . .
                . # . . .
                # # . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        # . . . .
                . . . . .
                # . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(3000)
    basic.show_leds("""
        . # . . .
                # . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(4000)
    basic.show_leds("""
        # . . . .
                # # . . .
                # . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(3000)
    basic.show_leds("""
        # . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . # . . .
                . # . . .
                # # . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
basic.forever(on_forever)
