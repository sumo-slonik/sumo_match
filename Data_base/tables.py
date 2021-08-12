from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Date, ForeignKey

Base = declarative_base()


class Club(Base):
    __tablename__ = 'clubs'
    club_name = Column(String)
    city = Column(String)
    foundation_date = Column(Date)
    club_id = Column(Integer, primary_key=True)
    province = Column(String)
    competitors = relationship("Competitor")

    def __init__(self, club_name, city, foundation_date, club_id, province):
        self.club_name = club_name
        self.city = city
        self.foundation_date = foundation_date
        self.club_id = club_id
        self.province = province

    def __str__(self) -> str:
        return self.club_name + ' ' + self.club_id


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
        return str(self.age_category) + ' ' + self.weight_category


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


class CategoryAtCompetitions(Base):
    __tablename__ = 'categories_at_competitions'
    category_id = Column(Integer, ForeignKey('weight_categories.category_id'))
    competition_id = Column(Integer, ForeignKey('competitions.competition_id'))
    category_at_competition_id = Column(Integer, primary_key=True)
    match = relationship("Match")

    def __init__(self, category_id, competition_id):
        self.category_id = category_id
        self.competition_id = competition_id


class Match(Base):
    __tablename__ = 'matches'
    first_competitor = Column(String, ForeignKey('competitors.licence_no', ))
    second_competitor = Column(String, ForeignKey('competitors.licence_no'))
    category_id = Column(Integer, ForeignKey('categories_at_competitions.category_at_competition_id'))
    match_id = Column(Integer, primary_key=True)
    winner = Column(String, ForeignKey('competitors.licence_no'))

    def __init__(self, first_competitor, second_competitor, category_id, winner,match_id):
        self.first_competitor = first_competitor
        self.second_competitor = second_competitor
        self.category_id = category_id
        self.winner = winner
        self.match_id = match_id
