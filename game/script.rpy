# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define me     = Character("Me")

# Main Characters
define sa     = Character("Samsara")
define se     = Character("Avi")
define jo     = Character("Joseph")
define gw     = Character("GW Person")

# Background Characters
define part_0 = Character("Participant 0")
define part_1 = Character("Participant 1")
define part_2 = Character("Participant 2")

# Game variables
default done_flashback = False
default score          = 0

# The game starts here. Joseph says he's looking for the best volunteer at GWU
label start:
    scene bg blue
    
    show character joseph
    
    jo "Hello there! My name is Joseph Schiarizzi, and I am looking for the best volunteer at Hackital."
    jo "I am one of the organisers and would love for someone to just appear in front of me..."
    
    jump pre_0

# Signing up for Hackital as a participant
label pre_0:

    scene bg dorm
    
    "Last month..."
    
    me "Oh boy, I am so excited to sign up to participate in Hackital!"

    jump pre_1
    
# You getting a red shirt instead of a black shirt / flashback
label pre_1:

    scene bg registration
    
    "The morning of Hackital, I commuted from my dorm bulding on campus so that I could be the first to show up."
    "I'm so glad that they gave me travel reimbursement for that 2-block trip!"
    
    show character samsara
    with fade
    
    sa "What size shirt?"
    
    menu:
        "Small":
            pass
        "Medium":
            pass
        "Large":
            pass
        "Extra-Large":
            pass
        "Any size is fine...":
            pass
            
    sa "Okay awesome, here you go! Don't forget to make a hack for Hack Harassment!"
    
    jump realisation

label realisation:
    
    "I look down at the shirt... It's red, unlike the pile of black shirts on the table."
    "Not sure what that means..."

    if done_flashback:
        $ done_flashback = False
        jump pre_5

    jump pre_2

# Joseph pitching Hackital to OS
label pre_2:

    "At my operating systems class two weeks ago..."
    
    scene bg os
    show character joseph
    with fade
    
    jo "Hey everyone, in case you didn't know, Hackital is in two weeks. So register at hackital.io."
    
    "For some reason this pitch sounded familiar."

    jump pre_3

# Joseph pitching Hackital to GWTC
label pre_3:

    "At Tech Collective four weeks ago..."
    
    scene bg gwtc
    show character joseph
    with fade
    
    jo "Hey everyone, in case you didn't know, Hackital is in two weeks. So register at hackital.io."
    
    "Joseph was very passionate about getting people to sign up for Hackital. He's pitched it to me at least 10 times now!"
    "Of course, that might have to do with him organising this event."

    jump pre_4

# Joseph books the Hackital venue and realises he needs more volunteers
label pre_4:

    "One year ago..."
    
    scene bg gw
    show character joseph
    with fade
    
    jo "... And that is why you should let us host Hackital again this year."
    
    show character gw
    
    gw "Works for me."

    $ done_flashback = True
    jump realisation
    
# Joseph telling you that you are a volunteer
label pre_5:

    "Joseph approaches the table."
    
    show character joseph
    with fade
    
    jo "Hey there, how's my newest volunteer?"
    
    me "I didn't ask for this..."
    
    jo "What do you mean? You wanted to volunteer."
    
    me "Oh, you're right..."
    
    "Was he though? I don't remember even realising that hackathons needed volunteers."

    jump sam_0

# Samsara asking if you'll be making a #HackHarassment hack
label sam_0:

    sa "Sorry to interrupt, but just checking, even if you are volunteering you should be aware that you can still submit a hack to the HackHarassment challenge."

    if done_flashback:
        $ done_flashback = False
        jump job
        
    "Now that I think about it, I've heard a lot about HackHarassment."

    jump sam_1

# Making posters at 3am (with foreshadowing)
label sam_1:

    "The previous night..."
    
    scene bg dorm
    show character samsara
    with fade

    sa "Thank you so much for helping with these posters."
    
    me "Yeah, no problem. I wasn't doing anything anyways."
    
    sa "If you're having fun now, wait until tomorrow! You're gonna really enjoy it."
    
    me "Yeah I hope so. I'm putting off 9001 essays for this."
    
    sa "You should write an essay about your #HackHarassment submission."
    
    sa "Anyways, I got to go get 2 hours of sleep. See you at 7am tomorrow!"
    
    me "See you tomorrow!"
    
    "Wait... Isn't Hackital supposed to start at 10am? Must have made a last minute schedule change..."
    
    scene bg registration
    with fade
    
    "Back to Hackital..."
    $ done_flashback = True

    jump sam_0

# Joseph gives you a choice what you want to do
label job:

    show character joseph

    jo "Hey you still there? I was explaining the different volunteer positions you can do."
    
    "Eh, not like I need to know them anyways. I'm not volunteering."
    
    jo "So which one do you want to do?"
    
    "Oh, guess I am..."

    menu:
        "I want to do registration.":
            jump reg_0
        "I want to do hardware checkout.":
            jump har_0
        "I want to do events.":
            jump eve_0

# Registration event 0
label reg_0:
    scene bg registration
    with fade
    
    "Welp, guess I should make the most of it and work the registration table."
    
    jump reg_1

# Registration event 1
label reg_1:

    jump reg_2

# Registration event 2
label reg_2:

    if score == 3:
        jump reg_pass
    else:
        jump reg_fail

# Registration pass event
label reg_pass:

    # This ends the game.
    return

# Registration fail event
label reg_fail:

    # This ends the game.
    return

# Hardware event 0
label har_0:

    scene bg hardware
    with fade
    
    "Welp, guess I should make the most of it and help manage the hardware."

    jump har_1

# Hardware event 1
label har_1:

    jump har_2

# Hardware event 2
label har_2:

    if score == 3:
        jump har_pass
    else:
        jump har_fail

# Hardware pass event
label har_pass:

    # This ends the game.
    return

# Hardware fail event
label har_fail:

    # This ends the game.
    return

# Events event 0
label eve_0:
    
    scene bg registration
    with fade

    "Welp, guess I should make the most of it and help run events."

    jump eve_1

# Events event 1
label eve_1:

    jump eve_2

# Events event 2
label eve_2:

    if score == 3:
        jump eve_pass
    else:
        jump eve_fail

# Events pass event
label eve_pass:

    # This ends the game.
    return

# Events fail event
label eve_fail:

    # This ends the game.
    return
