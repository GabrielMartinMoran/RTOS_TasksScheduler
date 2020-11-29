from src.models.execution_matrix import ExecutionMatrix
import matplotlib.pyplot as plt
import os
import webbrowser
from copy import deepcopy
import random

class ExecutionMatrixDrawer:

    FILENAME = 'result.html'
    PROCESSORS_COLORS = ['#f1c5c5', '#ffeb99', '#c3aed6', '#f5b971', '#b9cced', '#e9e1cc']

    def __init__(self):
        self.processors_colors = deepcopy(self.PROCESSORS_COLORS)

    def draw_matrix(self, matrix: ExecutionMatrix):        
        headers = self.__generate_headers(matrix)
        data = self.__generate_data(matrix)
        table = """
        <style>
            body {
                background: #5d5b6a;
            }
            table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
                min-width: 20px;
            }
            th {
                background: #454545;
                color: white;
            }
            td {
                text-align: center;
            }
        </style>
        <table>
            {headers}
            {data}
        </table>
        """.replace('{headers}', headers).replace('{data}', data)
        self.__show_result(table)

    def __generate_headers(self, matrix: ExecutionMatrix):
        headers = ['Processors'] + [str(x) for x in range(matrix.hyperperiod)]
        th_s = ''
        for x in headers:
            th_s += f'<th>{x}</th>'
        return f'<tr>{th_s}</tr>'

    def __generate_data(self, matrix: ExecutionMatrix):
        data = ''
        for x in range(len(matrix.processors)):
            color = self.__get_random_color()
            data += f'<tr style="background: {color};"><td>Proc. {x}</td>'
            for t in matrix.processors[x].time_units:
                data += '<td>'
                if t is not None:
                    data += t.name
                data += '</td>'
            data += '</tr>'
        return data

    def __show_result(self, html):
        f = open(self.FILENAME,'w')
        f.write(html)
        f.close()
        filename = 'file:///'+os.getcwd()+'/' + self.FILENAME
        webbrowser.open_new_tab(filename)

    def __get_random_color(self):
        color = random.choice(self.processors_colors)
        self.processors_colors.remove(color)
        if len(self.processors_colors) == 0:
            self.processors_colors = deepcopy(self.PROCESSORS_COLORS)
        return color
