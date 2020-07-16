#! /usr/bin/python

import string
import sys
import getopt
import random

argumentList = sys.argv[1:] 
options = "hgic:"
long_options = ["help", "generate", "info", "count ="] 
count = 1

def main():
    header()

    if len(argumentList) == 0:
        welcome()
    else:
        parse()

def welcome():
    print("Choose one of the options below to generate a GUID.")
    print("To generate multiple GUID's at once use the --count command line parameters.")
    print("1. Generate")
    print("2. About GUID's")
    print("3. Show all options")
    selection = int(input("Selection: "))

    if selection == 1:
        generate()
    elif selection == 2:
        about()
    else:
        showOptions()

def parse():
    global count

    try: 
        arguments, values = getopt.getopt(argumentList, options, long_options) 
        
        for currentArgument, currentValue in arguments: 
            if currentArgument in ("-h", "--help"): 
                showOptions()
            elif currentArgument in ("-i", "--info"):
                about()
            elif currentArgument in ("-c", "--count"): 
                count = int(currentValue)
        
        for currentArgument, currentValue in arguments: 
            if currentArgument in ("-g", "--generate"): 
                generate() 
                
    except getopt.error as err: 
        print (str(err)) 

def generate():
    global count

    for x in range(count):
        guid = ""
        for c in "xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx":
            if c == "x":
                # x is [0-9, a-f] 
                guid += random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"])
            elif c == "M":
                # M is [1-5] 
                guid += random.choice(["1", "2", "3", "4", "5"])
            elif c == "N":
                # N is [8, 9, a, b]
                guid += random.choice(["8", "9", "a", "b"])
            else:
                # Dash
                guid += c
        print("The generated GUID is: " + guid)
    

def header(): 
    print("   ___ _   _ ___ ___     ___                       _           ")
    print("  / __| | | |_ _|   \   / __|___ _ _  ___ _ _ __ _| |_ ___ _ _ ")
    print(" | (_ | |_| || || |) | | (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|")
    print("  \___|\___/|___|___/   \___\___|_||_\___|_| \__,_|\__\___/_|  \n")

def about():
    print("What is a GUID?")
    print("A GUID is an acronyom that stands for Globally Unique Identifier, they are also referred to as UUIDs or Universaly Unique Identifiers - there is no real difference between the two.")
    print("Technically they are 128-bit unique reference numbers used in computing which are highly unlikely to repeat when generated despite there being no central GUID authority to ensure uniqueness.")
    print("")
    print("What does a GUID look like?")
    print("A GUID follows a specific structure defined in RFC 4122 and come in a few different versions and variants.")
    print("All variants follow the same structure xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx where M represents the version and the most significant bits of N represent the variant.")
    print("")
    print("How unique is unique?")
    print("")
    print("A GUID is a unique number that can be used as an identifier for anything in the universe, but unlike ISBN there is no central authority - the uniqueness of a GUID relies on the algorthm that was used to generate it.") 
    print("We'll look at the types of GUIDs later, but assuming a randomly generated GUID you have about the same chance of getting hit by a meteorite in a year as getting a collision in 10-30 trillion GUIDs.")
    print("")
    print("For more information visit: http://guid.one/guid\n")

def showOptions():
    print("-g, --generate      Generate a GUID.")
    print("                    Will default to 1 GUID if no argument is supplied for '--count'.")
    print("                    Example usage: guid.py -c <count> -g")
    print("-c, --count         Specify the number of GUID's to generate.")
    print("-i, --info          Information about what a GUID is and the structure.\n")
    
main()