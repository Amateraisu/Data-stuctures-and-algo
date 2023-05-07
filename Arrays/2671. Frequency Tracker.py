class FrequencyTracker:

    def __init__(self):
        self.count = collections.defaultdict(int)
        self.freq = collections.defaultdict(int)

    def add(self, number: int) -> None:
        self.freq[self.count[number]] -= 1 if self.freq[self.count[number]] != 0 else 0
        self.count[number] += 1
        self.freq[self.count[number]] += 1
        # print("adding" ,number)
        # print(self.freq)
        # print(self.count)
        # print("===")

    def deleteOne(self, number: int) -> None:
        # print("deleting", number)
        if self.count[number] > 0:
            self.freq[self.count[number]] -= 1
            self.count[number] -= 1
            self.freq[self.count[number]] += 1
            # print(self.freq)
        # print(self.count)
        # print("###")

    def hasFrequency(self, frequency: int) -> bool:
        # print(self.freq, frequency)

        # print(self.freq)
        # print(self.count)
        # print("HJERE")

        return self.freq[frequency] > 0
