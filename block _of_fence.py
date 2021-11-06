"""
here is the python code that calculates the amount of the blocks needed to fence a piece of land regsrdless of the size
"""
length _of_land = int(input("please enter the length of the land in the feet"))
width_of_land = int(input("please enter the length of the land in feet"))
perimeter_of_land = 2*(length_of_land + width_of_land)

#using f-string print formatting
print(f"hereis the perimeterof the land in feet ={perimeter_of_land")feet

#converting feet to metre
length_in_meter =round(perimeter_of_land * 0.3048)
print(f"here is the length of the land in metre: {length_in_metre} metre")
#space for gate
space_for_gate =int(input("please enter the space needed for the gate in feet"))
space_for_gate_metre = round(space_for_gate * 0.3048)
print(f"the space you ")