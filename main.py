from prettytable import PrettyTable
from turtle import Turtle,Screen
import another_module
print(another_module.another_variable)
timmy=Turtle()
timmy.shape("turtle")
timmy.color("chartreuse3")
timmy.forward(100)
print(timmy)
my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
table=PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Carmender"])
table.add_column("Type",["Electric",'Water',"Fire"])
print(table._align="l")
print(table)
