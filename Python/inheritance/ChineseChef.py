from Chef import Chef

# Chef is inherited by ChineseChef so now all of Chef's methods are available to ChineseChef


class ChineseChef(Chef):

    def make_fried_rice(self):
        print("The Chef made fried rice")


myChef = ChineseChef()
myChef.make_special_dish()  # burritos?
