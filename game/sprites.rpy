## Sprites for the characters

## Jacob Sprites ##############################################################
# This is how Jacob's sprites move

#Normal Sprite
image jacob norm:
    "images/jacob/norm/jacob_n1.png"
    zoom 0.95
    pause 1.0
    "images/jacob/norm/jacob_n2.png"
    pause 1.0
    "images/jacob/norm/jacob_n3.png"
    pause 1.0
    repeat

#Mad Sprite
image jacob mad:
    "images/jacob/mad/jacob_mad1.png"
    zoom 0.95
    pause 1.0
    "images/jacob/mad/jacob_mad3.png"
    pause 1.0
    repeat

#Angry Sprite
image jacob angy:
    "images/jacob/mad/jacob_mad1.png"
    zoom 0.95
    pause 1.0
    "images/jacob/mad/jacob_mad2.png"
    pause 0.3
    "images/jacob/mad/jacob_mad3.png"
    pause 1.0
    repeat

#Glad Sprite
image jacob glad:
    "images/jacob/glad/jacob_glad1.png"
    zoom 0.95
    pause 1.0
    "images/jacob/glad/jacob_glad2.png"
    pause 1.0
    "images/jacob/glad/jacob_glad3.png"
    pause 1.0
    repeat

#Shocked Sprite
image jacob shoc:
    "images/jacob/shoc/jacob_shoc1.png"
    zoom 0.95
    pause 1.0
    "images/jacob/shoc/jacob_shoc2.png"
    pause 1.0
    "images/jacob/shoc/jacob_shoc3.png"
    pause 1.0
    repeat

#Anxious Sprite
image jacob anxi:
    "images/jacob/anxi/jacob_anxi1.png"
    zoom 0.95
    pause 1.0
    "images/jacob/anxi/jacob_anxi2.png"
    pause 1.0
    "images/jacob/anxi/jacob_anxi3.png"
    pause 1.0
    repeat

#Emotional Sprite
image jacob emo:
    "images/jacob/emo/jacob_emo1.png"
    zoom 0.95
    pause 1.0
    "images/jacob/emo/jacob_emo2.png"
    pause 1.0
    "images/jacob/emo/jacob_emo3.png"
    pause 1.0
    repeat

#Emotional but More Sprite
image jacob emomore:
    "images/jacob/emomore/jacob_emomoe1.png"
    zoom 0.95
    pause 1.0
    "images/jacob/emomore/jacob_emomoe2.png"
    pause 1.0
    "images/jacob/emomore/jacob_emomoe3.png"
    pause 1.0
    repeat

#Fear Sprite
image jacob fear:
    "images/jacob/fear/jacob_fear1.png"
    zoom 0.95
    pause 1.0
    "images/jacob/fear/jacob_fear2.png"
    pause 1.0
    "images/jacob/fear/jacob_fear3.png"
    pause 1.0
    repeat

#Joy Sprite
image jacob joy:
    "images/jacob/joy/jacob_joy1.png"
    zoom 0.95
    pause 1.0
    "images/jacob/joy/jacob_joy2.png"
    pause 1.0
    "images/jacob/joy/jacob_joy3.png"
    pause 1.0
    repeat

#Piss Sprite
image jacob piss:
    "images/jacob/piss/jacob_piss1.png"
    zoom 0.95
    pause 1.0
    "images/jacob/piss/jacob_piss2.png"
    pause 1.0
    "images/jacob/piss/jacob_piss3.png"
    pause 1.0
    repeat

#Current Sprite matching with his Mood
image jacob curr:
    ConditionSwitch (
        "jmood == 14", "jacob norm",
        "jmood < 14", "jacob mad",
        "jmood > 14", "jacob glad",
    )

#Kill Sprite
image jacob kill = "images/jacob/jacob_KILL.png"

## I remember when Jacob was first designed, he was all I could think about for days...


## July Sprites ################################################################

# Normal Sprite
image july norm:
    "images/july/norm/july_norm1.png"
    zoom 0.95
    pause 1.0
    "images/july/norm/july_norm2.png"
    pause 1.0
    "images/july/norm/july_norm3.png"
    pause 1.0
    repeat

# Angry Sprite
image july angy:
    "images/july/angry/july_angy1.png"
    zoom 0.95
    pause 1.0
    "images/july/angry/july_angy2.png"
    pause 1.0
    "images/july/angry/july_angy3.png"
    pause 1.0
    repeat

# Annoyed Sprite
image july annoy:
    "images/july/annoy/july_annoy1.png"
    zoom 0.95
    pause 1.0
    "images/july/annoy/july_annoy2.png"
    pause 1.0
    "images/july/annoy/july_annoy3.png"
    pause 1.0
    repeat

# Cocky Sprite
image july cocky:
    "images/july/cocky/july_cock1.png"
    zoom 0.95
    pause 1.0
    "images/july/cocky/july_cock2.png"
    pause 1.0
    "images/july/cocky/july_cock3.png"
    pause 1.0
    repeat

# Distressed Sprite
image july distr:
    "images/july/distr/july_distress1.png"
    zoom 0.95
    pause 1.0
    "images/july/distr/july_distress2.png"
    pause 1.0
    "images/july/distr/july_distress3.png"
    pause 1.0
    repeat

# Embaressed Sprite
image july emb:
    "images/july/emb/july_emb1.png"
    zoom 0.95
    pause 1.0
    "images/july/emb/july_emb2.png"
    pause 1.0
    "images/july/emb/july_emb3.png"
    pause 1.0
    repeat

# Happy Sprite
image july happy:
    "images/july/happy/july_happy1.png"
    zoom 0.95
    pause 1.0
    "images/july/happy/july_happy2.png"
    pause 1.0
    "images/july/happy/july_happy3.png"
    pause 1.0
    repeat

# Nervous Sprite
image july nerv:
    "images/july/nerv/july_nerv1.png"
    zoom 0.95
    pause 1.0
    "images/july/nerv/july_nerv2.png"
    pause 1.0
    "images/july/nerv/july_nerv3.png"
    pause 1.0
    repeat

# Shocked Sprite
image july shoc:
    "images/july/shoc/july_shoc1.png"
    zoom 0.95
    pause 1.0
    "images/july/shoc/july_shoc2.png"
    pause 1.0
    "images/july/shoc/july_shoc3.png"
    pause 1.0
    repeat


## It took me and Soundskies like 2 hours to design her LMAO

## tHANK u, next SPRITES ##00110111 00100000 01110010 01101001 01101110 01100111 01110011

# Normal Sprite
image hank norm:
    zoom 0.95
    "images/hank/norm/hank_norm1.png"
    pause 1.0
    "images/hank/norm/hank_norm2.png"
    pause 1.0
    "images/hank/norm/hank_norm3.png"
    pause 1.0
    repeat

# Happy Sprite
image hank happ:
    zoom 0.95
    "images/hank/happy/hank_happ1.png"
    pause 1.0
    "images/hank/happy/hank_happ2.png"
    pause 1.0
    "images/hank/happy/hank_happ3.png"
    pause 1.0
    repeat

# Embarrassed Sprite
image hank emba:
    zoom 0.95
    "images/hank/emba/hank_emba1.png"
    pause 1.0
    "images/hank/emba/hank_emba2.png"
    pause 1.0
    "images/hank/emba/hank_emba3.png"
    pause 1.0
    repeat

# Scared Sprite
image hank scare:
    zoom 0.95
    "images/hank/scare/hank_scare1.png"
    pause 1.0
    "images/hank/scare/hank_scare2.png"
    pause 1.0
    "images/hank/scare/hank_scare3.png"
    pause 1.0
    repeat

# Shocked Sprite
image hank shoc:
    zoom 0.95
    "images/hank/shoc/hank_shoc1.png"
    pause 1.0
    "images/hank/shoc/hank_shoc2.png"
    pause 1.0
    "images/hank/shoc/hank_shoc3.png"
    pause 1.0
    repeat

# Upset Sprite
image hank upset:
    zoom 0.95
    "images/hank/upset/hank_upset1.png"
    pause 1.0
    "images/hank/upset/hank_upset2.png"
    pause 1.0
    "images/hank/upset/hank_upset3.png"
    pause 1.0
    repeat

# Fucked Sprite
image hank fuck:
    zoom 0.95
    "images/hank/fuck/hank_f1.png"
    pause 1.0
    "images/hank/fuck/hank_f2.png"
    pause 1.0
    "images/hank/fuck/hank_f3.png"
    pause 1.0
    repeat

# Terrified Sprite
image hank terr:
    zoom 0.95
    "images/hank/terr/hank_terr1.png"
    pause 1.0
    "images/hank/terr/hank_terr2.png"
    pause 1.0
    "images/hank/terr/hank_terr3.png"
    pause 1.0
    repeat

# Roar Sprite
image hank roar:
    zoom 0.95
    "images/hank/roar/hank_roar1.png"
    pause 1.0
    "images/hank/roar/hank_roar2.png"
    pause 1.0
    "images/hank/roar/hank_roar3.png"
    pause 1.0
    repeat

image hank ph:
    zoom 0.62
    "images/hank/hank_ph.png"


## James Sprites ###############################################################

# Normal Sprite
image james norm:
    zoom 0.95
    "images/james/norm/james_norm1.png"
    pause 1.0
    "images/james/norm/james_norm2.png"
    pause 1.0
    "images/james/norm/james_norm3.png"
    pause 1.0
    repeat

# Annoyed Sprite
image james annoy:
    zoom 0.95
    "images/james/annoy/james_annoy1.png"
    pause 1.0
    "images/james/annoy/james_annoy2.png"
    pause 1.0
    "images/james/annoy/james_annoy3.png"
    pause 1.0
    repeat

# Happy Sprite
image james happ:
    zoom 0.95
    "images/james/happ/james_happ1.png"
    pause 1.0
    "images/james/happ/james_happ2.png"
    pause 1.0
    "images/james/happ/james_happ3.png"
    pause 1.0
    repeat

# Pog1 Sprite
image james pog1:
    zoom 0.95
    "images/james/pog/james_pog1.png"
    pause 1.0
    "images/james/pog/james_pog2.png"
    pause 1.0
    "images/james/pog/james_pog3.png"
    pause 1.0
    repeat

# Pog2 Sprite
image james pog2:
    zoom 0.95
    "images/james/pog/james_pog4.png"
    pause 1.0
    "images/james/pog/james_pog5.png"
    pause 1.0
    "images/james/pog/james_pog6.png"
    pause 1.0
    repeat

# Pog3 Sprite
image james pog3:
    zoom 0.95
    "images/james/pog/james_pog1.png"
    pause 1.0
    "images/james/pog/james_pog2.png"
    pause 1.0
    "images/james/pog/james_pog3.png"
    pause 1.0
    "images/james/pog/james_pog4.png"
    pause 0.1
    "images/james/pog/james_pog5.png"
    pause 0.1
    repeat

# Skeptical Sprite
image james skep:
    zoom 0.95
    "images/james/skep/james_skep1.png"
    pause 1.0
    "images/james/skep/james_skep2.png"
    pause 1.0
    "images/james/skep/james_skep3.png"
    pause 1.0
    repeat

# Smug Sprite
image james smug:
    zoom 0.95
    "images/james/smug/james_smug1.png"
    pause 1.0
    "images/james/smug/james_smug2.png"
    pause 1.0
    "images/james/smug/james_smug3.png"
    pause 1.0
    repeat

# Bonus Sprite
image james bonus:
    zoom 0.95
    "images/james/z/james_asdf1.png"
    pause 0.1
    "images/james/z/james_asdf2.png"
    pause 0.3
    "images/james/z/james_asdf3.png"
    pause 0.2
    "james norm"
    repeat

# Neutral Sprite
image james neu:
    zoom 0.95
    "images/james/_neu/james_neu1.png"
    pause 1.0
    "images/james/_neu/james_neu2.png"
    pause 1.0
    "images/james/_neu/james_neu3.png"
    pause 1.0
    repeat

# Angry Sprite
image james angry:
    zoom 0.95
    "images/james/_angy/james_angy1.png"
    pause 1.0
    "images/james/_angy/james_angy2.png"
    pause 1.0
    "images/james/_angy/james_angy3.png"
    pause 1.0
    repeat

# Laughing Sprite
image james laug:
    zoom 0.95
    "images/james/_laug/james_laug1.png"
    pause 1.0
    "images/james/_laug/james_laug2.png"
    pause 1.0
    "images/james/_laug/james_laug3.png"
    pause 1.0
    repeat

# Upset Sprite
image james ups:
    zoom 0.95
    "images/james/_ups/james_ups1.png"
    pause 1.0
    "images/james/_ups/james_ups2.png"
    pause 1.0
    "images/james/_ups/james_ups3.png"
    pause 1.0
    repeat

# Screaming Sprite
image james scre:
    zoom 0.95
    "images/james/_scre/james_scre1.png"
    pause 1.0
    "images/james/_scre/james_scre2.png"
    pause 1.0
    "images/james/_scre/james_scre3.png"
    pause 1.0
    repeat


## Joss Sprites ################################################################

# Normal Sprite
image joss norm:
    zoom 0.95
    "images/joss/norm/joss_norm1.png"
    pause 1.0
    "images/joss/norm/joss_norm2.png"
    pause 1.0
    "images/joss/norm/joss_norm3.png"
    pause 1.0
    repeat

# Happy Sprite
image joss happ:
    zoom 0.95
    "images/joss/happ/joss_happ1.png"
    pause 1.0
    "images/joss/happ/joss_happ2.png"
    pause 1.0
    "images/joss/happ/joss_happ3.png"
    pause 1.0
    repeat

# Upset Sprite
image joss upse:
    zoom 0.95
    "images/joss/upse/joss_upse1.png"
    pause 1.0
    "images/joss/upse/joss_upse2.png"
    pause 1.0
    "images/joss/upse/joss_upse3.png"
    pause 1.0
    repeat

# Nervous Sprite
image joss nerv:
    zoom 0.95
    "images/joss/nerv/joss_nerv1.png"
    pause 1.0
    "images/joss/nerv/joss_nerv2.png"
    pause 1.0
    "images/joss/nerv/joss_nerv3.png"
    pause 1.0
    repeat



#
