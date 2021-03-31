from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from personal_competitor import *


def load_competitors_to_nodes(nodes_names, competitors_list, main_window):
    for node, competitor in zip(nodes_names, competitors_list):
        main_window.ui.__dict__[node].setAlignment(Qt.AlignCenter)
        main_window.ui.__dict__[node].append(competitor.get_name())
        main_window.ui.__dict__[node].append(competitor.get_club())
        main_window.ui.__dict__[node].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";text-align: center;")


def print_eliminations_16(eliminations, main_window):
    def node_name(node_number):
        return "el_16_node_" + str(node_number)

    # print competitor in nodes
    node_names = [node_name(x) for x in range(4, 32)]
    competitors = [x.get_competitor() for x in eliminations.tree[4:]]
    load_competitors_to_nodes(node_names, competitors, main_window)

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
    if actual_node.get_competitor() == right_child.get_competitor():

        main_window.ui.__dict__[right_node_name].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";"
                                                                          "text-align: center;"
                                                                          "border: 3px solid Lime;"
                                                                          )
        main_window.ui.__dict__[left_node_name].setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";"
                                                                          "text-align: center;"
                                                                          "border: 3px solid red;"
                                                                          )


def clearNodes(nodes, main_window):
    for i in nodes:
        main_window.ui.__dict__[i].setStyleSheet("")


def colorNodeBorder(node_number, main_window):
    main_window.ui.__dict__["el_16_node_" + str(node_number)].setStyleSheet("border: 2px solid red;")
