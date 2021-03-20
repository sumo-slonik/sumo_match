from personal_competitor import PersonalCompetitor


class ClubCompetotor:

    def __init__(self, firs_competitor, second_competitor, third_competitor, substitute, club_name,
                 is_free_fight=False):
        self.is_free_fight = is_free_fight
        self.club_name = club_name
        # this fields will be instance of PersonalCompetitor
        self.substitute = substitute
        self.third_competitor = third_competitor
        self.second_competitor = second_competitor
        self.firs_competitor = firs_competitor
        self.has_been_changed = False
        self.changes = {1: self.__change_first, 2: self.__change_second, 3: self.__change_third}

    def get_club_name(self):
        return self.club_name

    def get_firs_competitor(self):
        return self.firs_competitor

    def get_second_competitor(self):
        return self.second_competitor

    def get_third_competitor(self):
        return self.third_competitor

    def get_substitute(self):
        return self.substitute

    def __change_first(self):
        self.firs_competitor, self.substitute = self.substitute, self.firs_competitor

    def __change_second(self):
        self.second_competitor, self.substitute = self.substitute, self.second_competitor

    def __change_third(self):
        self.third_competitor, self.substitute = self.substitute, self.third_competitor

    def use_substitute(self, number_of_competitor_to_change):
        if not self.has_been_changed:
            self.has_been_changed = True
            self.changes[number_of_competitor_to_change]()
        else:
            print("Change has been already done")
