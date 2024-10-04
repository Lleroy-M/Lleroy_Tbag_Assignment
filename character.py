class character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description 
        self.conversation = None

    def describe(self):
        print(f"{self.name}is in this room1") 
        print(self. description)

    def set_conversation(self, conversation):
        self.conversation = conversation 

    def get_conversation(self):
        return self.conversation

    def talk(self):
        if self.set_conversation is not None:
            print(f"[{self.name}] says: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you")

    def fight(self, combat_item):
        print(f"{self.name} doesn't want to talk to you")
        return True
    
class Enemy(character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"you fend {self.name} off with the {combat_item}!!")
            return True 
        else: 
            print(f"{self.name} crashes you, peny adventurer")
            return False
