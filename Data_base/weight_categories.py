import hashlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Data_base.tables import WeightCategory


def generate_id(weight_category, age_category, gender):
    description = weight_category + age_category + gender
    return int(hashlib.sha1(description.encode("utf-8")).hexdigest(), 16) % (10 ** 8)


class WeightCategoriesAdder:
    age_categories = ("Dziecko (u12)",
                      "Młodzik (u14)",
                      "Kadet (u16)",
                      "Junior (u18)",
                      "Młodzierzowiec (u21)",
                      "Młodzierzowiec (u23)",
                      "Senior ")
    woman_weight_categories = {
        age_categories[0]: [str(x) for x in range(30, 61, 5)] + ['+60','+ 60'],
        age_categories[1]: [str(x) for x in range(35, 66, 5)] + ['+65', '+ 65','+60','+ 60'],
        age_categories[2]: [str(x) for x in range(45, 71, 5)] + ['+65', '+ 65','+70', '+ 70', 'open'],
        age_categories[3]: [str(x) for x in range(50, 76, 5)] + ['+70', '+ 70', '+75', '+ 75', 'open'],
        age_categories[4]: [str(x) for x in range(50, 66, 5)] + ['73', '80', '+80', '+ 80', '95', '+95', '+ 95',
                                                                 'open'],
        age_categories[5]: [str(x) for x in range(50, 66, 5)] + ['73', '80', '+80', '+ 80', '95', '+95', '+ 95',
                                                                 'open'],
        age_categories[6]: [str(x) for x in range(50, 66, 5)] + ['73', '80', '+80', '+ 80', '95', '+95', '+ 95', 'open']
    }

    man_weight_categories = {
        age_categories[0]: [str(x) for x in range(35, 61, 5)] + ['+60', '+ 60'],
        age_categories[1]: [str(x) for x in range(40, 71, 5)] + ['+70', '+ 70','35'],
        age_categories[2]: [str(x) for x in range(55, 96, 10)] + ['50', '+95', '+ 95', 'open'],
        age_categories[3]: [str(x) for x in range(60, 101, 10)] + ['55', '+100', '+ 100', 'open'],
        age_categories[4]: ['70', '77', '85', '92', '100', '115', '+115', '+ 115', 'open'],
        age_categories[5]: ['70', '77', '85', '92', '100', '115', '+115', '+ 115', 'open'],
        age_categories[6]: ['70', '77', '85', '92', '100', '115', '+115', '+ 115', 'open']
    }
    weight_categories = [woman_weight_categories, man_weight_categories]

    def __init__(self, DATABSE_URI):
        self.db = create_engine(DATABSE_URI)
        self.cat_id = 0

    def add_categories(self):
        session_maker = sessionmaker(self.db)
        session = session_maker()
        # session.query(WeightCategory).delete()
        for count, gender in enumerate(['kobiety', 'mężczyźni']):
            for age_category in self.weight_categories[count]:
                for category in self.weight_categories[count][age_category]:
                    to_add = WeightCategory(category, age_category, generate_id(category, age_category, gender), gender)
                    session.merge(to_add)
        session.commit()


if __name__ == '__main__':
    DATABSE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='admin',
                                                                                        server='localhost',
                                                                                        database='sumo_match_maker')
    weight_category_adder = WeightCategoriesAdder(DATABSE_URI)
    weight_category_adder.add_categories()
