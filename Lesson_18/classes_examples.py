class River:
    # list of all rivers
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length

        # adding current river to the list of all rivers.
        River.all_rivers.append(self)

    def get_info(self):
        print(f'The length of the {self.name} is {self.length} km.')


        # creating class instances/objects.
nile = River('Nile', 39405)
ganga = River('Ganga', 34566)
cavery = River('Cavery', 345)

# print all river names
for river in River.all_rivers:
    print(river.name)

# calling a method.
# self.method()
nile.get_info()
# we could also call the method in a different way.
# class.method(self)
River.get_info(ganga)
