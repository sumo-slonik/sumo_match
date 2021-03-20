class PersonalCompetitor:
    def __init__(self, name=None, club=None, weight=None, category=None, birth_year=None, is_free_fight=False):
        self.name = name
        self.club = club
        self.weight = weight
        self.is_free_fight = is_free_fight
        self.category = category
        self.birth_year = birth_year

    def get_name(self):
        return self.name

    def get_first_name(self):
        return self.name.split()[0]

    def get_surname(self):
        return self.name.split()[1]

    def get_weight(self):
        return self.weight

    def get_club(self):
        return self.club

    def get_birth_year(self):
        return self.birth_year

    def custom_string_repr(self, show_first_name=True, show_surname_name=True, show_club=True, show_birth_year=True,
                           show_weight=True):
        result = ""
        if show_first_name:
            result += self.get_first_name()
        if show_surname_name:
            result += self.get_surname()
        if show_club:
            result += self.get_club()
        if show_birth_year:
            result += self.get_birth_year()
        if show_weight:
            result += self.get_weight()
        return result

    def __str__(self):
        return self.custom_string_repr()
