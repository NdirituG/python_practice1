age = 20
is_teen = age > 12 and age < 20
print(is_teen)
# this is a string printed in python
phrase = '"and she said", you\'re a bad person!'
print(phrase)
FirstName = "Denis"
SecondName = "Macharia"
FullName = (FirstName + " " + SecondName)
print(FirstName * 5)
print(len(FullName))
coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)
print("hippo" * 12)
print("the caucasian chalk circle".title())
print(FullName.upper())
text = "One fish, two fish, red fish, blue fish."
print(text.count('fish '))
laptop = "Acer"
print(laptop.lower())
print(laptop.upper())
print(FullName.isspace())
print(FullName.count('a'))
print("Denis has {} balloons".format(50))
artist = "Freddie Mercury"
thats_what_he_said = "another one bites the dust"
print("one famous singer, {} said, {}.".format(artist, thats_what_he_said))
new_phrase = "Paw, of the Kung Fu Panda once said, \"Stairs, my old nemesis!\""
print(new_phrase.split(None, 3))
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust " \
        "yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be " \
        "tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating," \
        "\n  And yet don’t look too good, nor talk too wise: "
print(verse)
message = "the length of the string verse is {}. The index of the first occurrence of the word 'and' in verse is {}\n"\
    ". The index of the last occurrence of the word 'you in verse is {} and the count of the occurences of the word 'you'\n"\
    " in verse is {}."
length = len(verse)
first_index = verse.find('and')
last_index = verse.rfind('you')
count = verse.count('you')
print(message.format(length, first_index, last_index, count))
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
months.pop()
months.append("malaya")
months[3] = "Denis\' Day"
print(months)
print(months)
print(months[0] + "\n", months[5])
print(len(months[0]))
print(len(months))
print(months[-1][0])
q1 = months[-1:-3]
print("the first three months of the year are: " + str(q1))
print("The first six months of the year are: " + str(months[:6]))
print('and' in verse, 'you' not in verse)
print('January' in months)
bool_for_string = 'this' in 'this is a string'
print(bool_for_string)
print(type(months))
VINIX = ['C', 'MA', 'BA', 'PG', 'CSCO', 'VZ', 'PFE', 'HD', 'INTC', 'T', 'V', 'UNH', 'WFC', 'CVX',
         'BAC', 'JNJ', 'GOOGL', 'GOOG', 'BRK.B', 'XOM', 'JPM', 'FB', 'AMZN', 'MSFT', 'AAPL']
print("VINIX is of type " + str(type(VINIX)))
print('MA' in VINIX)
sentence1 = "I wish to register a complaint."
print(sentence1[30])
scores = ["B", "C", "A", "D", "B", "A"]
grades = scores
print("variable scores is of type " + str(type(scores)))
print("variable grades is of type " + str(type(grades)))
print("scores: " + str(scores))
del months[-1]
print(months)
print(sorted(months, reverse=True))
new_str = "-".join(["a", "computer", "is", "an", "electronic",
                    "device", "that", "accepts"])
print(new_str)
a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]
print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))
names = ["Carol", "Albert", "Ben", "Donna"]
print("&".join(sorted(names)))
names2 = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))
Thika = (13.4125, 103.866667)
print(type(Thika))
print("Thika is at latitude: {} and longitude {}".format(Thika[0], format(Thika[1])))
numbers = [1, 2, 6, 3, 1, 1, 6]
print(type(numbers))
uniq_no = set(numbers)
print(type(uniq_no), uniq_no)
fruit = {1, 2, 6, 3, 1, 1, 6}
fruit.add(7)
print(fruit)
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))
b.add(5)
print(b.pop())
elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
print(type(elements))
print(elements['carbon'])
names = {'Brian': 924, 'Denis': 35, 'John': 57, 'Moses': 56}
print(type(names))
names['Kevin'] = 53
print(names)
print('Ian' in names)
x = (names.get('Barbara'))
is_null = x is None
print(is_null)
