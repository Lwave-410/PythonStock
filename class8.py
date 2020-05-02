class first_class:
    def first_function(self, cost, price, order):
        print("this is first functino")
        return (price - cost) * order

    def secon_function(self):
        print("this is second fucntion")

    def three_function(self):
        print("this is three functino")

    def four_function(self):
        print("this is four fucntion")


cooker = first_class()
print(cooker.first_function(10, 20, 30))
