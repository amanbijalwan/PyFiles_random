
user0 = {
    'name': 'Tom',
    'username': 'jerryHunter',
    'pass': 'eatSleepRepeat'
}

for key, value in user0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print("\n\n")

aliens = []

for alien in range(30):
    new_alien = {'color': 'green', 'speed': '20', 'points': '10'}
    aliens.append(new_alien)
print(".........")

for alien in aliens[:5]:
    print(alien)

print(f"Total aliens are: {len(aliens)}")