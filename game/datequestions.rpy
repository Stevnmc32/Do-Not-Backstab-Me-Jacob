# Questions for Date Night

# Question 1
label s4q1:
    menu:
        j "What is your name?"

        "Joss.":
            $ jmood += 2
            call s4q1r1 from _call_s4q1r1
        "...":
            $ jmood -= 1
            call s4q1r2 from _call_s4q1r2
        "Should've Checked my ID.":
            $ jmood -= 2
            call s4q1r3 from _call_s4q1r3

    return

# Question 2
label s4q2:
    menu:
        j "You got any way to support yourself?"

        "Umm... I’m an {i}accountant{/i}...":
            $ jmood += 1
            call s4q2r1 from _call_s4q2r1
        "I steal.":
            $ jmood -= 1
            call s4q2r2 from _call_s4q2r2
        "I work at wcdonalds.":
            $ jmood += 2
            call s4q2r3 from _call_s4q2r3

    return

# Question 3
label s4q3:
    menu:
        j "How do you go about choosing which people should be closest to you?"

        "I have two.":
            $ jmood += 2
            call s4q3r1 from _call_s4q3r1
        "I don’t like people.":
            $ jmood += 1
            call s4q3r2 from _call_s4q3r2
        "How many friends do {i}you{/i} have?":
            $ jmood -= 2
            call s4q3r3 from _call_s4q3r3

    return

# Question 4
label s4q4:
    menu:
        j "Well? “What makes you unique?”"

        "I’m in a band.":
            $ jmood += 2
            call s4q4r1 from _call_s4q4r1
        "I’m good at stealing.":
            $ jmood -= 2
            call s4q4r2 from _call_s4q4r2
        "My fashion sense?":
            $ jmood -= 1
            call s4q4r3 from _call_s4q4r3

    return

# Question 5
label s4q5:
    menu:
        j "If you could have any super power what would it be? "

        "What?":
            $ jmood -= 1
            call s4q5r1 from _call_s4q5r1
        "Invisibility.":
            $ jmood -= 2
            call s4q5r2 from _call_s4q5r2
        "Flight!":
            $ jmood += 2
            call s4q5r3 from _call_s4q5r3

    return

# Question 6
label s4q6:
    menu:
        j "Do you feel safe around me?"

        "Yes.":
            $ jmood +=2
            call s4q6r1 from _call_s4q6r1

        "No!":
            $ jmood -= 2
            $ notsafe = True
            call s4q6r2 from _call_s4q6r2

        "...":
            $ jmood -= 1
            call s4q6r3 from _call_s4q6r3

    return

# Question 7
label s4q7:
    menu:
        j "We met through..."

        "An app.":
            call s4q7r1 from _call_s4q7r1
        "A basement.":
            call s4q7r2 from _call_s4q7r2
        "Hank.":
            call s4q7r3 from _call_s4q7r3

    return

#
