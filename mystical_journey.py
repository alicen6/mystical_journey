# This is the mystical journey, based off of stories I've told, and things
# that have happened in my life.

from sys import exit
from random import randint
import random


print "Welcome to the Mystical Journey. Some may have heard that it was a"
print "mostly auditory experience. However, that had much to do with the"
print "poor lighting. Now with that fixed, we invite you join us on the"
print "~MYSTICAL JOURNEY~"
print " "
print " "
print " "

# set up character
print "Now, before we start the journey, who are you?"
name = raw_input("Name, please: ")
print "Nice to meet you " + name + "!"


def choose_class():
    print " "
    print "Are you an adventurer, a warrior, a thief, or a gnome?"
    print " "
    class_choice = raw_input("please enter a class: ")
    print " "
    if class_choice == "adventurer":
        print "Ah! An adventurer! You must have travelled the world!"
        start()
    elif class_choice == "warrior":
        start()
    elif class_choice == "thief":
        start()
    elif class_choice == "gnome":
        start()
    else:
        print "Huh? I'm afraid I don't understand"
        choose_class()


def start():
    print " "
    print "Are you ready to begin on the Mystical Journey?"
    start_time = raw_input("yes or no?: ")
    if start_time == "yes":
        round_one()
    elif start_time == "no":
        print " "
        print "Are you sure?"
        double_check = raw_input("yes or no?: ")
        if double_check == "yes":
            print " "
            print "Okay, well maybe next time."
            exit(0)
        elif double_check == "no":
            print " "
            print "So you are ready!"
            round_one()
        else:
            print "I don't understand."
            start()
    else:
        print "I don't understand."
        start()


def round_one():
    print " "
    print " "
    print "You finally open your eyes, realizing that you've been having"
    print "an inner monologue with yourself this entire time. Are you"
    print "sure you're not on drugs? Maybe you are."
    print "None of that class stuff actually matters at all."
    print "Looking around, you're standing at a crossroads."
    print "You can go east, west or north."
    print " "
    direction = raw_input("Where do you go?: ")
    if direction == "east":
        east()
    elif direction == "west":
        west()
    elif direction == "north":
        north()
    else:
        print " "
        print "You passed out from thinking too hard, try again."


def east():
    print " "
    print " "
    print "Onward to the east you travel, it isn't long before you come face"
    print "to face with a baked potato. Oddly, it seems to be sitting in the"
    print "middle of a small clearing, on a stump. You wonder how this is"
    print "possible. What do you do?"
    print " "
    potato = raw_input("keep walking, eat it, throw something: ")
    if potato == "keep walking":
        print " "
        print "You only get a few steps past the potato before a voice is ",
        print "heard."
        print '"WHO GOES THERE?" the voice booms and you jump, startled.'
        print "You stop, what do you say?"
        potato_talk = raw_input("just a spud!, nobody!, your king!: ")
        print " "
        if potato_talk == "just a spud!":
            print " "
            print 'The potato replies, "Oh, okay! Carry on then!"'
            east_two()
        elif potato_talk == "nobody!":
            print " "
            print "You have confused the potato, it somehow rolls away."
            east_two()
        elif potato_talk == "your king!":
            print " "
            print "The potato laughs at you, and you find yourself wrapped in"
            print "tin foil, unable to move, being rolled into a giant"
            print "microwave by many small potatoes."
            exit(0)
        else:
            print " "
            print "The potato and everything else vanishes in a puff of smoke."
            vanish()
    elif potato == "eat it":
        print " "
        print "I can't believe you ate something you found in the woods, ",
        print "gross."
        print "That might come back to haunt you, or at least haunt your"
        print "intestines. You keep walking east."
        east_two()
    elif potato == "throw something":
        print " "
        print "You missed."
        exit(0)
    else:
        print " "
        print "Huh. I guess that worked"
        east_two()


def west():
    print " "
    print " "
    print "So you decided to head west? Better be careful. Up ahead, you see a"
    print 'horse. It turns around as your approach, "I AM A UNICORN!"'
    print "Clearly, this beast is delusional and needs your help."
    print "'I do not need help', it grumbled angrily. It's wrong, trust me."
    print "I suggest taking it with you, or trying one of those magic liquids"
    print "in your pocket."
    print " "
    horse_choice = raw_input("take the unicorn or magic liquid?: ")
    if horse_choice == "take the unicorn":
        print " "
        print "This adventure just gets better and better!"
        horse()
    elif horse_choice == "magic liquid":
        print " "
        print "You pull out 3 bottles of liquids, none of them are labeled."
        print "You don't want to waste all three, so you randomly choose one."
        liquid_choice = randint(1, 3)
        if liquid_choice == 1:
            print " "
            print "A red liquid, almost looks like juice. When you pour it,"
            print "the liquid just makes the horse sticky. Looks like it "
            print "was just juice. The horse kicks you to death."
            exit(0)
        elif liquid_choice == 2:
            print " "
            print "Blue liquid, hopefully this is the right one. Something"
            print "starts to happen as your pour the liquid over the horse."
            print "After a minute or two, you are now faced with a horse"
            print "the size of a house cat. How useful. You decide to take"
            print "it with you."
            tiny_horse()
        else:
            print " "
            print "The green liquid, hopefully it's lucky! As you start to "
            print "pour it, gravity fails and it twists and turns, becoming an"
            print "actual horn on the horse's head."
            print "NOW you're a unicorn! The horse is so grateful, it shows "
            print "you hidden path further west."
            west_two()
    else:
        print " "
        print "While fumbling around, you spilled the three liquids together."
        print "It caused a massive explosion, and everyone died."
        exit(0)


def north():
    print " "
    print "As you trudge north, you can feel the air getting slightly colder."
    print "It's not a noticeable amount yet, but you do want a jacket. Before"
    print "long, you see a black cat with its back facing you. It turns as you"
    print "approach. The cat has only one eye, and a googly eye where the "
    print "other one should be."
    print " "
    print "'Meow?'"
    print " "
    print "The cat shows you three shells at its feet. Lifting one, you can "
    print "see a marble. The cat wants to play a game."
    print " "
    cat_game = raw_input("Will you play the cat's game?: ")
    if cat_game == "yes":
        print " "
        print "The cat indicates that you must choose the shell the marble is "
        print "under, after it mixes the shells."
        shell_match = False

        while not shell_match:
            shell_choice = int(raw_input("Pick 1, 2 or 3: "))
            marble_loc = randint(1, 3)
            if shell_choice == marble_loc:
                print " "
                print "You got it! The cat looks as defeated as a one-eyed cat"
                print "can, and pulls a lever that sends you sliding through "
                print "a trap door."
                shell_match = True
            else:
                print " "
                print "You failed! The cat laughs at you and forces you to try"
                print "again"
        trap_door()

    elif cat_game == "no":
        print " "
        print "Before you can even turn around, the cat swallows you whole."
        exit(0)
    else:
        print " "
        print "You have confused the cat. It sneezes on you and everything "
        print "goes up in a puff of white smoke!"
        vanish()


def east_two():
    print " "
    print "That potato was weird. At least now you've gone past it. Continuing"
    print "eastward on your journey, you soon find yourself at the edge of a"
    print "body of water. There's no way around the water, but you do see a "
    print "cave up the beach. There is also a strange swirling hole in the "
    print "water. Lastly, there seems to be a chicken wandering the beach."
    print " "
    east_two_decision = raw_input("cave, water, or chicken: ")
    if east_two_decision == "cave":
        print " "
        print "You go into the cave, it's dark. This journey is turning back"
        print "into a mostly auditory experience. You slip, you fall, you hit"
        print "your head."
        trap_door()
    elif east_two_decision == "water":
        print " "
        print "Interesting. You're going to swim out to a mysterious hole in"
        print "the water? You're asking for death, so here you go."
        exit(0)
    elif east_two_decision == "chicken":
        print " "
        print "You get the uncontrollable urge to chase the chicken. Maybe "
        print "you're just hungry. Of course, the chicken runs from you."
        print "Once you're out of breath, the chicken approches and challenges"
        print "you to a game of Rock, Paper, Scissors"
        beat_chicken = False
        chicken_round = 1
        while not beat_chicken:
            user_choice = raw_input("rock, paper, or scissors?: ")
            chicken_options = ['rock', 'paper', 'scissors']
            chicken_choice = random.choice(chicken_options)
            chicken_round += 1
            if user_choice == chicken_choice:
                # chicken_round += 1
                print " "
                print "It's a tie! Round " + str(chicken_round)
            elif user_choice == 'scissors' and chicken_choice == 'rock':
                # chicken_round += 1
                print " "
                print "You lose! Try again! Round " + str(chicken_round)
            elif user_choice == 'paper' and chicken_choice == 'scissors':
                # chicken_round += 1
                print " "
                print "You lose! Try again! Round " + str(chicken_round)
            elif user_choice == 'rock' and chicken_choice == 'paper':
                # chicken_round += 1
                print " "
                print "You lose! Try again! Round " + str(chicken_round)
            else:
                print " "
                print "You win! It took " + str(chicken_round) + " rounds!"
                print "Suddenly the chicken levitates away, leaving behind a"
                print "small pastry labeled 'EAT ME'."
                beat_chicken = True
        print " "
        eat_me = raw_input("Do you eat the pastry?: ")
        if eat_me == "yes":
            print " "
            print "Your stomach turns after you swallow the pastry whole. That"
            print "might have been a bad idea. You squeeze your eyes shut in"
            print "discomfort, and don't notice the white smoke clouds"
            print "billowing around you."
            vanish()
        elif eat_me == "no":
            print " "
            print "Horrified at where the pastry could have come from, you "
            print "turn and throw it into the water. That was gross. Now with"
            print "nothing left to do, you lay down on the sand and enjoy the"
            print "rest of your life as a beach bum."
            exit(0)
        else:
            print " "
            print "Just touching the pastry has given you a bad trip, and you "
            print "fall over in the sand and die."
            exit(0)
    else:
        print " "
        print "Okay, so you decided to stay on this beach and live the rest of"
        print "your life. I've seen worse decisions get made for sure."
        exit(0)


def vanish():
    print " "
    print "The last thing you might remember is a cloud of smoke. You find "
    print "yourself on a very small island, surrounded by gnomes. They tell"
    print "you the only way off the island is to beat them 5 times in their"
    print "version of Ro Sham Bo."
    beat_gnome = 0
    total_rounds = 0

    while beat_gnome < 5 and total_rounds < 15:
        user_pick = raw_input("""Pick rock, paper, scissors, dog,
        lizard, gun, gnome: """)
        gnome_options = ['rock', 'paper', 'scissors', 'dog', 'lizard', 'gun',
        'gnome']
        gnome_pick = random.choice(gnome_options)
        total_rounds += 1
        if user_pick == gnome_pick:
            print " "
            print "It's a tie! Try again!"
        elif user_pick == "rock":
            if gnome_pick == "lizard" or gnome_pick == "gun" or gnome_pick == "scissors":
                print " "
                print "You win!"
                beat_gnome += 1
            else:
                print " "
                print "You lose! Try again!"
        elif user_pick == "paper":
            if gnome_pick == "dog" or gnome_pick == "gnome" or gnome_pick == "rock":
                print " "
                print "You win!"
                beat_gnome += 1
            else:
                print " "
                print "You lose! Try again!"
        elif user_pick == "scissors":
            if gnome_pick == "lizard" or gnome_pick == "gun" or gnome_pick == "paper":
                print " "
                print "You win!"
                beat_gnome += 1
            else:
                print " "
                print "You lose! Try again!"
        elif user_pick == "dog":
            if gnome_pick == "gnome" or gnome_pick == "rock" or gnome_pick == "scissors":
                print " "
                print "You win!"
                beat_gnome += 1
            else:
                print " "
                print "You lose! Try again!"
        elif user_pick == "lizard":
            if gnome_pick == "gnome" or gnome_pick == "dog" or gnome_pick == "paper":
                print " "
                print "You win!"
                beat_gnome += 1
            else:
                print " "
                print "You lose! Try again!"
        elif user_pick == "gun":
            if gnome_pick == "lizard" or gnome_pick == "dog" or gnome_pick == "paper":
                print " "
                print "You win!"
                beat_gnome += 1
            else:
                print " "
                print "You lose! Try again!"
        elif user_pick == "gnome":
            if gnome_pick == "rock" or gnome_pick == "gun" or gnome_pick == "scissors":
                print " "
                print "You win!"
                beat_gnome += 1
            else:
                print " "
                print "You lose! Try again!"
        else:
            print " "
            print "That's not an option, try again."
    if beat_gnome >= 5:
        print " "
        print "You beat the gnomes! They push you through a small hole in the"
        print "ground, where you begin falling in pitch black darkness."
        trap_door()
    elif total_rounds >= 15:
        print " "
        print "You lost! The gnomes are now claiming you as their prisoner"
        print "forever. You'll never be able to leave! :("
        exit(0)


def horse():
    print " "
    print "You walk with the horse for a while, before coming across a camp."
    print "All of the people in the camp immediately position to attack you."
    print "Glancing at your new horse friend, the only option is obvious, you"
    print "must mount your mighty steed and kill everyone in sight!"
    townspeople = 100

    while townspeople > 0:
        attacks = {'stomp': 1, 'kick': 2, 'pound': '3', 'charge': 4}
        multiplier = randint(1, 5)
        user_attack = raw_input("Do you stomp, kick, pound or charge?: ")
        if user_attack in attacks:
            user_multi = attacks[user_attack]
        damage_done = multiplier * user_multi
        print " "
        print "Townspeople health: " + str(townspeople)
        print "Damage done: " + str(damage_done)
        townspeople -= damage_done

    print " "
    print "You've killed everyone! But with the ground being soaked in blood,"
    print "a sinkhole suddenly opens up and swallows you whole!"
    trap_door()


# def tiny_horse(): sell it for a price, def in def? have to haggle to specific
# price

# def west_two(): oregon trail, dysentery

# trap_door(): mole people ends in final boss

choose_class()
