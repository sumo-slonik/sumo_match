import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Data_base.tables import AgeCategory


class AgeCategoriesUpdater:
    age_categories = (("Dziecko (u12)", 0, 12),
                      ("Młodzik (u14)", 12, 14),
                      ("Kadet (u16)", 12, 16),
                      ("Junior (u18)", 16, 18),
                      ("Młodzierzowiec (u21)", 16, 21),
                      ("Młodzierzowiec (u23)", 16, 23),
                      ("Senior ", 17, 100))

    def __init__(self, DATABSE_URI):
        self.actual_year = datetime.datetime.now().year
        self.db = create_engine(DATABSE_URI)

    def add_categories(self):
        session_maker = sessionmaker(self.db)
        session = session_maker()
        session.query(AgeCategory).delete()
        for category in self.age_categories:
            new_category = AgeCategory(category[0], self.actual_year - category[1], self.actual_year - category[2])
            print(new_category)
            session.add(new_category)
        session.commit()


if __name__ == '__main__':
    DATABSE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='admin',
                                                                                        server='localhost',
                                                                                        database='sumo_match_maker')
    age_categories_updater = AgeCategoriesUpdater(DATABSE_URI)
    age_categories_updater.add_categories()
