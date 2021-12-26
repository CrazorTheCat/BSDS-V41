from Classes.Packets.PiranhaMessage import PiranhaMessage


class OutOfSyncMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeVint(fields["ServerChecksum"])
        self.writeVint(fields["ClientChecksum"])
        self.writeVint(fields["Tick"])

    def decode(self):
        fields = {}
        fields["ServerChecksum"] = self.readVint()
        fields["ClientChecksum"] = self.readVint()
        fields["Tick"] = self.readVint()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24104

    def getMessageVersion(self):
        return self.messageVersion