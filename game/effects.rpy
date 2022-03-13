# Declare transitions below this line, using the define statement

define enterleft = ComposeTransition(dissolve, after=easeinleft)
define enterright = ComposeTransition(dissolve, after=easeinright)
define entertop = ComposeTransition(dissolve, after=easeintop)
define enterbot = ComposeTransition(dissolve, after=easeinbottom)

# set ATLs and inits using the init block? here
init:
    ## Flip sprite animation
    transform flip:
        linear 0.02  alpha 0.0
        xzoom -1.0
        linear 0.02  alpha 1.0

    ## Unflips a sprite
    transform unflip:
        linear 0.2  alpha 0.0
        xzoom 1.0
        linear 0.2  alpha 1.0
