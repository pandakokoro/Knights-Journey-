
"""
Python Marathon of Knight's — Day 004
Mission: Knight Squad Analyzer

REASONING:
1. Store multiple knight power levels in a list.
2. Use a loop to process each power level.
3. Add each power level to the squad's total power.
4. Count knights whose power is at least 60.
5. Track the strongest power encountered.

DESIGN DECISIONS:
- A list stores multiple values in one variable.
- A for loop processes each item without repeating code.
- total_power and ready_count are accumulators.
- strongest_power tracks the maximum seen so far.
- Starting strongest_power at 0 assumes power levels are non-negative.

ASSUMPTIONS:
- The list contains integer power levels.
- A knight is battle-ready when power >= 60.
- The list is not empty.

LEARNING GOAL:
Understand lists, iteration, accumulators, counting,
and tracking a running maximum.
"""

print("⚔️ KNIGHT SQUAD ANALYZER ⚔️")

powers = [45, 80, 65, 30, 95]

total_power = 0
ready_count = 0
strongest_power = 0

for power in powers:
    total_power += power

    if power >= 60:
        ready_count += 1

    if power > strongest_power:
        strongest_power = power

print("\n📊 SQUAD REPORT")
print(f"Squad Size: {len(powers)}")
print(f"Total Power: {total_power}")
print(f"Battle-Ready Knights: {ready_count}")
print(f"Strongest Power: {strongest_power}")
