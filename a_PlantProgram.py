import a_PlantClass as pc

primrose = pc.Plant("Green")  # instance of Superclass

sunflower = pc.Flower("Yellow")  # instance of Subclass, requires 2
# arguments: color AND petals

print(primrose.get_color())

# Works bc subclass inherits method from superclass
print(sunflower.get_color())
print(sunflower.get_petals())


# print(primrose.get_petals())  # Superclass cannot call methods from subclass
