# The Gallery code

init python:

    g = Gallery()

    g.button("Jacob's Sprites")
    g.image("jacob norm")
    g.image("jacob mad")
    g.image("jacob glad")
    g.image("jacob angy")
    g.image("jacob shoc")
    g.image("jacob anxi")
    g.image("jacob emo")
    g.image("jacob emomore")
    g.image("jacob fear")
    g.image("jacob joy")
    g.image("jacob piss")
    g.image("jacob kill")

    g.button("Joss' Sprites")
    g.image("joss norm")
    g.image("joss happ")
    g.image("joss nerv")
    g.image("joss upse")

    g.button("July's Sprites")
    g.image("july norm")
    g.image("july angy")
    g.image("july annoy")
    g.image("july cocky")
    g.image("july distr")
    g.image("july emb")
    g.image("july happy")
    g.image("july nerv")
    g.image("july shoc")

    g.button("Hank's Sprites")
    g.image("hank norm")
    g.image("hank happ")
    g.image("hank emba")
    g.image("hank scare")
    g.image("hank shoc")
    g.image("hank upset")
    g.image("hank fuck")
    g.image("hank terr")
    g.image("hank roar")

    g.button("Backgrounds")
    g.image("bg room")
    g.image("bg park2")
    g.image("bg park1")
    g.image("bg backyard")
    g.image("bg bridge")
    g.image("bg forest1")
    g.image("bg forest2")
    g.image("bg forest3")
    g.image("bg bedroom")
    g.image("bg room og")


    g.button("James' Sprites")
    g.image("james norm")
    g.image("james annoy")
    g.image("james happ")
    g.image("james pog1")
    g.image("james pog2")
    g.image("james pog3")
    g.image("james skep")
    g.image("james smug")
    g.image("james neu")
    g.image("james ups")
    g.image("james angry")
    g.image("james laug")
    g.image("james scre")
    #g.image("james bonus")

    g.button("Extra")
    g.image("ex1")
    g.image("ex2")
    g.image("ex3")
    g.image("ex4")
    g.image("ex5")
    g.image("ex6")
    g.image("ex7")
    g.image("ex8")
    g.image("ex9")
    g.image("ex10")

    g.transition = dissolve

image icon jacob = "images/gall/bja.png"
image icon joss = "images/gall/bjo.png"
image icon july = "images/gall/bju.png"
image icon hank = "images/gall/bha.png"
image icon james = "images/gall/bpog.png"
image icon bg = "images/gall/bbg.png"
image icon extra = "images/gall/bmo.png"
image ex1 = "images/gall/excon1.png"
image ex2 = "images/gall/excon2.png"
image ex3 = "images/gall/excon3.png"
image ex4 = "images/gall/excon4.png"
image ex5 = "images/gall/excon5.png"
image ex6 = "images/gall/excon6.png"
image ex7 = "images/gall/excon7.png"
image ex8 = "images/gall/excon8.png"
image ex9 = "images/gall/excon9.png"
image ex10 = "images/gall/excon10.png"

screen gallery():

    tag menu

    add "bg room"

    label "{size=+30}Gallery{/size}" xalign 0.94 yalign 0.75

    grid 4 2:

        xfill True
        yfill True

        add g.make_button("Jacob's Sprites", "icon jacob", xalign=0.5, yalign=0.5)
        add g.make_button("James' Sprites", "icon james", xalign=0.5, yalign=0.5)
        

        add g.make_button("July's Sprites", "icon july", xalign=0.5, yalign=0.5)
        add g.make_button("Hank's Sprites", "icon hank", xalign=0.5, yalign=0.5)

        add g.make_button("Backgrounds", "icon bg", xalign=0.5, yalign=0.5)
        add g.make_button("Extra", "icon extra", xalign=0.5, yalign=0.5)
        

        add g.make_button("Joss' Sprites", "icon joss", xalign=0.5, yalign=0.5)
        textbutton "Return" action Return() xalign 0.35 yalign 0.70


# Music Room ##################################################################

init python:

    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)
    

    # Step 2. Add music files.
    
    mr.add("audio/song/Dark-Things-2_V001.mp3")
    mr.add("audio/song/Dusk.mp3")
    mr.add("audio/song/Darkness-Approaches_Looping.mp3")

    mr.add("audio/song/Bradley/Bear_Hug.mp3")
    mr.add("audio/song/Bradley/After_Hours.mp3")
    mr.add("audio/song/Bradley/Ghost_in_the_Park.mp3")
    mr.add("audio/song/Bradley/Midnight_Chatter.mp3")
    mr.add("audio/song/Bradley/Midnight_Rant.mp3")

# Step 3. Create the music room screen.
screen music_room:

    tag menu

    add "musroo"

    label "{size=+30}Music Room{/size}" xalign 0.05 yalign 0.05

    grid 4 2:

        xfill True
        yfill True

        # The buttons that play each track.
        textbutton "Dark Things 2" action mr.Play("audio/song/Dark-Things-2_V001.mp3") xalign 0.35 yalign 0.80 
        textbutton "Dusk" action mr.Play("audio/song/Dusk.mp3") xalign 0.5 yalign 0.80
        textbutton "Darkness Approaching" action mr.Play("audio/song/Darkness-Approaches_Looping.mp3") xalign 0.35 yalign 0.80
        textbutton "Bear Hug" action mr.Play("audio/song/Bradley/Bear_Hug.mp3") xalign 0.35 yalign 0.80
        textbutton "After Hours" action mr.Play("audio/song/Bradley/After_Hours.mp3") xalign 0.35 yalign 0.00
        textbutton "Ghost In The Park" action mr.Play("audio/song/Bradley/Ghost_in_the_Park.mp3") xalign 0.35 yalign 0.00
        textbutton "Midnight Chatter" action mr.Play("audio/song/Bradley/Midnight_Chatter.mp3") xalign 0.35 yalign 0.0
        textbutton "Midnight Rant" action mr.Play("audio/song/Bradley/Midnight_Rant.mp3") xalign 0.35 yalign 0.0

    #null height 20

    # Buttons that let us advance tracks.
    textbutton "Next" action mr.Next() xalign 0.40 yalign 0.20
    textbutton "Previous" action mr.Previous() xalign 0.25 yalign 0.20

    #null height 20

    # The button that lets the user exit the music room.
    textbutton "Return" action ShowMenu("main_menu") xalign 0.10 yalign 0.20

    # Start the music playing on entry to the music room.
    on "replace" action mr.Play()

    # Restore the main menu music upon leaving.
    on "replaced" action Play("music", "audio/song/Darkness-Approaches_Looping.mp3")




#
