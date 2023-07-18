## Answers for Date Night

#What is your name?
# Joss (++)
label s4q1r1:
    show jacob shoc
    j "Joss... Jacob. Nice pair of names, I think."
    show jacob glad
    j " Not to be too forward of course."
    show jacob joy
    j "You have a cool name,"
    show jacob norm
    extend " don’t think I’ve heard anything like that before."
    show jacob anxi
    j "Uh, good job..."
    j "On that..."
    return

#“...” (-)
label s4q1r2:
    show jacob glad
    j "What, tongue tied already?"
    show jacob joy
    extend " Didn’t know I was so charming."
    show jacob anxi
    j  "Seriously though, you’re going to have to work with me here.{nw}"
    menu:
        extend ""
        "...":
            pass
    show jacob fear
    j "Are you mad? I know it’s basic etiquette,"
    show jacob emomore
    extend " but considering the circumstances you’re going to have to cut me some slack.{nw}"
    menu:
        extend ""
        "Joss.":
            pass
    show jacob joy
    j "See? That wasn’t so hard was it?"
    show jacob glad
    j "Joss. Nice name."
    return

#Should’ve checked my ID (--)
label s4q1r3:
    show jacob mad
    j "{i}Don’t{/i} be a smartass."
    show jacob emomore
    j "You’re lucky I’m even asking."
    j "I’m sure you can guess, but I don't tend to get buddy-buddy with my captives."
    show jacob mad
    j  "Not enough to care about their names, anyways."
    menu:
            extend ""
            "...":
                pass
    show jacob angy
    j "Don’t be like that. C’mon, you’re just going to piss me off if you keep playing around."
    menu:
            extend ""
            "Joss.":
                pass
    show jacob joy
    j "Thank you."
    return

#What is your job?
# Umm... I’m an accountant (+)
label s4q2r1:
    show jacob shoc
    j "Oh, office guy huh?"
    show jacob glad
    extend " Wouldn’t have pegged you as one."
    show jacob joy
    j "I’d love to see someone like you in the office though, bet you’d be the prettiest one there."
    show jacob emo
    j "Absolutely adorable in your little suit and tie."
    show jacob glad
    j "The office sucks though, doesn’t it?"
    return

# I steal (-)
label s4q2r2:
    show jacob shoc
    j "As a living?"
    show jacob anxi
    j "Did you even try getting a job,"
    show jacob mad
    extend " or was that just the first thing that came to mind?"
    show jacob norm
    j "What about music or gardening or something?"
    show jacob angy
    j "Stealing isn’t as glamorous as you think."
    extend " Living like a criminal isn’t fun."
    show jacob emomore
    j "I don’t know where you got that idea from but take it from me."
    show jacob emo
    j "I remember my first murder-"
    show jacob anxi
    j "..."
    show jacob norm
    j "Y’know what? Nevermind. Let’s move on."
    return

# I work at wcdonalds (++)
label s4q2r3:
    show jacob anxi
    j "Wcdonalds?"
    menu:
        extend ""
        "Wctoleratin' it.":
            pass
    j "What?"
    menu:
        extend ""
        "I...":
            pass
    menu:
        extend ""
        "I have to say that or else they’ll fire me.":
            pass
    show jacob fear
    j "Wi- will they even know?"
    menu:
        extend ""
        "They’ll know.":
            pass
    show jacob anxi
    j "I was going to make a snarky comment, but now I just feel bad."
    j "I know we didn’t know each other before this but..."
    show jacob norm
    j "Whatever. I guess I understand why you stole from me now."
    show jacob angy
    j "That’s not a pardon by the way. I’m still pissed about that."
    return

#How do you go about choosing which people should be closest to you?
# “I have two.” (++)
label s4q3r1:
    show jacob shoc
    j "Two?{w} Two friends?"
    show jacob anxi
    j "Oh."
    show jacob glad
    extend " Great,"
    show jacob joy
    extend " glad you’re spoken for."
    show jacob joy
    j "I- uh- {w}never really had many friends growing up."
    show jacob anxi
    extend " If you couldn’t tell that it is."
    show jacob norm
    j "Well, that must be nice."
    return

#“I don’t like people.”(+)
label s4q3r2:
    show jacob glad
    j "Have I told you how much I like you?"
    show jacob joy
    extend " Short and sweet."
    show jacob glad
    j "Couldn’t have said it better myself."
    show jacob fear
    j "People are scary. I don’t like them either."
    show jacob anxi
    j "Still though, not having any friends is just a little bit pathetic isn’t it?"
    show jacob glad
    extend " Maybe we can make some together."
    show jacob norm
    j "Who knows though, I’d rather have one really good friend than 2 subpar ones."
    return

#How many friends do you have?”(--)
label s4q3r3:
    show jacob shoc
    j "Seesh {i}sorry{/i}, touchy subject huh? Didn’t mean to stab you where it hurts."
    show jacob glad
    j "Heh, join the club. Just don't be so defensive about it."
    show jacob norm
    extend " That’s where it turns from cool to pathetic."
    show jacob angy
    j "And then it turns from pathetic, to James."
    show jacob fear
    j "Just don’t tell him I said that, he scares even me sometimes."
    show jacob joy
    j "I could probably take him in a fight though."
    j "..."
    show jacob fear
    j "{size=-10} probably {/size}"
    return

#Well? “What makes you unique?
# I’m in a band (++)
label s4q4r1:
    show jacob shoc
    j "A band?"
    menu:
        extend ""
        "...Actually, not {i}my{/i} band.":
            pass
    show jacob norm
    j "..."
    menu:
        extend ""
        "A band I’m in.":
            pass
    show jacob glad
    j "No, no I get how it is."
    show jacob joy
    j "Music can be so personal, sometimes a band can really feel like you own it."
    show jacob glad
    j "I don’t blame you for being possessive, everyone is to a degree. Or to an extent."
    show jacob joy
    j "I play a few instruments."
    j "You already know about the drums, but I also dabble with the violin. Among others."
    show jacob glad
    j "Haha, maybe we can start a band together."
    j "I think we’d have a good gimmick. Jazz with violins and drums."
    return

# I’m good at stealing. (--)
label s4q4r2:
    show jacob angy
    j "Oh.{w} Oh you think thats funny, huh?"
    show jacob emomore
    j "Yeah, {i}yeah{/i}, you were good at it until you stole from {b}ME{/b}!"
    j "Maybe I should be grateful you suck at your ‘hobby’."
    show jacob angy
    j "You sure as hell seem happy about it."
    show jacob emomore
    j "Don’t make me regret taking you out,"
    show jacob piss
    extend " or I’ll really show you how I take people out!"
    show jacob norm
    j "..."
    j "Ugh. Stealing isn’t a personality trait."
    show jacob angy
    j "Fuck,"
    extend " it’s barely even a hobby. Not even a unique one at that!"
    show jacob glad
    j "You wanna know what I think? I think there’s more to you than that."
    show jacob joy
    j "There has to be more to you than that. And I’m saying this for your own sake."
    show jacob glad
    j "I see a little bit of myself in you."
    j " You’re... a diamond in the rough right?"
    j " I understand. You just need to be pressurized, sanded,"
    extend " and {i}cut{/i} before you can show this world your value."
    show jacob joy
    j "It’s worth it, in my experience anyways."
    j "The way I see it, you can go far when you commit yourself to something worthy.{w} Hell, {w}I know I did."
    j "..."
    return

# My fashion sense? (-)
label s4q4r3:
    show jacob anxi
    j "You don’t sound so sure about that. And your fashion sense doesn’t seem...{w} particularly unique... "
    menu:
        extend ""
        "Then nothing":
            pass
    show jacob glad
    j "C’mon there must be something."
    menu:
        extend ""
        "...":
            pass
    show jacob angy
    j "This website is fucking stupid anyways, I probably shouldn’t have bookmarked it."
    show jacob fear
    j "Uh- I only bookmarked it for-"
    show jacob shoc
    extend " to make fun of it,"
    show jacob joy
    extend " by the way."
    show jacob anxi
    j "I don’t actually use it for inspiration or anything."
    show jacob joy
    extend " Haha."
    j "That’d be.. Stupid. Haha."
    return

#If you could have any super power what would it be?
#What? (-)
label s4q5r1:
    show jacob angy
    j "Okay, okay cut me some slack."
    show jacob emo
    j "It wasn’t that bad of a question."
    show jacob norm
    j "Doubt you could do better. I’d like to see you try.{nw}"
    menu:
        extend ""
        "...":
            pass
    show jacob glad
    j "See? That's what I thought."
    return

# Invisibility (--)
label s4q5r2:
    show jacob anxi
    j "A stupider part of me wants to give you the benefit of the doubt..."
    show jacob angy
    j "but I just can’t shake the feeling you’re only going to use a power like that for crimes."
    j "Otherwise, what do you have to be so sneaky about huh?"
    show jacob joy
    j "C’mon, I thought we were over this phase of stealing."
    show jacob glad
    j "Do I need to kidnap you again? Or do you prefer worse?"
    return

# Flight (++)
label s4q5r3:
    show jacob norm
    j "..."
    j "That's..."
    show jacob glad
    extend " really cute actually."
    j "For some reason it makes me happy hearing you say that."
    show jacob joy
    j "Just promise me you won’t fly too close to the sun."
    show jacob glad
    extend " And don’t hang too low either, alright?"
    show jacob norm
    j "People usually forget about that part of the story"
    show jacob emo
    extend " but if you soar too low your wings will grow brittle and break."
    show jacob joy
    j "Just keep your chin up, stay out of trouble, and you’ll be fine."
    return
#Do you feel safe around me?
# Yes (++)
label s4q6r1:
    show jacob glad
    show hank happ
    show july annoy
    j "See?"
    j "Nothing wrong here."
    show jacob joy
    extend "I’m a completely reliable guy that would NEVER murder ANYONE."
    show jacob glad
    extend "{size=-10} Not even a little.{/size}"
    show jacob joy
    j "I wouldn’t even evade taxes, and I’m rich!"
    show july nerv
    ju "Well, I guess his morals are alright?"
    show hank emba
    h "Yeah, can you believe it? Everyone evades taxes!"
    show jacob anxi
    extend " My dad evades taxes!"
    show hank happ
    show july annoy
    ju "I’d still like to hear {i}your{/i} explanation about the knife though."
    show jacob joy
    j "I’m very cautious."
    extend " It is a park in the middle of the night after all."
    show jacob norm
    j "Who knows what lurks in these bushes. Like {i}ferrets{/i} or {i}bears{/i}."
    show hank terr
    show jacob shoc
    h "Yeah, or even... even streamers!"
    show july distr
    ju "Hank that’s so dumb."
    show jacob anxi
    show july nerv
    extend " Even for me."
    show hank scare
    h "You don’t know what those people can do July! Y’know they say it was a streamer who killed Kennedy?"
    show hank norm
    show july norm
    ju "Anyways,"
    show july emb
    extend " fine."
    ju "I guess that checks out."
    show july angy
    ju "Don’t think I won’t beat your ass if you do anything to Joss though."
    show jacob joy
    show july annoy
    j "Wouldn’t dream of it. Now if you’ll excuse us."
    show july nerv
    ju "Ugh..."
    show hank emba
    h "Bye-bye Mr. Jacob! See ya Joss!"
    hide july
    hide hank
    with moveoutright
    hide screen moodcurrent
    scene bg forest2
    show july nerv at left
    show hank norm at right
    with pushleft
    #follow h&ju
    show hank emba
    h "Oh they grow up so fast don’t they?"
    ju "Yeah... I still don’t like that guy though. Hope they don’t get too chummy."
    show july annoy
    ju "Hank you said you knew him? Tell me what you know."
    show hank happ
    h "Oh! Okay!"
    stop music fadeout(1.0)
    scene bg park1
    show jacob norm
    with pushright
    play music ghost
    j "..."
    return

# No (--)
label s4q6r2:
    show july angy
    show jacob shoc
    ju "I knew it!"
    show july annoy
    extend " There's no way Joss would be with some ugly old creep!"
    show hank happ
    h "Yeah!"
    show hank shoc
    extend " Wait, I thought that was exactly Joss’ type?"
    show july cocky
    ju "Only if they’re rich!"
    show jacob emomore
    j "I {i}am{/i} rich! Hey, wait a minute! I’m not old!"
    show july angy
    show jacob anxi
    ju "Yeah, and you aren’t beaten to a pulp either!"
    show july annoy
    extend " Not yet anyways!"
    show jacob angy
    j "Hey! Calm yourself."
    show jacob joy
    extend " We’re all friends here, right?"
    j "It’s not like I’m a murderer, we can talk rationally."
    show july angy
    ju "Oh I’m going to kick your ass back to the stone age."
    show july annoy
    ju "You better pray you can kill me with that knife in one go."
    stop music fadeout(1.0)
    show hank at right with move
    show jacob piss zorder 3 at center with move
    j "Hnng- Fuck!"
    show july shoc
    show jacob at right with move
    hide jacob with moveoutleft
    play music ah
    show hank at center with move
    show july distr
    "Jacob shoulders July before running off with you."
    ju "Agh!"

    scene bg forest2
    show jacob piss
    with fade
    #Fade to another park bg
    j "Were you {b}TRYING{/b} to get me caught, you little shit!?{nw}"
    menu:
        extend ""
        "...":
            pass
    show jacob angy
    j "Don't- Don’t answer that. Just don’t say anything right now."
    j "That {b}wasn’t{/b} funny."
    extend " You’re lucky I didn’t punt your little friend."
    show jacob anxi
    j "And the only reason I didn’t was because Hank was there."
    show jacob angy
    j "You better thank {b}GOD{/b} Hank was there.{nw}"
    menu:
        extend ""
        "And what if they find you?":
            pass
    show jacob glad
    j "Haha."
    j "That’s cute. You’re cute."
    show jacob joy
    j "I’m rich,"
    extend " I’ll be {i}more{/i} than fine."
    show jacob angy
    j "You didn’t achieve anything with that stunt."
    j "You on the other hand..."
    return

#... (-)
label s4q6r3:
    show jacob anxi
    j "Joss?"
    show july nerv
    ju "Joss say nothing if you’re scared."
    pause
    show july angy
    show jacob fear
    ju "See! Hank, get him!"
    show hank shoc
    h "Huh? Why? He seems pretty normal to me."
    show hank happ
    extend " That’s about usually what she always says anyways"
    show july annoy
    show jacob anxi
    ju "I-I... yeah I guess..."
    show july angy
    ju "That knife! Explain that knife then!"
    show jacob fear
    show july shoc
    j "Well, I’m sure you didn’t come empty-handed either am I right?"
    show jacob joy
    show july annoy
    j "You never know what kind of trouble you’ll find in the dark."
    show jacob glad
    j "Or what kind of trouble finds you."
    show july distr
    ju "Fuck, fine. Okay. I guess you would’ve said something if you were in trouble,"
    show july norm
    extend " right Joss?"
    show jacob anxi
    show july shoc
    show hank emba
    h "Yeah, maybe they're actually head over heels in love!"
    show jacob norm
    extend " She’s speechless!"
    show july annoy
    h "July! It’s true love don’t you see?"
    show jacob anxi
    show hank happ
    j "Uh- yeah-"
    j "We’ll have to continue our date if we want to see if we’ll get that far."
    show jacob glad
    j "Now if you’ll excuse us."
    hide jacob with moveoutleft
    show hank at left with move
    show july at center with move
    # joss and jacob walk off
    show july distr
    ju "Hnng..."
    show july angy
    ju "Hank, tell me everything you know about that guy. You’re sleeping over at my place tonight."
    show july
    show hank emba
    h "Yippee!!"
    show july annoy
    show hank norm
    h "Wait but your TV is smaller than mine..."
    extend " can we-"
    show july emb
    show hank emba
    ju"Fine, fine. We’re going to your place."
    hide hank with moveoutleft
    hide july with moveoutleft
    scene bg park1
    show jacob norm
    with fade
    return

#We met through...
#an app
label s4q7r1:
    show hank shoc
    show july shoc
    show jacob shoc
    h "Grndr?"
    j "Grndr?"
    menu:
        extend ""
        "Yes. Grndr.":
            pass
    show hank emba
    show july emb
    h "Omg good for you! Love is love!"
    show hank happ
    h "I’m glad you’re getting back out there, even old people deserve love"
    show jacob angy
    show july annoy
    j "I’m not {i}that{/i} old."
    show jacob anxi
    show hank emba
    h "Oh lemme see your account!"
    show july norm
    show hank happ
    extend "I wanna see how old you are!"
    menu:
        extend ""
        "He got suspended.":
            pass
    show jacob angy
    show hank emba
    h "Oh same!"
    show jacob anxi
    show july nerv
    show hank happ
    h "Yeah apparently you can't set people up with each other?"
    show jacob fear
    h "They said I couldn’t give people’s addresses out to other people,"
    show july emb
    extend " but it's not my fault I’m so compassionate!!"
    h "I just felt so bad for the ugly guys! They deserve love too."
    show jacob anxi
    h "I think."
    show july annoy
    ju "And you guys decided to meet at a park?"
    extend " At {i}night{/i}"
    show jacob joy
    j "Naturally."
    menu:
        extend ""
        "Yes.":
            pass
    show jacob shoc
    show july shoc
    ju "Oh."
    show july norm
    ju "{i}Oohh{/i}. Nice."
    show hank norm
    ju "And I assume the knife is for..."
    show july cocky
    ju "Damn Joss, didn’t think you were into that."
    show july happy
    ju "Well! Good for you, you bagged a dilf. Don’t let us get in your way."
    show july nerv
    ju "...But"
    return

#a basement
label s4q7r2:
    show july angy
    ju "Hank, close your eyes."
    show jacob fear
    show hank shoc
    j "No! No! What he means is a bar..."
    show jacob glad
    show july emb
    extend " called The {i}Basement{/i}!"
    show jacob angy
    show hank emba
    j "{size=-10}C’mon work with me here. I {b}really{/b} don’t feel like having to kill three people. And I actually like Hank.{/size}"
    show hank happ
    h "Oh I love that place! The guys they hire there are {i}so{/i} hot!"
    show hank emba
    h "And the DJ is SO nice! He let me play {i}7 Rings{/i} for 2 hours once after I got him like super drunk!"
    menu:
        extend ""
        "Yeah... that bar.":
            pass
    show jacob angy
    j "Hank! Don’t go to places like that!"
    show hank norm
    h "But the guys call me pretty whenever I give them money!"
    show jacob shoc
    j "Oh they do, do they?"
    show jacob angy
    j "{size=-10}Seems like I have more people to visit.{/size}"
    j "Just don’t go near that place, only creeps hang out there."
    show jacob anxi
    j "Um. except me of course. I only go there to uh-"
    show jacob glad
    j "The food is good. Love the bowl full of nuts they put on the bar."
    show hank emba
    h "Yeah, I love the nuts there too!"
    show jacob shoc
    show july angy
    show hank shoc
    j "Hank!{nw}"
    ju "Hank!"
    ju "Hank, I’ll deal with you later."
    show july annoy
    ju "{i}You{/i}."
    extend " Jacob was it? {i}You{/i} are a strange, {b}strange{/b}, little man."
    return

#hank
label s4q7r3:
    show july shoc
    show jacob fear
    show hank emba
    ju "Hank?"
    show july nerv
    extend " Hank, how many old rich men do you know?"
    ju " Do you just keep them in your back pocket or something?"
    show july annoy
    extend " What the hell?"
    show hank upset
    show jacob anxi
    show july shoc
    h "No! The only rich man I love is my dad!"
    show hank norm
    show jacob glad
    show july annoy
    j "Um, but don’t you remember introducing us Hank?"
    extend " Remember,"
    show jacob anxi
    extend " it was for the..."
    extend " uh..."
    menu:
        extend ""
        "The drums":
            pass
    j "Right!"
    show jacob joy
    extend " The drums. And y’know, one thing led to another..."
    show hank emba
    show july emb
    h "Aww, and now you guys are getting married?"
    show jacob anxi
    show hank shoc
    j "No!"
    show jacob fear
    j "I mean- not yet? It’s too early for that."
    show hank emba
    h "Joss and Jacob sitting in a tree..."
    show jacob emomore
    show hank scare
    j "Shutup!"
    show jacob emo
    show hank norm
    ju "Ok. Ok. I guess that checks out. I remember that too."
    show jacob anxi
    show july annoy
    show hank shoc
    ju "Joss I thought you were going to steal it or something?"
    show hank happ
    ju "Did you just knock on the front door and ask?"
    menu:
        extend ""
        "Yes.":
            pass
    show july cocky
    ju "And here I thought I taught you better than that."
    show july happy
    ju "Well, nice to see it worked out."
    show jacob angy
    show july annoy
    j "You taught her that?"
    ju "You aren’t getting me to say anything unless a lawyer is present. I know my rights!"
    return
#hank fish eyes


    #continue to ending
