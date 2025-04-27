print("Enter your Details")
YourName = str(input("Your Name:"))
YourAge = int(input("Your age:"))
CityYouLiveIn = str(input("City You Live In:"))
YourFavouriteFood =  str(input("Your Favourite Food:"))
YourFavouriteColor = str(input("Your Favourite Color:"))
YourSpiritAnimal = str(input("Your Spirit Animal:"))
OneThingYouLoveDoing=  str(input("One Thing You LOVE Doing:"))

print("🧠 Know Your Personality")
print("✨ Let's discover who you really are with some fun data magic!")
print("Scanning colors, foods, and animal energies...")

import time
time.sleep(2)

print("💫 Calculating your personality type using complex non-scientific logic...")
YourAgeInMonths = YourAge *12
lastDigitOfAge = YourAge % 10
SecretPersonality = YourName[:2].upper() + str(lastDigitOfAge) + YourSpiritAnimal[0] + YourFavouriteColor[0]
if YourAgeInMonths < 18:
    YourTitle = "Young Explorer"
elif YourAgeInMonths >= 18 and YourAgeInMonths <= 30:
    YourTitle = "Adventurer"
elif YourAgeInMonths > 30: 
    YourTitle ="Wise Owl"
else:
    print("invalid Age")
time.sleep(2)
print(f"\n 🎉 Hey {YourName}, here's your fun personality report!")

print(f"\n🌆 You're from {CityYouLiveIn}, a place of dreams!")

print(f"\n🍿 You love {YourFavouriteFood} and enjoy doing {OneThingYouLoveDoing}.")

print(f"\n🎨 You vibe with the color {YourFavouriteColor} and your spirit animal is the {YourSpiritAnimal}")

print(f"\n📅 You've lived approximately {YourAgeInMonths} months already.")

print(f"\n🧩 You belong to the '{YourTitle}' tribe.")

print(f"\n🔐 Your Secret Personality Code is: 💡 {SecretPersonality}")