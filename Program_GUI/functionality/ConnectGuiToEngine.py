def connect_gui_to_engine(main_window, all_match_engine):
    def make_match(left_child_win, engine, window):
        engine.print_match(window)
        engine.make_match(left_child_win)
        engine.print_match(window)

    def go_to_next_round(engine, window):
        engine.go_to_next_round()
        engine.print_match(window)

    main_window.ui.next_match.clicked.connect(lambda: go_to_next_round(all_match_engine, main_window))
    main_window.ui.prev_match.clicked.connect(lambda: all_match_engine.go_to_prev_round())
    main_window.ui.win_left.clicked.connect(lambda: make_match(True, all_match_engine, main_window))
    main_window.ui.win_right.clicked.connect(lambda: make_match(False, all_match_engine, main_window))
    all_match_engine.print_match(main_window)