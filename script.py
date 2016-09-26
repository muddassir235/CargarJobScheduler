minutes = []

for i in range(10):
    minutes.append([2,2,2,2,2])

INOBD= 0
INOCD = 1
INOBCD = 2
INOB = 3
INOC = 4

exit = None

while not exit:

    print "Enter start minute"
    minute = raw_input()

    startTime = int(minute)


    # print "Enter end hour in 24 hour format"
    # hour = raw_input()

    print "Enter end minute"
    minute = raw_input()

    endTime = int(minute)

    print "Are You a male? Enter 1 for Yes and Enter 0 for no"
    male = raw_input() == "1"

    available = True
    carForMale = False

    for m in range(startTime,endTime+1):
        if male:
            if((minutes[m][INOB] is 0 or  (minutes[m][INOBD] is 0 and minutes[m][INOBCD] is 0)) and ((minutes[m][INOCD] is 0 and minutes[m][INOBCD] is 0) or minutes[m][INOC] is 0) ):
                available = False
            if minutes[m][INOB] is 0 or  (minutes[m][INOBD] is 0 and minutes[m][INOBCD] is 0):
                carForMale = True
        else:
            if minutes[m][INOC] is 0 or (minutes[m][INOCD] is 0 and minutes[m][INOBCD] is 0):
                available = False


    if(available):
        if(male):
            if carForMale:
                if minutes[m][INOCD] == 0:
                    for m in range(startTime,endTime+1):
                        minutes[m][INOBCD] = minutes[m][INOBCD] - 1
                else:
                    for m in range(startTime, endTime+1):
                        minutes[m][INOCD] = minutes[m][INOCD] - 1

                for m in range(startTime, endTime+1):
                    minutes[m][INOC] = minutes[m][INOC] - 1

                print "You are a male but there are no bikes available so we will assign you a car driver which will cost extra"

            else:
                if minutes[m][INOBD] == 0:
                    for m in range(startTime, endTime+1):
                        minutes[m][INOBCD] = minutes[m][INOBCD] -1
                else:
                    for m in range(startTime, endTime+1):
                        minutes[m][INOBD] = minutes[m][INOBD] -1

                for m in range(startTime, endTime+1):
                    minutes[m][INOB] = minutes[m][INOB] - 1

                print "You are a male and you have been assigned a bike"

        else:
            if minutes[m][INOCD] == 0:
                for m in range(startTime, endTime+1):
                    minutes[m][INOBCD] = minutes[m][INOBCD] - 1
            else:
                for m in range(startTime, endTime+1):
                    minutes[m][INOCD] = minutes[m][INOCD] - 1

            for m in range(startTime, endTime+1):
                minutes[m][INOC] = minutes[m][INOC] - 1

            print "You are a female and you have been assigned a car"


    else:
        if male:
            print "There are no bikes or cars available"
        else:
            print "There are no cars available"

    print minutes

    print "Do you want to stop? Enter True for Yes and False for No"
    exit = raw_input() == "True"

    if exit:
        break