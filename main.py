def last_early(my_str):
    my_new_str = my_str[:-1]
    my_str = my_str.lower()
    if my_str[-1] in my_new_str.lower():
        return True
    else:
        return False


# print(last_early("Wow"))

def distance(num1, num2, num3):
    if abs(num2) - abs(num1) < abs(2) or abs(num3) - abs(num1) < abs(2):
        if abs(num2) - abs(num1) > abs(2) or abs(num2) - abs(num3) > abs(2) or abs(num3) - abs(num1) > abs(2):
            return True
    return False


def fix_age(age):
    if age in range(13, 20):
        if age in range(15, 17):
            return float(age)
        age = age - age
    return float(age)


def filter_teens(a=13, b=13, c=13):
    res = fix_age(a) + fix_age(b) + fix_age(c)
    return res


def chocolate_maker(small, big, x):
    print(chocolate_maker(3, 1, 8))


def func(num1, num2):
    """
    this function multiplicate the 2 parameters
    :param num1: a number
    :param num2: a number
    :type num1: float
    :type num2: float
    :return: multiplication of the 2 params
    :rtype: float
    """
    return num1 * num2


def main():
    print(func(3, 4))


if _name_ == "_main_":
    main()


def shift_left(my_list):
    new_list = my_list[:1]
    my_list = my_list[1:]
    print(my_list + new_list)


# res = shift_left(['monkey', 2.0, 1])
# print(res)

def format_list(my_list):
    n = len(my_list)
    # s = ", "
    # s.join(my_list)
    l = "and "
    l.join(my_list[n - 1])
    return (my_list)


# my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
# x = format_list(my_list)
# print(x)

def extend_list_x(list_x, list_y):
    n = len(list_y)
    list_x.insert(0, list_y[2])
    list_x.insert(0, list_y[1])
    list_x.insert(0, list_y[0])
    print(list_x)


# x = [4, 5, 6]
# y = [1, 2, 3]
# res = extend_list_x(x, y)
# print(res)

def are_lists_equal(list1, list2):
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False


# w = [0.6, 1, 2, 3]
# e = [3, 2, 0.6, 1]
# r = [9, 0, 5, 10.5]
# res = are_lists_equal(w, e)
# print(res)

def longest(my_list):
    x = sorted(my_list, key=len)
    n = len(my_list)
    print(x[n - 1])


# lst1 = ["111", "234", "2000", "goru", "birthday", "09"]
# res = longest(lst1)
# print(res)

def squared_numbers(start, stop):
    x = start
    while x < stop + 1:
        print(x * x)
        x += 1


# res = squared_numbers(-3, 3)
# print(res)

def is_greater(my_list, n):
    for num in my_list:
        if num >= n:
            print(num)


# res1 = is_greater([1, 30, 25, 60, 27, 28], 28)
# print(res1)

def numbers_letters_count(my_str):
    numbers = "0987654321"
    x = 0
    for i in my_str:
        if i in numbers:
            x += 1
            y = len(my_str)
            res = [x, y - x]
    print(res)


# res2 = numbers_letters_count("Python 3.6.3")
# print(res2)


def seven_boom(end_number):
    for num in range(end_number):
        if "7" in str(num) or num % 7 == 0:
            num = "BOOM"
        print(num)


# res3 = seven_boom(47)
# print(res3)

def sequence_del(my_str):
    my_new_str = ""
    last_char = ""
    for x in my_str:
        if x == last_char:
            continue
        else:
            my_new_str += x
            last_char = x
    print(my_new_str)


# res4 = sequence_del("SSSSsssshhhh")
# print(res4)

# tomatoes,potatoes,onions,mushrooms,cheese,eggs,meat,cheese,cheese

# groceries = input('write a list of groceries (one comma between them but no spaces): ', )
# list_of_groceries = groceries.split(',')
# action = input('choose a number between 1-9: ', )

def item():
    item = input('check if item on the list, write an item: ', )
    if item in list_of_groceries:
        return True
    else:
        return False


def is_item_on_list():
    is_item = input('check how many of this item are on the list, write an item: ', )
    how_many = list_of_groceries.count(is_item)
    return (how_many)


def remove_item():
    is_item = input('remove the exessive items, write an item: ', )
    list_of_groceries.remove(is_item)
    return (list_of_groceries)


def remove_items():
    is_item = input('remove the exessive items, write an item: ', )
    how_many = list_of_groceries.count(is_item)
    for i in range(how_many - 1):
        list_of_groceries.remove(is_item)
    return (list_of_groceries)


def check_errors():
    for i in list_of_groceries:
        if len(i) < 4:
            print('these do not fit on the list of groceries:', i)
        L = list(i)
        for x in L:
            if x.isalpha() == False:
                print('these do not fit on the list of groceries:', i)


def groceries_to_do():
    action1 = action
    while True:
        if action1 == "1":
            print(list_of_groceries)
            action1 = input('choose a number between 1-9: ', )
        elif action1 == "2":
            print(len(list_of_groceries))
            action1 = input('choose a number between 1-9: ', )
        elif action1 == "3":
            res = item()
            if res == True:
                print("yes, this item is on the list")
            else:
                print("no, the item is not on the list")
            action1 = input('choose a number between 1-9: ', )
        elif action1 == "4":
            res1 = is_item_on_list()
            print(res1)
            action1 = input('choose a number between 1-9: ', )
        elif action1 == "5":
            is_item = input('choose an item to remove from list, write an item: ', )
            list_of_groceries.remove(is_item)
            print(list_of_groceries)
            action1 = input('choose a number between 1-9: ', )
        elif action1 == "6":
            add_item = input('add this item to the list, write an item: ', )
            list_of_groceries.append(add_item)
            print(list_of_groceries)
            action1 = input('choose a number between 1-9: ', )
        elif action1 == "7":
            res3 = check_errors()
            print(res3)
            action1 = input('choose a number between 1-9: ', )
        elif action1 == "8":
            res4 = remove_items()
            print(res4)
            action1 = input('choose a number between 1-9: ', )
        else:
            break


# res = groceries_to_do()
# print(res)

def arrow(my_char, max_length):
    for i in range(max_length + 1):
        print(my_char * i)
    for i in range(max_length - 1, 0, -1):
        print(my_char * i)


# print(arrow('*', 5))

tuples = [('apple', '5.4'), ('orange', '7.2'), ('yellow', '5.0')]


def tup(s):
    return s[-1]


def sort_prices(list_of_tuples):
    print
    sorted(list_of_tuples, key=tup)


# res2 = sort_prices(tuples)
# print(res2)

first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)


def mult_tuple(tuple1, tuple2):
    for i in tuple1:
        for x in tuple2:
            print(i, x)
    for i in tuple2:
        for x in tuple1:
            print(i, x)


# res = mult_tuple(first_tuple, second_tuple)
# print(res)

dic_mariah = {
    "first_name": "Mariah",
    "last_name": "Carey",
    "birth_date": "27.03.1970",
    "hobbies": ["Sing", "Compose", "Act"]
}


def main():
    number = input("insert a number between 1-7:", )
    if number == "1":
        print(dic_mariah["last_name"])
    elif number == "2":
        print(dic_mariah["birth_date"][3:5])
    elif number == "3":
        print(len(dic_mariah["hobbies"]))
    elif number == "4":
        print(dic_mariah["hobbies"][2])
    elif number == "5":
        dic_mariah["hobbies"] += ["Cooking"]
    elif number == "6":
        date = dic_mariah["birth_date"][0:2]
        month = dic_mariah["birth_date"][3:5]
        year = dic_mariah["birth_date"][6:]
        print(date, month, year)
    elif number == "7":
        dic_mariah["age"] = 37
        print(dic_mariah["age"])
    main()


# main()

magic_str = "abra cadabra"


def count_chars(my_str):
    my_str1 = my_str.replace(" ", "")
    dict_str = {}
    for i in my_str1:
        x = my_str1.count(i)
        my_str1.replace(i, "")
        dict_str[i] = x
    return dict_str


# res = count_chars(magic_str)
# print(res)

course_dict = {'I': 3, 'love': 3, 'self.py!': 2}


def inverse_dict(my_dict):
    inv_map = {}
    for k, v in my_dict.items():
        inv_map[v] = inv_map.get(v, []) + [k]
    return inv_map


# res = inverse_dict(course_dict)
# print(res)

list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless',
                 'salted', 'staled', 'greatening', 'lasted', 'resmelts']


def sub_lists(l):  # im not using that at the moment.
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists


def sort_anagrams(list_of_strings):
    list_anagrams = []
    s = 0
    for i in list_of_strings:
        for x in list_of_strings:
            if i == x:
                continue
            if sorted(i) == sorted(x):
                list_of_strings.remove(x)
                list_anagrams += [[x]]
        list_of_strings.remove(i)
        list_anagrams += [[i]]
    list_anagrams += list_of_strings
    return list_anagrams


res = sort_anagrams(list_of_words)
print(res)


# C:\Users\oksh\Desktop\All my favorite songs.txt
def file_word():
    file = input("put file name: ")
    set1 = set()
    action = input("choose an action from rev, last or sort:", )
    x = open(file, 'r')
    g = x.read()
    list_of_lines = x.readlines()
    g = g.lower()
    h = g.split(" ")
    set1 = set1.union(h)
    p = g.split("\n")
    if action == 'sort':
        return (sorted(set1))
    if action == 'rev':
        for line in p:
            print(line[::-1])
    if action == 'last':
        num = input("enter the number of last lines you want:")
        num = int(num)
        for i in range(num):
            print(p[-num])
            num += -1
    x.close()


res = file_word()
print(res)
# C:\Harry Potter Books.txt

COMMA = ", "
dates = ""
books_file = open("C:\Harry Potter Books.txt", 'r')
for row in books_file:
    date = row.split(COMMA)[1]
    dates += date
books_file.close()

dates_file = open(r"C:\Users\oksh\Desktop\Harry Potter dates.txt", 'w')
dates_file.write(dates)
dates_file.close()


def copy_file_content(source, destination):
    with open(source, 'r') as x:
        with open(destination, 'w') as y:
            x = x.read()
            y = y.write(x)


res = copy_file_content(r'C:\all my favorirte songs.txt', 'C:\years.txt')
print(res)


def who_is_missing(file_name):
    with open(file_name, 'r') as x:
        nums = x.read()
        list_nums = nums.split(',')
        for i in list_nums:
            i = int(i)
        new_list = sorted(list_nums)
        print(new_list)
        s = 1
        for i in new_list:
            if i == str(s):
                s += 1
            else:
                i = int(i) - 1
                y = open(r'C:\Users\oksh\Desktop\found.txt', 'w')
                y = y.write(str(i))
                return i
                y.close()


res = who_is_missing(r'C:\nums.txt')
print(res)

f = open(r"C:\Users\oksh\Desktop\What.txt", "r")
cd_data = f.read()
cd_split = cd_data.split("\n")
cd_i = []
for element in cd_split:
    cd_i.append(element.split(":"))
cd_dict = {}
for item in cd_i:
    cd_dict[item[0]] = item[1]
f.close()
print(cd_dict)


def my_mp3_playlist(file_path):
    f = open(file_path, "r")
    file = f.read()
    splited_file = file.split("\n" and ";")
    # print(splited_file)
    numbers = set()
    my_tuple = ()
    for i in splited_file:
        if ":" in i:
            new_i = i.replace(":", ".")
            num = float(new_i)
            numbers.add(num)
    x = max(numbers)
    y = str(x)
    x = y.replace(".", ":")
    for index, val in enumerate(splited_file):
        if x in val:
            song = (splited_file[index - 2])
            str_song = (str(song))
    number = file.count("\n")
    list_of = []
    list_of.append(str_song)
    list_of.append(number)
    for i in splited_file:
        num = splited_file.count(i)
        if num > 1:
            artist = i
    list_of.append(artist)
    my_tuple += tuple(list_of)
    return my_tuple
    f.close()


res = my_mp3_playlist(r"C:\all my favorirte songs.txt")
print(res)


def my_mp4_playlist(file_path, new_song):
    f = open(file_path, "r+")
    file = f.read()
    splitted_file = file.split("\n")
    list_of_songs = []
    for i in splitted_file:
        list_of_songs.append(i.split(";"))
    list_of_songs[2][0] = new_song
    list_file = []
    str_file = ""
    for i in list_of_songs:
        list_file += i
    for i in list_file:
        if i == '':
            list_file.remove(i)
    for i in range(len(list_file)):
        if i % 4 == 0:
            list_file.insert(i, ".")
    del list_file[0]
    list_file.insert(-3, ".")
    for i in list_file:
        if i == ".":
            str_file += "\n"
        if i != ".":
            str_file += i + ";"
    print(str_file)
    f.seek(0)
    f.write(str_file)
    f.truncate()
    new_file = f.read()
    print(new_file)
    f.close()


res = my_mp4_playlist(r"C:\all my favorirte songs.txt", "Python Love Story")
print(res)


def double_str(string):
    new_string = ""
    for i in string:
        new_string += i * 2
    return new_string


what = "hi man sup?"


# print(double_str(what))

def double_letter(str_thing):
    return list(map(double_str, "hi man sup?"))


print("".join(double_letter(what)))


def is_devided(num):
    if num % 4 == 0:
        return num


print(list(filter(is_devided, range(67))))

import functools

string = "267875536"

the_list = list(string)


def add(a, b):
    return int(a) + int(b)


def sum_of_digits(number):
    print(functools.reduce(add, the_list))


print(sum_of_digits(string))


def add(a):
    return str(a).join(" $")


list_of = ["12", "23", "1", "54", "5"]
print(','.join(list(map(add, list_of))))

money_list = [str(x) + "$" for x in range(10)]
print(', '.join(money_list))


def combine_coins(coin, numbers): return ', '.join(map(lambda s, n: s + str(n), [coin for i in numbers], numbers))


print(combine_coins("$", [2, 3, 4, 42, 12, 76]))


def intersection(list_1, list_2):
    return set([x for x in list_1 if x in list_2])


d = [1, 5, 9, 5, 6]
s = [5, 5, 6, 6, 7, 7]
print(intersection(d, s))


def is_prime(number):
    return all(number % i != 0 for i in range(2, number))


res = is_prime(2819)
print(res)


def is_funny(string):
    return all(char == 'h' or char == 'a' for char in string)


print(is_funny("hahahahahaha"))

alphabet = "abcdefghijklmnopqrstuvwxyz"


def caesar_decode(code, offset):
    return ["".join(chr(ord(i) + 2)) for i in password]


password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
print("".join(caesar_decode(password, -2)))

with open(r'C:\words.txt', 'r+') as file: f = file.read().split()
leng = 4
print(list(i for i in f if len(i) == leng))
print(max(n for n in f))
print(sum(len(i) for i in f))
f.sort(key=len)
print("".join(f[0] + "\n" + f[1]))
with open(r'C:\Users\oksh\Desktop\name_length.txt', 'w') as new:
    x = new.write("".join((str(i) + "\n" for i in (str(list(len(i) for i in f))).split())))


class pixel:

    def _init_(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        num = (self._red + self._green + self._blue) // 3
        self._red = num
        self._green = num
        self._blue = num

    def print_pixel_info(self):
        the_list = ["x: ", str(self._x), ", ", "y: ", str(self._y), ", ", "Color: ", str(self._red), ", ",
                    str(self._green), ", ", str(self._blue), " "]
        if self._red == 0 and self._green == 0 and self._blue >= 50:
            the_list += ["-Blue"]
        elif self._red == 0 and self._blue == 0 and self._green >= 50:
            the_list += ["-Green"]
        elif self._green == 0 and self._blue == 0 and self._red >= 50:
            the_list += ["-Red"]
        print("".join(the_list))


def main():
    my_pixel = pixel(5, 6, 70)
    my_pixel.print_pixel_info()
    my_pixel.set_grayscale()
    my_pixel.print_pixel_info()


main()


class BigThing:

    def _init_(self, size=0):
        self.size = size

    def _size(self):
        if type(self.size) is int:
            print(self.size)
        else:
            print(len(self.size))


class BigCat(BigThing):

    def _init_(self, size, name):
        BigThing._init_(self, size)
        self.name = name

    def _size(self):
        BigThing._size(self)
        if 15 < (self.size) < 20:
            print(self.name + " is Fat")
        elif self.size > 20:
            print(self.name + " is Very Fat")
        else:
            print(self.name + " is OK")


def main():
    my_thing = BigThing(345)
    my_thing._size()
    cutie = BigCat(15, "mitzy")
    cutie._size()


main()


class animal:
    zoo_name = "Hayaton"

    def _init_(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        print(self._name)

    def is_hungry(self):
        if self._hunger > 0:
            return True

    def feed(self):
        self._hunger -= 1
        if self._hunger == 0:
            # print("Your pet is not hungry anymore")
            pass

    def talk(self, sound):
        return sound

    def special_method(self):
        pass


class dog(animal):

    def _init_(self, name, hunger=0):
        super()._init_(name, hunger)

    def get_name(self):
        return (self._name)

    def talk(self, sound="woof woof"):
        super().talk(self)
        return (sound)

    def special_method(self):
        fetch_stick = "There you go, sir!"
        return fetch_stick


class cat(animal):

    def _init_(self, name, hunger=0):
        super()._init_(name, hunger)

    def get_name(self):
        return (self._name)

    def talk(self, sound="meow"):
        super().talk(self)
        return (sound)

    def special_method(self):
        chase_laser = "Meeeeow"
        return chase_laser


class skunk(animal):

    def _init_(self, name, hunger=0):
        super()._init_(name, hunger)

    def get_name(self):
        return (self._name)

    def talk(self, sound="tsssss"):
        super().talk(self)
        return (sound)

    def special_method(self):
        stink = "Dear lord!"
        return stink

    def _stink_count(self, stink_count=6):
        return stink_count


class unicorn(animal):

    def _init_(self, name, hunger=0):
        super()._init_(name, hunger)

    def get_name(self):
        return (self._name)

    def talk(self, sound="Good day, darling"):
        super().talk(self)
        return (sound)

    def special_method(self):
        sing = "I’m not your toy..."
        return sing


class dragon(animal):

    def _init_(self, name, hunger=0):
        super()._init_(name, hunger)

    def get_name(self):
        return (self._name)

    def talk(self, sound="Raaaawr"):
        super().talk(self)
        return (sound)

    def special_method(self):
        breath_fire = "$@#$#@$"
        return breath_fire

    def _color(self, color="Green"):
        return color


def main():
    zoo_lst = []
    brownie = dog("Brownie", 10)
    zelda = cat("Zelda", 3)
    stinky = skunk("Stinky", 0)
    kieth = unicorn("Kieth", 7)
    lizzy = dragon("Lizzy", 1450)
    doggo = dog("Doggo", 80)
    kitty = cat("Kitty", 80)
    stinky_jr = skunk("Stinky Jr.", 80)
    clair = unicorn("Clair", 80)
    mcfly = dragon("McFly", 80)
    zoo_lst += [brownie, zelda, stinky, kieth, lizzy, doggo, kitty, stinky_jr, clair, mcfly]
    for animal in zoo_lst:
        print(type(animal)._name_, animal.get_name())
        print(animal.talk())
        print(animal.special_method())
        if isinstance(animal, skunk):
            print(animal._stink_count())
        if isinstance(animal, dragon):
            print(animal._color())
        while animal.is_hungry():
            animal.feed()
        print(animal.zoo_name)


main()


def read_file(file_name):
    try:
        print("_CONTENT_START_")
        f = open(file_name, 'r')
        rf = f.read()
    except:
        print("_NO_SUCH_FILE_")
    else:
        print(rf)
    finally:
        print("_CONTENT_END_")
    f.close()


print(read_file("C:\words.txt"))


class UnderAge(BaseException):

    def _init_(self, name, age):
        self._name = name
        self._age = age
        self._num = 18 - self._age

    def _str_(self):
        return "Im sorry %s, you are only %s years old, you'll be invited again in %s years" % (
        self._name, self._age, self._num)

    def get_age(self):
        return self._age


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(name, age)
    except UnderAge as e:
        print(e)
        return "Function Expected an age over 18, and instead got %s." % age
    else:
        print("You should send an invite to " + name)


print(send_invitation("yuli", 17))

import string


class UsernameContainsIllegalCharacter(Exception):

    def _init_(self, usermane, character, index):
        self._username = usermane
        self._character = character
        self._index = index

    def _str_(self):
        return 'The username %s contains an illegal character, "%s" at index %s' % (
        self._username, self._character, self._index)


class UsernameTooShort(Exception):

    def _init_(self, usermane):
        self._username = usermane

    def _str_(self):
        return "The username %s is too short" % self._username


class UsernameTooLong(Exception):

    def _init_(self, usermane):
        self._username = usermane

    def _str_(self):
        return "The username %s is too long" % self._username


class PasswordTooShort(Exception):

    def _init_(self, password):
        self._password = password

    def _str_(self):
        return "The password %s is too short" % self._password


class PasswordTooLong(Exception):

    def _init_(self, password):
        self._password = password

    def _str_(self):
        return "The password %s is too long" % self._password


class PasswordMissingCharacter(Exception):

    def _init_(self, password):
        self._password = password

    def _str_(self):
        return "The password %s is missing a character" % self._password


class Upper(PasswordMissingCharacter):

    def _init_(self, password):
        self._password = password

    def _str_(self):
        return "The password %s is missing a character (Uppercase)" % self._password


class Lower(PasswordMissingCharacter):

    def _init_(self, password):
        self._password = password

    def _str_(self):
        return "The password %s is missing a character (Lowercase)" % self._password


class Digit(PasswordMissingCharacter):

    def _init_(self, password):
        self._password = password

    def _str_(self):
        return "The password %s is missing a character (Digit)" % self._password


class Special(PasswordMissingCharacter):

    def _init_(self, password):
        self._password = password

    def _str_(self):
        return "The password %s is missing a character (Special)" % self._password


def check_input(username, password):
    try:
        for i in range(len(username)):
            if username[i] in string.punctuation:
                if username[i] != "_":
                    raise UsernameContainsIllegalCharacter(username, username[i], i)
        if len(username) < 3:
            raise UsernameTooShort(username)
        elif len(username) > 16:
            raise UsernameTooLong(username)
        elif len(password) < 8:
            raise PasswordTooShort(password)
        elif len(password) > 40:
            raise PasswordTooLong(password)
        s = 0
        n = 0
        d = 0
        f = 0
        for i in password:
            if i.isupper():
                n += 1
            if i.islower():
                d += 1
            if i.isnumeric():
                f += 1
            if i in string.punctuation:
                s += 1
        if n < 1:
            raise Upper(password)
        if d < 1:
            raise Lower(password)
        if f < 1:
            raise Digit(password)
        if s < 1:
            raise Special(password)

    except UsernameContainsIllegalCharacter as e:
        print(e)
        return "the username should only include numbers, letters or underline"
    except UsernameTooShort as e1:
        print(e1)
        return "the username should be at least 3 characters"
    except UsernameTooLong as e2:
        print(e2)
        return "the username should be no longer than 16 characters"
    except PasswordTooShort as e4:
        print(e4)
        return "the password should be at least 8 characters"
    except PasswordTooLong as e5:
        print(e5)
        return "the password should be no longer than 40 characters"
    except Upper as e6:
        return e6
    except Lower as e7:
        return e7
    except Digit as e8:
        return e8
    except Special as e9:
        return e9
    else:
        return "OK"


print(check_input("A_1", "4BCD3F6h1jk*1mn0p"))


def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the',
             'lo siento': 'im sorry'}
    s_sentence = sentence.split()
    gen = (words[n] for n in s_sentence)
    return " ".join([next(gen) for i in range(len(s_sentence))])


print(translate("el gato esta en la casa"))


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(f):
    prime_generator = (n for n in range(f, f * 2) if is_prime(n))
    return next(prime_generator)


print(first_prime_over(999))


def parse_ranges(ranges_string):
    ranges = (r.split("-") for r in ranges_string.split(","))
    for start, stop in ranges:
        for num in range(int(start), int(stop) + 1):
            yield num


print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))


def parse_ranges(ranges_string):
    ranges = (r.split("-") for r in ranges_string.split(","))
    the_thing = (num for start, stop in ranges for num in range(int(start), int(stop) + 1))
    return the_thing


print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))


def get_fibo():
    x = 0
    y = 1
    n = x + y
    print(x)
    print(n)
    while y <= n:
        yield n
        x = y
        y = n
        n = x + y


fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))

I
CREATED
A
WATCH
AND
DATE
GENERATOR!

def gen_range(start, limit):
    while True:
        for i in range(start, limit):
            yield i


def gen_years():
    for i in range(2022, 10 ** 10):
        yield i


the_seconds = gen_range(0, 61)
the_minutes = gen_range(0, 61)
the_hours = gen_range(0, 25)
the_years = next(gen_years())
the_months = gen_range(1, 14)


def gen_time():
    while True:
        for e in the_hours:
            if e == 24:
                break
            for r in the_minutes:
                if r == 60:
                    break
                for t in the_seconds:
                    txt = f'{e:02}:{r:02}:{t:02}'
                    if t == 60:
                        break
                    yield txt


# for i in gen_time():
#     print(i)

def gen_days(month, year):
    leap_year = False
    if (year % 400 == 0) and (year % 100 == 0):
        leap_year = True
    elif (year % 4 == 0) and (year % 100 != 0):
        leap_year = True
    else:
        leap_year = False

    days = 0
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days = 31
    if month == 2:
        days = 28
        if leap_year is True:
            days = 29
    if month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
    yield days


def gen_date():
    while True:
        for x in gen_years():
            for z in the_months:
                if z == 13:
                    break
                num = gen_days(z, x)
                number = next(num)
                for y in range(1, number + 1):
                    if y == number + 1:
                        break
                    txt = f'{x:02}/{z:02}/{y:02}'
                    for e in the_hours:
                        if e == 24:
                            break
                        for r in the_minutes:
                            if r == 60:
                                break
                            for t in the_seconds:
                                txt1 = f'{e:02}:{r:02}:{t:02}'
                                if t == 60:
                                    break
                                yield txt, txt1


count = 0
for i in gen_date():
    count += 1
    if count == 1 or count % 1000001 == 0:
        print(i)
import winsound

freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }
notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

the_notes = notes.split("-")
print(the_notes)

split_notes = []
for i in the_notes:
    x = i.split(",")
    split_notes.append(x)
print(split_notes)
for key, val in freqs.items():
    for i in split_notes:
        if key == i[0]:
            i[0] = val
print(split_notes)
for i, x in split_notes:
    winsound.Beep(int(i), int(x))

import itertools as it

a = [1] * 5 + [5] * 2 + [10] * 5 + [20] * 3

b = {e for i in range(len(money) + 1) for e in it.combinations(money, i) if sum(e) == 100}
print(len(b))


class End(Exception):

    def _init_(self, end):
        self._end = end

    def _str_(self):
        return "no more freq, its the %s" % self._end


class MusicNotes:

    def _init_(self):
        self.notes = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self.index = -1
        self.s = 1

    def _iter_(self):
        return self

    def _next_(self):
        self.index += 1
        if self.index > 6:
            self.s *= 2
            self.index = 0
        if self.s > 17:
            raise End("end")
        if True:
            return (self.notes[self.index] * self.s)


notes_iter = iter(MusicNotes())
# print(next(notes_iter))
for freq in notes_iter:
    print(freq)


def check_id_valid(id_number):
    new_id = []
    s = 0
    str_id = str(id_number)
    for i in str_id:
        if s % 2 != 0:
            new_id.append(str((int(i)) * 2))
        else:
            new_id.append(i)
        s += 1
    n = 0
    for i in new_id:
        if len(i) > 1:
            n += int(i[0])
            n += int(i[1])
        else:
            n += int(i)
    if n % 10 == 0:
        return True
    return False


# id = 123456783
# he = check_id_valid(id)
# print("id {} is valid? {}".format(id, he))

class IDIterator:

    def _init_(self, id):
        self._id = (id + 1)
        self.w = 0

    def _iter_(self):
        return self

    def _next_(self):
        while True:
            if self.w > 9:
                raise StopIteration
            if check_id_valid(self._id) == True:
                self._id += 1
                self.w += 1
                return (self._id - 1)
            else:
                self._id += 1


# num = IDIterator(123456780)
# for i in num:
#     print(i)

def id_generator(number):
    id_g = (n for n in range((number + 1), 1000000000) if check_id_valid(n))
    for i in range(10):
        yield (next(id_g))


# gen = id_generator(123456780)
# for i in gen:
#     print(i)

def find_id(num, type):
    if type == "gen":
        gen = id_generator(num)
        for i in gen:
            print(i)
    else:
        itter = IDIterator(num)
        for i in itter:
            print(i)


find = find_id(123456780, "it")
print(find)

from tkinter import *
from PIL import ImageTk, Image
import webbrowser

win = Tk()
win.geometry("700x600")
win.title("Rounded Button")
lab = Label(win, text="tis is my \n LABEL", underline=12, anchor=N, font=('Helvetica', 14),
            fg='blue')


def my_command(e):
    webbrowser.open_new('https://www.youtube.com/watch?v=Epqri124PYk')


def my_new_command(e):
    webbrowser.open_new('https://www.youtube.com/watch?v=Awf45u6zrP0')


click_btn = ImageTk.PhotoImage(file=r'C:\Users\oksh\Desktop\Untitled1.png')
img_label = Label(image=click_btn)
but = Button(win, image=click_btn, command=lambda: my_command(1), borderwidth=3, compound=LEFT)
but.pack(side=BOTTOM)
but.pack(pady=0)
lab.pack(pady=0)
lab.bind("<Button-1>", my_new_command)
win.mainloop()