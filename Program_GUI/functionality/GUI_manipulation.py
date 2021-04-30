from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from personal_competitor import *
from match_under_16 import MatchUnder16
from match_under_5 import MatchUnder5


def load_competitors_to_nodes(nodes_names, competitors_list, main_window, copy_nodes=[]):
    for node, competitor in zip(nodes_names, competitors_list):
        main_window.ui.__dict__[node].clear()
        main_window.ui.__dict__[node].setAlignment(Qt.AlignCenter)
        main_window.ui.__dict__[node].append(competitor.get_name())
        main_window.ui.__dict__[node].append(competitor.get_club())
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

def print_match_under_5_points(match_under_5, main_window):
    points = match_under_5.get_results()
    competitors = match_under_5.get_competitors()
    values = [points[x] for x in competitors]
    node_names = ["un_5_point_node_" + str(x) for x in range(1, 6)]
    load_values_to_nodes(node_names, values, main_window)


def print_actual_match_under_5(match_under_5, main_window):
    actual_match_id = match_under_5.get_actual_match_id()
    all_nodes = ["un_5_competitor_node_" + str(x) for x in range(1, 26)]
    colors_for_all = ['black'] * 25
    colors_for_actual = ['yellow'] * 2
    node_1 = 'un_5_competitor_node_' + str(match_under_5.get_actual_match_id() * 2 + 6)
    node_2 = 'un_5_competitor_node_' + str(match_under_5.get_actual_match_id() * 2 + 7)

    color_borders(all_nodes, colors_for_all, main_window)
    color_borders([node_1, node_2], colors_for_actual, main_window)


def print_match_under_5(match_under_5, main_window):
    node_names = ["un_5_competitor_node_" + str(x) for x in range(1, 26)]
    competitors_list = match_under_5.get_competitors()
    matches_nodes = dict()
    for match in match_under_5.matches:
        competitors_list.append(match.get_left_child())
        competitors_list.append(match.get_right_child())
    load_competitors_to_nodes(node_names, competitors_list, main_window)
    print_match_under_5_points(match_under_5, main_window)
    print_actual_match_under_5(match_under_5, main_window)


def print_match_under_4_points(match_under_4, main_window):
    points = match_under_4.get_results()
    competitors = match_under_4.get_competitors()
    values = [points[x] for x in competitors]
    node_names = ["un_4_point_node_" + str(x) for x in range(1, 5)]
    load_values_to_nodes(node_names, values, main_window)


def print_actual_match_under_4(match_under_4, main_window):
    actual_match_id = match_under_4.get_actual_match_id()
    all_nodes = ["un_4_competitor_node_" + str(x) for x in range(1, 17)]
    colors_for_all = ['black'] * 17
    colors_for_actual = ['yellow'] * 2
    node_1 = 'un_4_competitor_node_' + str(match_under_4.get_actual_match_id() * 2 + 5)
    node_2 = 'un_4_competitor_node_' + str(match_under_4.get_actual_match_id() * 2 + 6)

    color_borders(all_nodes, colors_for_all, main_window)
    color_borders([node_1, node_2], colors_for_actual, main_window)


def print_match_under_4(match_under_4, main_window):
    node_names = ["un_4_competitor_node_" + str(x) for x in range(1, 17)]
    competitors_list = match_under_4.get_competitors()
    matches_nodes = dict()
    for match in match_under_4.matches:
        competitors_list.append(match.get_left_child())
        competitors_list.append(match.get_right_child())
    load_competitors_to_nodes(node_names, competitors_list, main_window)
    print_match_under_4_points(match_under_4, main_window)
    print_actual_match_under_4(match_under_4, main_window)


def print_match_under_3_points(match_under_3, main_window):
    points = match_under_3.get_results()
    competitors = match_under_3.get_competitors()
    values = [points[x] for x in competitors]
    node_names = ["un_3_point_node_" + str(x) for x in range(1, 4)]
    load_values_to_nodes(node_names, values, main_window)


def print_actual_match_under_3(match_under_3, main_window):
    actual_match_id = match_under_3.get_actual_match_id()
    all_nodes = ["un_3_competitor_node_" + str(x) for x in range(1, 10)]
    colors_for_all = ['black'] * 9
    colors_for_actual = ['yellow'] * 2
    node_1 = 'un_3_competitor_node_' + str(match_under_3.get_actual_match_id() * 2 + 4)
    node_2 = 'un_3_competitor_node_' + str(match_under_3.get_actual_match_id() * 2 + 5)

    color_borders(all_nodes, colors_for_all, main_window)
    color_borders([node_1, node_2], colors_for_actual, main_window)


def print_match_under_3(match_under_3, main_window):
    node_names = ["un_3_competitor_node_" + str(x) for x in range(1, 10)]
    competitors_list = match_under_3.get_competitors()
    matches_nodes = dict()
    for match in match_under_3.matches:
        competitors_list.append(match.get_left_child())
        competitors_list.append(match.get_right_child())
    load_competitors_to_nodes(node_names, competitors_list, main_window)
    print_match_under_3_points(match_under_3, main_window)
    print_actual_match_under_3(match_under_3, main_window)
