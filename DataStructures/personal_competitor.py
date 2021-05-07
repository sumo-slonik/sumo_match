class Category:
    def __init__(self, category, gender, age):
        self.category = category
        self.gender = gender
        self.age = age

    def get_category(self):
        return self.category

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def __str__(self):
        return self.gender + ' ' + self.age + ' ' + self.category

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if self.category != other.category:
            return False
        if self.age != other.age:
            return False
        if self.gender != other.gender:
            return False
        return True

    def __hash__(self):
        return hash(self.gender+self.age+self.category)



class PersonalCompetitor:
    def __init__(self, name="", club="", weight="", category="", birth_year=0, licence_no='', is_free_fight=False):
        self.name = name
        self.club = club
        self.weight = weight
        self.is_free_fight = is_free_fight
        self.category = [category]
        self.birth_year = birth_year
        self.licence_no = licence_no
        self.losses = 0
        self.wins = 0

    def get_name(self):
        return self.name

    def get_first_name(self):
        return self.name.split()[1]

    def get_surname(self):
        return self.name.split()[0]

    def get_weight(self):
        return self.weight

    def get_club(self):
        return self.club

    def get_licence_no(self):
        return self.licence_no

    def get_birth_year(self):
        return self.birth_year

    def get_wins(self):
        return self.wins

    def get_category(self):
        return self.category

    def win(self):
        self.wins += 1

    def lose(self):
        self.losses += 1

    def add_category(self, category):
        self.category.append(category)

    def custom_string_repr(self, show_first_name=True, show_surname_name=True, show_club=True, show_birth_year=True,
                           show_weight=True):
        result = ""
        if self.is_free_fight:
            return "WOLNY LOS"
        if show_first_name:
            result += self.get_first_name() + ' '
        if show_surname_name:
            result += self.get_surname() + ' '
        if show_club:
            result += self.get_club() + ' '
        if show_birth_year:
            result += str(self.get_birth_year()) + ' '
        if show_weight:
            result += str(self.get_weight()) + ' '
        return result

    def get_is_free_fight(self):
        return self.is_free_fight

    def __str__(self):
        return self.custom_string_repr(1, 1, 1, 0, 0)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if self.is_free_fight != other.is_free_fight:
            return False
        if self.name != other.name:
            return False
        if self.club != other.club:
            return False
        if self.weight != other.weight:
            return False
        if self.birth_year != other.birth_year:
            return False
        return True

    def __hash__(self):
        return hash(self.name + self.club + str(self.birth_year) + self.licence_no)
