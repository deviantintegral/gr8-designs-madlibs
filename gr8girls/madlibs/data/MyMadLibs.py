#!/usr/bin/env python2.5

'''
Created on Apr 23, 2009

This program is for creating Madlibs with Python.

@author: Andrew Berry
@email: aberry@uoguelph.ca
'''

# Any line beginning with a # tells Python to ignore the line.
# This allows us to put in comments in our code, so we can remember
# how things work! There are many comments in this program to help both
# you and your team leader, so don't worry if you don't understand
# what they say.

# The "sys" module allows our program to read keys as they are typed
# from the keyboard, among many other things.
import sys

# This allows the program to automatically find new Madlibs when
# it's run
import MyMadLibs
import inspect

# If you want to be able to have multiple madlibs at the same time,
# you should create multiple "classes", with one class for each
# Madlib. Each class has two "functions"; 'blanks', for telling the
# computer what fill-in-the-blanks to ask for, and 'story', for telling
# the computer what your story is and where each answer goes.
class MyFirstMadLib:

    # Here begins the 'blanks' function. To add more blanks, add lines
    # in the following pattern:
    #
    # 'name-of-the-blank' : 'the instructions for the user',
    #
    # Remember to keep the indentation the same, and don't forget the
    # comma at the end of the line!
    def blanks(self):
        return {
            'animal' : 'The name of an animal',
            'place' : 'A place',
            'past-tense-verb' : 'A verb in the past tense',
            'noun' : 'A noun',
        }
    
    # Here begins the 'story' function. It is where we put together the blanks
    # and our story. I suggest putting each sentence on a line by itself, adding
    # to "story" on each line. Note the space at the beginning of the second
    # sentence.
    def story(self, blanks):
	story = "One day, a " + blanks['animal'] + " went to " + blanks['place'] + " and " + blanks['past-tense-verb'] + " a " + blanks['noun'] + "."
        # story = story + means to add the new sentence to the previous sentence
	story = story + " The next day, the " + blanks['noun'] + " went to " + blanks['place'] + " and " + blanks['past-tense-verb'] + " a " + blanks['animal'] + "."
        return story 

# To use this madlib as a starting point for a second Madlib,
# remove the hashes from the beginning of each line.

#class MySecondMadLib:
#    def blanks(self):
#         return {
#             'blank-1' : 'instructions-1',
#         }
#
#    def story(self, blanks):
#        story = "Put your story here " + blanks['blank-1']
#        return story

# This is the part of the program which glues all of the above together.
# If you've finished creating your madlibs, try reading and changing
# the code below to see what it does!
if __name__ == "__main__":
    # This code finds all of the Madlibs in this program.
    classes = []
    for name in dir(MyMadLibs):
        obj = getattr(MyMadLibs, name)
        if inspect.isclass(obj):
            classes.append(obj.__name__)

    # This is a "while loop". It repeats until you enter in a valid
    # number for a Madlib.
    while 1:
        print "Enter the number of the Madlib you want to run:"
        for index in range(0, len(classes)):
            print str(index + 1) + ". " + classes[index]

        try:
            number_to_run = int(sys.stdin.readline()[:-1]) - 1
            klass = getattr(MyMadLibs, classes[number_to_run])
            m = klass()
            break

        # You entered a number which doesn't exist.
        except IndexError:
            print "You must enter a valid number for a Madlib to run."
        # You entered a number which wasn't a number.
        except ValueError:
            print "You must enter a valid number for a Madlib to run."

    # First, we need to get the blanks to fill in.
    # Our program uses the blanks() function to determine what blanks
    # are needed by the Madlib. We "loop" through each of the blanks
    # and add the answers to the "answers" variable.
    blanks = m.blanks()
    answers = {}
    for key in blanks:
        print "Fill in an answer for '%s': " % blanks[key]
        # The [:-1] removes the newline from the input. This means that
        # when we print the answer, it doesn't force a new line.
        # "sys.stdin.readline()" tells Python to read a line of text
        # as you type it in.
        answers[key] = sys.stdin.readline()[:-1]

    # This takes the answers you typed in, sends them to the
    # story function, and then prints out the final story.
    print m.story(answers)

