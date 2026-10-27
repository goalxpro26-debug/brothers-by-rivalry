# Brothers by Rivalry — Part 1.
# An original visual novel. Two boys, one girl, a rivalry that becomes
# a brotherhood — and a parting nobody explains. (Part 1 ends there.)
# Characters are university students, all aged 20-21.

define aarav = Character(_("Aarav"), color="#ffb347", image="aarav")
define kabir = Character(_("Kabir"), color="#9ecbff", image="kabir")
define meera = Character(_("Meera"), color="#ff8fab", image="meera")

# Rivalry and bond decide how the parting feels in Part 1.
# Neither can stop the parting itself — that is the mystery of Part 2.
default rivalry = 0
default bond = 0
default meera_trust = 0

image bg town = "images/bg town.jpg"
image bg cafe = "images/bg cafe.jpg"
image bg festival = "images/bg festival.jpg"
image bg station = "images/bg station.jpg"
image bg rain = "images/bg rain.jpg"
image bg bridge = "images/bg bridge.jpg"

# Framed side portraits (rectangular busts, scaled to sit beside the textbox).
image side aarav neutral = Transform("images/aarav neutral.png", size=(220, 220))
image side aarav smile = Transform("images/aarav smile.png", size=(220, 220))
image side aarav angry = Transform("images/aarav angry.png", size=(220, 220))
image side kabir neutral = Transform("images/kabir neutral.png", size=(220, 220))
image side kabir smile = Transform("images/kabir smile.png", size=(220, 220))
image side kabir concerned = Transform("images/kabir concerned.png", size=(220, 220))
image side meera neutral = Transform("images/meera neutral.png", size=(220, 220))
image side meera smile = Transform("images/meera smile.png", size=(220, 220))
image side meera concerned = Transform("images/meera concerned.png", size=(220, 220))

label start:
    scene bg town
    with fade
    play music "audio/sfx/town-evening.mp3" loop

    voice "audio/voice/line001.mp3"
    "It starts the way most good stories start — not with a plan, but with a song spilling out of a café door on a warm summer evening."

    voice "audio/voice/line002.mp3"
    "The café is called The Third Seat. It has three tables by the window, and on open-mic nights, only two of them ever stay empty for long."

    voice "audio/voice/line003.mp3"
    "Meera runs those nights. She is twenty, she makes terrible jokes about the coffee, and she remembers everyone's song, even the ones they are too shy to finish."

    scene bg cafe
    with dissolve

    voice "audio/voice/line004.mp3"
    meera smile "Welcome in. If you're here to sing, the list is on the counter. If you're here to hide, the corner table is free."

    voice "audio/voice/line005.mp3"
    "Two boys walk in that summer. Not together. Not yet. And neither of them knows the other exists."

    menu:
        "Whose story do you follow first?"

        "Aarav — the loud one.":
            jump aarav_first

        "Kabir — the quiet one.":
            jump kabir_first

label aarav_first:
    voice "audio/voice/line006.mp3"
    aarav smile "Okay, okay — I know, I know. I'm late. But I brought the good kind of late. The kind with a song."

    voice "audio/voice/line007.mp3"
    "Aarav does not enter rooms. He arrives in them. Loud laugh, open jacket, a guitar case that has seen better decades and better jokes."

    voice "audio/voice/line008.mp3"
    aarav smile "Meera! One terrible coffee, please. And don't pretend you didn't save me the corner table."

    voice "audio/voice/line009.mp3"
    meera smile "I didn't save it. It saved itself. It knew you'd be loud enough for the whole street."

    voice "audio/voice/line010.mp3"
    aarav neutral "That's fair. That's completely fair. I am loud. But listen — I wrote something new, and I need one honest person to hear it first."

    voice "audio/voice/line011.mp3"
    "He plays, and he is not as careless as he looks. Under the jokes, the song is careful. It is about wanting to be chosen, not just noticed."

    voice "audio/voice/line012.mp3"
    meera neutral "Aarav. That was... actually good. Don't ruin it by making a joke right now."

    voice "audio/voice/line013.mp3"
    aarav smile "Too late. I already thought of one. I'm just being polite and not saying it."

    $ meera_trust += 1
    jump kabir_arrives

label kabir_first:
    voice "audio/voice/line014.mp3"
    "Kabir does not enter rooms either. He slips into them, the way rain slips into a street — quietly, and then suddenly everywhere."

    voice "audio/voice/line015.mp3"
    kabir neutral "One tea. No sugar. And... is the list still open?"

    voice "audio/voice/line016.mp3"
    meera smile "It is. Corner table, if you want it. You look like a corner-table person."

    voice "audio/voice/line017.mp3"
    kabir neutral "I am. I brought something. It's not finished. It probably never will be. But it has a middle that I like."

    voice "audio/voice/line018.mp3"
    "He does not perform. He just plays, eyes down, as if the song is a private thing he accidentally let everyone hear."

    voice "audio/voice/line019.mp3"
    "It is about a town he is afraid to leave, and a person he is afraid to stay for."

    voice "audio/voice/line020.mp3"
    meera smile "Kabir. Don't finish it yet. Some songs need to stay unfinished a little longer, so you keep coming back to them."

    voice "audio/voice/line021.mp3"
    kabir smile "Then I'll come back. That's... that's the plan, actually."

    $ meera_trust += 1
    jump aarav_arrives

label kabir_arrives:
    voice "audio/voice/line022.mp3"
    "A week later, Kabir arrives — and the corner table is not empty."

    voice "audio/voice/line023.mp3"
    kabir neutral "Oh. Someone is already... never mind. I'll take the other one."

    voice "audio/voice/line024.mp3"
    "He listens to Aarav sing, and he hates how good it is. Not because it is bad. Because it is honest, and honesty is supposed to be his thing."

    jump discovery

label aarav_arrives:
    voice "audio/voice/line025.mp3"
    "A week later, Aarav arrives — and the corner table is not empty."

    voice "audio/voice/line026.mp3"
    aarav neutral "Whoa. Okay. New guy. Playing my table's song, in my table's corner, with my table's light."

    voice "audio/voice/line027.mp3"
    "He listens to Kabir play, and he hates how good it is. Not because it is bad. Because it is quiet, and quiet is supposed to lose to loud."

    jump discovery

label discovery:
    scene bg cafe
    with dissolve

    voice "audio/voice/line028.mp3"
    meera smile "Oh, good. You're both here. Aarav, this is Kabir. Kabir, this is Aarav. You both sing on my nights, you both take my corner table, and you both —"

    voice "audio/voice/line029.mp3"
    "She stops. She sees it. Two boys, one look, one sudden, terrible understanding."

    voice "audio/voice/line030.mp3"
    aarav angry "Wait. You like her too?"

    voice "audio/voice/line031.mp3"
    kabir concerned "You... you like her too."

    voice "audio/voice/line032.mp3"
    meera concerned "Boys. Boys. I am standing right here. I am not a trophy, I am not a song, and I am not going to be the reason you two —"

    voice "audio/voice/line033.mp3"
    aarav angry "No, no, this is fine. This is perfect. We can settle this like adults. A competition. Whoever —"

    voice "audio/voice/line034.mp3"
    kabir neutral "No competition. That's not how this works. That's not how she works."

    voice "audio/voice/line035.mp3"
    "And that is where the fight starts. Not with fists. With stubbornness. His, loud. His, silent. Both absolute."

    menu:
        "The fight, round one. How does it go?"

        "Aarav makes it a loud public challenge.":
            $ rivalry += 2
            voice "audio/voice/line036.mp3"
            aarav angry "Fine! One month. Festival night. Whoever she chooses, the other one walks away. No hard feelings. Well — some hard feelings. But honourable ones."
            voice "audio/voice/line037.mp3"
            kabir concerned "I didn't agree to that. I never agree to things shouted at me."
            jump fight

        "Kabir refuses to play the game at all.":
            $ rivalry += 1
            voice "audio/voice/line038.mp3"
            kabir neutral "I'm not competing for a person. If you want to turn this into a contest, do it alone. I'll just... still be here. Every night. That's my answer."
            voice "audio/voice/line039.mp3"
            aarav angry "That's the most annoying answer possible. You know that, right? That's worse than losing."
            jump fight

        "Meera shuts it down before it starts.":
            $ meera_trust += 1
            voice "audio/voice/line040.mp3"
            meera concerned "Stop. Both of you. If you want my attention, earn it by being decent humans, not by winning a contest about me. Now sit down. Separate tables. And don't look at each other like that."
            voice "audio/voice/line041.mp3"
            "They sit down. Separate tables. And they look at each other exactly like that."
            jump fight

label fight:
    scene bg rain
    with vpunch

    voice "audio/voice/line042.mp3"
    "The rain starts that night, and it does not stop for days. The town smells like wet stone and bad decisions."

    voice "audio/voice/line043.mp3"
    "Aarav leaves five voice notes. Kabir leaves none, which somehow feels louder."

    voice "audio/voice/line044.mp3"
    aarav angry "He thinks silence makes him deep. It doesn't. It makes him unreadable, and unreadable is not the same as interesting."

    voice "audio/voice/line045.mp3"
    kabir concerned "He thinks volume makes him honest. It doesn't. It makes him hard to ignore, and hard to ignore is not the same as right."

    menu:
        "The next morning at the café, what happens?"

        "Aarav tries to out-sing Kabir, loudly.":
            $ rivalry += 2
            voice "audio/voice/line046.mp3"
            aarav smile "Watch this. I'm going to sing the song I wrote about her, right in front of him, and he's going to have to sit there and feel things."
            voice "audio/voice/line047.mp3"
            "He does. Kabir sits there. He feels things. He does not leave. That, more than the song, is what gets under Aarav's skin."
            jump forced_together

        "Kabir quietly fixes the café's broken speaker.":
            $ bond += 1
            voice "audio/voice/line048.mp3"
            "While Aarav is rehearsing his big moment, Kabir is under a table with a screwdriver, fixing the speaker nobody else noticed was dying."
            voice "audio/voice/line049.mp3"
            aarav neutral "Wait. You fixed that? I've been complaining about that speaker for a month."
            voice "audio/voice/line050.mp3"
            kabir neutral "Complaining is not fixing. Fixing is fixing."
            voice "audio/voice/line051.mp3"
            aarav smile "Okay. That was... annoyingly good. I hate that I respect that."
            jump forced_together

        "Meera makes them share one table.":
            $ bond += 1
            voice "audio/voice/line052.mp3"
            meera smile "One table left. You two can share it, or you can stand outside in the rain and be dramatic. Your choice. Dramatic is also an option. I'm just saying it's wet out there."
            voice "audio/voice/line053.mp3"
            "They share it. In silence. Then in sarcasm. Then, slowly, in actual conversation, because silence between two stubborn people gets boring faster than you'd think."
            jump forced_together

label forced_together:
    scene bg cafe
    with dissolve

    voice "audio/voice/line054.mp3"
    "And then Meera gives them the problem that changes everything."

    voice "audio/voice/line055.mp3"
    meera concerned "I need to tell you both something, and I need you to not make it about yourselves for five minutes. The landlord is selling the building. The festival is our last chance. If we don't fill the hall that night, The Third Seat closes."

    voice "audio/voice/line056.mp3"
    aarav neutral "Wait. Closes? Like... gone?"

    voice "audio/voice/line057.mp3"
    kabir concerned "When? How long do we have?"

    voice "audio/voice/line058.mp3"
    meera neutral "Three weeks. I need posters, a stage, performers, and money for the hall. I can't do it alone. And — I'm asking you both. Together."

    voice "audio/voice/line059.mp3"
    "Two rivals. One impossible job. No way out that doesn't involve each other."

    menu:
        "The festival mission. What do they take on first?"

        "Posters all over town — Aarav's loud plan.":
            $ bond += 1
            voice "audio/voice/line060.mp3"
            aarav smile "Posters! Every wall, every pole, every café window in town. If people don't come, it's because they were hiding under a rock, and I'll poster the rock too."
            voice "audio/voice/line061.mp3"
            kabir smile "I'll draw them. You shout about them. That's... actually a good division of labour. Don't let it go to your head."
            jump late_night

        "A stage built by hand — Kabir's quiet plan.":
            $ bond += 1
            voice "audio/voice/line062.mp3"
            kabir neutral "The stage is falling apart. If we rebuild it ourselves, we don't need to pay anyone, and people will come just to see if it holds."
            voice "audio/voice/line063.mp3"
            aarav smile "I love a plan that might collapse. Metaphorically. Not literally. Mostly not literally."
            voice "audio/voice/line064.mp3"
            "They build it. It holds. Barely. Proudly."
            jump late_night

        "Raising the hall money — together, door to door.":
            $ bond += 2
            voice "audio/voice/line065.mp3"
            meera smile "Door to door. Both of you. No arguing in front of donors. Smile, tell them about the café, and if you start competing, I will personally lock you in the storage room."
            voice "audio/voice/line066.mp3"
            "They argue in front of exactly one donor. Then they apologise together, in perfect, accidental unison, and the donor laughs and doubles the donation."
            jump late_night

label late_night:
    scene bg bridge
    with fade
    play music "audio/sfx/night-bridge.mp3" loop

    voice "audio/voice/line067.mp3"
    "Late one night, after the posters are up and the stage is standing, they end up on the bridge over the river, sharing terrible café coffee from a flask."

    voice "audio/voice/line068.mp3"
    aarav neutral "Can I ask you something, and can you not make it weird?"

    voice "audio/voice/line069.mp3"
    kabir neutral "I can try. No promises on the weird part."

    voice "audio/voice/line070.mp3"
    aarav neutral "Why her? Not — why do you like her. Why do you like her the way you do?"

    voice "audio/voice/line071.mp3"
    kabir smile "Because she listens like songs matter. And because she never asked me to be louder. Why you?"

    voice "audio/voice/line072.mp3"
    aarav smile "Because she laughed at my worst joke and then told me it was bad, to my face, kindly. Nobody does that. Everybody else just laughs."

    voice "audio/voice/line073.mp3"
    "Silence. Not the fighting kind. The good kind."

    menu:
        "On the bridge, what do they admit?"

        "Aarav admits he's scared of losing both of them.":
            $ bond += 2
            voice "audio/voice/line074.mp3"
            aarav neutral "I'm scared, okay? If she chooses you, I lose her. If she chooses me, I lose you. And I didn't know I could lose you, because three weeks ago I didn't even know you."
            voice "audio/voice/line075.mp3"
            kabir smile "You won't lose me. That's not how this works anymore. I think... I think we're stuck with each other now."
            jump festival_night

        "Kabir admits he was jealous, and it shamed him.":
            $ bond += 2
            voice "audio/voice/line076.mp3"
            kabir concerned "I was jealous of you. Not of your songs. Of how easy it is for you to be wanted. I thought quiet was better. It isn't better. It's just quieter."
            voice "audio/voice/line077.mp3"
            aarav smile "And I was jealous of you. Because you don't need applause to know you're good. I do. I really, really do."
            jump festival_night

        "They say nothing, and that's the honest part.":
            $ bond += 1
            voice "audio/voice/line078.mp3"
            "They say nothing for a long time. The river says enough for both of them. Sometimes the most honest thing two stubborn boys can do is sit still and not compete for one whole night."
            jump festival_night

label festival_night:
    scene bg festival
    with fade
    stop music
    play music "audio/sfx/festival-night.mp3" loop

    voice "audio/voice/line079.mp3"
    "Festival night. The hall is full. The stage holds. The posters worked, the money came in, and The Third Seat is, for one night at least, safe."

    voice "audio/voice/line080.mp3"
    meera smile "You did this. Both of you. Together. I don't know how to thank you without crying, so I'm going to thank you and also cry, and you're both going to pretend this is normal."

    voice "audio/voice/line081.mp3"
    aarav smile "We did it. Us. The loud one and the quiet one. The rivalry and the... whatever we are now."

    voice "audio/voice/line082.mp3"
    kabir smile "Brothers. I think that's the word. Don't make it weird. It's just the word."

    voice "audio/voice/line083.mp3"
    aarav smile "Brothers by rivalry. That's us. That's actually us."

    voice "audio/voice/line084.mp3"
    "They perform together that night. Not a competition. A duet. Loud and quiet, at the same time, and the hall goes silent in the way halls only go silent when something real is happening."

    voice "audio/voice/line085.mp3"
    "Meera watches from the side of the stage, and for the first time all summer, she does not look torn. She looks proud."

    voice "audio/voice/line086.mp3"
    "And that is when everything should get simple. It does not."

    jump parting

label parting:
    scene bg station
    with fade
    stop music
    play music "audio/sfx/station-goodbye.mp3" loop

    voice "audio/voice/line087.mp3"
    "Morning. The festival is over. The town is quiet in that clean, after-the-rain way."

    voice "audio/voice/line088.mp3"
    "At the station, there are two platforms. Two trains. Two different directions."

    voice "audio/voice/line089.mp3"
    "Aarav is on one platform, bag over his shoulder, ticket in his hand. Kabir is on the other, same bag, same ticket, opposite direction."

    voice "audio/voice/line090.mp3"
    "They do not explain. They do not argue. They do not even look surprised."

    if bond >= 5:
        voice "audio/voice/line091.mp3"
        "Aarav looks across the tracks, and Kabir looks back, and for one second, they smile — the smile of two people who know something nobody else in this station knows."
        voice "audio/voice/line092.mp3"
        "No wave. No shout. Just that smile. And then they turn away, each toward his own train."
    elif rivalry >= 4:
        voice "audio/voice/line093.mp3"
        "They look at each other across the tracks, and the old rivalry flickers there for a second — stubborn, familiar, almost fond."
        voice "audio/voice/line094.mp3"
        "Then they turn away, each toward his own train, without a word."
    else:
        voice "audio/voice/line095.mp3"
        "They do not look at each other at all. That, somehow, is the strangest part."

    voice "audio/voice/line096.mp3"
    "Meera stands between the platforms, watching both trains, watching both boys, and she does not know why they are leaving, or where they are going, or whether they planned this together."

    voice "audio/voice/line097.mp3"
    meera concerned "Wait — both of you? Where are you going? Why — why are you going different ways?"

    voice "audio/voice/line098.mp3"
    "No answer. The trains move. The station empties. The summer ends without an explanation."

    voice "audio/voice/line099.mp3"
    "Why did they go two different, separate paths? No one knows."

    voice "audio/voice/line100.mp3"
    "{b}End of Part 1.{/b}"

    voice "audio/voice/line101.mp3"
    "Brothers by Rivalry — Part 2 is coming."

    return
