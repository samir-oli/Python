# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# timmy.left(200)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("name", ['samir', 'prabin', 'saurab'])
table.add_column("type", ["electric", "water", "Fire"])
print(table.align)

print(table)