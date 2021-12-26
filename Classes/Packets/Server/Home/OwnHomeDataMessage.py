import time

from Classes.Packets.PiranhaMessage import PiranhaMessage


class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        ownedBrawlersCount = len(player.OwnedBrawlers)
        ownedPinsCount = len(player.OwnedPins)
        ownedThumbnailCount = len(player.OwnedThumbnails)
        ownedSkins = []

        for brawlerInfo in player.OwnedBrawlers.values():
            try:
                ownedSkins.extend(brawlerInfo["Skins"])
            except KeyError:
                continue

        self.writeVint(int(time.time()))
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(player.Trophies) # Trophies
        self.writeVint(player.HighestTrophies) # Highest Trophies
        self.writeVint(player.HighestTrophies)
        self.writeVint(player.TrophyRoadTier)
        self.writeVint(player.Experience) # Experience
        self.writeDataReference(28, player.Thumbnail) # Thumbnail
        self.writeDataReference(43, player.Namecolor) # Namecolor

        self.writeVint(0)

        self.writeVint(0) # Selected Skins

        self.writeVint(0) # Randomizer Skin Selected

        self.writeVint(0) # Current Random Skin

        self.writeVint(len(ownedSkins))

        for skinID in ownedSkins:
            self.writeDataReference(29, skinID)

        self.writeVint(0) # Unlocked Skin Purchase Option

        self.writeVint(0) # New Item State

        self.writeVint(0)
        self.writeVint(player.HighestTrophies)
        self.writeVint(0)
        self.writeVint(1)
        self.writeBoolean(True)
        self.writeVint(player.TokensDoubler)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(141)
        self.writeVint(135)

        self.writeVint(5)

        self.writeVint(93)
        self.writeVint(206)
        self.writeVint(456)
        self.writeVint(792)
        self.writeVint(729)

        self.writeBoolean(False) # Offer 1
        self.writeBoolean(False) # Offer 2
        self.writeBoolean(True) # Token Doubler Enabled
        self.writeVint(2)  # Token Doubler New Tag State
        self.writeVint(2)  # Event Tickets New Tag State
        self.writeVint(2)  # Coin Packs New Tag State
        self.writeVint(0)  # Change Name Cost
        self.writeVint(0)  # Timer For the Next Name Change

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(player.Tokens)
        self.writeVint(-1)

        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(len(player.SelectedBrawlers))
        for i in player.SelectedBrawlers:
            self.writeDataReference(16, i)

        self.writeString(player.Region)
        self.writeString(player.ContentCreator)

        self.writeVint(19)
        self.writeLong(2, 1)  # Unknown
        self.writeLong(3, 0)  # TokensGained
        self.writeLong(4, 0)  # TrophiesGained
        self.writeLong(6, 0)  # DemoAccount
        self.writeLong(7, 0)  # InvitesBlocked
        self.writeLong(8, 0)  # StarPointsGained
        self.writeLong(9, 1)  # ShowStarPoints
        self.writeLong(10, 0)  # PowerPlayTrophiesGained
        self.writeLong(12, 1)  # Unknown
        self.writeLong(14, 0)  # CoinsGained
        self.writeLong(15, 0)  # AgeScreen | 3 = underage (disable social media) | 1 = age popup
        self.writeLong(16, 1)
        self.writeLong(17, 1)  # TeamChatMuted
        self.writeLong(18, 1)  # EsportButton
        self.writeLong(19, 1)  # ChampionShipLivesBuyPopup
        self.writeLong(20, 0)  # GemsGained
        self.writeLong(21, 1)  # LookingForTeamState
        self.writeLong(22, 1)
        self.writeLong(24, 1)  # Have already watched club league stupid animation

        self.writeVint(0)

        self.writeVint(2)  # Brawlpass
        for i in range(8, 10):
            self.writeVint(i)
            self.writeVint(34500)
            self.writeBoolean(True)
            self.writeVint(0)

            self.writeUInt8(2)
            self.writeUInt(4294967292)
            self.writeUInt(4294967295)
            self.writeUInt(511)
            self.writeUInt(0)

            self.writeUInt8(1)
            self.writeUInt(4294967292)
            self.writeUInt(4294967295)
            self.writeUInt(511)
            self.writeUInt(0)

        self.writeVint(0)

        self.writeBoolean(True)
        self.writeVint(0)

        self.writeBoolean(True)
        self.writeVint(ownedPinsCount + ownedThumbnailCount)  # Vanity Count
        for i in player.OwnedPins:
            self.writeDataReference(52, i)
            self.writeVint(1)
            for i in range(1):
                self.writeVint(1)
                self.writeVint(1)

        for i in player.OwnedThumbnails:
            self.writeDataReference(28, i)
            self.writeVint(1)
            for i in range(1):
                self.writeVint(1)
                self.writeVint(1)

        self.writeBoolean(False)

        self.writeInt(0)

        self.writeVint(0)

        self.writeVint(25) # Count

        self.writeVint(1)
        self.writeVint(2)
        self.writeVint(3)
        self.writeVint(4)
        self.writeVint(5)
        self.writeVint(6)
        self.writeVint(7)
        self.writeVint(8)
        self.writeVint(9)
        self.writeVint(10)
        self.writeVint(11)
        self.writeVint(12)
        self.writeVint(13)
        self.writeVint(14)
        self.writeVint(15)
        self.writeVint(16)
        self.writeVint(17)
        self.writeVint(20)
        self.writeVint(21)
        self.writeVint(22)
        self.writeVint(23)
        self.writeVint(24)
        self.writeVint(30)
        self.writeVint(31)
        self.writeVint(32)

        self.writeVint(3) # Events

        eventIndex = 1
        for i in [5, 7, 24]:
            self.writeVint(-1)
            self.writeVint(eventIndex)  # EventType
            self.writeVint(0)  # EventsBeginCountdown
            self.writeVint(51208)  # Timer
            self.writeVint(0)  # tokens reward for new event
            self.writeDataReference(15, i)  # MapID
            self.writeVint(-1)  # GameModeVariation
            self.writeVint(2)  # State
            self.writeString()
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)  # Modifiers
            self.writeVint(0)
            self.writeVint(0)
            self.writeBoolean(False)  # Map Maker Map Structure Array
            self.writeVint(0)
            self.writeBoolean(False)  # Power League Data Array
            self.writeVint(0)
            self.writeVint(0)
            self.writeBoolean(False)  # ChronosTextEntry
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeVint(-1)
            self.writeBoolean(False)
            self.writeBoolean(False)
            eventIndex += 1

        self.writeVint(0) # Comming Events

        self.writeVint(10)  # Brawler Upgrade Cost
        self.writeVint(20)
        self.writeVint(35)
        self.writeVint(75)
        self.writeVint(140)
        self.writeVint(290)
        self.writeVint(480)
        self.writeVint(800)
        self.writeVint(1250)
        self.writeVint(1875)
        self.writeVint(2800)

        self.writeVint(4)  # Shop Coins Price
        self.writeVint(20)
        self.writeVint(50)
        self.writeVint(140)
        self.writeVint(280)

        self.writeVint(4)  # Shop Coins Amount
        self.writeVint(150)
        self.writeVint(400)
        self.writeVint(1200)
        self.writeVint(2600)

        self.writeBoolean(True)  # Show Offers Packs

        self.writeVint(0)

        self.writeVint(23)  # IntValueEntry

        self.writeLong(10008, 501)
        self.writeLong(65, 2)
        self.writeLong(1, 41000036)  # ThemeID
        self.writeLong(60, 36270)
        self.writeLong(66, 1)
        self.writeLong(61, 36270)  # SupportDisabled State | if 36218 < state its true
        self.writeLong(47, 41381)
        self.writeLong(29, 0)  # Skin Group Active For Campaign
        self.writeLong(48, 41381)
        self.writeLong(50, 0)  # Coming up quests placeholder
        self.writeLong(1100, 500)
        self.writeLong(1101, 500)
        self.writeLong(1003, 1)
        self.writeLong(36, 0)
        self.writeLong(14, 0)  # Double Token Event
        self.writeLong(31, 0)  # Gold rush event
        self.writeLong(79, 149999)
        self.writeLong(80, 160000)
        self.writeLong(28, 4)
        self.writeLong(74, 1)
        self.writeLong(78, 1)
        self.writeLong(17, 4)
        self.writeLong(10046, 1)

        self.writeVint(0) # Timed Int Value Entry

        self.writeVint(0)  # Custom Event

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeLong(player.ID[0], player.ID[1])  # PlayerID

        self.writeVint(0) # NotificationFactory

        self.writeVint(-1)
        self.writeBoolean(False)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(0, 0)
        self.writeVLong(0, 0)

        self.writeString(player.Name)
        self.writeBoolean(player.Registered)

        self.writeInt(0)

        self.writeVint(15)

        self.writeVint(3 + ownedBrawlersCount)

        for brawlerInfo in player.OwnedBrawlers.values():
            self.writeDataReference(23, brawlerInfo["CardID"])
            self.writeVint(1)

        self.writeDataReference(5, 8)
        self.writeVint(player.Coins)

        self.writeDataReference(5, 10)
        self.writeVint(player.StarPoints)

        self.writeDataReference(5, 13)
        self.writeVint(99999) # Club coins

        self.writeVint(ownedBrawlersCount)

        for brawlerID,brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVint(brawlerInfo["Trophies"])

        self.writeVint(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVint(brawlerInfo["HighestTrophies"])

        self.writeVint(0)

        self.writeVint(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVint(brawlerInfo["PowerPoints"])

        self.writeVint(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVint(brawlerInfo["PowerLevel"] - 1)

        self.writeVint(0)

        self.writeVint(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVint(brawlerInfo["State"])

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(player.Gems)  # Diamonds
        self.writeVint(player.Gems)  # Free Diamonds
        self.writeVint(player.Level)  # Player Level
        self.writeVint(100)
        self.writeVint(0)  # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVint(0)  # Battle Count
        self.writeVint(0)  # WinCount
        self.writeVint(0)  # LoseCount
        self.writeVint(0)  # WinLooseStreak
        self.writeVint(0)  # NpcWinCount
        self.writeVint(0)  # NpcLoseCount
        self.writeVint(2)  # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVint(0)

    def decode(self):
        fields = {}
        # fields["AccountID"] = self.readLong()
        # fields["HomeID"] = self.readLong()
        # fields["PassToken"] = self.readString()
        # fields["FacebookID"] = self.readString()
        # fields["GamecenterID"] = self.readString()
        # fields["ServerMajorVersion"] = self.readInt()
        # fields["ContentVersion"] = self.readInt()
        # fields["ServerBuild"] = self.readInt()
        # fields["ServerEnvironment"] = self.readString()
        # fields["SessionCount"] = self.readInt()
        # fields["PlayTimeSeconds"] = self.readInt()
        # fields["DaysSinceStartedPlaying"] = self.readInt()
        # fields["FacebookAppID"] = self.readString()
        # fields["ServerTime"] = self.readString()
        # fields["AccountCreatedDate"] = self.readString()
        # fields["StartupCooldownSeconds"] = self.readInt()
        # fields["GoogleServiceID"] = self.readString()
        # fields["LoginCountry"] = self.readString()
        # fields["KunlunID"] = self.readString()
        # fields["Tier"] = self.readInt()
        # fields["TencentID"] = self.readString()
        #
        # ContentUrlCount = self.readInt()
        # fields["GameAssetsUrls"] = []
        # for i in range(ContentUrlCount):
        #     fields["GameAssetsUrls"].append(self.readString())
        #
        # EventUrlCount = self.readInt()
        # fields["EventAssetsUrls"] = []
        # for i in range(EventUrlCount):
        #     fields["EventAssetsUrls"].append(self.readString())
        #
        # fields["SecondsUntilAccountDeletion"] = self.readVint()
        # fields["SupercellIDToken"] = self.readCompressedString()
        # fields["IsSupercellIDLogoutAllDevicesAllowed"] = self.readBoolean()
        # fields["isSupercellIDEligible"] = self.readBoolean()
        # fields["LineID"] = self.readString()
        # fields["SessionID"] = self.readString()
        # fields["KakaoID"] = self.readString()
        # fields["UpdateURL"] = self.readString()
        # fields["YoozooPayNotifyUrl"] = self.readString()
        # fields["UnbotifyEnabled"] = self.readBoolean()
        # super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion