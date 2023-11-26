class Item:
    def __init__(self, chunks):
        self.id = chunks[0]
        self.name = chunks[1]
        self.team = chunks[6]
        self.noc = chunks[7]
        self.year = chunks[9]
        self.sport = chunks[12]
        self.event = chunks[13]
        self.medal = chunks[14]
