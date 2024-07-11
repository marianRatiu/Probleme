# This week, we're going to play with f-strings, which in Python 3.6 provided an alternative syntax to the "str.format" method. I want to model a shopping cart, into which I can put items. I can then ask the cart to show me a short version of its contents, or a long version.
#
# Let's say that I decide to go shopping.  I'm going to create a cart, with an instance of Cart:
#     cart = Cart()
#
# I'll then add a number of items to my cart.  Each item is represented by an Item object, which has four attributes: quantity, measure, name, and price per measure.  Thus, if we're buying 1.5 kg of tomatoes at 5 currency units per kg, we'd say:
#     cart.add(Item(1.5, 'kg', 'tomatoes', 5))
#
# We can then add a bunch of such items to our shopping cart:
#     cart.add(Item(2, 'kg', 'cucumbers', 4))
#     cart.add(Item(1, 'tube', 'toothpaste',2))
#     cart.add(Item(1, 'box', 'tissues',4))
#
# We can then ask our cart for two different types of reports, using str.format. If we pass our object the "short" keyword after the colon in the format string, we'll just get an alphabetized list of the items:
#     print(f"Your cart contains: {cart:short}")
#
# In our case, that'll print:
#     Your cart contains: cucumbers, tissues, tomatoes, toothpaste
#
# But we can also ask for a "long" report using the format string, as follows:
#      print(f"Your cart:\n{cart:long}")
#
# The results:
#     Your cart:
#                 2 kg    cucumbers  @ $4.0...$8.0
#                 1 box   tissues    @ $4.0...$4.0
#               1.5 kg    tomatoes   @ $5.0...$7.5
#                 1 tube  toothpaste @ $2.0...$2.0
#
# You can, of course, adjust the formatting so that it's a bit nicer than this. But the idea is to have a table with the four attributes -- plus a final column containing the cost of that item.
#
# You'll need to create the Item and Cart classes, with particular emphasis on ensuring it works with str.format.
# class Item:
    def __init__(self,quantity,measure,name,price):
        self.quantity = quantity
        self.measure =measure
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.quantity} {self.measure} {self.name} at ${self.price}...${self.price*self.quantity}"
class Cart:

    def __init__(self):
        self.lst = []
    def add(self,item:Item):
        self.lst.append(item)

    def __format__(self, format_spec):
        if format_spec == "short":
            item_names = sorted(item.name for item in self.lst)
            return",".join(item_names)
        elif format_spec == "long":
            detailed_report ="\n".join(str(item) for item in self.lst)
            return detailed_report
        else:
            return super().__format__(format_spec)


cart = Cart()
cart.add(Item(1.5, 'kg', 'tomatoes', 5))
cart.add(Item(2, 'kg', 'cucumbers', 4))
cart.add(Item(1, 'tube', 'toothpaste', 2))
cart.add(Item(1, 'box', 'tissues', 4))

print(f"Your cart contains: {cart:short}")

print(f"Your cart:\n{cart:long}")