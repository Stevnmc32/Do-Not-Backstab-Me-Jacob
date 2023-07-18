# Responses to answers
# Now it's named properly!

## NOTE TO SELF: Add sprites later!
#Bix Is on the case!

# Set 1 Question 1 "Why did you break into my house?"
#"I thought it would be funny."
label s1q1r1:
    show jacob angy
    j "You thought it would be FUNNY to invade my privacy?!"
    show jacob norm
    j "Hmph."
    extend " Kids these days. They'll do anything for a crumb of attention."
    show jacob anxi
    j "You're just as bad as that damn red panda..."
    return

#"I need money."
label s1q1r2:
    show jacob norm
    j "Hm..."
    show jacob glad
    extend " I suppose you did have a motive behind this. I should've guessed by your raggedy clothes."
    show jacob norm
    j "I almost feel sorry for you."
    show jacob angy
    j "But others have far less. You took this out on someone else. No amount of money can hide that."
    return

#"You deserved it."
label s1q1r3:
    show jacob shoc
    j "How do {i}I{/i} deserve this?"
    show jacob angy
    j "I worked hard for my wealth and this house. I'm not some little lamb like you seem to think I am."
    show jacob emomore
    j "I work hard for the sake of EVERYONE. I'm not a selfish little child who takes their issues out on others."
    return


# Set 1 Question 2 "What are your thoughts on vegetarians?"
#"They're fine I guess..."
label s1q2r1:
    show jacob shoc
    j "Yeah! I don't get why people hate us!"
    show jacob joy
    j "We're just trying to live our lives, the pricks think they're sooo much better just cause they eat meat."
    return

#"They're annoying as hell."
label s1q2r2:
    show jacob angy
    j "Oh, you're one of THOSE people..."
    show jacob emomore
    j "Good to know you have no respect for my kind."
    show jacob angy
    j "So sorry that I physically can't eat meat, prick."
    return

# "I respect them."
label s1q2r3:
    show jacob glad
    j "Thank you, finally! We're just trying to live our lives."
    show jacob joy
    j "If only my neighbors were more like you. I hate living in a neighborhood full of carnivores."
    show jacob angy
    j "Always judging me for bringing casserole to the potluck... "
    show jacob fear
    extend "(Maybe they'll be next down here...)"
    return

#"You just want me to flatter you, huh sheep boy?"
#label s1q2r4:
#    show jacob emomore
#    j "You better watch your damn mouth! Listen here, you're going to play along, whether you want to or not."
#    show jacob angy
#    j "This isn't about flattery. This is about justice."
#    return


# Set 1 Question 3 "Do you think you deserve to die?"
#"Hell no!"
label s1q3r1:
    show jacob angy
    j "Of course. No one ever does. You're all the same."
    j "You always refuse to face the consequences of your actions. It's quite cowardly, really."
    show jacob glad
    j "Ah, but you'll repent either way. I'll make sure of it."
    return

#"Yeah..."
label s1q3r2:
    show jacob norm
    j "Hmm... I'm glad you're coming around."
    show jacob joy
    j "You understand that this is for the greater good."
    show jacob glad
    j "You agree that we can't have criminals running around free."
    extend " ...admirable of you."
    return

#"You're really pretentious."
label s1q3r3:
    show jacob emomore
    j "And how am I pretentious for bringing justice to the world?"
    show jacob angy
    j "The world would be a vile place without people like me."
    extend " A world full of people like you..."
    return


# Set 1 Question 4 "Do you think anyone truly 'deserves' to die?"
#"Of course not!"
label s1q4r1:
    show jacob angy
    j "Ah, but I disagree."
    extend " What about criminals, such as yourself,"
    extend " {i}thief?{/i}"
    show jacob emomore
    j "Murderers?"
    j "Terrorists?"
    j "Abusers?"
    show jacob angy
    j "They ruin the lives of others, then get to walk free and do it again?"
    j "No. They need to pay."
    return

#Absolutely. Some people don’t deserve to live."
label s1q4r2:
    show jacob glad
    j "Exactly my point. You seem to understand me pretty well..."
    return

#"Yes, but not me!"
label s1q4r3:
    show jacob angy
    j "Oh, you must think you're SO important then?"
    show jacob emomore
    j "Only YOU can get away with heinous acts, while everyone else can rot?"
    show jacob angy
    j "You're even more selfish than I thought..."
    return


# Set 1 Question 5 "What do you think about sheep?"
#"They're annoying and gross!"
label s1q5r1:
    show jacob angy
    j "Oh, you got some balls saying something like that right in front of one!"
    j "Are you stupid or something?"
    return

#"They're pretty cool."
label s1q5r2:
    show jacob norm
    j "I can tell your lying."
    show jacob angy
    j "I've heard that one before..."
    show jacob shoc
    j "But, I'm flattered..."
    return

#"They're really Ba-ad...."
label s1q5r3:
    show jacob angy
    j "That's so fucking stupid!"
    return
label s1q5r3A:
    show jacob anxi
    j "God, that's so dumb."
    show jacob glad
    j "...pfft."
    return


# Set 1 Question 6 "Do you value your life?"
#"Yes!"
label s1q6r1:
    show jacob anxi
    j "Sigh... expected."
    j "Moving on..."
    return

#"Not really."
label s1q6r2:
    j "As you shouldn't, thief."
    j "I'm sure there's more to unpack here, but I'm not your therapist,"
    extend " and frankly, I don't care."
    return

#"Why should I?"
label s1q6r3:
    show jacob joy
    j "Exactly. You shouldn't, thief."
    show jacob emomore
    j "You broke into my house."
    extend " You chose to attack another person, caring not for their wellbeing."
    show jacob angy
    j "You don't even care. There's not value in a life like that."
    return


# Set 2 Question 1 "Why do you think I want to kill you?"
#"Cause I broke into your house?"
label s2q1r1:
    show jacob emomore
    j "Yes, imbecile, you broke into my house."
    return

#label s2q1r2:
#    j "So I'M the asshole here?"
#    extend "For defending myself against someone who broke into myself?"
#    j "You think I kill without motive? I'm not a barbarian."
#    return

#"I'm assuming you don't like me?"
label s2q1r3:
    show jacob glad
    j "Gee, what gave you that impression?"
    show jacob angy
    j "No, I don't like you. You literally broke into my house."
    return

#"No idea!"
label s2q1r4:
    show jacob piss
    j "You LITERALLY broke into my house and expect me to believe that?"
    show jacob emomore
    j "Leave the gaslighting to me."
    return


# Set 2 Question 2 "Would you kill 10 people to save 100?"
#"Yes. It's for the greater good."
label s2q2r1:
    show jacob joy
    j "Indeed. I'll never understand this 'moral dilemma' about it that everyone goes on about. More lives are being saved."
    show jacob glad
    j "How is this a bad thing? Perhaps some are just too cowardly to do what's right."
    show jacob joy
    j "They just don't see how much good that a little murder can do. Not us though, huh?"
    return

#"No! That's still murder."
label s2q2r2:
    show jacob angy
    j "Tsk. Naive, really. Yes, it is still murder, but think of the impact!"
    show jacob piss
    j "What's the use of a few lousy lives if it means saving many more?"
    show jacob piss
    j "It's clearly a fair trade. Perhaps you're just too soft."
    return

#"Depends on who lives and who dies."
label s2q2r3:
    show jacob shoc
    j "I suppose that's true... I mean, we wouldn't want someone like me to die, would we?"
    j "There's no point in killing innocent people, leaving just the rotten ones."
    show jacob norm
    j "But at the end of the day, more lives are being saved... hm."
    return

#label s2q2r4:
#    j "And you're a filthy goddamn coward! You think I don't know what I'm doing, is that it?"
#    j "Do you think I'm some sort of amateur? I'm deadly serious about this. You're really testing my patience here, kid."
#    j "I'M the killer, and YOU'RE the victim. You should be grateful that I haven't ended your pathetic excuse for a life already."
#    return


# Set 2 Question 3 "What do you think I do for a living?"
# "Kill people?"
label s2q3r1:
    show jacob shoc
    j "Really?"
    show jacob angy
    extend " That's your best guess? How would I even make money off of this?"
    j "It's not like I sell organs or stream myself like a dumbass."
    show jacob anxi
    j "No, this is just..."
    show jacob glad
    extend " a hobby, you could say."
    return

#"Business stuff?"
label s2q3r2:
    show jacob shoc
    j "Well, either you know me better than I thought, or the outfit gave it away."
    show jacob norm
    j "Either way, yes."
    return

#"Hopefully not a barber"
label s2q3r3:
    show jacob emo
    j "What?"
    show jacob emomore
    j "WHAT?"
    show jacob piss
    j "I'LL HAVE YOU KNOW I'D MAKE A FANTASTIC BARBER, I SPEND HOURS EVERY DAY TAKING CARE OF MY WOOL"
    show jacob emo
    j "..."
    show jacob anxi
    j "moving on."
    return



# Set 2 Question 4 "Do you think one person's mistakes can define them?"
#"No. Nobody is perfect."
label s2q4r1:
    show jacob joy
    j "Well, you're right about that second part."
    j "Everyone makes mistakes, sure,"
    show jacob angy
    extend " but that doesn't change the impact that mistake has on others."
    show jacob norm
    j "You don't always get to say 'sorry' and expect everything to be alright."
    show jacob angy
    extend " You have to own up to it."
    return

#"Yes."
label s2q4r2:
    show jacob glad
    j "Mhm. Everyone makes mistakes, but some are far greater than others."
    show jacob angy
    j "And sometimes those mistakes can't be forgiven."
    return

#"I don't regret robbing you, by the way."
label s2q4r3:
    show jacob emomore
    j "GOD have you no shame?!"
    show jacob piss
    j "You're really starting to piss me off."
    show jacob angy
    extend " How can you not see your wrongdoings?"
    return


# Set 2 Question 5 "If you could, would you kill me?"
#"Yes, absolutely."
label s2q5r1:
    show jacob anxi
    j "Well, I can't say I blame you."
    show jacob glad
    extend " Still, it's sad to see how blind you are."
    show jacob angy
    j "This is for your own good. For the good of {b}EVERYONE.{/b}"
    return

#"No. It would make me just as bad."
label s2q5r2:
    show jacob glad
    j "Exactly. Killing those who do 'wrong' deeds in your eyes does nothing."
    show jacob joy
    j "It just adds another murderer to the population."
    show jacob anxi
    extend " ...wait."
    return

#"Literally who would say 'no'??"
label s2q5r3:
    show jacob angy
    j "Someone with {i}sense{/i}, perhaps?"
    show jacob piss
    j "Someone who values the comfort of others and knows their place in society?"
    show jacob norm
    extend " Good people."
    return

# Set 2 Question 6 "Are you scared of what I'll do to you?"
#"Yes."
label s2q6r1:
    show jacob glad
    j "Mhm... you should be."
    return

#"Nah."
label s2q6r2:
    show jacob shoc
    j "Literally how?"
    show jacob glad
    j "It’s okay,"
    show jacob norm
    extend " you can admit that you’re afraid of the man waving a knife in front of you literally saying"
    show jacob joy
    j "'I’m going to kill you'."
    show jacob norm
    extend " No one is gonna judge you."
    show jacob glad
    j "Except me."
    extend " And I’m already doing that."
    return

#"Not really. In fact, I think I'll enjoy this"
label s2q6r3:
    show jacob shoc
    j "..."
    show jacob glad
    extend " you're disgusting"
    return
#ADD DIALOGUE FOR SET 3
#Bix Is on the case!

#"Do you know who I am?"
# Set 3 Question 1

#"A serial killer?"
label s3q1r1:
    show jacob angy
    j "Very funny, smartass. Watch yourself, I don't like snarky people."
    return

#"Some rich dude I guess."
label s3q1r2:
    show jacob glad
    j "Clearly. How did you think I could afford a lavish house like this?"
    extend " You sure took notice."
    show jacob joy
    j "This room alone likely costs more money than you've seen in your entire life."
    show jacob glad
    j " Soundproof basements are far more expensive than you would think..."
    return

#"You're Jacob."
label s3q1r3:
    show jacob shoc
    j  "Huh. You did your research, then."
    show jacob fear
    j "You clearly aren't from around here, so how..."
    return


# Set 3 Question 2 "What is your biggest fear?"
#"This exact situation."
label s3q2r1:
    show jacob joy
    j "Well, how unfortunate for you! Frankly, it’s your own fault."
    show jacob glad
    j "You’re getting exactly what you deserve."
    show jacob joy
    j "You could even call it your personal hell! I’ve outdone myself again"
    return


#"Hank"
label s3q2r3:
    show jacob shoc
    j "Really? My marshmallow of a neighbor?"
    #laugh animation here
    show jacob glad
    j "Baaaahaha!"
    show jacob joy
    j "He’s a big ol’ bear, but I don’t think he could hurt a fly if he even tried. He’s pathetic."
    return


#"Dying alone."
label s3q2r4:
    show jacob norm
    j "Yeah, don’t we all, buddy..."
    return


# Set 3 Question 3 "Do you think your family will miss you? Your friends?"
#"Yes! They would never abandon me!"
label s3q3r1:
    show jacob glad
    j "How sweet."
    show jacob norm
    extend " Unfortunately that they’ll never know what happened to you."
    return

#"Probably not."
label s3q3r2:
    show jacob shoc
    j "That’s a relief."
    show jacob fear
    j "Good to know that I won’t have to worry too much about getting involved with a case or anything."
    show jacob joy
    j "Not that they would catch me anyway..."
    return


#"Does your family miss you?"
label s3q3r3:
    show jacob emo
    j "... No."
    show jacob anxi
    extend " No they do not."
    return


# Set 3 Question 4  "Do you think someone will come rescue you?"
#"Yes! I bet they’re on their way right now!"
label s3q4r1:
    show jacob glad
    j "Oh, how cute."
    show jacob joy
    j "As if anyone even knows that you’re down here."
    show jacob angy
    j "No,"
    show jacob joy
    extend " it’s just you and me."
    return


#"I don’t {b}want{/b} anyone to rescue me."
label s3q4r3:
    show jacob shoc
    j "Fascinating..."
    show jacob glad
    j "You’ve accepted your fate I see?"
    extend " Or maybe you just like spending time with me?"
    show jacob joy
    j "Either way, I’m glad to know you won’t even try to struggle."
    return


#"I don't {b}need{/b} anyone to rescue me"
label s3q4r4:
    show jacob glad
    j "Ah, you think you can get yourself out of this?"
    show jacob angy
    extend " Do you think I’m an idiot or something?"
    j "You’re not getting out of those ropes, let alone out of this house."
    show jacob glad
    j "It would be pretty funny to see you try, but we’ve got business to do."
    return


# Set 3 Question 5 "Do you believe in a perfect society?"
#"No, that's impossible."
label s3q5r1:
    show jacob glad
    j "Nonsense."
    show jacob joy
    j " It’s not as much of a feat as you might think."
    show jacob glad
    extend " What causes all the problems in society?"
    show jacob angy
    j "Cowards."
    extend "Criminals."
    show jacob piss
    extend " If there were no wrongdoers like {i}you{/i},"
    show jacob angy
    j "life could be peaceful for those who deserve it."
    show jacob norm
    extend " Life would be good..."
    return

#"Yes"
label s3q5r2:
    show jacob shoc
    j "You get it then, yeah?"
    show jacob angy
    extend " A perfect society doesn’t have criminals."
    show jacob glad
    j "I’m doing this to help society."
    extend " That’s all I want."
    extend " A better society,"
    extend " yes."
    show jacob joy
    j "Those who deserve life deserve to live a just one."
    return

#"We already live in a perfect society."
#do funky stuff with the sprite
label s3q5r3:
    show jacob piss
    j "How could you possibly think this is a perfect society?"
    show jacob emomore
    extend " Do you not see all the injustice?"
    extend " Crimes unpunished?"
    j "The government not lifting a finger to help?"
    show jacob angy
    j "No,"
    extend " the only perfect society is one where people like this pay for their actions."
    j "And I see that look on your face."
    extend " Don't you start with that whole,"
    show jacob joy
    j "'oh, but JACOB,"
    extend " you can't have the good without the bad!"
    extend " What would be the point of living then?'"
    show jacob angy
    j "bullshit."
    j "There's no point in living when your life can be ruined at any moment and no one cares."
    return

# Set 3 Question 6 "Do you enjoy this?"
#"...yes."
label s3q6r1:
    show jacob anxi
    j "...degenerate."
    return

#"Gross, no."
label s3q6r2:
    show jacob shoc
    j "I’m surprised."
    show jacob norm
    extend " You’re taking this whole situation fairly well."
    return

#"And what if I do?"
label s3q6r3:
    show jacob fear
    j "... next question."
    return


# Question 7 "Do you think I'm bad person?"
#"Yes."
label q7r1:

    show jacob joy
    j "Well now, I think we've been through enough here to prove that I am not."
    show jacob angy
    j "Give me one good reason why I'm a bad person."
    show jacob shoc
    j "Because I kill people? "
    show jacob angy
    extend " Because I tie them up in my basement and interrogate them with “pointless” questions?"
    show jacob emomore
    j "{b}THOSE{/b} are bad people! I'm doing you and everyone else a favor!"
    show jacob angy
    j "In fact, you should be {b}THANKING{/b} me!"
    show jacob piss
    j "I'm tired of everyone misunderstanding me."
    show jacob emo
    j "I'm doing the right thing."
    j "You're all just too cowardly to understand."
    show jacob fear
    j "Always too meek... "
    extend " never able to take action."
    j "Never able to help people, even when they beg you to. They do nothing."
    show jacob emo
    j "..."
    j "They did nothing..."
    j "No one should have to go through that. "
    show jacob emomore
    extend " And I'll make sure no one does."
    show jacob shoc
    j "Uh..."
    return


label q7r2:
    show jacob glad
    j "Yes..."
    extend " yes you are right. I'm not a bad person."
    show jacob joy
    j "As I've said time and time again, I am helping people. I'm keeping dangerous people like you out of {b}society{/b}."
    show jacob shoc
    j "Though maybe..."
    show jacob glad
    extend " maybe you aren't so dangerous after all."
    j "You understand me, or at least you understand me more than any of my other victims. You understand that this is for the greater good."
    show jacob emo
    j "That... is this what's right. It's right to hurt those who hurt others. It's the only way to keep ourselves safe."
    j "We can't just shy away and expect everything to be okay and that someone else will solve our problems for us."
    show jacob joy
    j "We're almost like heroes in that way, yeah? We're protecting society and everyone is none the wiser."
    j "Even you, agreeing with me, choosing to die... it's almost heroic."
    show jacob angy
    j " ...I am {b}NOT{/b} a bad person. "
    show jacob glad
    extend "{b} I'm a damn hero.{/b}"
    show jacob shoc
    j "Oh! Uh..."
    return

label q7r3:
    show jacob shoc
    j "Oh, uh..."
    show jacob emo
    extend " ok."
    return









#
