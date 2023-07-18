#Ending Scenes
# It's self explanatory...

#Pre-Ending (Sets up the endings) ###################################################
label afterQ7:

    $ renpy.block_rollback()

    hide screen moodcurrent

    show jacob fear
    j "Please pardon me a second."
    show jacob fear at offscreenright with move
    hide jacob fear

    "Jacob swiftly left the room."

    show jacob norm with dissolve

    j "..."

    j "Eh, anyways..."

    j "Ok, I've decided..."

    $ show_quick_menu = False

    if persistent.Endings >= 3:
        if jmood > 22:
            jump HorEnd
        else:
            if jmood < 5:
                jump AltEnd
            else:
                pass
    else:
        pass
    if jmood == 14:
        jump NeuEnd
    elif jmood > 18:
        jump AccEnd
    elif jmood > 15:
        jump PosEnd
    elif jmood < 9:
        jump VioKillEnd
    elif jmood < 13:
        jump NegEnd
    else:
        jump NeuEnd

#Neutral Ending (He doesn't do anything) #############################################
label NeuEnd:

    show jacob norm

    j "..."

    j "I..."

    show jacob anxi

    extend " haven't come to a conclusion actually. I don't know what to do with you."

    j "You're a puzzling one for sure..."

    show jacob norm

    j "Tell you what, I'm a busy man. I'm gonna go take care of some business, and I'll think about it."

    show jacob norm

    j "For now, you just stay here."

    show jacob angy

    extend " {b}Don't{/b} bother trying to get out."

    show jacob norm

    j "This room is soundproof and, full offense, I doubt you could sneak around my house without me catching you again."

    show jacob glad

    j "Goodbye."

    hide jacob with easeoutright

    "..."

    "..."

    "..."

    $ show_quick_menu = False

    scene black with fade

    if persistent.NeuEndCheck:
        pass

    else:
        $ persistent.Endings += 1
        $ persistent.NeuEndCheck = True

    jump end



#Alive Ending (You get to live!) ###########################################################
label PosEnd:

    show jacob joy

    extend " ...Maybe you aren't as bad as I thought you were."

    show jacob anxi

    j "Perhaps my judgement has failed me this time."

    show jacob glad

    j "I will let you go."

    show jacob angy

    extend " But don't think this means you're off scot-free."

    j "Don't forget for even a {i}second{/i} that I'll have my eyes on you."

    show jacob norm

    j "Watch yourself. Test my judgement again and you'll see what happens."

    show jacob piss

    j "And if you breathe a word about this to {b}ANYONE{/b}, it will be your last. I swear on it."

    show jacob angy

    j "The moment I untie you, I want you gone, got it?"

    show jacob glad

    j "Goodbye."

    $ show_quick_menu = False

    #scene white with Dissolve(1.0)
    show white:
        alpha .9
    with Dissolve(0.5)

    scene black with fade

    if persistent.PosEndCheck:
        pass

    else:
        $ persistent.Endings += 1
        $ persistent.PosEndCheck = True

    jump end



#Negative Ending (He kills you) ####################################################
label NegEnd:

    show jacob angy

    j "..."

    j "God you're a nuisance!"

    show jacob anxi

    j "You aren't terrible, just... {b}annoying.{/b}"

    show jacob norm

    j "Seriously kids these days with their slays, pogs, and memes."

    show jacob piss

    j "Can't you take this seriously for 15 minutes, when your {b}LIFE{/b} is on the line?"

    show jacob angy

    j "I'm going to make sure you shut up. Forever."

#It's a little rough, but it works! \(^w^)/
label KillScene:

    $ show_quick_menu = False

    window hide

    #play sound vineboom

    show jacob kill
    camera:
        perspective True
        zpos 0 ypos 0
        linear 0.12 zpos -300 ypos -100
    with vpunch
    play sound stab
    show red:
        alpha .5
    with Dissolve(0.1)


    #scene red with Dissolve(1.0)
    scene black with fade

    if persistent.NegEndCheck:
        pass

    else:
        $ persistent.Endings += 1
        $ persistent.NegEndCheck = True

    jump end

# Violent Kill ending (Cutscene Kill Ending) ###########################################
label VioKillEnd:

    show jacob piss

    j "You've proven to me that you're just as much of a piece of shit that I thought you were."

    show jacob angy

    j "You don't deserve to live."

    $ dead = True

    $ show_quick_menu = False

    window hide

# Cutscene Kill Ending ##################

label movtest:

    if persistent.VioKillEndCheck:
        pass

    else:
        $ persistent.Endings += 1
        $ persistent.VioKillEndCheck = True

    scene black with fade

    pause 0.3

    $ renpy.movie_cutscene("images/badend.webm")

    jump end

#Date Ending (Must get 3 endings then get Jacob's mood to max. There are two outcomes.) ###
label HorEnd:

    show jacob norm

    j "..."

    show jacob glad

    j "I've grown fond of you."

    show jacob joy

    j "{i}Very{/i} fond of you, actually. I'd like to get to know you a bit better."

    show jacob shoc

    j "Only if you want to, of course...{nw}"

    menu:
        extend ""
        "Sure":
            jump HorY
        "No!":
            jump HorN

# DATE YES END (Unlocks Date Night) #####################################
label HorY:

    show jacob joy

    j "Well then! I suppose we should get out of this stuffy basement."

    show jacob norm

    j "I'm not untying you yet though. Can't be too careful!"

    show jacob anxi

    j "That's not weird is it? I hope not, yeesh, maybe this isn't a good idea..."

    j "..."

    show jacob glad

    j "You're cool with it tho, {i}right?{/i} Right!"

    $ show_quick_menu = False

    if persistent.HorYEndCheck:
        pass

    else:
        $ persistent.Endings += 1
        $ persistent.HorYEndCheck = True
        play sound notice
        $ renpy.notify("Date Night Mode has been unlocked!")

    scene white with Dissolve(1.0)

    scene black with fade

    jump end

# DATE NO END ########################################################
label HorN:

    show jacob anxi

    j "Ah well, it was worth a shot. Yikes, that's embarrassing..."

    show jacob fear

    j "Did I seem desperate? No, I don't think so... Did I??"

    show jacob emo

    j "Uh... well I guess I still have to kill you. This is far too embarrassing to let slip. I really will miss you though."

    show jacob norm

    j "Farewell..."

    $ dead = True

    window hide

    show jacob emo:
        zoom 1.0
        linear 1.0 zoom 1.5 yalign 20
    with vpunch
    play sound stab

    show red:
        alpha .5
    with Dissolve(0.5)

    #scene red with Dissolve(1.0)
    scene black with fade

    $ show_quick_menu = False

    if persistent.HorNEndCheck:
        pass

    else:
        $ persistent.Endings += 1
        $ persistent.HorNEndCheck = True

    jump end

# Accomplice Ending #####################################
label AccEnd:
    show jacob glad
    j "Hm, you're very interesting. I see it in you, you share the same views as me."
    j "You see the world for what it truly is, a place filled with vile criminals that need to be purged."
    show jacob norm
    j "You could help me, Y'know."
    show jacob emo
    j "Help me end this scourge to society, this plague that haunts us. Help me, please.{nw}"
    menu:
        extend ""
        "Yes":
            jump AccY
        "No":
            jump AccN

label AccY:
    show jacob glad
    j "Very good! We'll get started right away!"
    show jacob norm
    j "Your first kill will be rough, but you'll get over it."
    show jacob joy
    j "This will be a great partnership!"

    scene white with Dissolve(1.0)
    scene black with fade


    $ show_quick_menu = False

    if persistent.AccEndCheck:
        pass
    else:
        $ persistent.Endings += 1
        $ persistent.AccEndCheck = True

    jump end

label AccN:
    show jacob anxi
    j "I guess I misread you, I thought you were different, or were you just telling me what I wanted to hear?"
    j "You wouldn't be the first."
    show jacob norm
    j "That's too bad. I really thought we could've done something together."
    j "Farewell..."

    show jacob kill
    camera:
        perspective True
        zpos 0 ypos 0
        linear 0.12 zpos -300 ypos -100
    with vpunch
    play sound stab
    show red:
        alpha .5
    with Dissolve(0.1)

    scene black with fade

    $ show_quick_menu = False

    if persistent.AccNoEndCheck:
        pass
    else:
        $ persistent.Endings += 1
        $ persistent.AccNoEndCheck = True
    jump end


#Game Crash Ending (Get Jacob's Mood to 1) #############################################
label AltEnd:

    if persistent.RareKillEndCheck:
        pass

    else:
        $ persistent.Endings += 1
        $ persistent.RareKillEndCheck = True

    show jacob emomore

    j "THAT'S IT!"

    show jacob piss

    j "YOU DON'T DESERVE TO LIVE!"

    show jacob emo

    j "I DONT NEED ANYMORE QUESTIONS TO SEE THAT!"

    show jacob angy

    j "Good fucking riddance."

    $ show_quick_menu = False

    window hide

    show jacob piss
    camera:
        perspective True
        zpos 0 ypos 0
        linear 0.1 zpos -300 ypos -100
    with vpunch

    if renpy.variant("pc"):
        $ renpy.quit()
    else:
        jump altend2

label altend2: 
    stop music
    window hide
    scene bg error
    pause(5.0)
    call ComCheck from _call_ComCheck
    jump end



#End (What do you think this is?)
label end:

    if jmood < 24:
        pass
    else:
        "..."
        "..."
        "..."

    stop music fadeout 1.0

    window hide

    scene black with fade

    centered "{color=#ffffff}{size=+50}END{/size}{/color}"

# Add a Call to here in date mode! ####################################################

label ComCheck:

    if persistent.Endings >= 9 and persistent.DendCount >= 4:
        if persistent.ConEndCheck:
            pass
        else:
            "Congrats on getting all the endings!"
            $ persistent.ConEndCheck = True
            play sound notice
            $ renpy.notify("Gallery and Music Room has been unlocked!")
            return
    else:
        pass

    $ rd_funfact=renpy.random.choice(funfact)

    if rng > 7:
        if dead == True:
            call postDeadEnds from _call_postDeadEnds
        else:
            pass
    else:
        pass

    return

label postDeadEnds:
    scene black with fade
    pause
    scene bg bridge with dissolve
    play music chat fadein 5.0
    show jacob norm with dissolve
    j "..."
    j "...It's done."
    play sound "audio/sfx/vineb00m.mp3"
    show james norm at left with moveinleft
    pog "Omg hey jacob!"
    show jacob shoc at right with move
    j "Bah, you again."
    show james pog1
    pog "Omg you got another kill! Such a good kd ratio!"
    show jacob anxi
    j "What the hell are you talking about?"
    show james happ
    pog "Chat this is Jacob! Say hi!"
    show jacob fear
    j "Are you recording this?! I could be convicted!"
    show james smug
    pog "Streaming it actually!"
    show james happ
    pog "Don't worry, chat is cool!"
    show jacob mad
    j "That's even worse! Why would you do something that could get you caught like this?!"
    show james norm
    pog "Money tee hee!"
    show james smug
    pog "People pay premium to watch murder live!"
    show jacob anxi
    j "How are you not in jail yet?"
    show james happ
    pog "Trade secret! Teehee."
    scene black with fade
    return
