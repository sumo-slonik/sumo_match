def connect_gui_to_engine(main_window, all_match_engine):
    print("conektowanie_______________________________________")
    def make_match(left_child_win, engine, window):
        engine.print_match(window)
        engine.make_match(left_child_win)
        engine.print_match(window)

    def go_to_next_round(engine, window):
        engine.go_to_next_round()
        engine.print_match(window)

    main_window.AllMatchEngine = all_match_engine

    main_window.ui.next_match.clicked.connect(lambda: go_to_next_round(main_window.AllMatchEngine, main_window))
    main_window.ui.prev_match.clicked.connect(lambda: main_window.AllMatchEngine.go_to_prev_round())
    main_window.ui.win_left.clicked.connect(lambda: make_match(True, main_window.AllMatchEngine, main_window))
    main_window.ui.win_right.clicked.connect(lambda: make_match(False, main_window.AllMatchEngine, main_window))
    main_window.ui.make_match_button.clicked.connect(lambda: main_window.AllMatchEngine.go_to_team_match())
    main_window.AllMatchEngine.print_match()
