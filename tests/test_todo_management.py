from test_todomvc.model import todomvc

todomvc = todomvc.TodoMVC()


def test_default_workflow():
    todomvc.open()

    todomvc.add('a', 'b', 'c')
    todomvc.assert_all_todos('a', 'b', 'c')

    todomvc.edit_by_enter('b', 'b edited')

    todomvc.complete('b edited')
    todomvc.clear_completed()
    todomvc.assert_all_todos('a', 'c')

    todomvc.cancel_edit('c', 'to be canceled')

    todomvc.delete('c')
    todomvc.assert_all_todos('a')
