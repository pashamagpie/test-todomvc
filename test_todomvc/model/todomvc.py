from selene.support.conditions import have
from selene.support.shared import browser


class TodoMVC:

    def __init__(self):
        self.todos = browser.all('#todo-list>li')
        self.be_completed = have.css_class('completed')
        self.be_active = self.be_completed.not_

    def open(self):
        browser.open('https://todomvc4tasj.herokuapp.com/')
        script_on_clear_completed = "return 'click' in \
            $._data($('#clear-completed')[0],'events')"
        browser.should(have.js_returned(True, script_on_clear_completed))
        return self

    def add(self, *names: str):
        for name in names:
            browser.element('#new-todo').type(name).press_enter()
        return self

    def given_opened_with(self, *names: str):
        self.open()
        self.add(*names)
        return self

    def check_filter(self, name: str):
        browser.element('.selected') \
            .should(have.exact_text(name))
        return self

    def assert_all_todos(self, *names: str):
        self.todos.should(have.exact_texts(*names))
        return self

    def assert_active_todos(self, *names: str):
        self.todos.filtered_by(self.be_active).should(have.exact_texts(*names))
        return self

    def assert_completed_todos(self, *names: str):
        self.todos.filtered_by(self.be_completed).should(have.exact_texts(*names))
        return self

    def assert_items_left(self, counter: int):
        browser.element('#todo-count>strong') \
            .should(have.exact_text(str(counter)))
        return self

    def _start_editing(self, name: str, edited_text):
        self.todos.element_by(have.exact_text(name)).double_click()
        return self.todos.element_by(have.css_class('editing')) \
            .element('.edit').with_(set_value_by_js=True).set_value(edited_text)

    def edit_by_enter(self, name: str, edited_text):
        self._start_editing(name, edited_text).press_enter()
        return self

    def edit_by_tab(self, name: str, edited_text):
        self._start_editing(name, edited_text).press_tab()
        return self

    def edit_by_click_outside(self, name: str, edited_text):
        self._start_editing(name, edited_text)
        browser.all('#info>p').first.click()
        return self

    def _toggle(self, name: str):
        self.todos.element_by(have.exact_text(name)) \
            .element('.toggle').click()
        return self

    def clear_completed(self):
        browser.element('#clear-completed').click()
        return self

    def cancel_edit(self, name: str, edited_text):
        self._start_editing(name, edited_text).press_escape()
        return self

    def delete(self, *names: str):
        for name in names:
            self.todos.element_by(have.exact_text(name)).hover() \
                .element('.destroy').click()
        return self

    def complete(self, *names: str):
        for name in names:
            self.todos.element_by(have.exact_text(name)) \
                .should(self.be_active)
            self._toggle(name)
        return self

    def toggle_all(self):
        browser.element('#toggle-all').click()
        return self

    def activate(self, *names: str):
        for name in names:
            self.todos.element_by(have.exact_text(name)) \
                .should(self.be_completed)
            self._toggle(name)
        return self
