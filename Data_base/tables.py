import hashlib

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Date, ForeignKey

Base = declarative_base()


def generate_hash(*description):
    res = ''
    for i in description:
        res += str(i)
    return int(hashlib.sha1(res.encode("utf-8")).hexdigest(), 16) % (10 ** 8)


class Club(Base):
    __tablename__ = 'clubs'
    club_name = Column(String)
    city = Column(String)
    foundation_date = Column(Date)
    club_id = Column(Integer, primary_key=True)
    province = Column(String)
    competitors = relationship("Competitor")
    licences = relationship("ClubsLicences")

    def __init__(self, club_name, city, foundation_date, club_id, province):
        self.club_name = club_name
        self.city = city
        self.foundation_date = foundation_date
        self.club_id = club_id
        self.province = province

    def __str__(self) -> str:
        return self.club_name + ' ' + self.city

    def __hash__(self):
        return generate_hash(self.club_name, self.club_id)

    def __eq__(self, other):
        if isinstance(other, Club):
            return self.__hash__() == other.__hash__()
        else:
            return False


class Competitor(Base):
    __tablename__ = 'competitors'
    name = Column(String)
    surname = Column(String)
    club = Column(Integer, ForeignKey('clubs.club_id'))
    licence_no = Column(String, primary_key=True)
    born_date = Column(Date)
    gender = Column(String)

    first_competitor_match = relationship('Match', foreign_keys='Match.first_competitor', lazy='dynamic')
    second_competitor_match = relationship('Match', foreign_keys='Match.second_competitor', lazy='dynamic')
    winner_match = relationship('Match', foreign_keys='Match.winner', lazy='dynamic')
    competitor = relationship('ApplicationsForCompetitions', foreign_keys='ApplicationsForCompetitions.competitor',
                              lazy='dynamic')

    def __init__(self, name, surname, club, licence_no, born_date, gender):
        self.name = name
        self.surname = surname
        self.club = club
        self.licence_no = licence_no
        self.born_date = born_date
        self.gender = gender

    def __str__(self) -> str:
        return self.name + ' ' + self.surname + ' ' + str(self.club) + ' ' + str(self.licence_no) + ' ' + str(
            self.born_date) + ' ' + \
               self.gender

    def __hash__(self):
        return generate_hash(self.club, self.licence_no, self.name, self.surname, self.gender, self.born_date)

    def __eq__(self, other):
        if not isinstance(other, Competitor):
            return False
        if self.club != other.club:
            return False
        if self.licence_no != other.licence_no:
            return False
        if self.name != other.name:
            return False
        if self.surname != other.surname:
            return False
        if self.gender != other.gender:
            return False
        if self.born_date != other.born_date:
            return False
        return True


class AgeCategory(Base):
    __tablename__ = 'age_categories'
    category = Column(String, primary_key=True)
    min_year = Column(Integer)
    max_year = Column(Integer)
    weight_cat = relationship("WeightCategory")

    def __init__(self, category, min_year, max_year):
        self.category = category
        self.min_year = min_year
        self.max_year = max_year

    def __str__(self):
        return self.category + ' ' + str(self.min_year) + '-' + str(self.max_year)


class WeightCategory(Base):
    __tablename__ = 'weight_categories'
    weight_category = Column(String)
    age_category = Column(String, ForeignKey('age_categories.category'))
    category_id = Column(Integer, primary_key=True)
    gender = Column(String)
    match = relationship("CategoryAtCompetitions")

    def __init__(self, weight_category, age_category, category_id, gender):
        self.weight_category = weight_category
        self.age_category = age_category
        self.category_id = category_id
        self.gender = gender

    def __str__(self):
        return str(self.age_category) + ' ' + self.weight_category + ' ' + self.gender

    def __hash__(self):
        return generate_hash(self.__str__().split(' '))

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __lt__(self, other):
        first = first = self.weight_category
        second = other.weight_category
        first = first.split('(')[0]
        second = second.split('(')[0]
        if 'open' in second:
            return True
        if 'open' in first:
            return False
        elif '+' in second:
            if '+' in first:
                first = first.replace('+', '')
                second = second.replace('+', '')
                return int(first) < int(second)
            return True
        else:
            return int(first) < int(second)


class CompetitionType(Base):
    __tablename__ = 'competition_types'
    competition_type = Column(String, primary_key=True)
    competition = relationship("Competition")

    def __init__(self, competition_type):
        self.competition_type = competition_type


class Competition(Base):
    __tablename__ = 'competitions'
    competition_name = Column(String)
    city = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    competition_type = Column(String, ForeignKey('competition_types.competition_type'))
    competition_id = Column(Integer, primary_key=True)
    competition = relationship("CategoryAtCompetitions")

    def __init__(self, competition_name, city, start_date, end_date, competition_type, competition_id):
        self.competition_name = competition_name
        self.city = city
        self.start_date = start_date
        self.end_date = end_date
        self.competition_type = competition_type
        self.competition_id = competition_id

    def __str__(self):
        return self.city + ' ' + self.start_date + ' ' + self.end_date

    def __hash__(self):
        return generate_hash(self.__str__())

    def __eq__(self, other):
        if not isinstance(other, Competition):
            return False
        return self.__str__() == other.__str__()


class CategoryAtCompetitions(Base):
    __tablename__ = 'categories_at_competitions'
    category_id = Column(Integer, ForeignKey('weight_categories.category_id'))
    competition_id = Column(Integer, ForeignKey('competitions.competition_id'))
    category_at_competition_id = Column(Integer, primary_key=True)
    match = relationship("Match")
    application = relationship("ApplicationsForCompetitions")

    def __init__(self, category_id, competition_id, category_at_competition_id):
        self.category_id = category_id
        self.competition_id = competition_id
        self.category_at_competition_id = category_at_competition_id


class Match(Base):
    __tablename__ = 'matches'
    first_competitor = Column(String, ForeignKey('competitors.licence_no', ))
    second_competitor = Column(String, ForeignKey('competitors.licence_no'))
    category_id = Column(Integer, ForeignKey('categories_at_competitions.category_at_competition_id'))
    match_id = Column(Integer, primary_key=True)
    winner = Column(String, ForeignKey('competitors.licence_no'))
    description = Column(String)

    def __init__(self, first_competitor, second_competitor, category_id, winner, match_id, description):
        self.first_competitor = first_competitor
        self.second_competitor = second_competitor
        self.category_id = category_id
        self.winner = winner
        self.match_id = match_id
        self.description = description


class ApplicationsForCompetitions(Base):
    __tablename__ = 'applications_for_competitions'

    def __init__(self, competitor, category_at_competition, application_id):
        self.competitor = competitor
        self.category_at_competition = category_at_competition
        self.application_id = application_id

    competitor = Column(String, ForeignKey('competitors.licence_no', ))
    category_at_competition = Column(Integer, ForeignKey('categories_at_competitions.category_at_competition_id'))
    application_id = Column(Integer, primary_key=True)


class ClubsLicences(Base):
    __tablename__ = 'club_licences'

    def __init__(self, competitor, date):
        self.club = competitor
        self.date = date

    def __eq__(self, other):
        return self.club == other.club

    def __hash__(self):
        return self.club

    club = Column(Integer, ForeignKey('clubs.club_id'), primary_key=True)
    date = Column(Date)
