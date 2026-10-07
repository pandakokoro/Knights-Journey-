"""
Python Marathon of Knight's — Day 003
Mission: Knight Rank & Battle Readiness Analyzer

REASONING:
1. Get the Knight's name, power, and XP from the user.
2. Convert numerical input into integers so calculations and
   comparisons can be performed.
3. Calculate the Knight's level from XP.
4. Determine the Knight's rank from power:
   - 80 or more  -> Elite
   - 50 or more  -> Warrior
   - otherwise   -> Rookie
5. Determine battle readiness using both power and XP.
6. A Knight is battle-ready only when:
   - power is at least 60
   - XP is at least 500
7. Use a boolean variable to store the readiness state.
8. Display all calculated information in a readable report.

DESIGN DECISIONS:
- if / elif / else is used for mutually exclusive rank levels.
- and is used because both readiness requirements must be true.
- Boolean state is stored instead of repeating the condition.
- f-strings are used for formatted output.

ASSUMPTIONS:
- Name is entered as text.
- Power and XP are valid integers.
- Power and XP are non-negative.

LEARNING GOAL:
Understand how multiple conditions combine with
arithmetic and variables to produce a meaningful program state.
"""

print("⚔️ KNIGHT READINESS ANALYZER ⚔️")

name = input("Knight Name: ")
power = int(input("Power Level: "))
xp = int(input("XP Earned: "))

level = xp // 100 + 1

if power >= 80:
    rank = "Elite"
elif power >= 50:
    rank = "Warrior"
else:
    rank = "Rookie"

ready = power >= 60 and xp >= 500

print("\n📊 KNIGHT REPORT")
print(f"Name   : {name}")
print(f"Power  : {power}")
print(f"XP     : {xp}")
print(f"Level  : {level}")
print(f"Rank   : {rank}")
print(f"Ready  : {ready}")