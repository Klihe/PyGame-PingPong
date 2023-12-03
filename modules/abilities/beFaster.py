from modules.abilities.ability import Ability

class BeFaster(Ability):
    def __init__(self, player, slot, cooldownTime, abilityTime, speedIncrease):
        super().__init__(player, cooldownTime, abilityTime)
        self.slot = slot
        self.speedIncrease = speedIncrease

    def startFunc(self):
        super().startFunc()
        if self.active:
            self.player.speed = self.speedIncrease

    def endFunc(self):
        super().endFunc()

    def updateFunc(self):
        super().updateFunc()