

class Effect:
    def __init__(self, function, effect_class, effect_type, blockable, value, addition) -> None:
        self.function = function
        self.effect_class = effect_class
        self.type = effect_type
        self.blockable = blockable
        self.value = value

    def update_effect(self):
        if self.duration > 0:
            self.duration -= 1
