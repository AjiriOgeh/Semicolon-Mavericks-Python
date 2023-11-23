age = int(input("Enter your age: "))
maxheartrate = 220 - age

targetheartrate1 = (50 / 100) * maxheartrate
targetheartrate2 = (85 / 100) * maxheartrate

print("Your maximum heartrate is", maxheartrate,"beats per minute")
print(f"Your target heart rate is between {targetheartrate1:.2f} beats per minute to {targetheartrate2:.2f} beats per minute")