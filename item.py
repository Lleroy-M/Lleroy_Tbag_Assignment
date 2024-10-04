class Item():
    def __init__(self): 
        self.name = None
        self.get_description = None

    def get_name(self):
        return self.name
    
    def set_name(self, item_name):
        self.name = item_name

    def get_description(self):
        return self.get_description
    
    def set_description(self, item_description):
        self.description = item_description