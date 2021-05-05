import datetime
import inspect


class Settings:
    def __init__(self, window):
        self.window = window
        self.actual_year = datetime.datetime.now().year
        self.keys = ['child', 'u14', 'u16', 'u18', 'u21', 'u23', 'senior']
        self.methods = {x[0]: x[1] for x in inspect.getmembers(self, predicate=inspect.ismethod)}
        self.ages = {'child': [self.actual_year, self.actual_year], 'u14': [self.actual_year, self.actual_year],
                     'u16': [self.actual_year, self.actual_year], 'u18': [self.actual_year, self.actual_year],
                     'u21': [self.actual_year, self.actual_year], 'u23': [self.actual_year, self.actual_year],
                     'senior': [self.actual_year, self.actual_year]}
        self.window.ui.saveSettingsButton.clicked.connect(lambda: self.save_to_file())
        for i in range(1, 15):
            self.window.ui.__dict__['age_slider_' + str(i)].valueChanged.connect(self.methods['slider_' + str(i)])
            self.window.ui.__dict__['age_slider_' + str(i)].setMaximum(self.actual_year)
            self.window.ui.__dict__['age_slider_' + str(i)].setMinimum(self.actual_year - 60)

        self.red_from_file()
        self.set_and_print_sliders()

    def save_to_file(self):
        def age_repr(age):
            return str(age[0]) + ';' + str(age[1]) + '\n'

        with open('Settings/settings.txt', 'w') as file:
            for i in self.ages:
                file.write(i + ';' + age_repr(self.ages[i]))

    def red_from_file(self):
        with open('Settings/settings.txt', 'r') as file:
            for i in file:
                i = i.strip()
                i = i.split(';')
                self.ages[i[0]] = [int(i[1]), int(i[2])]

    def show_values(self):

        for i in range(7):
            self.window.ui.__dict__['age_textEdit_' + str(2 * i + 1)].setText(str(self.ages[self.keys[0]][0]))
            self.window.ui.__dict__['age_textEdit_' + str(2 * i + 2)].setText(str(self.ages[self.keys[0]][1]))

    def slider_1(self, value):
        self.window.ui.__dict__['age_textEdit_1'].setText(str(value))
        self.ages['child'][0] = value

    def slider_2(self, value):
        self.window.ui.__dict__['age_textEdit_2'].setText(str(value))
        self.ages['child'][1] = value

    def slider_3(self, value):
        self.window.ui.__dict__['age_textEdit_3'].setText(str(value))
        self.ages['u14'][0] = value

    def slider_4(self, value):
        self.window.ui.__dict__['age_textEdit_4'].setText(str(value))
        self.ages['u14'][1] = value

    def slider_5(self, value):
        self.window.ui.__dict__['age_textEdit_5'].setText(str(value))
        self.ages['u16'][0] = value

    def slider_6(self, value):
        self.window.ui.__dict__['age_textEdit_6'].setText(str(value))
        self.ages['u16'][1] = value

    def slider_7(self, value):
        self.window.ui.__dict__['age_textEdit_7'].setText(str(value))
        self.ages['u18'][0] = value

    def slider_8(self, value):
        self.window.ui.__dict__['age_textEdit_8'].setText(str(value))
        self.ages['u18'][1] = value

    def slider_9(self, value):
        self.window.ui.__dict__['age_textEdit_9'].setText(str(value))
        self.ages['u21'][0] = value

    def slider_10(self, value):
        self.window.ui.__dict__['age_textEdit_10'].setText(str(value))
        self.ages['u21'][1] = value

    def slider_11(self, value):
        self.window.ui.__dict__['age_textEdit_11'].setText(str(value))
        self.ages['u23'][0] = value

    def slider_12(self, value):
        self.window.ui.__dict__['age_textEdit_12'].setText(str(value))
        self.ages['u23'][1] = value

    def slider_13(self, value):
        self.window.ui.__dict__['age_textEdit_13'].setText(str(value))
        self.ages['senior'][0] = value

    def slider_14(self, value):
        self.window.ui.__dict__['age_textEdit_14'].setText(str(value))
        self.ages['senior'][0] = value

    def set_and_print_sliders(self):
        self.show_values()
        for i in range(7):
            self.window.ui.__dict__['age_slider_' + str(2 * i + 1)].setValue(self.ages[self.keys[i]][0])
            self.window.ui.__dict__['age_slider_' + str(2 * i + 2)].setValue(self.ages[self.keys[i]][1])

if __name__ == '__main__':
    settings = Settings(None)
    settings.red_from_file()
    settings.save_to_file()
    print()
