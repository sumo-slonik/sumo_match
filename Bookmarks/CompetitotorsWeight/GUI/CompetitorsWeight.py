from Bookmarks.CompetitotorsWeight.GUI.StyleSheets.CustomCalendar import CustomCalendarWidget
from Bookmarks.CompetitotorsWeight.GUI.main_window import Ui_MainWindow, QTableWidgetItem
from Bookmarks.CompetitotorsWeight.GUI.ui_competitiorsWeight import *
from Bookmarks.CompetitotorsWeight.GetingCompetitions import CompetitionsGetter
from Bookmarks.CompetitotorsWeight.GetingDeclaredCompetitors import DeclaredCompetitorsGetter, \
    ApplicationForCompetitorGetter
from Data_base.tables import Competitor, Match, CategoryAtCompetitions, Competition, WeightCategory


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.db_address = ('mysql+mysqlconnector://{user}:{password}@{server}/{database}', 'root', 'admin')
        self.ui = Ui_MainWindow()
        self.competitions_list = None
        self.competitors_list = None
        self.selected_competition = None
        self.ui.setupUi(self)
        self.gettingDeclaredCompetitors = DeclaredCompetitorsGetter(*self.db_address)
        self.gettingCompetitions = CompetitionsGetter(*self.db_address)
        self.applicationForCompetitorGetter = ApplicationForCompetitorGetter(*self.db_address)
        # self.showFullScreen()
        self.hide_profile_panel()
        self.connect_buttons_to_functions()
        self.change_calender_widget_to_custom()
        self.connect_widget_to_functions()
        self.show()

    def change_calender_widget_to_custom(self):
        self.ui.calendarWidget.setVisible(False)
        self.ui.verticalLayout_3.removeWidget(self.ui.calendarWidget)
        self.ui.calendarWidget = CustomCalendarWidget(self.ui.CompetitionPanel)
        self.ui.calendarWidget.setObjectName(u"calendarWidget")
        self.ui.verticalLayout_3.addWidget(self.ui.calendarWidget)

    def hide_profile_panel(self):
        self.ui.SingleCompetitorPanel.setVisible(False)

    def show_profile_panel(self):
        self.ui.SingleCompetitorPanel.setVisible(True)

    def connect_buttons_to_functions(self):
        self.ui.hideCompetitorPanelButton.clicked.connect(self.hide_profile_panel)

    def connect_widget_to_functions(self):
        self.ui.calendarWidget.clicked.connect(self.calendar_date_clicked)
        self.ui.CompetitonTable.clicked.connect(self.competition_clicked)
        self.ui.CompetitorsTable.clicked.connect(self.competitor_clicked)

    def show_competitions_in_date(self, date):
        table = self.ui.CompetitonTable
        competitions = self.gettingCompetitions.get_competitions(date)
        self.competitions_list = competitions
        table.setRowCount(len(competitions))
        competition: Competition
        for row, competition in enumerate(competitions):
            table.setItem(row, 0, QTableWidgetItem(competition.competition_name))
            table.setItem(row, 1, QTableWidgetItem(competition.city))

    def calendar_date_clicked(self):
        date = self.ui.calendarWidget.selectedDate()
        date = date.toPython()
        self.show_competitions_in_date(date)

    def competition_clicked(self):
        index = (self.ui.CompetitonTable.selectionModel().currentIndex())
        row = index.row()
        competition = self.competitions_list[row]
        self.selected_competition = competition
        self.show_competitors_declared_in_competition(competition)

    def show_competitors_declared_in_competition(self, competition):
        table = self.ui.CompetitorsTable
        competitors = self.gettingDeclaredCompetitors.get_declared_competitors(competition)
        self.competitors_list = competitors
        table.setRowCount(len(competitors))
        competition: Competition
        for row, competitor in enumerate(competitors):
            table.setItem(row, 0, QTableWidgetItem(competitor.name))
            table.setItem(row, 1, QTableWidgetItem(competitor.surname))
            table.setItem(row, 2, QTableWidgetItem(competitor.gender))
            table.setItem(row, 3, QTableWidgetItem(str(competitor.born_date)))
            table.setItem(row, 4, QTableWidgetItem(competitor.licence_no))

    def competitor_clicked(self):
        index = (self.ui.CompetitorsTable.selectionModel().currentIndex())
        row = index.row()
        competitor = self.competitors_list[row]
        self.show_competitor(competitor)

    def show_competitor(self, competitor):
        self.show_profile_panel()
        self.ui.CompetitorName.setText(competitor.name)
        self.ui.CompetitorSurname.setText(competitor.surname)
        self.ui.CompetitorBornDate.setText(str(competitor.born_date))
        self.ui.CompetitorClub.setText(str(competitor.club))
        self.ui.CompetitorLicenceNo.setText(str(competitor.licence_no))
        self.show_categories_for_competitor(competitor)
        categories = self.gettingDeclaredCompetitors.get_competitor_categories(competitor, self.selected_competition)
        for i in categories:
            print(i)

    def show_categories_for_competitor(self,competitor):
        categories = self.applicationForCompetitorGetter.get_categories_for_competitor(competitor)
        table = self.ui.competitorsCategoriesTable
        table.setRowCount(len(categories))
        category:WeightCategory
        for row, category in enumerate(categories):
            table.setItem(row, 0, QTableWidgetItem(category.age_category))
            table.setItem(row, 1, QTableWidgetItem(category.weight_category))

