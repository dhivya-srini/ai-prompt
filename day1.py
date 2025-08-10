'''from rich import print
from rich.panel import Panel

name = "Dhivya"
age = 25
interest = "AI Tools"

content = f"My name is: {name}\nAge: {age} years old\nInterest: {interest}"
print(Panel(content, title="AI PROFILE"))'''
'''from tabulate import tabulate

rows = [["My name is", "Dhivya"],
        ["Age", "25 years old"],
        ["Interest", "AI Tools"]]

print(tabulate(rows, tablefmt="grid"))'''
width = 40   # choose once
title = "AI PROFILE"
lines = ["My name is: Dhivya", "Age: 25 years old", "Interest: AI Tools"]

print("+" + "="*width + "+")
print("|" + title.center(width) + "|")
print("+" + "-"*width + "+")
for s in lines:
    print("|" + s.center(width) + "|")
print("+" + "-"*width + "+")
