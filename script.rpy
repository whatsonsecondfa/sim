# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

#for fatten animation
define x_0 = 0.47
define x_1 = 0.47
define x_2 = 0.47
define x_3 = 0.47
define x_4 = 0.47
define x_5 = 0.47
define y_0 = 0.47
define y_1 = 0.47
define y_2 = 0.47
define y_3 = 0.47
define y_4 = 0.47
define y_5 = 0.47

# The game starts here.

transform slide_right(time, width, height):
    center
    linear time xzoom (1 - (width / 2)) yzoom (1 + (height / 2)) center
    linear time xzoom (1 + (width / 2)) yzoom (1 - (height / 2))

#init python:
#    def testFunction():
#        show test at slide_right(0.3, 4)

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    jump showFeedee

    # This ends the game.

    return
