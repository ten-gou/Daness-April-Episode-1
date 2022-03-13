# The script of the game goes in this file.

# set ATLs and inits using the init block? here
init:
    # Flip sprite animation
    transform flip:
        linear 0.02  alpha 0.0
        xzoom -1.0
        linear 0.02  alpha 1.0

    # Unflips a sprite
    transform unflip:
        linear 0.2  alpha 0.0
        xzoom 1.0
        linear 0.2  alpha 1.0

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define da = Character("Daness") # Daness
define ap = Character("April") # April

label start:



    return
