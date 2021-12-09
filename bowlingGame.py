class BowlingGame:
    def __init__(self):
        self.rolls = []  # each roll will have the number of pins knocked down
        # [8, 10, 12, 8 ]

    def roll(self, pins):
        self.rolls.append(pins)  # add number of pins to the roll

    def score(self):
        result = 0
        rollIndex = 0
        for frameIndex in range(10):  # each game will have 10 frames
            # made change to check if the first roll is a strike
            # change StrikeScore to strikeScore to call the right function
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2
        return result  # change the indentation so that it returns the result at the end of the for loop

    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex+1] == 10

    def strikeScore(self, rollIndex):
        return 10 + self.rolls[rollIndex+1] + self.rolls[rollIndex+2]

    def spareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
