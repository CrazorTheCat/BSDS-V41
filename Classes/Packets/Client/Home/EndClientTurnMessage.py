from Classes.Logic.LogicCommandManager import LogicCommandManager
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage


class EndClientTurnMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        self.readBoolean()
        fields["Tick"] = self.readVint()
        fields["Checksum"] = self.readVint()
        fields["CommandsCount"] = self.readVint()
        super().decode(fields)
        fields["Commands"] = []
        for i in range(fields["CommandsCount"]):
            fields["Commands"].append({"ID": self.readVint()})
            if not LogicCommandManager.isServerToClient(fields["Commands"][i]["ID"]):
                self.readVint()
                self.readVint()
                self.readVLong()
            if LogicCommandManager.commandExist(fields["Commands"][i]["ID"]):
                command = LogicCommandManager.createCommand(fields["Commands"][i]["ID"])
                print("Command", LogicCommandManager.getCommandsName(fields["Commands"][i]["ID"]))
                if command is not None:
                    command.decode(self)
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        pass

    def getMessageType(self):
        return 14102

    def getMessageVersion(self):
        return self.messageVersion