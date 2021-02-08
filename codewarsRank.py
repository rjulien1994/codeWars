class User():
    ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.maxProgress = 100

    def inc_progress(self, num):
        d = self.ranks.index(num) - self.ranks.index(self.rank)
        if d == -1:
            self.progress += 1
        elif d == 0:
            self.progress += 3
        elif d > 0:
            self.progress += 10*d*d
        
        while self.progress >= self.maxProgress and self.rank < 8:
            self.progress -= self.maxProgress
            self.rank = self.ranks[self.ranks.index(self.rank)+1]

        if self.rank == 8:
            self.progress = 0

user = User()

user.inc_progress(6)

print(user.rank)
print(user.progress)
