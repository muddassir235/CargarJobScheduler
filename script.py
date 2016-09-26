
class JobScheduler:

    # array that stores all data for all the minutes in a specific day
    minutes = []

    INOBD = 0 # index number of bike drivers
    INOCD = 1 # index number of car drivers
    INOBCD = 2 # index number of (car and bike) drivers
    INOB = 3 # index number of bikes
    INOC = 4 # index number of cars

    def setTimeline(self, minutes):
        self.minutes = minutes

    def subscribe(self, startTime, endTime, male):

        # subscription avaiable
        available = True

        # do we need to assign a car to a male passenger
        carForMale = False

        # for all the minutes between start time and end time
        for m in range(startTime, endTime + 1):
            if male:
                # if we have at least one bike available and have at least one bike driver or general purpose driver
                #       OR
                # we have at least one car available and at least one car or general purpose driver available
                #       THEN
                # leave available as 'True' otherwise make it 'False
                if ((self.minutes[m][self.INOB] is 0 or (self.minutes[m][self.INOBD] is 0 and self.minutes[m][self.INOBCD] is 0)) and (
                    (self.minutes[m][self.INOCD] is 0 and self.minutes[m][self.INOBCD] is 0) or self.minutes[m][self.INOC] is 0)):
                    available = False

                # if there no bikes available or there are zero bike and general purpose riders then
                # even if the passenger is male assign them a car
                if self.minutes[m][self.INOB] is 0 or (self.minutes[m][self.INOBD] is 0 and self.minutes[m][self.INOBCD] is 0):
                    carForMale = True
            else:
                # if no cars are available or there are nos car or general purpose drivers
                if self.minutes[m][self.INOC] is 0 or (self.minutes[m][self.INOCD] is 0 and self.minutes[m][self.INOBCD] is 0):
                    available = False

        # if subscription available
        if (available):
            if (male):
                # in case we want to assign a car to a male passenger
                if carForMale:

                    # boolean: If at least one car driver is present between the start and end duration
                    car_driver_present = True

                    for m in range(startTime, endTime+1):
                        if( self.minutes[m][self.INOCD] == 0):
                            car_driver_present = False

                    # car driver is present
                    if car_driver_present:

                        # remove the car driver the minute indices
                        for m in range(startTime, endTime + 1):
                            self.minutes[m][self.INOBCD] = self.minutes[m][self.INOBCD] - 1

                    else: # only general purpose driver available

                        # remove the general purpose driver the minute indices
                        for m in range(startTime, endTime + 1):
                            self.minutes[m][self.INOCD] = self.minutes[m][self.INOCD] - 1

                    # remove the car from all the minute indices
                    for m in range(startTime, endTime + 1):
                        self.minutes[m][self.INOC] = self.minutes[m][self.INOC] - 1

                    print "You are a male but there are no bikes available so we will assign you a car driver which will cost extra"

                else: # a bike and driver are available

                    # boolean: a bike driver is preset
                    bike_driver_present = True

                    for m in range(startTime, endTime + 1):
                        if (self.minutes[m][self.INOBD] == 0):
                            bike_driver_present = False

                    if bike_driver_present: # at least one bike driver is present

                        # remove that bike driver from the minute indices
                        for m in range(startTime, endTime + 1):
                            self.minutes[m][self.INOBCD] = self.minutes[m][self.INOBCD] - 1

                    else: # at least one gen purpose driver is present

                        # remove that gen purpose driver from minutes indices
                        for m in range(startTime, endTime + 1):
                            self.minutes[m][self.INOBD] = self.minutes[m][self.INOBD] - 1


                    # remove the bike from all the minutes between start and end times
                    for m in range(startTime, endTime + 1):
                        self.minutes[m][self.INOB] = self.minutes[m][self.INOB] - 1

                    print "You are a male and you have been assigned a bike"

            else: # female passenger

                # boolean: is a car driver present
                car_driver_present = True

                for m in range(startTime, endTime + 1):
                    if (self.minutes[m][self.INOCD] == 0):
                        car_driver_present = False

                if car_driver_present: # at least one car driver is present

                    # remove that car driver for all minute indices in the range
                    for m in range(startTime, endTime + 1):
                        self.minutes[m][self.INOBCD] = self.minutes[m][self.INOBCD] - 1

                else: # at least one gen purpose driver is present

                    # remove that gen purpose driver for all minute indices in the range
                    for m in range(startTime, endTime + 1):
                        self.minutes[m][self.INOCD] = self.minutes[m][self.INOCD] - 1

                # remove the car for all the minute indices in the range
                for m in range(startTime, endTime + 1):
                    self.minutes[m][self.INOC] = self.minutes[m][self.INOC] - 1

                print "You are a female and you have been assigned a car"


        else: # subscription is not available
            if male:
                print "There are no bikes or cars available"
            else:
                print "There are no cars available"

        print self.minutes

    def getMinutes(self):
        return self.minutes




