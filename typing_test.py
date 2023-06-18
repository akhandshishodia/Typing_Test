
from time import time #to record the time

# now to calculate the accuracy of imput prompt
def accuracy(prompt):
    global inwords

    words = prompt.split() #splits every word into a list item
    errors = 0

    for i in range(len(inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors+=1
        else:
            if inwords[i]==words[i]:
                if(inwords[i+1] == words[i+1]) and (inwords[i-1] == words[i-1]):
                    continue
                else:
                    errors+=1
            else:
                errors+=1
    return errors

# now to calculate the speed of typing words per minute
def speed(inprompt,stime,etime):
    global time_
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    speed = (twords/time_)*60

    return speed

# calculate the total elapsed time
def elapsedtime(stime,etime):
    time_ = etime - stime # etime is the end-time and stime is the start-time
    return time_

if __name__ == "__main__":
    prompt = "I am Akhand Shishodia. I am currently pursuing MBA  . My interests are Analytics, Chess and Cricket. I am from UP."
    # this is the paragraph which we have to type
    print("type the below paragraph:")
    print(prompt)

    # checking to input Enter basically it will see
    input("Press Enter when you are ready to check your speed!!!!!")

    # recording time for input
    stime = time()
    inprompt = input()
    etime = time()

    #collect all the information returned by the functions
    time_ = round(elapsedtime(stime,etime),2) #round off the time
    speed_ = speed(inprompt,stime,etime)
    errors = accuracy(prompt)

    #printing all the required data to see results

    print("Total time elapsed = ", time_, "seconds")
    print("Average Typing Speed = ", speed_, "wpm")
    print("errors = ", errors)