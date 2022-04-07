# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define da = Character("Daness") # Daness
define ap = Character("April") # April

label start:

# bg morning doorway entrance moving in boxes in hallway

# daness - work clothes - holding box of stuff - enterleft to right
# daness move down and up + shake screen

da "-Aaand that should do the trick!"

# daness - - normal pose -

da "Where's April? I'm starving!"
da "{cps=8}{b}OOH APRIL!{/b}{/cps}"
ap "Nnngh?"

# april - pajama - closed eye yawn slouch - enterright to right(slowly)

ap "{i}*yawns*{/i} What is it?"
da "Let's get some food- I'm hungry, and you haven't eaten yet, right?"

# april - - normal pose happy -

ap "FOOD?!"
da "Yup, a new restaurant opened up downtown. Go and get ready, kay~"
ap "Kaykay~"

# april - - - exits right

# bg outside of doorway overlooking skyline daytime

da "Today is going to be a good day."

jump Act1Scene1:

    return
