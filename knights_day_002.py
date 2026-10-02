
"""
Python Marathon of Knight's — Day 002
Mission: Knight Battle Analyzer

REASONING:
1. Get two knight names and their power levels from the user.
2. Convert power inputs to integers because input() returns strings.
3. Calculate total power using addition.
4. Calculate the power gap using abs() so the difference
   is always non-negative, regardless of who has more power.
5. Compare both power levels:
   - If Knight 1 has more power, Knight 1 wins.
   - If Knight 2 has more power, Knight 2 wins.
   - If neither is stronger, the result is a draw.
6. Use None to represent that no winner exists in a draw.
   This is clearer than using a fake name or an empty string.

DESIGN DECISIONS:
- if / elif / else handles the three possible outcomes.
- winner is checked with "is None" to detect the draw state.
- f-strings make the report readable.
- This version assumes the user enters valid integer power levels.

LEARNING GOAL:
Understand how input, variables, arithmetic, comparisons,
conditional logic, and output work together in one program.
"""

print("⚔️ KNIGHT BATTLE ANALYZER ⚔️")

knight_1 = input("Enter Knight 1 name: ")
power_1 = int(input("Enter Knight 1 power: "))

knight_2 = input("Enter Knight 2 name: ")
power_2 = int(input("Enter Knight 2 power: "))

total_power = power_1 + power_2
power_gap = abs(power_1 - power_2)

if power_1 > power_2:
    winner = knight_1
elif power_2 > power_1:
    winner = knight_2
else:
    winner = None

print("\n📊 BATTLE REPORT")
print(f"{knight_1}: {power_1}")
print(f"{knight_2}: {power_2}")
print(f"Combined Power: {total_power}")
print(f"Power Difference: {power_gap}")

if winner is None:
    print("Result: DRAW 🤝")
else:
    print(f"Winner: {winner} 🏆")