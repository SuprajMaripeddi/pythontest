from datetime import date

today = date.today()
with open('first.txt', 'r') as reader:
    # Note: readlines doesn't trim the line endings
    dog_breeds = reader.readlines()
with open('secondfile.txt', 'a') as writer:
    for breed in dog_breeds:
        writer.write(breed + '\n')
finaloutput = open("secondfile.txt", "r").read()
outputwithdate= finaloutput + "Plugins info are updated on this day" + str(today)
file1 = open("secondfile.txt", "a+")  # append mode
file1.write("Plugins info are updated on this day" + str(today) + '\n')
file1.close()
file3 = open("secondfile.txt", "r").read() # append mode
print(file3)
