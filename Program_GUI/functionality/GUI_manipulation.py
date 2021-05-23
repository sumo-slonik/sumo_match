from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from DataStructures.personal_competitor import *
from Matches.types_of_matches import TypeOFMatch



def load_competitors_to_nodes(nodes_names, competitors_list, main_window, copy_nodes=[]):
    is_personal = isinstance(competitors_list[0], PersonalCompetitor)
    for node, competitor in zip(nodes_names, competitors_list):
        main_window.ui.__dict__[node].clear()
        main_window.ui.__dict__[node].setAlignment(Qt.AlignCenter)
        if is_personal:
            main_window.ui.__dict__[node].append(competitor.get_name())
            main_window.ui.__dict__[node].append(competitor.get_club())
        else:
            main_window.ui.__dict__[node].append(competitor.get_club_name())
        main_window.ui.__dict__[node].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";text-align: center;")
    for node in copy_nodes:
        tmp = main_window.ui.__dict__[node[:-4]].toPlainText()
        main_window.ui.__dict__[node].setPlainText(tmp)


def load_values_to_nodes(nodes_names, values, main_window):
    for node, value in zip(nodes_names, values):
        main_window.ui.__dict__[node].clear()
        main_window.ui.__dict__[node].setAlignment(Qt.AlignCenter)
        main_window.ui.__dict__[node].append(str(value))
        main_window.ui.__dict__[node].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";text-align: center;")


def print_eliminations_16(eliminations, main_window):
    def node_name(node_number):
        return "el_16_node_" + str(node_number)

    # print competitor in nodes
    node_names = [node_name(x) for x in range(1, 32)]
    cpy_nodes = [node_name(x) + "_cpy" for x in range(2, 8)]
    competitors = [x.get_competitor() for x in eliminations.tree[1:]]
    load_competitors_to_nodes(node_names, competitors, main_window, cpy_nodes)
    # print("xd  ", eliminations.tree[1].get_competitor())
    # change border color for actual node
    actual_match_id = eliminations.get_actual_match_id()
    main_window.ui.__dict__[node_name(actual_match_id)].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";"
                                                                      "text-align: center;"
                                                                      "border: 4px solid yellow;"
                                                                      )
    actual_node = eliminations.get_actual_node()
    left_child = actual_node.get_left_child()
    right_child = actual_node.get_right_child()
    left_node_name = node_name(actual_match_id * 2)
    right_node_name = node_name(actual_match_id * 2 + 1)
    if actual_node.get_competitor() == left_child.get_competitor():
        main_window.ui.__dict__[left_node_name].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";"
                                                              "text-align: center;"
                                                              "border: 3px solid Lime;"
                                                              )
        main_window.ui.__dict__[right_node_name].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";"
                                                               "text-align: center;"
                                                               "border: 3px solid red;"
                                                               )
    elif actual_node.get_competitor() == right_child.get_competitor():
        main_window.ui.__dict__[right_node_name].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";"
                                                               "text-align: center;"
                                                               "border: 3px solid Lime;"
                                                               )
        main_window.ui.__dict__[left_node_name].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";"
                                                              "text-align: center;"
                                                              "border: 3px solid red;"
                                                              )
    else:
        main_window.ui.__dict__[right_node_name].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";"
                                                               "text-align: center;"
                                                               "border: 3px solid yellow;"
                                                               )
        main_window.ui.__dict__[left_node_name].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";"
                                                              "text-align: center;"
                                                              "border: 3px solid yellow;"
                                                              )


def print_repechage_16(repechage, main_window):
    def node_name(node_number):
        return "rep_16_node_" + str(node_number)

    # print competitor in nodes
    node_names = [node_name(x) for x in range(2, 16)]
    # cpy_nodes = [node_name(x) + "_cpy" for x in range(2, 8)]
    cpy_nodes = []
    competitors = [x.get_competitor() for x in repechage.tree[2:]]
    load_competitors_to_nodes(node_names, competitors, main_window, cpy_nodes)
    # print("xd  ", eliminations.tree[1].get_competitor())
    # change border color for actual node
    actual_match_id = repechage.get_actual_match_id()
    main_window.ui.__dict__[node_name(actual_match_id)].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";"
                                                                      "text-align: center;"
                                                                      "border: 4px solid yellow;"
                                                                      )
    actual_node = repechage.get_actual_node()
    left_child = actual_node.get_left_child()
    right_child = actual_node.get_right_child()
    left_node_name = node_name(actual_match_id * 2)
    right_node_name = node_name(actual_match_id * 2 + 1)
    if actual_node.get_competitor() == left_child.get_competitor():
        main_window.ui.__dict__[left_node_name].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";"
                                                              "text-align: center;"
                                                              "border: 3px solid Lime;"
                                                              )
        main_window.ui.__dict__[right_node_name].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";"
                                                               "text-align: center;"
                                                               "border: 3px solid red;"
                                                               )
    elif actual_node.get_competitor() == right_child.get_competitor():
        main_window.ui.__dict__[right_node_name].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";"
                                                               "text-align: center;"
                                                               "border: 3px solid Lime;"
                                                               )
        main_window.ui.__dict__[left_node_name].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";"
                                                              "text-align: center;"
                                                              "border: 3px solid red;"
                                                              )
    else:
        main_window.ui.__dict__[right_node_name].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";"
                                                               "text-align: center;"
                                                               "border: 3px solid yellow;"
                                                               )
        main_window.ui.__dict__[left_node_name].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";"
                                                              "text-align: center;"
                                                              "border: 3px solid yellow;"
                                                              )


def print_bronze_medals(bronze_fights, main_window):
    # first bronze match
    main_window.ui.__dict__["rep_16_node_2_cpy"].clear()
    main_window.ui.__dict__["rep_16_node_2_cpy"].setAlignment(Qt.AlignCenter)
    main_window.ui.__dict__["rep_16_node_2_cpy"].append(bronze_fights[0].get_left_child().get_name())
    main_window.ui.__dict__["rep_16_node_2_cpy"].append(bronze_fights[0].get_left_child().get_club())
    main_window.ui.__dict__["rep_16_node_2_cpy"].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";text-align: center;")
    main_window.ui.__dict__["firstBronzeFinalist_16_node"].clear()
    main_window.ui.__dict__["firstBronzeFinalist_16_node"].setAlignment(Qt.AlignCenter)
    main_window.ui.__dict__["firstBronzeFinalist_16_node"].append(bronze_fights[0].get_right_child().get_name())
    main_window.ui.__dict__["firstBronzeFinalist_16_node"].append(bronze_fights[0].get_right_child().get_club())
    main_window.ui.__dict__["firstBronzeFinalist_16_node"].setStyleSheet(
        "font: 75 10pt \"MS Shell Dlg 2\";text-align: center;")
    main_window.ui.__dict__["textEdit_4"].clear()
    main_window.ui.__dict__["textEdit_4"].setAlignment(Qt.AlignCenter)
    main_window.ui.__dict__["textEdit_4"].append(bronze_fights[0].get_competitor().get_name())
    main_window.ui.__dict__["textEdit_4"].append(bronze_fights[0].get_competitor().get_club())
    main_window.ui.__dict__["textEdit_4"].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";text-align: center;")

    # second bronze match
    main_window.ui.__dict__["rep_16_node_3_cpy"].clear()
    main_window.ui.__dict__["rep_16_node_3_cpy"].setAlignment(Qt.AlignCenter)
    main_window.ui.__dict__["rep_16_node_3_cpy"].append(bronze_fights[1].get_left_child().get_name())
    main_window.ui.__dict__["rep_16_node_3_cpy"].append(bronze_fights[1].get_left_child().get_club())
    main_window.ui.__dict__["rep_16_node_3_cpy"].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";text-align: center;")
    main_window.ui.__dict__["secondBronzeFinalist_16_node"].clear()
    main_window.ui.__dict__["secondBronzeFinalist_16_node"].setAlignment(Qt.AlignCenter)
    main_window.ui.__dict__["secondBronzeFinalist_16_node"].append(bronze_fights[1].get_right_child().get_name())
    main_window.ui.__dict__["secondBronzeFinalist_16_node"].append(bronze_fights[1].get_right_child().get_club())
    main_window.ui.__dict__["secondBronzeFinalist_16_node"].setStyleSheet(
        "font: 75 10pt \"MS Shell Dlg 2\";text-align: center;")
    main_window.ui.__dict__["textEdit_5"].clear()
    main_window.ui.__dict__["textEdit_5"].setAlignment(Qt.AlignCenter)
    main_window.ui.__dict__["textEdit_5"].append(bronze_fights[1].get_competitor().get_name())
    main_window.ui.__dict__["textEdit_5"].append(bronze_fights[1].get_competitor().get_club())
    main_window.ui.__dict__["textEdit_5"].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";text-align: center;")


def print_match_under_16(match_under_16, main_window):
    # if match_under_16.get_actual_match_id() <= 15 or match_under_16.get_actual_match_id() > 22:
    print_eliminations_16(match_under_16.get_eliminations(), main_window)
    if match_under_16.get_actual_match_id() >= 15:
        print_repechage_16(match_under_16.get_repechage(), main_window)
    if match_under_16.get_actual_match_id() > 20:
        print_bronze_medals(match_under_16.bronzeFights, main_window)
    elements = ["Eliminations_button", "HalfFinal_button", "Repechage_button", "Final_button"]
    # eliminations matches (with half finals) [1,14], repechages [15,20], finals (with bronzes) [21,22,23]
    id = match_under_16.get_actual_match_id()
    colors = []
    if 1 <= id <= 12:
        colors = ["Lime", "Black", "Black", "Black"]
        main_window.ui.match_16.setCurrentWidget(main_window.ui.Eliminations)
    if 13 <= id <= 14:
        colors = ["Black", "Lime", "Black", "Black"]
        main_window.ui.match_16.setCurrentWidget(main_window.ui.HalfFinals)
    if 15 <= id <= 20:
        colors = ["Black", "Black", "Lime", "Black"]
        main_window.ui.match_16.setCurrentWidget(main_window.ui.Repechage)
    if 21 <= id <= 23:
        colors = ["Black", "Black", "Black", "Lime"]
        main_window.ui.match_16.setCurrentWidget(main_window.ui.Finals)
    color_borders(elements, colors, main_window)


def clearNodes(nodes, main_window):
    for i in nodes:
        main_window.ui.__dict__[i].setStyleSheet("")


def colorNodeBorder(node_number, main_window):
    main_window.ui.__dict__["el_16_node_" + str(node_number)].setStyleSheet("border: 2px solid red;")


def color_borders(elements, colors, main_window):
    for color, element in zip(colors, elements):
        main_window.ui.__dict__[element].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";"
                                                       "text-align: center;"
                                                       "border: 3px solid " + color + ";"
                                                       )


# ////////////////////////////////////////////////////////////////////////////
# TO DO : uogulnić poniższe funkcje bo robią w zasadzie to samo
# ////////////////////////////////////////////////////////////////////////////

def print_match_under_5_points(match_under_5, main_window, name="un_5_point_node_"):
    points = match_under_5.get_results()
    competitors = match_under_5.get_competitors()
    values = [points[x] for x in competitors]
    node_names = [name + str(x) for x in range(1, 6)]
    load_values_to_nodes(node_names, values, main_window)


def print_actual_match_under_5(match_under_5, main_window, name='un_5_competitor_node_'):
    actual_match_id = match_under_5.get_actual_match_id()
    all_nodes = [name + str(x) for x in range(1, 26)]
    colors_for_all = ['black'] * 25
    colors_for_actual = ['yellow'] * 2
    node_1 = name + str(match_under_5.get_actual_match_id() * 2 + 6)
    node_2 = name + str(match_under_5.get_actual_match_id() * 2 + 7)

    color_borders(all_nodes, colors_for_all, main_window)
    color_borders([node_1, node_2], colors_for_actual, main_window)


def print_match_under_5(match_under_5, main_window, name="un_5_competitor_node_", points_name='un_5_point_node_'):
    node_names = [name + str(x) for x in range(1, 26)]
    competitors_list = match_under_5.get_competitors()
    matches_nodes = dict()
    for match in match_under_5.matches:
        competitors_list.append(match.get_left_child())
        competitors_list.append(match.get_right_child())
    load_competitors_to_nodes(node_names, competitors_list, main_window)
    print_match_under_5_points(match_under_5, main_window, points_name)
    print_actual_match_under_5(match_under_5, main_window, name)


def print_match_under_4_points(match_under_4, main_window, name="un_4_point_node_"):
    points = match_under_4.get_results()
    competitors = match_under_4.get_competitors()
    values = [points[x] for x in competitors]
    node_names = [name + str(x) for x in range(1, 5)]
    load_values_to_nodes(node_names, values, main_window)


def print_actual_match_under_4(match_under_4, main_window, name="un_4_competitor_node_"):
    actual_match_id = match_under_4.get_actual_match_id()
    all_nodes = [name + str(x) for x in range(1, 17)]
    colors_for_all = ['black'] * 17
    colors_for_actual = ['yellow'] * 2
    node_1 = name + str(match_under_4.get_actual_match_id() * 2 + 5)
    node_2 = name + str(match_under_4.get_actual_match_id() * 2 + 6)

    color_borders(all_nodes, colors_for_all, main_window)
    color_borders([node_1, node_2], colors_for_actual, main_window)


def print_match_under_4(match_under_4, main_window, name="un_4_competitor_node_", points_name='un_4_point_node_'):
    node_names = [name + str(x) for x in range(1, 17)]
    competitors_list = match_under_4.get_competitors()
    matches_nodes = dict()
    for match in match_under_4.matches:
        competitors_list.append(match.get_left_child())
        competitors_list.append(match.get_right_child())
    load_competitors_to_nodes(node_names, competitors_list, main_window)
    print_match_under_4_points(match_under_4, main_window, points_name)
    print_actual_match_under_4(match_under_4, main_window, name)


def print_match_under_3_points(match_under_3, main_window, name="un_3_point_node_"):
    points = match_under_3.get_results()
    competitors = match_under_3.get_competitors()
    values = [points[x] for x in competitors]
    node_names = [name + str(x) for x in range(1, 4)]
    load_values_to_nodes(node_names, values, main_window)


def print_actual_match_under_3(match_under_3, main_window, name="un_3_competitor_node_"):
    actual_match_id = match_under_3.get_actual_match_id()
    all_nodes = [name + str(x) for x in range(1, 10)]
    colors_for_all = ['black'] * 9
    colors_for_actual = ['yellow'] * 2
    node_1 = name + str(match_under_3.get_actual_match_id() * 2 + 4)
    node_2 = name + str(match_under_3.get_actual_match_id() * 2 + 5)

    color_borders(all_nodes, colors_for_all, main_window)
    color_borders([node_1, node_2], colors_for_actual, main_window)


def print_match_under_3(match_under_3, main_window, name="un_3_competitor_node_", points_name="un_3_point_node_"):
    node_names = [name + str(x) for x in range(1, 10)]
    competitors_list = match_under_3.get_competitors()
    matches_nodes = dict()
    for match in match_under_3.matches:
        competitors_list.append(match.get_left_child())
        competitors_list.append(match.get_right_child())
    load_competitors_to_nodes(node_names, competitors_list, main_window)
    print_match_under_3_points(match_under_3, main_window, points_name)
    print_actual_match_under_3(match_under_3, main_window, name)


def print_match_under_5_wrapper(match_under_5_wrapper, main_window,
                                names=("un_5_competitor_node_", 'un_5_point_node_', "un_4_competitor_node_",
                                       'un_4_point_node_', "un_3_competitor_node_", "un_3_point_node_"), scenes=5,
                                group=None):
    if match_under_5_wrapper.actual_state == 5:
        if scenes == 5:
            main_window.ui.match_5.setCurrentWidget(main_window.ui.under_5)
        if scenes == 10:
            if group == 1:
                main_window.ui.Grup_I_Under10_G1.setCurrentWidget(main_window.ui.under_5_g1)
            if group == 2:
                main_window.ui.Grup_II_Under10_G2.setCurrentWidget(main_window.ui.under_5_g2)
        print_match_under_5(match_under_5_wrapper.engine, main_window, names[0], names[1])
    if match_under_5_wrapper.actual_state == 4:
        if scenes == 5:
            main_window.ui.match_5.setCurrentWidget(main_window.ui.under_4)
        if scenes == 10:
            if group == 1:
                main_window.ui.Grup_I_Under10_G1.setCurrentWidget(main_window.ui.under_4_g1)
            if group == 2:
                main_window.ui.Grup_II_Under10_G2.setCurrentWidget(main_window.ui.under_4_g2)
        print_match_under_4(match_under_5_wrapper.engine, main_window, names[2], names[3])
    if match_under_5_wrapper.actual_state == 3:
        if scenes == 5:
            main_window.ui.match_5.setCurrentWidget(main_window.ui.under_3)
        if scenes == 10:
            if group == 1:
                main_window.ui.Grup_I_Under10_G1.setCurrentWidget(main_window.ui.under_3_g1)
            if group == 2:
                main_window.ui.Grup_II_Under10_G2.setCurrentWidget(main_window.ui.under_3_g2)
        print_match_under_3(match_under_5_wrapper.engine, main_window, names[4], names[5])


def print_actual_competitors(competitor1, competitor2, window):
    def competitor_to_description(competitor):
        result = ''
        result += 'Imię:'
        result += competitor.get_first_name()
        result += '\n'
        result += 'Nazwisko:'
        result += competitor.get_surname()
        result += '\n'
        result += 'Klub:'
        result += competitor.get_club()
        result += '\n'
        result += 'Waga:'
        result += competitor.get_weight()
        result += '\n'
        result += 'Wygrane:'
        result += str(competitor.get_wins())
        result += '\n'
        return result

    def club_to_description(competitor):
        result = ''
        result += 'Nazwa:'
        result += competitor.get_club_name()
        result += '\n'
        result += 'I:'
        result += str(competitor.get_first_competitor().name)
        result += '\n'
        result += 'II:'
        result += str(competitor.get_second_competitor().name)
        result += '\n'
        result += 'III:'
        result += str(competitor.get_third_competitor().name)
        result += '\n'
        result += 'IV:'
        result += str(competitor.get_substitute().name)
        result += '\n'
        return result
    if isinstance(competitor1,PersonalCompetitor):
        window.ui.Competitor_1.setPlainText(competitor_to_description(competitor1))
        window.ui.Competitor_2.setPlainText(competitor_to_description(competitor2))
    else:
        window.ui.Competitor_1.setPlainText(club_to_description(competitor1))
        window.ui.Competitor_2.setPlainText(club_to_description(competitor2))


def print_match_under_10(match_under_10, main_window):
    state = match_under_10.state
    main_window.ui.AllMatchesWraper.setCurrentWidget(main_window.ui.MatchUnder10)
    if state in [0,1]:
        names = ('un_10_5_grup_1_competitor_node_', 'un_10_5_grup_1_point_node_', 'un_10_4_grup_1_competitor_node_',
                 'un_10_4_grup_1_point_node_', 'un_10_3_grup_1_competitor_node_', 'un_10_3_grup_1_point_node_')
        print_match_under_5_wrapper(match_under_10.first_group, main_window, names, 10, 1)
    if state == 1:
        names = ('un_10_5_grup_2_competitor_node_', 'un_10_5_grup_2_point_node_', 'un_10_4_grup_2_competitor_node_',
                 'un_10_4_grup_2_point_node_', 'un_10_3_grup_2_competitor_node_', 'un_10_3_grup_2_point_node_')
        print_match_under_5_wrapper(match_under_10.second_group, main_window, names, 10, 2)
    if state == 2:
        node_names = ['un_10_half_final_competitor_node_' + str(x) for x in range(1, 5)]
        load_competitors_to_nodes(node_names, match_under_10.overtime.competitors, main_window)
    if state == 3:
        node_names = ['un_10_half_final_competitor_node_5', 'un_10_final_competitor_node_1']
        load_competitors_to_nodes(node_names, [match_under_10.overtime.tree[0].get_competitor()] * 2, main_window)
    if state == 4:
        node_names = ['un_10_half_final_competitor_node_6', 'un_10_final_competitor_node_2']
        load_competitors_to_nodes(node_names, [match_under_10.overtime.tree[1].get_competitor()] * 2, main_window)
    if state == 5:
        node_names = ['un_10_final_competitor_node_3']
        load_competitors_to_nodes(node_names, [match_under_10.overtime.tree[2].get_competitor()], main_window)


def show_message(window, message, slide=False):
    window.ui.Communicate.setPlainText(message)
    if slide:
        actual_size = window.ui.right_menu.width()
        if actual_size == 0:
            new_size = 250
            window.leftMenuAnimation = QPropertyAnimation(window.ui.right_menu, b"minimumWidth")
            window.leftMenuAnimation.setDuration(450)
            window.leftMenuAnimation.setStartValue(actual_size)
            window.leftMenuAnimation.setEndValue(new_size)
            window.leftMenuAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            window.leftMenuAnimation.start()


def print_team_match(team_match, main_window):
    print("powinno zmienić")
    main_window.ui.AllMatchesWraper.setCurrentWidget(main_window.ui.TeemMatch)
    team1_nodes = ['team_1_competitor_' + str(x) for x in range(1, 5)]
    team2_nodes = ['team_2_competitor_' + str(x) for x in range(1, 5)]
    load_competitors_to_nodes(team1_nodes, team_match.team1.get_competitors_list(), main_window)
    load_competitors_to_nodes(team2_nodes, team_match.team2.get_competitors_list(), main_window)
    main_window.ui.team_1_score.setText(str(team_match.score[0]))
    main_window.ui.team_2_score.setText(str(team_match.score[1]))
    main_window.ui.TeamName_1.setText(str(team_match.team1.get_club_name()))
    main_window.ui.TeamName_2.setText(str(team_match.team2.get_club_name()))


def hide_wind_buttons(main_window, hide):
    main_window.ui.win_left.setVisible(not hide)
    main_window.ui.win_right.setVisible(not hide)


def change_match_buttons(main_window, is_team, match):
    if is_team:
        hide_wind_buttons(main_window,not match)
        main_window.ui.make_match_button.setVisible(not match)
        main_window.ui.go_to_all_match_button.setVisible(match)
    else:
        main_window.ui.make_match_button.setVisible(False)
        main_window.ui.go_to_all_match_button.setVisible(False)


def print_randomisation_results(main_window,competitors,match_type):
    if match_type == TypeOFMatch.Under5:
        node_names = ['RandRes5_'+str(i+1) for i in range(len(competitors))]
        load_competitors_to_nodes(node_names,competitors,main_window)
        main_window.ui.stackedWidget_2.setCurrentWidget(main_window.ui.RandomFunctionRes5)
    if match_type == TypeOFMatch.Under10:
        node_names = ['RandRes10_'+str(i+1) for i in range(len(competitors[0]))]
        load_competitors_to_nodes(node_names,competitors[0],main_window)

        node_names = ['RandRes10_'+str(i+6) for i in range(len(competitors[1]))]
        load_competitors_to_nodes(node_names,competitors[1],main_window)

        main_window.ui.stackedWidget_2.setCurrentWidget(main_window.ui.RandomFunctionRes10)
    if match_type == TypeOFMatch.Under16:
        node_names = ['RandRes16_'+str(i+1) for i in range(len(competitors))]
        load_competitors_to_nodes(node_names,competitors,main_window)
        main_window.ui.stackedWidget_2.setCurrentWidget(main_window.ui.RandomFunctionRes16)