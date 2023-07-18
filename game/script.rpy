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

    if persistent.Endings > 0:
        $ qpick = renpy.random.randint(1, 3) #Uncomment later
        #$ qpick = 1 # Remove later

        menu:
            "Would you like to skip the intro?"

            "Yes":
                #$ introskip = True  #Uncomment later
                jump skipintro

            "No":
                pass

    else:
        $ qpick = 1

    "(While on your way home after band practice, you stop by the park with your bandmates.)"

    scene bg park2
    with Dissolve(1.0)

    play music hug

    show july emb at left 
    show hank norm at right 
    with dissolve

    ju "Sigh...Great job, doofus."

    show hank upset 

    h "HEY! I already said I was sorry for breaking Joss' drums!"

    show hank shoc

    h "I can't see why you're making such a big fuss about this, Joss could just buy a new one!"

    show hank norm at center 
    with move

    "(Hank looks at you for a second.)"

    show hank emba

    h "Nevermind, I see now..."

    show hank happ at right with move
    show july shoc

    h "Maybe ask someone to borrow theirs?"

    show july annoy

    ju "Who would just lend us a drum set?"

    h "Maybe we could ask my neighbor Jacob! He has a whole music room, not a very good one though..."

    show hank emba

    extend " {size=-10}cuz there's no Arianna merch in there.{/size}{nw}"

    menu:
        extend ""
        "hm...":
            pass

    show july norm at center with move

    ju "Whatever, we'll figure it out later. We're meeting up at the park again tonight, right?"

    show hank happ

    h "Yeah! People online keep begging me to go outside more often!"

    play sound run
    show hank at offscreenright with move
    

    "(Hank jaunts off.)"

    show july nerv

    ju "There's no way some stranger would just give us a drum set..."

    show july annoy

    ju "Hey! Don't be late, and don't do anything stupid. "

    show july cocky

    extend "...without me of course."

    scene black with fade

    stop music fadeout 1.0

    "(You think you have an idea on how to get those drums...)"

label maincourse:

    scene black with fade

    play sound run
    pause(4.0)
    play sound knock
    pause(1.0)

    "..."
    "..."
    extend "?"

    scene bg room
    show jacob anxi
    show black
    with dissolve
    camera:
        perspective True
        xpos -450 ypos -100 zpos -620
        linear 1.0 xpos -450 ypos -100 zpos -600

    pause 0.5

    hide black with Dissolve(0.7)

    camera:
        perspective True
        xpos -450 ypos -100 zpos -600
        linear 0.7 xpos 430 ypos -220 zpos -600

    pause 1.0

    show jacob norm

    camera:
        perspective True
        xpos 430 ypos -220 zpos -600
        linear 1.2 xpos -150 ypos 30 zpos -600
        pause 0.11
        linear 0.5 xpos 0 ypos -150 zpos -600
        pause 0.2
        linear 0.9 xpos 0 ypos 0 zpos 0

    play music noise fadein 3.0

    pause 3.2

    play sound "audio/voice/baa.mp3"

    pause

    $ show_quick_menu = True

label afterintro:

    $ renpy.block_rollback()

    "(Your eyes slowly blink open...)"
    "(You're in an unfamiliar room, tied to a chair.)"
    "(There's a tall ram standing before you.)"

    j "Hey, you, you're finally awake."

    show jacob glad

    j "Might be wondering where you are, eh?"

    show jacob mad

    j "You're in my fucking house, that's what!"

    j "Well, that's the least of your worries, kid."

    j "You thought you could hide from me, huh? Nice try."

    j "To put it plainly, I'm going to kill you."

    show jacob anxi

    extend " Or, well... I might."

    show jacob norm

    j "I have some questions to ask you."

    show jacob glad

    j "No point in killing someone without getting a bit of information from them, as I always say."

    show screen moodcurrent

    show jacob glad

    j "Maybe, if you manage to convince me, I'll let you go."

    show jacob norm

    j "But don't get your hopes up. I'm the serial killer, you're the victim. Remember that."

    j "Alright, let's see here..."

    show jacob mad

    call q1b from _call_q1b

label afterQ1:

    $ renpy.block_rollback()

    show jacob curr

    j "Well now we're getting somewhere!"

    j "Ok, lemme think of something else to ask..."

    j "..."

    show jacob norm

    call q2b from _call_q2b

label afterQ2:

    $ renpy.block_rollback()

    show jacob curr

    j "Let's see what else..."


    call q3b from _call_q3b

label afterQ3:

    $ renpy.block_rollback()

    show jacob curr

    j "Hmm, I think I'm starting to get an impression of you..."

    j "Just a few more questions, ok?"

    call q4b from _call_q4b

label afterQ4:

    $ renpy.block_rollback()

    show jacob curr

    j "Interesting... moving on."

    call q5b from _call_q5b

label afterQ5:

    $ renpy.block_rollback()

    show jacob curr

    j "Ok what next..."

    call q6b from _call_q6b

    jump afterQ6

label afterQ6:

    $ renpy.block_rollback()

    show jacob curr

    j "Now I'll ask one last question for you..."

    call q7 from _call_q7

    jump afterQ7

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