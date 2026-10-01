name = " ".join(input("Knight Name: ").split()).title()
age = int(input("Age: "))
power = int(input("Power Level: "))
xp = int(input("XP Earned: "))

level = xp // 100 + 1
rank = "Elite" if power >= 80 else "Warrior" if power >= 50 else "Rookie"
status = "Adult" if age >= 18 else "Minor"

print(f"""
⚔️ KNIGHT PROFILE
Name   : {name}
Age    : {age}
Status : {status}
Power  : {power}
XP     : {xp}
Level  : {level}
Rank   : {rank}
""")