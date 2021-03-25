from test_todomvc.model import todomvc

todomvc = todomvc.TodoMVC()


def test_add_single():
    todomvc.open()

    todomvc.add('a')

    todomvc.assert_all_todos('a').assert_items_left(1)


def test_add_many():
    todomvc.open()

    todomvc.add('a', 'b', 'c')

    todomvc.assert_all_todos('a', 'b', 'c').assert_items_left(3)


'''def test_edit_by_enter():
    todomvc.given_opened_with('a', 'b', 'c')

    todomvc.edit_by_enter('b', 'b edited')

    todomvc.assert_all_todos('a', 'b edited', 'c').assert_items_left(3)


def test_edit_by_tab():
    todomvc.given_opened_with('a', 'b', 'c')

    todomvc.edit_by_tab('b', 'b edited')

    todomvc.assert_all_todos('a', 'b edited', 'c').assert_items_left(3)


def test_edit_by_click_outside():
    todomvc.given_opened_with('a', 'b', 'c')

    todomvc.edit_by_click_outside('b', 'b edited')

    todomvc.assert_all_todos('a', 'b edited', 'c').assert_items_left(3)


def test_cancel_edit():
    todomvc.given_opened_with('a', 'b', 'c')

    todomvc.cancel_edit('b', 'b edited')

    todomvc.assert_all_todos('a', 'b', 'c').assert_items_left(3)


def test_edit_to_empty_line():
    todomvc.given_opened_with('a', 'b', 'c')

    todomvc.edit_by_enter('b', '')

    todomvc.assert_all_todos('a', 'c').assert_items_left(2)


def test_complete():
    todomvc.given_opened_with('a', 'b', 'c')

    todomvc.complete('b')

    todomvc.assert_completed_todos('b').assert_active_todos('a', 'c') \
        .assert_items_left(2)


def test_complete_all():
    todomvc.given_opened_with('a', 'b', 'c').complete('b')

    todomvc.toggle_all()

    todomvc.assert_completed_todos('a', 'b', 'c').assert_active_todos() \
        .assert_items_left(0)


def test_activate():
    todomvc.given_opened_with('a', 'b', 'c').toggle_all()

    todomvc.activate('b')

    todomvc.assert_active_todos('b').assert_completed_todos('a', 'c') \
        .assert_items_left(1)


def test_activate_all():
    todomvc.given_opened_with('a', 'b', 'c').toggle_all()

    todomvc.toggle_all()

    todomvc.assert_active_todos('a', 'b', 'c').assert_completed_todos() \
        .assert_items_left(3)


def test_clear_completed():
    todomvc.given_opened_with('a', 'b', 'c', 'd').complete('b', 'd')

    todomvc.clear_completed()

    todomvc.assert_all_todos('a', 'c').assert_items_left(2)


def test_delete():
    todomvc.given_opened_with('a', 'b', 'c')

    todomvc.delete('b')

    todomvc.assert_all_todos('a', 'c').assert_items_left(2)'''
