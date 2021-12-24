import socket
import time

from Classes.ClientsManager import ClientsManager
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler


class LoginMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["AccountID"] = self.readLong()
        fields["PassToken"] = self.readString()
        fields["ClientMajor"] = self.readInt()
        fields["ClientMinor"] = self.readInt()
        fields["ClientBuild"] = self.readInt()
        fields["ResourceSha"] = self.readString()
        fields["Device"] = self.readString()
        fields["PreferredLanguage"] = self.readDataReference()
        fields["PreferredDeviceLanguage"] = self.readString()
        fields["OSVersion"] = self.readString()
        fields["isAndroid"] = self.readBoolean()
        fields["IMEI"] = self.readString()
        fields["AndroidID"] = self.readString()
        fields["isAdvertisingEnabled"] = self.readBoolean()
        fields["AppleIFV"] = self.readString()
        fields["RndKey"] = self.readInt()
        fields["AppStore"] = self.readVint()
        fields["ClientVersion"] = self.readString()
        fields["TencentOpenId"] = self.readString()
        fields["TencentToken"] = self.readString()
        fields["TencentPlatform"] = self.readVint()
        fields["DeviceVerifierResponse"] = self.readString()
        fields["AppLicensingSignature"] = self.readString()
        fields["DeviceVerifierResponse"] = self.readString()
        fields["SupercellIdToken"] = self.readCompressedString()
        fields["UpdateMaintenanceMode"] = self.readBoolean()
        fields["YoozooOsdkTicket"] = self.readString()
        fields["YoozooDeviceId"] = self.readString()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        ClientsManager.AddPlayer(calling_instance.player.ID, calling_instance.client)
        calling_instance.player.ClientVersion = f'{str(fields["ClientMajor"])}.{str(fields["ClientBuild"])}.{str(fields["ClientMinor"])}'
        loginOkinfo = fields
        loginOkinfo["Socket"] = calling_instance.client
        fields["Socket"] = calling_instance.client
        db_instance = DatabaseHandler()
        if db_instance.playerExist(fields["PassToken"], fields["AccountID"]):
            db_instance.loadAccount(calling_instance.player, fields["AccountID"])

        elif fields["AccountID"] != [0, 0]:
            db_instance.createAccount(fields["AccountID"], fields["PassToken"], calling_instance.player.getDataTemplate(fields["AccountID"][0], fields["AccountID"][1], fields["PassToken"], True))

        else:
            db_instance.createAccount(fields["AccountID"], fields["PassToken"], calling_instance.player.getDataTemplate(fields["AccountID"][0], fields["AccountID"][1], fields["PassToken"]))

        contentUpdateInfo = Utility.getContentUpdaterInfo()
        if fields["ResourceSha"] != contentUpdateInfo[1]:
            Messaging.sendMessage(20103, {'Socket': calling_instance.client, 'ErrorID': 7, 'Message': None, 'FingerprintData': Utility.getFingerprintData(contentUpdateInfo[1]), 'ContentURL': f'http://{socket.gethostbyname(socket.gethostname())}:8080'})

        elif fields["ClientMajor"] == 41:
            Messaging.sendMessage(20104, loginOkinfo)
            Messaging.sendMessage(24101, fields, calling_instance.player)
            # time.sleep(4.5)
            # fields = {"Result": 1, "Rank": 1, "MapID": [15, 0], "HeroesCount": 1, "Heroes": [{"Brawler": {"ID": [16, 0], "SkinID": [29, 0]}, "Team": 0, "IsPlayer": True, "PlayerName": "Crazor"}]}
            # fields["Socket"] = calling_instance.client
            # Messaging.sendMessage(23456, fields, calling_instance.player)

    def getMessageType(self):
        return 10101

    def getMessageVersion(self):
        return self.messageVersion