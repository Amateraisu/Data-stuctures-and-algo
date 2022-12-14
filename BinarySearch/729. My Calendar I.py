from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()
        

    def book(self, start: int, end: int) -> bool:

        idx = self.calendar.bisect_left([start, end])
        if idx > 0 and self.calendar[idx - 1][1] > start:
            return False

        if idx <= len(self.calendar) - 1 and self.calendar[idx][0] < end:
            return False

        self.calendar.add([start, end])

        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)