# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Samsara")
define j = Character("Joseph")
define player = Character("Me")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show samsara happy

    # These display lines of dialogue.

    s "Hey... would you like to volunteer for Hackital, the hackathon in the nation's capital?"

    menu:
    
        "Sure...":
            jump morning_1
            
        "I'd love to!":
            jump morning_1

label morning_1:

    s "Awesome! See you in the morning!"
    
    scene bg joseph_room
    with fade
    
    "I arrived at Joseph's room in the morning and was greeted with a large cart."
    
    show joseph neutral
    
    j "Thanks for showing up! We have 15 trips to make and then we'll be done moving all the stuff to the Marvin Center."
    
    player "Sounds fun..."

    # This ends the game.

    return