# The script of the game goes in this file.


# The game starts here.

label splashscreen:
    scene black
    if persistent.endCount < 9:
        $ persistent.endCount = 9
    else:
        pass
    call ComCheck from _call_ComCheck_1
    $ rd_funfact=renpy.random.choice(funfact)
    "INFO! View Trigger Warnings on the {a=https://boredbradley.itch.io/jacobextra}Itch.io page{/a}"
    with Pause(1)
    return

label start:

    scene black
    with Dissolve(1.0)
    stop music fadeout 1.0
    $ show_quick_menu = False
    $ rng = renpy.random.randint(1,10)
    python:
        y_name = renpy.transform_text(renpy.input("Name your victim", length=32),upper)

    if persistent.Endings > 0:
        $ qpick = renpy.random.randint(1, 3) #Uncomment later
        #$ qpick = 1 # Remove later

        menu:
            "Would you like to skip the prologue?"

            "Yes":
                #$ introskip = True  #Uncomment later
                jump select

            "No":
                pass

    else:
        $ qpick = 1
    
    "TODO: add attic setting"
    "TODO: add sound effects"
    scene black #attic
    with Dissolve(1.0)
    stop music fadeout 1.0
    js "Any luck?"
    yn "Nope"
    js "They’ve gotta be here somewhere, we just need to keep looking!"
    yn "Yeah, yeah, I-"
    js "Pearl? You ok?"
    yn "Yeah, I just found something weird..."
    js "Alright, if you say so."
    yn "...who’s Jacob?"
    js "What did you-"
    js "Ooh, VHS tapes! I wonder what they’ve got on them-"
    yn "If you’ll excuse me-"
    scene black #vcr player
    with Dissolve(1.0)
    stop music fadeout 1.0
    yn "...Why does it say my old name?"
    yn "I wonder if this is why I can’t remember."
    yn "Guess I should watch them?"
    scene black
    with Dissolve(1.0)
    stop music fadeout 1.0

label select:
    $ show_quick_menu = False

    call screen chaper_select
    return

label chapter_one:
    "TODO: add chapter one"
    jump end

label chapter_two:
    "TODO: add chapter two"
    jump end

label end:

    stop music fadeout 1.0

    window hide

    scene black with fade

    centered "{color=#ffffff}{size=+50}END{/size}{/color}"
    return



label StartTrigger:
    $ show_quick_menu = False
    n "Mentions of: Self dying,
Possessive behavior, 
Breaking and entering,
Bad people get away with bad things,
Murder,
Flashing lights,
Cussing,
Furries,
Stealing."
    return


label skipintro:
    scene bg room 
    show jacob norm 
    with fade
    play music noise fadein 3.0
    $ show_quick_menu = True
    jump afterintro

label savetest:
    #Thank you Stevenmc32!
    call screen confirm(message="Enable Saving?",yes_action=SetVariable("persistent.saveunlock", True) and ShowMenu("savetestre"), no_action=SetVariable("persistent.saveunlock", False) and ShowMenu("savetestre"))
    return

label savetestre:
    call screen main_menu()