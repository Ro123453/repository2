class student:
    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.energy = 100
        self.happy = 50
        self.alive = True

    def to_study(self):
        print('Time to study!')
        self.progress += 0.5
        self.happy -= 2
        self.energy -= 5

    def to_sleep(self):
        print('Time to sleep!')
        self.happy += 3
        self.energy = 100

    def to_chill(self):
        print('Time to rest!')
        self.energy -= 10
        self.progress += 0.1
        self.happy += 8

    def is_alive(self):
        if (self.progress < -0.5):
            self.alive = False
        elif (self.happy <= 0):
            print('Depresion')
            self.alive = False

    def end_of_day(self):
        print(f'Happy = {self.happy}\nProgress = {self.progress}')