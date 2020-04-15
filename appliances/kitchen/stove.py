from appliances.appliance import Appliance

class Stove(Appliance):

    def __init__(self, color, heat_method="electric"):
        super(Stove, self).__init__(color)

    def cook_food(self):
        print("Ding. Your food of choice is piping hot and ready!")
