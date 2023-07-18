
label sschange:
    $ show_quick_menu = True

    $ persistent.saveunlock = True

    return

label StartDate:
    stop music fadeout 1.0
    scene bg forest3 with fade
    show jacob norm with dissolve

    $ show_quick_menu = True
    $ killmode = False

    "Due to.... {i}unique{/i} circumstances, you find yourself on a date with Jacob."
    play music ghost

    show jacob glad

    j "Ah, here. We made it."

    show jacob norm

    j "What, you have a problem with a park date?"

    show jacob joy

    j "I myself enjoy a quiet stroll through the woods."

    j "Helps cool the mind after a soul-crushing day of work."

    show jacob anxi

    j "...So does killing people but that's a different story."

    show jacob glad

    show screen moodcurrent

    j "...Ahem, anyways let's get this date started shall we?"

    call s4q1 from _call_s4q1

label afterD1:
    show jacob anxi

    j "Joss, how do you make a living?"

    show jacob norm

    j "I don't expect you to be a full time thief, considering how much you messed this heist up."

    show jacob shoc

    j "No offense,"

    show jacob anxi

    extend " ...kind of."

    show jacob glad

    j "But you must have a way to pay for food right?"

    call s4q2 from _call_s4q2

label afterD2:
    scene bg forest1
    show jacob norm
    with fade

    j "I work in information technology, if you couldn't tell."
    show jacob glad
    extend " Mondays amiright?"
    menu:
        extend ""
        "You mean I.T?":
            pass
    show jacob joy
    j "...Yeah. But doesn't it sound a lot cooler when I {i}don't{/i} abbreviate it?"
    show jacob glad
    j "I think it's funny. I used to believe that with office folks, you didn't have to look out for them."
    show jacob norm
    j " {i}The small fries are too boring to do crime.{/i} Or so I thought, until one day... "
    show jacob mad
    j "Well, the rich are always looking to take from the poor. "
    show jacob emo
    j "It made me realize that making friends at the office isn't the best idea,"
    show jacob emomore
    extend " those things aren't looking out for anyone but themselves."
#    show jacob glad
#    j "I think it's funny. I used to believe, that with office folks, you didn't have to think twice about them."
#    show jacob norm
#    j "{i}They're small fries. Small fries are too boring to do crime.{/i}"
#    show jacob joy
#    j "Or so I thought, until {i}you{/i} found your way into {i}my{/i} home. You're just full of surprises aren't you?"
    j "Oh well, maybe I just don't get out too often. With work, and {i}hobbies,{/i} I really can't spare the time for dates."
    show jacob anxi
    j "Or friends, actually I can't remember the last time I had any meaningful interactions."
    stop music
    show james norm at right with moveinright
    play sound vineboom
    show jacob shoc at left with move
    play music chat
    pog "YOOO! Impromptu collab stream!?? (Talking to chat btw haha :3)"
    show jacob angy
    show james happ
    pog "Whatsup chat!!, You'll never guess who we just met!!"
    show james pog1
    pog "That's right- Jacob!! With his next victim too!"
    show james smug
    show jacob anxi
    pog "Stay tuned, we're finally gonna see if Jacob twists his knife when he stabs, or if he's just a straight shooter!"
    show james skep
    show jacob norm
    pog "So Jacob, who exactly is our lucky ducky? When are you gonna kill them? More importantly, when is it {i}my{/i} turn?"
    show james smug
    pog "Just kidding haha, of course you wouldn't kill me! :3"
    show jacob anxi
    j "...Yeah ...anyways."
    show jacob norm
    j "This is my... date. If you couldn't tell."
    show james annoy
    $ renpy.music.set_pause(True, channel="music")
    pog "{cps=5}Oh...{/cps} {cps=10}that's so... ...{/cps}{nw}"
    $ renpy.music.set_pause(False, channel="music")
    show james happ
    extend "Poggers! {size=-10}yeah...{/size}"
    show james skep
    pog "I couldn't tell, actually. I mean why would you have a knife on a date right?"
    show james pog3
    show jacob anxi
    pog "C'mon, tell me Jacob, this is just some sick mind trick right? You're gonna kill it right?"
    show jacob angy
    j "What the fuck is wrong with you."
    show james happ
    pog "Ahahaha!! Of course you are, let's go guys! (talking to chat)"
    show james pog2
    pog "Okay so for the new ones, we just caught Jacob in the middle of some good ol' psychological torture! What do you think chat, should we leave him to it?{nw}"
    menu:
        extend ""
        "Why are you streaming in the woods?":
            pass
    show james norm
    pog "Oh wow {size=-10}ahaha{/size},"
    extend " didn't know he let you talk {size=-5}haha{/size} isn't that {i}soo{/i} cute?"
    show james pog3
    extend " Right guys?"
    show james pog2
    extend " Don't you {i}love{/i} when they're {b}SO{/b} confused?"
    show james smug
    extend " You're going to make such a {i}lovely{/i} lampshade!"
    show james annoy
    pog "Well..."
    show james norm
    extend " if you must know,"
    show james smug
    extend " I just hit a milestone!"
    extend " Have you ever hit a milestone before?"
    extend " {size=-5}{i}Doubt it.{/i}{/size}"
    extend " I'm going corpse hunting as a celebration."
    pog "Have {i}you{/i} ever hunted a corpse?{nw}"
    menu:
        extend ""
        "I don't thin-":
            pass
    pog "Yeah, I doubt it."
    show jacob shoc
    show james norm
    j "Wait corpse hunting?"
    show jacob fear
    show james skep
    extend  " For what corpses?! {size=-10}*nervous chuckle*{/size}"
    show jacob glad
    extend " There's no corpses here! {size=-10}*nervous chuckle*{/size}"
    show james smug
    pog "Oooh... wink wink, right Jacob? Wouldn't want any of your exes to show up right? Speaking of exes, how'd you even meet this simp?"
    show james skep
    show jacob anxi
    j "The justice system."
    show james norm
    pog "Well chat! Seems like our Jacob is busy, sorry but we'll just have to come around later to see the good shit!"
    show james annoy
    pog "So that means stick around, and remember I have all your addresses so if {b}ANYONE{/b} leaves-"
    show james happ
    show jacob norm
    pog "Well anyways, have fun you two! It was {b}SOOO{/b} nice meeting you X3"
    stop music fadeout(1.5)
    hide james with moveoutright
    show jacob anxi at center with move
    play music ghost
    j "Yeah... for future reference I'd recommend avoiding him. Like staying a street away from him at all times, kid has major issues.{nw}"
    menu:
        extend ""
        "What exactly... is his problem?":
            pass
    show jacob norm
    j "It's not all bad I guess, he looks up to me at least."
    show jacob glad
    extend " So we know he isn't terrible at picking role models."
    show jacob joy
    extend " It just makes me think we're lucky for being one of the normal ones."
    show jacob anxi
    j "Maybe that's just what being antisocial does to a person. {w}Maybe that's why it's important to keep people around..."
    show jacob norm
    j "..."
    show jacob joy
    j "Though suppose some people are just naturally unhinged, everyone at every corner is just waiting to stab you in the back. I guess that's not too far off from reality."

    call s4q3 from _call_s4q3

label afterD3:
    show jacob norm

    j "I don't know if I've mentioned this before, but I've never actually been this far with a person before."
    j "..."
    show jacob shoc
    j "I mean! With a captive, I mean!"
    show jacob joy
    j "I've been on a few dates, not to toot my own horn but I'm kind of a catch, heh."
    show jacob glad
    j "Lucky you, amiright?"
    show jacob anxi
    j "Well, I only mention it to say that I've run out of questions. Which is a...{w} first,{w} I usually have them stocked up."
    show jacob joy
    j "Aww, I guess you just have that effect on me."
    show jacob norm
    extend " Anyways, excuse me while I look at my phone for a bit."
    j "..."
    show jacob anxi
    j "{i}10 Perfect Questions to Ask On The First Date To Really Get To Know Someone{/i}"
    j "Says that I should ask you..."
    j "{i}“What makes you unique?”{/i}"
    show jacob angy
    extend " Tch- {w}that's a stupid question!"
    show jacob norm
    j "Well?"

    call s4q4 from _call_s4q4

label afterD4:
    show jacob joy
    j "Y'know what though?{w}"
    show jacob norm
    extend " Fuck this website,{w}"
    show jacob mad
    extend " this is for losers. We're better than that!"
    show jacob emomore
    j "In fact, I should kill the person who wrote this for giving out such abysmal advice!"
    show jacob joy
    j "Joking! I wouldn't waste time on this schmuck."
    show jacob glad
    j "..."
    show jacob anxi
    j "{size=-10}Hold on a bit though, let me just write down their name...{/size}"
    show jacob joy
    j "I can think of better questions on the spot, like-"
    extend " like..."
    show jacob shoc
    j "Oh!"

    call s4q5 from _call_s4q5

label afterD5:
    scene bg park1
    show jacob glad
    with fade
    j "Maybe it's time {i}you{/i} start asking me some questions though."
    show jacob joy
    extend " It is a date after all, and things like that should be reciprocal.{nw}"
    menu:
        extend ""
        "...":
            pass
    show jacob glad
    j "Don't be shy, I usually don't bite. No wrong questions. really.{nw}"
    menu:
        extend ""
        "...Why do you-":
            pass
    scene black
    stop music
    hide screen moodcurrent
    pause(2.0)

    scene bg forest2
    show july angy
    with fade
    play music ah

    ju "Is this {b}{i}ANOTHER{/i}{/b} fucking tree? Jesus Christ, how many trees does a park even need to have?"
    show july annoy
    ju "Are- Are we just going around in circles? Bro, if Joss really is in trouble, than he better pay me back {b}BIG{/b} time for saving their ass."
    show july angy at left with move
    ju "Hank, I thought you said you knew this place like the back of your hand!?"
    show hank scare at right with dissolve
    h "I did!"
    show hank happ
    show july annoy
    extend " But then I got a manicure and-"
    show hank emba
    h "My hand is basically, like new now! It got so much prettier! You should get one too July! I really think it could help."
    show july distr
    ju "..."
    show hank scare
    show july annoy
    h "U-Um! Anyways! Yeah, so I kind of got distracted... and then more trees popped up in this park... Way more than I remember..."
    show hank upset
    h "Really, it's mother natures fault. This is why my dad supports global warming! Stupid trees! Your time is coming!"
    show july emb
    ju "Hank! You should never a blame a milf for {b}anything!{/b} So it's not Mother Nature's fault."
    show july annoy
    ju "Now focus! We need to look for Joss, and we can't do that if we're just wandering around the park in circles!"
    show hank happ
    h "Have you tried like- just sticking left? I mean like, Duh.  Everyone knows that when you're lost you stick left."
    show july distr
    ju "That's for mazes not-"
    show july shoc
    show hank shoc
    extend " Wait- wait, who's that? Does he have a knife?"
    show hank happ at offscreenleft with move
    stop music
    ju "Hank! Stay! Wai-{nw}"

    scene bg park1
    show jacob shoc
    show hank happ at right
    with pushright
    show screen moodcurrent
    play music hug

    h "OMG! Mr. Jacobson! Or? Mr. Jacob? I always forget, did you get married yet? Is it Mrs. Jacob now?"

    show jacob at left
    show hank at center
    with move
    show july shoc at right with moveinright

    ju "Hank!"
    j "Hank?{nw}"
    menu:
        extend ""
        "Hank.":
            pass

    show hank shoc
    h "Hank?{nw}"
    show hank emba
    extend " Oh! That's me!"
    show july nerv
    ju "Wait was that Joss?"
    show hank happ
    h "Look, I brought my friend July!"
    show july distr
    ju "No! Don't say my name you dumba-"
    show july emb
    ju "Ugh whatever, the covers blown anyways. Jesus Hank, I thought I already taught you about aliases."
    show hank shoc
    show jacob anxi
    h "Aliases sounds like Arianna though! And my heart is only big enough for one Arianna! Its... It's grande size... like a starducks drink."
    show july angy
    show hank shoc
    show jacob shoc
    ju "Hank! Joss! Get over here, what have I told you about strange men in parks?"
    show jacob angy
    j "What? I'm not strange!"
    ju "Yeah, but you're a man right? Even worse! Now back away from the Joss!"
    show jacob anxi
    j "Hey, hey you've got it all wrong. Me and your dear Joss are simply on a date. Not that it concerns you."
    show july emb
    ju "Yeah, not so fast. Like I'd believe that. A date? Really?"
    show jacob norm
    j "I'm sure they appreciate the gesture, but I'm also sure she's just as anxious to resume our little rendezvous. Now, if you'll excuse us."
    show july annoy
    ju "He can speak for himself! Joss, where'd you even meet this goober?{nw}"
    menu:
        extend ""
        "It's a long story...":
            pass
    show july norm
    show jacob anxi
    ju "We have time."

    call s4q7 from _call_s4q7

label afterD6:
    show july nerv
    ju "Joss, are you sure you feel safe around this guy?"
    ju "What's your play here dude?"
    show jacob glad
    j "Good question. I'd also like to know that."

    call s4q6 from _call_s4q6


label afterD7:

    j "Hey, meet me at the bridge..."
    show jacob anxi
    extend " Alone."
    show jacob norm
    j "I have something to tell you."
    menu:
        extend ""
        "Ok":
            pass
    stop music fadeout(2.0)
    scene bg bridge
    show jacob norm
    with fade
    play music dusk

    jump afterDQ7



label tease:
    stop music
    scene bg bridge
    show jacob glad
    j "..."
    play music ghost
    j "Can't have you knowing where I live and all..."
