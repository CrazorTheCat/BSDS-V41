import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler

OwnedBrawlersLatest = {
    0: {'CardID': 0, 'Skins': [0, 29, 52, 122, 159, 195, 196, 320, 321, 322, 358], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    1: {'CardID': 4, 'Skins': [1, 2, 103, 69, 135, 217, 303, 323, 324, 325, 326, 330, 331, 376], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    2: {'CardID': 8, 'Skins': [3, 25, 64, 102, 178, 218, 219, 262, 391], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    3: {'CardID': 12, 'Skins': [4, 5, 58, 72, 91, 201, 242, 397, 398], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    4: {'CardID': 16, 'Skins': [9, 26, 68, 130, 171, 223, 224, 394], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    5: {'CardID': 20, 'Skins': [10, 11, 96, 208, 263, 301, 302, 443], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    6: {'CardID': 24, 'Skins': [12, 27, 59, 90, 92, 116, 220, 221, 356, 433], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    7: {'CardID': 28, 'Skins': [13, 44, 47, 123, 162, 174, 253, 254, 392], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    8: {'CardID': 32, 'Skins': [14, 15, 436, 60, 79, 148, 297, 298, 346], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    9: {'CardID': 36, 'Skins': [6, 56, 57, 97, 160, 236, 276, 314, 315, 316, 395, 427, 428, 457], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    10: {'CardID': 40, 'Skins': [7, 28, 30, 128, 183, 187, 213, 317, 318, 319, 353, 359, 435, 437], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    11: {'CardID': 44, 'Skins': [18, 50, 63, 75, 173, 228, 230, 227, 229, 311], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    12: {'CardID': 48, 'Skins': [19, 20, 49, 95, 100, 101, 248, 249, 388], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    13: {'CardID': 52, 'Skins': [21, 71, 140, 214, 342, 403, 404], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    14: {'CardID': 56, 'Skins': [22, 94, 98, 99, 163, 216, 245, 362, 363, 441], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    15: {'CardID': 60, 'Skins': [23, 108, 120, 147, 197, 198, 234, 381], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    16: {'CardID': 64, 'Skins': [24, 179, 354, 408, 409], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    17: {'CardID': 68, 'Skins': [32, 111, 145, 259, 260, 282], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    18: {'CardID': 72, 'Skins': [34, 70, 158, 250, 251, 264, 350], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    19: {'CardID': 95, 'Skins': [41, 61, 88, 165, 274, 448, 449], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    20: {'CardID': 100, 'Skins': [42, 45, 125, 225, 226, 244], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    21: {'CardID': 105, 'Skins': [67, 117, 172, 304, 305, 387], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    22: {'CardID': 110, 'Skins': [86, 190, 243, 246, 247], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    23: {'CardID': 115, 'Skins': [62, 110, 126, 131, 199, 200, 312], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    24: {'CardID': 120, 'Skins': [77, 215, 309, 442, 450, 451], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    25: {'CardID': 125, 'Skins': [73, 93, 104, 132, 134, 267, 308, 421, 422], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    26: {'CardID': 130, 'Skins': [81, 146, 222, 273, 344, 419, 420], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    27: {'CardID': 177, 'Skins': [106, 109, 143, 283, 399, 400, 406], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    28: {'CardID': 182, 'Skins': [113, 118, 210, 287, 370, 371], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    29: {'CardID': 188, 'Skins': [114, 139, 188, 284, 285, 290, 364, 365], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    30: {'CardID': 194, 'Skins': [119, 167, 185, 186, 209], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    31: {'CardID': 200, 'Skins': [121, 152, 332, 333, 412], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    32: {'CardID': 206, 'Skins': [127, 137, 202, 232, 310, 401, 402], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    34: {'CardID': 218, 'Skins': [142, 176, 189, 307, 440, 444, 445], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    35: {'CardID': 224, 'Skins': [155, 180, 241, 366, 367, 386], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    36: {'CardID': 230, 'Skins': [156, 194, 233, 368, 369], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    37: {'CardID': 236, 'Skins': [157, 177, 211, 378, 382], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    38: {'CardID': 279, 'Skins': [184, 203, 292, 416], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    39: {'CardID': 296, 'Skins': [206, 212, 270, 389, 425, 426], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    40: {'CardID': 303, 'Skins': [207, 280, 423, 424], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    41: {'CardID': 320, 'Skins': [231, 237, 266, 306, 446, 447], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    42: {'CardID': 327, 'Skins': [239, 357], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    43: {'CardID': 334, 'Skins': [240, 281, 434], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    44: {'CardID': 341, 'Skins': [261, 268, 286], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    45: {'CardID': 358, 'Skins': [265, 277, 345, 417], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    46: {'CardID': 365, 'Skins': [271, 294], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    47: {'CardID': 372, 'Skins': [272, 390, 415], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    48: {'CardID': 379, 'Skins': [278], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    49: {'CardID': 386, 'Skins': [288, 343, 385], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    50: {'CardID': 393, 'Skins': [289, 453], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    51: {'CardID': 410, 'Skins': [352, 380], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    52: {'CardID': 417, 'Skins': [360], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    53: {'CardID': 427, 'Skins': [396, 430], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    54: {'CardID': 434, 'Skins': [418, 455], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
}

class LogicPurchaseOfferCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeVInt(0)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["Unk1"] = calling_instance.readVInt()
        fields["Unk2"] = calling_instance.readDataReference()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields):
        if fields["Unk1"] == 0:
            db_instance = DatabaseHandler()
            player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
            for i,v in player_data["OwnedBrawlers"].items():
                v["Skins"] = OwnedBrawlersLatest[int(i)]["Skins"]
            db_instance.updatePlayerData(player_data, calling_instance)
            Messaging.sendMessage(24104, {"Socket": calling_instance.client, "ServerChecksum": 0, "ClientChecksum": 0, "Tick": 0})

    def getCommandType(self):
        return 519