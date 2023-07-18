# The script with variables and shit

# Jacob's Mood
# This dictates the ending, it increases or decreases whenever you answer a question.
default jmood = 14


#Image for mood names in the moodbox

image neutral_neg:
    zoom 0.24
    "moods_imgs/em_neu.png"
    pause 0.5
    "images/moods_imgs/em_neuneg.png"
    pause 0.5
    repeat

image neutral_pos:
    zoom 0.24
    "moods_imgs/em_neu.png"
    pause 0.5
    "images/moods_imgs/em_neupos.png"
    pause 0.5
    repeat

image enraged:
    zoom 0.24
    "moods_imgs/em_enr1.png"

image enraged2:
    zoom 0.24
    "moods_imgs/em_enr1.png"
    pause 0.3
    "images/moods_imgs/em_enr2.png"
    pause 0.3
    repeat

image neutral:
    "moods_imgs/em_neu.png"
    zoom 0.24

image amused:
    "moods_imgs/em_amu.png"
    zoom 0.24

image annoyed:
    "moods_imgs/em_ann.png"
    zoom 0.24

image horny:
    "moods_imgs/em_hor.png"
    zoom 0.24

image intrigued:
    "moods_imgs/em_int.png"
    zoom 0.24

image pissed:
    "moods_imgs/em_piss.png"
    zoom 0.24

image quenched:
    "moods_imgs/em_que.png"
    zoom 0.24

image satisfied:
    "moods_imgs/em_sat.png"
    zoom 0.24

image pleased:
    "moods_imgs/em_plea.png"
    zoom 0.24



# Scale:
# 1-4 (Neg X3), 5-8 (Neg X2), 9-12 (Neg)
# 13, 14, 15 (Neu)
# 16-18 (Pos), 19-21 (Pos X2), 22-24 (Pos X3)
image moodname:
    ConditionSwitch (
        "jmood > 24 and persistent.Endings >= 3 and killmode == True", "horny",
        "jmood > 23", "quenched",
        "jmood < 2", "enraged2",
        "jmood == 14", "neutral",
        "jmood > 21", "intrigued",
        "jmood > 18", "amused",
        "jmood > 15", "pleased",
        "jmood < 5", "enraged",
        "jmood < 9", "pissed",
        "jmood < 13", "annoyed",
        "jmood < 14", "neutral_neg",
        "jmood > 14", "neutral_pos",
    )


#Endings notify
#Tells you how many endings you've achieved (There's 7)
define persistent.Endings = 0
define persistent.DEndings = 0

#Tells you how many endings there are (There's 8 main endings, The 8th is a secret.)
define persistent.endCount = 9
define persistent.DendCount = 4
define persistent.ConEndCheck = False # All Endings cleared

#Checks to make sure it doesn't keep adding numbers to persistent.Endings
#OG Ends
define persistent.PosEndCheck = False
define persistent.NegEndCheck = False
define persistent.NeuEndCheck = False
define persistent.HorYEndCheck = False
#New Ends
define persistent.HorNEndCheck = False # Rejecting Jacob's date
define persistent.VioKillEndCheck = False # Cutscene Kill
define persistent.AccEndCheck = False # Accomplice Ending
define persistent.RareKillEndCheck = False # Game Crash Ending
define persistent.AccNoEndCheck = False # Accomplice Ending

# Date Night Endings <3
define persistent.PosDEndCheck = False
define persistent.NegDEndCheck = False
define persistent.NeuDEndCheck = False
define persistent.JeaDEndCheck = False


#Menu related flags & Like Flags in general
$ introskip = False
default killmode = True
default show_quick_menu = False
define persistent.saveunlock = False
default rng = 0
default dead = False
define persistent.DateNotify = False
define nosafe = False


## Sounds ###############################################################################
# Songs ####################

## Eric Matyas Songs
define audio.noise = "audio/song/Dark-Things-2_V001.mp3"
define audio.dusk = "audio/song/Dusk.mp3"
define audio.dark = "audio/song/Darkness-Approaches_Looping.mp3"

## Bradley Songs
define audio.ghost = "audio/song/Bradley/Ghost_in_the_Park.mp3"
define audio.hug = "audio/song/Bradley/Bear_Hug.mp3"
define audio.ah = "audio/song/Bradley/After_Hours.mp3"
define audio.chat = "audio/song/Bradley/Midnight_Chatter.mp3"
define audio.rant = "audio/song/Bradley/Midnight_Rant.mp3"

#SFX
define audio.stab = "audio/sfx/PM_BB_DESIGNED_CINEMATIC_CHOPS_31.mp3"
define vineboom = "audio/sfx/vineb00m.mp3"
define audio.run = "audio/sfx/foley_footsteps_running_shingle_children_pass.mp3"
define audio.knock = "audio/sfx/zapsplat_impacts_body_hit_punch_or_kick_whoosh_012_90406.mp3"
define audio.click = "audio/sfx/zapsplat_multimedia_button_click_bright_003_92100.mp3"
define audio.notice = "audio/sfx/zapsplat_musical_retro_classic_vibraphone_mystery_tone_001_45103.mp3"
define audio.ring = "audio/sfx/zapsplat_multimedia_ringtone_mallets_marimba_smartphone_004_84893.mp3"

#Color Backgrounds
image red = "#FF0000"
image white = "#ffffff"

#ETC
$ centered = Character(None, xalign=0.5, yalign=0.5)



# The voice beeps and defining names ###########################################
# Jacob's voice (so handsome...)
# Make sure preferences.afm_time doesn't equal 0 or it won't work
init python:
    def jacob_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/voice/baa.mp3",loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

# July's voice
init python:
    def july_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/voice/julyvb.mp3",loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

# Hank's voice
init python:
    def hank_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/voice/hankvb.mp3",loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

# James' voice
init python:
    def james_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/voice/jamesvb.mp3",loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

# Names
define y = Character("JOSS")
define j = Character("JACOB", color= "#782222", callback=jacob_voice)
define ju = Character("JULY", color= "#703e59", callback=july_voice)
define h = Character("HANK", color= "#34547d", callback=hank_voice)
define pog = Character("JAMES", color= "#356334", callback=james_voice)
define n = nvl_narrator


## Misc Transforms #############################################################


# Tranform for choices. Thxs https://lemmasoft.renai.us/forums/viewtopic.php?t=34340
transform fromRight:
        subpixel True
        alpha 0.0 xalign 2.0 
        parallel:
            easein 1.0 alpha 1.0
        parallel:
            easein 1.0 xalign 1.0
        on hide:
            easein 1.0 alpha 0.0 xalign 2.0 

# Transform for main menu (based on above)
transform fromLeft:
        subpixel True
        alpha 0.0 xalign 0.0 
        parallel:
            easein 1.0 alpha 1.0
        parallel:
            easein 1.0 xalign 0.03
        on hide:
            easein 1.0 alpha 0.0 xalign 0.0 


#Fun Facts #####################################################################
default funfact=[
    "Don't eat grass","We don't romantize suicide","Don't be dumm",
    "programming is 90% crying and 10% programming","Is the Game Jam version even canon?","Excuse me, I love you. <3",
    "You wouldn’t understand, you aren’t in the discord","Who’s James?","Don’t mind the cat",
    "JJJJH","Hank is gay","You are not immune to Brutus Propaganda", # 6.5 Inches
    "Who the hell is Patches?","Just Moni- wait wrong game","Jacob likes black coffee, and he likes it very fancy.",
    "James was made by the discord","All I ever wanted was the world...","Yuh", # 7/15
    "15","Removed Herobrine","Jacob’s favorite game is animal crossing",
    "Stop asking for a dating sim, it's already here!","July is also Gay","Everyone is gay",
    ":)","Get it, HORNs?","We see you SF 69 and SF 420",
    "You can still change the title!","You can change him","Baark",
    "JANMI died for this","It’s only mostly a game","Is any of this actual facts?",
    "No <3","Thank god Bix insulted my graphic design skills","Triangle knife can’t hurt you",
    "Jacob has Levis on","Do Not Dump Me Jacob is on its way","Still can’t program a gallery",
    "Don’t worry, you’re not a furry, Jacob’s simply built differently.","It’s only a matter of time...","Bixarre wuz here",
    "James lies","YO Switch port when???","Still a better love story than Twilight...",
    "Soundskies, why are you late?","Tumblr is banned","Remember when July was a rabbit? Me neither...",
    "Hank has more Ariana Grande merch than you","Jacob isn’t submissive and breedable","James isn’t dominant and infertile",
    "No plans for an android port right now.","We know you are playing for the date ending","Bradley get’s an F in graphic design",
    "Soundskies carried the group project","James is a sugar baby","Remember to save your game!",
    "James has Jacob’s house key","maid dREss JAcob","Just keep breathin",
    "A perfectly drawn, non tool assisted perfect 360 degree circle.","Send in your headcanons and we’ll make them canon","Has anyone seen my blue hoodie?",
    "Best 6 minutes of my life","Jacob spends 2 hours taking care of his wool","I simped so hard I infiltrated the dev team",
    "I have to stop myself from making a Taylor Swift reference","There are more fun facts than actual lines of dialogue","vegetarians are cool but not this one ",
    "There are more endings than you think","I took time to program this","Press the Start button to start!",
    "There's a glitch with the fun facts, but i don't feel like fixing it","Imagine if we could afford voice acting...","Some answers make Jacob mad",
    "You can hug jacob, but only once...","I remember it all too well...","Mhm!",
    "You all need some water","Never gonna give you up","Jcaob can be your angle;; ... or yuor devil",
    "01101000 01100101 01111001 00100000 01100010 01100101 01110011 01110100 01101001 01100101","position","An exception has occurred",
    "Bixarre is running a daycare at this point","You may be in Jacob’s basement, but are you in his walls?","Bixarre traced minecraft screenshots",
    "Joss is ace","null","look behind you", # 01010011 01110000 01100001 01100111 01101000 01100101 01110100 01110100 01101001
    "GO HAVE YOUR WEDDING AND TAKE ME OFF THE GUEST LIST","hey pretty princess","I want your love, and I want your revenge",
    "I haven't touched this code in months wtf is this?","I'd rather be dry, but at least I'm alive","The message below will be my new nickname",
    "Remind me to stfu","Call me maybe?","I kissed a girl and I liked it",
    "she would've been a belieber","","I need sleep", 
    "There are over 100 fun facts!","Fannon Jacob is only in your dreams I’m sorry","sub","Jshit was once in the game"
    ]