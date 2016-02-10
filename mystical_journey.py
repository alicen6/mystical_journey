# This is the mystical journey, based off of stories I've told, and things
# that have happened in my life.

from sys import exit
from random import randint


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
        print "Are you sure?"
        double_check = raw_input("yes or no?: ")
        if double_check == "yes":
            print "Okay, well maybe next time."
            exit(0)
        elif double_check == "no":
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
        potato_talk = raw_input("just a spud!, nobody!, your king!")
        print " "
        if potato_talk == "just a spud!":
            print 'The potato replies, "Oh, okay! Carry on then!"'
            east_two()
        elif potato_talk == "nobody!":
            print "You have confused the potato, it somehow rolls away."
            east_two()
        elif potato_talk == "your king!":
            print " "
            print "The potato laughs at you, and you find yourself wrapped in"
            print "tin foil, unable to move, being rolled into a giant"
            print "microwave by many small potatoes."
            exit(0)
        else:
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
        print "You missed."
        exit(0)
    else:
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


# def north(): one eyed cat

# def east_two(): flying

# def vanish(): gnome island

# def horse(): jousting

# def tiny_horse(): sell it for a price, def in def?

# def west_two(): robots?

choose_class()
