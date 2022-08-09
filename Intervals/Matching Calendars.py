def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # Write your code here.
    person1Availability = getAvailability(calendar1, dailyBounds1)
    person2Availability = getAvailability(calendar2, dailyBounds2)

    
    # find common time slot 
    commonTimeSlot = getCommonTimeSlot(person1Availability, person2Availability, meetingDuration)
    print("result", commonTimeSlot)

    return commonTimeSlot 




def getAvailability(calendar, dailyBounds):
    res = []
    prev = dailyBounds[0]

    if calendar == []:
        return [dailyBounds]

    for meeting in calendar:
        if meeting[0] != prev:
            res.append([prev, meeting[0]])
        prev = meeting[1]

    if prev != dailyBounds[1]:
        res.append([prev, dailyBounds[1]])
    

    return res


def getCommonTimeSlot(person1Availability, person2Availability, meetingDuration):
    # first put them in sorted order according to the first time 
    result = []
    combinedArray = person1Availability + person2Availability

    combinedArray.sort(key = lambda x : convertTimeToMinutes(x[0]))
    
    mergedIntervals = mergeIntervals(combinedArray)
    for interval in mergedIntervals:
        if isValid(interval, meetingDuration):
            result.append(interval)

    return result

def isValid(interval, meetingDuration):
    start = interval[0]
    end = interval[1]
    if convertTimeToMinutes(end) - convertTimeToMinutes(start) >= meetingDuration:
        return True 

    return False

def convertTimeToMinutes(time):
    hour, minutes = time.split(":")
    timeInMinutes = 60 * int(hour) + int(minutes)
    return timeInMinutes

def mergeIntervals(array):
    currentInterval = array[0]
    res = []
    didIntersect = False 
    for i in range(1, len(array)):
        interval = array[i]
        if convertTimeToMinutes(interval[0]) <= convertTimeToMinutes(currentInterval[1]):
            currentInterval = [max(interval[0], currentInterval[0], key = lambda x: convertTimeToMinutes(x)), min(interval[1], currentInterval[1], key = lambda x: convertTimeToMinutes(x))]
            res.append(currentInterval)


        currentInterval = interval  

    return res