#This file is here to make the long and boring functions invisible

def findCommand(keyWord):

    keyWord_list = ["adjust","change","what","remember"]

    if keyWord in keyWord_list: #matched keyWord
        print("Detected key word "+keyWord)
        if keyWord == "adjust":
            print("you want to adjust")
            #adjust
        if keyWord == "change":
            print("you want to change")
        if keyWord == "what":
            print("you want to ask")
        if keyWord == "remember":
            print("you want me to remember")
    else: #didn't match keyWord
        print("Sorry, no key word detected.")
