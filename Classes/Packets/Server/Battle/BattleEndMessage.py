from io import BytesIO

from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class BattleEndMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeLong(0, 1)
        self.writeLong(0, 1)
        self.writeVint(1) # Battle End Game Mode
        self.writeVint(fields["Rank"]) # Result (Victory/Defeat/Draw/Rank Score)
        self.writeVint(0) # Tokens Gained
        self.writeVint(1250) # Trophies Result
        self.writeVint(0) # Power Play Points Gained
        self.writeVint(0) # Doubled Tokens
        self.writeVint(0) # Double Token Event
        self.writeVint(0) # Token Doubler Remaining
        self.writeVint(0) # Special Events Level Passed
        self.writeVint(0) # Epic Win Power Play Points Gained
        self.writeVint(0) # Championship Level Reached
        self.writeBoolean(False)
        self.writeVint(0)
        self.writeVint(0)
        self.writeBoolean(False)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(True)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVint(-1)
        self.writeBoolean(False)

        self.writeVint(fields["HeroesCount"])
        for heroEntry in fields["Heroes"]:
            self.writeBoolean(heroEntry["IsPlayer"])
            self.writeBoolean(bool(heroEntry["Team"]))
            self.writeBoolean(bool(heroEntry["Team"]))
            self.writeVint(1)
            for i in range(1):
                self.writeDataReference(heroEntry["Brawler"]["ID"][0], heroEntry["Brawler"]["ID"][1])
            self.writeVint(1)
            for i in range(1):
                self.writeDataReference(heroEntry["Brawler"]["SkinID"][0], heroEntry["Brawler"]["SkinID"][1])
            self.writeVint(1)
            for i in range(1):
                self.writeVint(1250)
            self.writeVint(1)
            for i in range(1):
                self.writeVint(11)
            self.writeVint(1)
            for i in range(1):
                self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeBoolean(heroEntry["IsPlayer"])
            if heroEntry["IsPlayer"]:
                self.writeLong(player.ID[0], player.ID[1])
            self.writeString(heroEntry["PlayerName"])
            self.writeVint(100)
            self.writeVint(28000000)
            self.writeVint(43000000)
            self.writeVint(46000000)
            if heroEntry["IsPlayer"]:
                self.writeBoolean(True, 1)
                self.writeVLong(5, 4181497)
                self.writeString('Orange eSPORT')
                self.writeDataReference(8, 16)

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(2)

        self.writeVint(1)
        self.writeVint(1250)
        self.writeVint(1250)

        self.writeVint(5)
        self.writeVint(999999)
        self.writeVint(999999)

        self.writeDataReference(28, 0)
        self.writeBoolean(False, 1)
        self.writeBoolean(False, 1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeBoolean(False)
        self.writeVint(-1)
        self.writeBoolean(False)

        print(self.messagePayload.hex())

    def decode(self):
        fields = {}
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 23456

    def getMessageVersion(self):
        return self.messageVersion