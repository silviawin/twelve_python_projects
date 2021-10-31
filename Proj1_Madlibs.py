
# string concatenation 3 types
# say "subscribe to ______"
# youtuber = ""
#  1) print("subscribe to" + youtuber)
#  2) print("subscribe to {}" .format(youtuber))
#  3) print(f"subscribe to {youtuber}")

youtuber = "Kylie Ying"
print("subscribe to " + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Please say a verb: ")
verb2 = input("Please say anoter verb: ")
plant = input("Name of a plant: ")


madLib = f"Computer program is so {adj}! It makes me so excited all the time because \"" \
         f"I love to {verb1}. Stay hydrated and {verb2} like you are a {plant}!"

print(madLib)
