#Write a program that will accept user input that describes a tire then calculate and display the tire's volume. Record the tire information in a log file.
tire_width = float(input("Enter the tire width (mm): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
wheel_diameter = float(input("Enter the diameter of the wheel (inches): "))
import math
# Calculate the volume of the tire
volume = (math.pi * tire_width**2 * aspect_ratio * (tire_width * aspect_ratio + 2540 * wheel_diameter)) / 10000000000
print(f"The volume of the tire is {volume:.2f} liters.")
from datetime import datetime
current_date_and_time = datetime.now()
print(f"Date: {current_date_and_time.date()}")
# Log the information in a text file
from datetime import datetime 
with open("tire_volume_log.txt", "a") as log_file:
    log_file.write(f"{current_date_and_time.date()}, {tire_width}, {aspect_ratio}, {wheel_diameter}, {volume:.2f}\n")
#Have the user enter a tire width in mm.
#Have the user enter the aspect ratio.
#Have the user enter the diameter of the wheel in inches.
#Calculate and display the tire's volume.
#Log the information in a text file.
#current date (Do NOT include time)
#width of the tire
#aspect ratio of the tire
#diameter of the wheel
#volume of the tire (rounded to two decimal places)