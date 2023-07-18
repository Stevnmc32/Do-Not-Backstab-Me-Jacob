# Endings for Date Night

label afterDQ7:

    $ renpy.block_rollback()

    hide screen moodcurrent

    j "I just wanted to let you know that..."

    if jmood < 7:
        jump NegDEnd
    elif jmood > 17:
        jump PosDEnd
    else:
        jump NeuDEnd


# Neutral Date Ending ##################################################################

label NeuDEnd:
    show jacob anxi
    j "This was a disaster, I probably shouldn't pick up people in my basement..."
    show jacob glad
    j "You aren't too bad though."
    j "I'll see you around?"
    show jacob joy
    extend " {size=-10}Hopefully not.{/size} Anyways,"
    show jacob norm
    extend" {b}BYE.{/b}"
    hide jacob with dissolve

    $ show_quick_menu = False

    scene black with fade

    if persistent.NeuDEndCheck:
        pass

    else:
        $ persistent.DEndings += 1
        $ persistent.NeuDEndCheck = True

    jump end


# Positive Date Ending ##################################################################

label PosDEnd:
    if nosafe == True:
        jump posnoend
    else:
        jump posendcont1
label posnoend:
    show jacob mad
    j "Ugh..."
    show jacob norm
    j "I just can't stay mad at you."
    j "It's not like I'm stupid.{w=.5}"
    show jacob glad
    extend " I know why you did that."
    show jacob anxi
    j "Its just-{w=.5}"
    show jacob fear
    extend " I-"
    show jacob mad
    j "Fuck..."
    show jacob norm
    j "You’re a good person.{w=.5}"
    show jacob glad
    extend " Heh.{w=.5}"
    extend " Y’know that, right?{w=.5}"
    show jacob joy
    extend " And If I was any kinder, I’d probably feel bad about tying you down."
    j "But you also know you’re here because you deserve it...{w=.5}"
    show jacob glad
    extend "right?"
    show jacob norm
    j "I already explained to you that it's your own fault that you're here."
    j "I understand that you can't warm up to me right away, but..."
    show jacob joy
    j "Well, just think of it as a {i}moral{/i} rehab."
    jump posendcont1
#FLAG PART OVER CONTINUE TO NORMAL
label posendcont1:
    show jacob glad
    j "We should head get back to my place."
    j "Eventful night, huh?"
    show jacob joy
    j "Well, come along now. Can’t have you roaming about. Wild streamers are around, just like Hank said, right?"
    j "Wouldn’t want to get {i}stabbed{/i}."
    hide jacob joy with moveoutleft
    scene bg backyard
    show jacob norm
    with fade
    j "Y’know..."
    show jacob glad
    j "I’ve been thinking actually."
    show jacob norm
    j "I’ve told you you’re a good person before, right?{nw}"
    menu:
        extend ""
        "I hope.":
            pass

    show jacob glad
    j "You're a {i}great{/i} person actually."
    j "It’s like- {w=1}"
    extend "It’s like I {i}finally{/i} feel like a person, instead of an outlier from society."
    show jacob joy
    j "It’s this weird feeling in my brain, like, I feel like I have to pick the {i}exact{/i} answer from a list of responses so I can win your affection."
    $ renpy.music.set_pause(True, channel="music")
    show jacob fear
    j "..."
    show jacob emomore
    j "... I love you."
    $ renpy.music.set_pause(False, channel="music")
    show jacob anxi
    j "I-{w=.5}"
    extend "I think anyways."
    j "I’ve {i}never{/i} felt this connected before. {w=.5}"
    show jacob fear
    extend " Never.{w=.5}"
    show jacob anxi
    extend " Haha,{w=.5}"
    show jacob glad
    extend " I think I might even forgive you for the whole stealing thing.{w=.5}"
    show jacob joy
    extend " Water under the bridge, am I right?"
    j "C'mon inside."
    hide jacob joy with moveoutleft
    scene bg kitchen
    show jacob anxi
    with pushright
    j "So..."
    show jacob norm
    j "Listen. I’m not sugarcoating it anymore. I’m certain. I {i}LOVE{/i} you."
    show jacob glad
    j "WE have something special. It’s not too soon, it’s different! We’re just...{w=.5}"
    show jacob joy
    extend "different! {w=.5}"
    show jacob glad
    extend "It’s like- {w=.5}"
    show jacob shoc
    extend "it’s- {w=.5}"
    j "It’s {i}perfect{/i}. {i}You’re{/i} perfect. You’re perfect for {i}me{/i}.{w}"
    extend " {b}You{/b} are what I’m missing. You feel the same way don’t you? Right? {w}"
    show jacob mad
    extend "Right?"
    menu:
        extend ""
        "Jacob...":
            pass
    show jacob anxi
    j "I could-"
    show jacob glad
    j "I believe I could settle down with someone like you. {w}"
    show jacob joy
    extend "If I ever felt so inclined to give up my pursuit of true justice."
    show jacob emo
    j "I would never do that though. Not yet."
    show jacob fear
    j "My work isn’t finished yet."
    j "But.{w}"
    show jacob norm
    extend " But! I think we could do great things together.{w}"
    show jacob glad
    extend " You and me against the world, y’know! Together We can...{w}"
    show jacob joy
    extend " We can fix this shitshow!{nw}"
    menu:
        extend ""
        "Why.":
            pass
    show jacob mad
    j "Why?"
    j "Why what? {w}"
    show jacob emomore
    extend "Don’t you think working together is more efficient? You {i}do{/i} feel the same way right?{nw}"
    menu:
        extend ""
        "I... I think...":
            pass
    show jacob mad
    j "...{nw}"
    menu:
        extend ""
        "But I need to know why! Why do you kill people? Why did I almost die!?":
            pass
    show jacob shoc
    j "...{nw}"
    menu:
        extend ""
        "What did I do wrong?":
            pass
    show jacob fear
    j "..."
    show jacob anxi
    j "..."
    show jacob glad
    j "..."
    show jacob joy
    j "Personal questions already, huh? Warms my heart to see our relationship growing so fast."
    show jacob glad
    j "...{nw}"
    menu:
        extend ""
        "...":
            pass
    show jacob anxi
    j "Look, I’m sorry about that. I really am, I didn’t think..."
    show jacob anxi
    j "I just thought-{w}"
    show jacob emo
    extend " I... was wrong about you, I’m truly, truly sorry about that."
    show jacob emomore
    j "But!{w}"
    extend " But Joss believe me!{w}"
    extend " I will never, {i}NEVER{/i}, pull a knife on you again! I would’ve never done that had I known what kind of person you are!"
    show jacob emo
    j "You can feel safe around me! Really! I promise!{w}"
    extend " Please?{nw}"
    menu:
        extend ""
        "...":
            pass
    j "I uhm..."
    j "As for why I do this..."
    if jmood > 23 and persistent.DEndings >= 3:
        jump JeaDend
    else:
        pass
    if jmood > 19:
        jump backstory
    else:
        jump nobackstory
label backstory:
    show jacob shoc
    j "It’s because it’s the right thing to do. Isn’t it?{w}"
    show jacob fear
    extend " I mean just think about it Joss!"
    j "How much crime goes unpunished?{w}"
    show jacob mad
    extend " Every day on the news you hear a new story about some piece of shit doing the new heinous thing of the day."
    j "{b}Everyday.{/b}"
    show jacob mad
    j " And it. {w}Just. {w}Doesn’t.{w}"
    show jacob piss
    extend " {b}Stop!{/b}"
    show jacob emomore
    j "Even the politicians are in on it! In fact, they’re usually the ones orchestrating the whole goddamn thing! Them and the fucking cops!"
    show jacob mad
    j "Not until now that is."
    j "I know no one deserves to die, but, some people {i}really{/i} deserve to die."
    show jacob glad
    j "I mean,{w}"
    show jacob joy
    extend " you’ve probably felt that way about me at some point, haven’t you?"
    j "Fuck people. Basically.{w}"
    show jacob mad
    extend " {i}Fuck everyone{/i}."
    j "The monsters, but especially the cowards who don’t do anything. They’re just as much to blame."
    j "When...{w}"
    show jacob shoc
    extend "When I was younger my father abused me.{w} And no matter what {i}I{/i} did,{w}"
    show jacob mad
    extend " I was somehow {b}ALWAYS{/b} the one at fault.{w}"
    show jacob emo
    extend "I was {i}always{/i} the problem child."
    j "As a kid... there’s not much you can do. Everyone wants to control you. They all want you to stay small, quiet, and out of trouble."
    show jacob fear
    j "I mean what could I do? I was just a kid."
    show jacob emo
    extend " Nothing I could do, short of dying."
    show jacob shoc
    j "Well..."
    extend " There was {i}one{/i} thing."
    show jacob mad
    j "But I didn't think of that until my junior year,"
    extend " and by then my father had already died."
    show jacob norm
    j "Somewhat happy ending, I guess. My dad died. Not by me, I regret that, but he died none the less."
    j "I guess what I’m saying is, I do it for the people who are forced to stay small."
    j "They deserve retribution. If I can give that to them, then it’s worth it."
    jump posendcont2
label nobackstory:
    show jacob mad
    j "Fuck people. Basically.{w}"
    show jacob piss
    extend "{b}Fuck{/b} everyone!"
    jump posendcont2
label posendcont2:
    j "Joss..."
    j "You're a special one. This is fate. I don’t always kidnap people. And the few times I do, I make sure they regret being in my house."
    j "Anyone I have {i}ever{/i} killed has deserved it. I do my research, I take my time. I’m not insane, and I don't {i}like{/i} killing. But I have to."
    j "Someone has to."
    menu:
        extend ""
        "I...":
            pass
    show jacob glad
    j "Look the point is, I like you a {i}lot{/i}. I gave you a chance, and you’ve done more than proven yourself. This worked out."
    j "This worked out, really, really, well. I’m glad you’re here. I wouldn’t have it any other way. I would very much enjoy a second date with you. If I could be so honored."
    j "Let me just put the knife back. You’re already untied right? You can go if you want, you already know where my place is."
    show jacob joy
    extend " So if you want to come by tomorrow..."
    j "Or..."
    j "...You can even stay over at my place."
    show jacob anxi
    j "If-"
    extend " if you want to,"
    extend " only."
    extend " Of course haha."
    extend " You can sleep on the couch-"
    j "or-"
    j "or something."
    j "I- I won’t even tie you up in the basement this time haha!"
    show jacob glad
    j "So..."
    show jacob joy
    menu:
        j "How about it? You up for a second date?"

        "That'd be nice.":
            show jacob shoc
            j "..."
            show jacob glad
            $ jmood += 1

        "You're literally insane.":
            show jacob anxi
            j "Wait... Don't go!{nw}"
            show jacob emomore
            "Please!{nw}"
            $ jmood -= 1
            pass

    $ show_quick_menu = False

    scene black with fade

    if persistent.PosDEndCheck:
        pass

    else:
        $ persistent.DEndings += 1
        $ persistent.PosDEndCheck = True

    jump end

#editors note we were gonna have joss kill jacob but were too lazy :'(

# Negative Date Ending ##################################################################

label NegDEnd:
    show jacob angy
    j "I thought you KNEW stealing was bad. What the hell happened?"
    show jacob anxi
    j "It's like you did a complete 180!"
    show jacob emomore
    j "What? Just cause you were out of the basement, you thought you were out of the woods?"
    show jacob anxi
    j "Shit..."
    show jacob emo
    j "I wanted to believe you changed. But you're just like the rest.  At least I know that now. People don't change. Noted."
    show jacob norm
    j "Thank you for that. I guess."
    show jacob angy
    j "I- I really did try y'know? I gave you so many chances- TOO many chances- And- and you're the first to ever get this far."
    show jacob emo
    j "It's like you strung me along, god I feel so {b}STUPID.{/b}"
    show jacob anxi
    j "Ugh..."
    j "Christ, I need a nap. You disgust me. A criminal and a liar. Fuck you. I can't wait to go home, re-evaluate my judgment maybe, and eat a nice dinner. Yeah."
    show jacob norm
    j "..."
    show jacob piss
    camera:
        perspective True
        zpos 0 ypos 0
        linear 0.1 zpos -300 ypos -100
    with vpunch
    j "Oh. After I dump your corpse into the river of course!"

    $ show_quick_menu = False

    scene black with fade

    if persistent.NegDEndCheck:
        pass

    else:
        $ persistent.DEndings += 1
        $ persistent.NegDEndCheck = True

    jump end


# Jealous Date Ending ##################################################################

label OLDJeaDend:
    $ renpy.block_rollback()
    show jacob glad
    j "Let's go to my place."
    scene bg kitchen with fade
    show jacob anxi
    "(Jacob is appearing noticeably more sheepish than usual.)"
    show jacob norm
    j "There's something I need to tell you..."
    show jacob anxi
    j "I..."
    j "I..."
    extend " I lo-"
label JeaDend:
    #$ renpy.block_rollback()
    stop music
    play sound ring
    "(RING RING RING)"
    show jacob shoc
    j "Oh shoot, it's work related. Please excuse me."
    show jacob at offscreenleft with move
    stop music
    play music chat
    play sound vineboom
    show james norm with moveinright
    pog "And {i}thaaaat{/i} should be all! For new viewers,{nw}"
    show james happ
    extend " hit the sub!{w} And for old viewers stay tuned for a new {i}collab{/i} with me and Joss!"
    show james pog1
    pog 'You might see him in a future stream after this :3 Remember to bring your wallets too,'
    show james happ
    extend " I don't do anything to the face unless our donation goal is reached ):3 Buh-bye!!!"
    show james norm
    pog "Bloop! owo"
    play sound click
    stop music
    window auto hide
    pause

    window auto hide
    show bg kitchen:
        subpixel True
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
        linear 0.85 matrixcolor InvertMatrix(3.07)*ContrastMatrix(4.36)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    with Pause(0.95)
    show bg kitchen:
        matrixcolor InvertMatrix(3.07)*ContrastMatrix(4.36)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    window auto show


    $ renpy.block_rollback()
    show james neu
    pog "{b}You fucking whore.{/b}"
    play music rant
    show james angry
    pog "I bet you think you're {i}soo{/i} smart, right? I bet you think you're sooo smart for getting out of the basement."
    show james laug
    pog "You're not.{w} You're interesting, I'll give you that, but you aren't tricky in the slightest."
    show james norm
    pog "So... how'd you do it anyways? :3 Huh? Trade secret?"
    show james neu
    pog "Cause I've been trying for months,"
    show james angry
    extend " {size=+10}{b}MONTHS,{/b}{/size}"
    extend " to get as close-"
    extend " {b}CLOSER{/b} actually- "
    show james ups
    pog " And you can just- what? Walk right in and get kidnapped, and now you have him wrapped around your little claw?"
    pog "I just can't{nw}"
    show james scre
    extend " {b}FUCKING BELIEVE YOU! DON'T YOU ALREADY HAVE TWO FRIENDS? DON'T YOU ALREADY HAVE ENOUGH?{/b}"
    show james ups
    pog "You-"
    extend " you already have people..."
    extend " I... I don't have anyone, Joss."
    pog "..."
    show james neu
    pog "You are {b}not{/b} special. Not in the way I am to him."
    show james laug
    pog "He's just going to kill you, hes good at that. He's really good at that actually, and I've seen it before!"
    pog "At {i}that{/i} bridge in fact! There were so many bodies... And you didn't even notice them!"
    pog "All you'll be is a distraction thats overstayed it's welcome..." # FIX IT LATER!!!!!!!
    show james angry
    pog "Fuck you,"
    extend " I can't wait until things go back to normal before you {b}fucked{/b} things up for me."
    show james neu
    pog "I understand, by the way."
    extend " Why you would want more."
    show james laug
    extend " Who wouldn't want a rich husband, am I right?"
    extend " That's all you poor people ever talk about."
    show james laug
    pog "But {b}CHRIST!{/b}{w} To throw your friends away?{w} Poor little July and Hank?"
    show james angry
    pog "Just for-"
    extend " for what? For a fucking fling?"
    extend " For-{nw}"
    show james scre
    extend " You fucking!{nw}"

    menu:
        extend ""
        "You're stupid":
            pass

    $ show_quick_menu = False
    show james ups
    menu:
        pog "What?"
        "You're so fucking stupid!":
            pass
    menu:
        pog "..."
        "I don't want Jacob, I don't want to be here! It's not my fault!":
            pass

    show james neu
    menu:
        pog "..."
        "That he- he just what? That he just likes me better?":
            pass

    menu:
        pog "..."
        "Sorry you {b}suck{/b}.":
            pass

    show james ups
    menu:
        pog "..."
        "I mean, it wasn't {i}that{/i} hard, it {i}really{/i} wasn't that hard.":
            pass
    menu:
        pog "..."
        "I just said what he wanted to hear.":
            pass

    show james angry
    menu:
        pog "..."
        "I can't be sorry if you're that dumb.":
            jump jpt5
label jpt5:
    menu:
        pog "..."
        "Or {b}lonely{/b}. That's not my fault either.":
            jump jpt6

label jpt6:
    menu:
        pog "..."
        "I wish you knew two friends isn't a lot. I wish you knew that, and I wish you weren't as deranged as you are now.":
            pass
    menu:
        pog "..."
        "I {i}don't{/i} want more relationships, not with Jacob.":
            jump jpt7

label jpt7:
    menu:
        pog "..."
        "{i}Especially{/i} not with Jacob.":
            pass
    menu:
        pog "..."
        "But it's almost worth it if it means making you more mad.":
            jump jpt8

label jpt8:

    show james angry
    pog "..."

    window auto hide
    camera:
        perspective True
        subpixel True
        parallel:
            pos (1, 1)
            linear 0.54 pos (-11, -80)
        parallel:
            zpos 3.0
            easein_bounce 0.54 zpos -434.0
    with Pause(0.64)
    camera:
        pos (-11, -80) zpos -434.0

    window auto show

    $ renpy.block_rollback()

    menu:
        pog "..."
        "I think someone like you should {b}die.{/b}":
            jump jpt9

label jpt9:
    menu:
        pog "..."
        "He thinks you're a {i}freak{/i} you know? He told me so himself.":
            jump jpt10

label jpt10:
    menu:
        pog "..."
        "And it's kind of sad really, even your fake father doesn't like you.":
            jump jpt11

label jpt11:
    show james ups
    menu:
        pog "..."
        "I can't imagine how it is for the real one.":
            pass
    menu:
        pog "..."
        "If he hasn't abandoned you already anyways.":
            jump jpt12
label jpt12:
    menu:
        pog "..."
        "Just like Jacob is going to.":
            jump jpt13

label jpt13:
    window auto hide
    $ jmood = 1
    show screen moodcurrent
    pause

    camera:
        subpixel True
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
        linear 0.39 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.67)*SaturationMatrix(4.96)*BrightnessMatrix(0.29)*HueMatrix(0.0)
    with Pause(0.1)
    camera:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.67)*SaturationMatrix(4.96)*BrightnessMatrix(0.29)*HueMatrix(0.0)
    window auto show

    $ renpy.block_rollback()
    show james laug
    pog "{color=#ff0000}{b}I'm going to gut you like a fish.{/b}{/color}"
    pog "{color=#ff0000}{b}And millions will love it.{/b}{/color}"
    pog "{color=#ff0000}{b}Why.{/b}{/color}"
    pog "{color=#ff0000}{b}Why.{/b}{/color}"
    show james scre
    pog "{cps=120}{color=#ff0000}{b}Why, why, why, {i}WHY.{/i} Are you so {i}intent{/i} on taking him from me!? What did I do? WHAT DID I DO? If I KNOW I CAN-{/b}{/color}{/cps}"
    show james ups
    pog "I can...{w} fix it..."
    show james neu
    pog "..."
    show james laug
    pog "Hahaha!"
    show james norm
    pog "Y'know what! It doesn't matter!"
    show james laug
    extend " It doesn't matter :) !"
    show james norm
    extend " It's whatever, it's all just goofs anyways X3"
    show james laug
    pog "New stream idea! {color=#ff0000}{b}You run!{/b}{/color}{w} Yeah!"
    pog "Then,{w} I fucking kill you."
    show james happ
    pog "Don't worry about Jacob btw :3 I got that {i}all{/i} figured out. I'm sure he won't ask though,{w} doubt he cares about you {i}that{/i} much."
    pog "I mean, he's easy to play right? That's what you said? It shouldn't take too much convincing haha! "
    show james laug
    $ show_quick_menu = False
    hide screen moodcurrent
    pog "Well, here's your headstart!"
    show james scre
    "Bloop!"
    play sound click
    window auto hide
    stop music
    scene black
    play sound run
    pause(4.0)
    play sound knock
    pause(1.1)
    play sound stab
    pause(1.0)
    play sound stab
    pause(0.23)
    play sound stab
    pause(0.2)
    play sound stab
    pause(0.12)
    play sound stab
    pause(0.1)
    play sound stab


    if persistent.JeaDEndCheck:
        pass

    else:
        $ persistent.DEndings += 1
        $ persistent.JeaDEndCheck = True

    jump end

#
