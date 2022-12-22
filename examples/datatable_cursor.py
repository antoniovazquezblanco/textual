#!/usr/bin/env python

'''
Datatables cursor type example.
'''

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.reactive import reactive
from textual.widgets import DataTable, Footer, Header


class DynamicBindingsApp(App):
    '''
    A TUI application that allows you to change datatable cursor types dynamically.
    '''
    BINDINGS = [
        Binding(key="s", action="cursor('cell')", description="Cell cursor"),
        Binding(key="r", action="cursor('row')", description="Row cursor"),
        Binding(key="c", action="cursor('column')", description="Column cursor")
    ]

    def compose(self) -> ComposeResult:
        '''Build the UI'''
        yield Header(show_clock=True)
        yield DataTable()
        yield Footer()

    def on_mount(self):
        '''On widgets mount, add datatable contents'''
        datatable = self.query_one(DataTable)
        for c in range(3):
            datatable.add_column(f'Col {c}')
        for r in range(10):
            datatable.add_row(f'Cell(1, {r})', f'Cell(2, {r})', f'Cell(3, {r})')

    def action_cursor(self, cursor) -> None:
        '''Toggle to cell type'''
        self.query_one(DataTable).cursor_type = cursor


if __name__ == "__main__":
    app = DynamicBindingsApp()
    app.run()
