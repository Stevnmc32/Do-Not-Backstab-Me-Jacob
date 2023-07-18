# List of questions that Jacob ask
#

##
label q1b:
    if qpick == 1:
        call s1q1 from _call_s1q1
    elif qpick == 2:
        call s2q1 from _call_s2q1
    elif qpick == 3:
        call s3q1 from _call_s3q1
    else:
        call qerror from _call_qerror
    return

label q2b:
    if qpick == 1:
        call s1q2 from _call_s1q2
    elif qpick == 2:
        call s2q2 from _call_s2q2
    elif qpick == 3:
        call s3q2 from _call_s3q2
    else:
        call qerror from _call_qerror_1
    return

label q3b:
    if qpick == 1:
        call s1q3 from _call_s1q3
    elif qpick == 2:
        call s2q3 from _call_s2q3
    elif qpick == 3:
        call s3q3 from _call_s3q3
    else:
        call qerror from _call_qerror_2
    return

label q4b:
    if qpick == 1:
        call s1q4 from _call_s1q4
    elif qpick == 2:
        call s2q4 from _call_s2q4
    elif qpick == 3:
        call s3q4 from _call_s3q4
    else:
        call qerror from _call_qerror_3
    return

label q5b:
    if qpick == 1:
        call s1q5 from _call_s1q5
    elif qpick == 2:
        call s2q5 from _call_s2q5
    elif qpick == 3:
        call s3q5 from _call_s3q5
    else:
        call qerror from _call_qerror_4
    return

label q6b:
    if qpick == 1:
        call s1q6 from _call_s1q6
    elif qpick == 2:
        call s2q6 from _call_s2q6
    elif qpick == 3:
        call s3q6 from _call_s3q6
    else:
        call qerror from _call_qerror_5
    return



label qerror:
    "ITS NOT WORKING HELP HELP HELP"

###########################################

label s1q1:
    menu:
        j "Why did you break into my house?"

        "I thought it would be funny.":
            $ jmood -= 1
            call s1q1r1 from _call_s1q1r1
        "I need money.":
            $ jmood += 1
            call s1q1r2 from _call_s1q1r2
        "You deserved it.":
            $ jmood -= 2
            call s1q1r3 from _call_s1q1r3

    return

label s1q2:
    menu:
        j "What are your thoughts on vegetarians?"

        "They're fine I guess...":
            $ jmood += 1
            call s1q2r1 from _call_s1q2r1
        "They're annoying as hell.":
            $ jmood -= 1
            call s1q2r2 from _call_s1q2r2
        "I respect them.":
            $ jmood += 2
            call s1q2r3 from _call_s1q2r3
        #"You just want me to flatter you, huh sheep boy?":
        #    $ jmood -= 1
        #    call s1q2r4

    return

label s1q3:
    menu:
        j "Do you think you deserve to die?"

        "Hell no!":
            $ jmood -= 1
            call s1q3r1 from _call_s1q3r1
        "Yeah...":
            $ jmood += 1
            call s1q3r2 from _call_s1q3r2
        "You're really pretentious.":
            $ jmood -= 2
            call s1q3r3 from _call_s1q3r3

    return

label s1q4:
    menu:
        j "Do you think anyone truly 'deserves' to die?"

        "Of course not!":
            $ jmood -= 1
            call s1q4r1 from _call_s1q4r1
        " Absolutely. Some people don’t deserve to live.":
            $ jmood += 1
            call s1q4r2 from _call_s1q4r2
        "Yes, but not me!":
            $ jmood -= 2
            call s1q4r3 from _call_s1q4r3

    return

label s1q5:
    menu:
        j "What do you think about sheep?"

        "They're annoying and gross!":
            $ jmood -= 1
            call s1q5r1 from _call_s1q5r1
        "They're pretty cool.":
            $ jmood += 1
            call s1q5r2 from _call_s1q5r2
        "They're really Ba-ad....":
            if rng > 5:
                $ jmood -= 1
                call s1q5r3 from _call_s1q5r3
            if rng < 5:
                $ jmood += 2
                call s1q5r3A from _call_s1q5r3A


    return

label s1q6:
    menu:
        j "Do you value your life?"

        "Yes!":
            $ jmood -= 1
            call s1q6r1 from _call_s1q6r1
        "Not really.":
            $ jmood += 1
            call s1q6r2 from _call_s1q6r2
        "Why should I?":
            $ jmood += 2
            call s1q6r3 from _call_s1q6r3
        #"You better let me out of here if you value yours.":
            #$ jmood -= 2
            #call s1q6r4

    return

label s2q1:
    menu:
        j "Why do you think I want to kill you?"

        "Cause I broke into your house?":
            $ jmood += 2
            call s2q1r1 from _call_s2q1r1
        #"Cause you're an asshole.":
        #    $ jmood -= 2
        #    call s2q1r2
        "I'm assuming you don't like me?":
            $ jmood += 1
            call s2q1r3 from _call_s2q1r3
        "No idea!":
            $ jmood -= 1
            call s2q1r4 from _call_s2q1r4

    return

label s2q2:
    menu:
        j "Would you kill 10 people to save 100?"

        "Yes. It's for the greater good.":
            $ jmood += 2
            call s2q2r1 from _call_s2q2r1
        "No! That's still murder.":
            $ jmood -= 1
            call s2q2r2 from _call_s2q2r2
        "Depends on who lives and who dies.":
            $ jmood += 1
            call s2q2r3 from _call_s2q2r3
        #"Oh my God, you are SO pretentious...":
            #$ jmood -= 2
            #call s2q2r4

    return

label s2q3:
    menu:
        j "What do you think I do for a living?"

        "Kill people?":
            $ jmood -= 1
            call s2q3r1 from _call_s2q3r1
        "Business stuff?":
            $ jmood += 1
            call s2q3r2 from _call_s2q3r2
        "Hopefully not a barber":
            $ jmood -= 2
            call s2q3r3 from _call_s2q3r3

    return

label s2q4:
    menu:
        j "Do you think one person's mistakes can define them?"

        "No. Nobody is perfect.":
            $ jmood -= 1
            call s2q4r1 from _call_s2q4r1
        "Yes.":
            $ jmood += 1
            call s2q4r2 from _call_s2q4r2
        "I don't regret robbing you, by the way.":
            $ jmood -= 2
            call s2q4r3 from _call_s2q4r3

    return

label s2q5:
    menu:
        j "If you could, would you kill me?"

        "Yes, absolutely.":
            $ jmood -= 1
            call s2q5r1 from _call_s2q5r1
        "No. It would make me just as bad.":
            $ jmood += 1
            call s2q5r2 from _call_s2q5r2
        "Literally who would say 'no'??":
            $ jmood -= 2
            call s2q5r3 from _call_s2q5r3

    return

label s2q6:
    menu:
        j "Are you scared of what I'll do to you?"

        "Yes.":
            $ jmood += 1
            call s2q6r1 from _call_s2q6r1
        "Nah.":
            $ jmood -= 1
            call s2q6r2 from _call_s2q6r2
        "Not really. In fact, I think I'll enjoy this":
            $ jmood += 2
            call s2q6r3 from _call_s2q6r3

    return

label s3q1:
    menu:
        j "Do you know who I am?"

        "A serial killer?":
            $ jmood -= 1
            call s3q1r1 from _call_s3q1r1
        "Some rich dude I guess.":
            $ jmood += 1
            call s3q1r2 from _call_s3q1r2
        #"No.":
        #    $ jmood -= 1
        #    call s3q1r3
        "You're Jacob.":
            $ jmood += 2
            call s3q1r3 from _call_s3q1r3

    return

label s3q2:
    menu:
        j "What is your biggest fear?"

        "This exact situation.":
            $ jmood += 2
            call s3q2r1 from _call_s3q2r1
        "Hank":
            $ jmood -= 1
            call s3q2r3 from _call_s3q2r3
        "Dying alone.":
            $ jmood += 1
            call s3q2r4 from _call_s3q2r4

    return

label s3q3:
    menu:
        j "Do you think your family will miss you? Your friends?"

        "Yes! They would never abandon me!":
            $ jmood -= 1
            call s3q3r1 from _call_s3q3r1
        "Probably not.":
            $ jmood += 1
            call s3q3r2 from _call_s3q3r2
        "Does your family miss you?":
            $ jmood -= 2
            call s3q3r3 from _call_s3q3r3

    return

label s3q4:
    menu:
        j "Do you think someone will come rescue you?"

        "Yes! I bet they’re on their way right now!":
            $ jmood -= 1
            call s3q4r1 from _call_s3q4r1
        "I don’t {b}want{/b} anyone to rescue me.":
            $ jmood += 2
            call s3q4r3 from _call_s3q4r3
        "I don't {b}need{/b} anyone to rescue me":
            $ jmood -= 2
            call s3q4r4 from _call_s3q4r4

    return

label s3q5:
    menu:
        j "Do you believe in a perfect society?"

        "No, that's impossible.":
            $ jmood -= 1
            call s3q5r1 from _call_s3q5r1
        "Yes":
            $ jmood += 1
            call s3q5r2 from _call_s3q5r2
        "We already live in a perfect society.":
            $ jmood -= 2
            call s3q5r3 from _call_s3q5r3

    return

label s3q6:
    menu:
        j "Do you enjoy this?"

        "...yes.":
            $ jmood += 1
            call s3q6r1 from _call_s3q6r1
        "Gross, no.":
            $ jmood -= 1
            call s3q6r2 from _call_s3q6r2
        "And what if I do?":
            $ jmood += 1
            call s3q6r3 from _call_s3q6r3

    return


#label q16:
#    menu:
#        j "Have you been honest with these answers?"
#
#        "Yes.":
#            $ jmood += 1
#            call q16r1
#        "Yeah, toooooootttaaalllllly...":
#            $ jmood += 1
#            call q16r2
#        "Nope.":
#            $ jmood -= 1
#            call q16r3
#
#    return


label q7:
    menu:
        j "Do you think I'm bad person?"

        "Yes.":
            $ jmood -= 3
            call q7r1 from _call_q7r1
        "No.":
            $ jmood += 3
            call q7r2 from _call_q7r2
        "I don't know.":
            call q7r3 from _call_q7r3


    return







#
