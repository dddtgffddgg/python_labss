import PySimpleGUI as sg
from calculations import calculate_triangle_area

def main():
    layout = [
        [sg.Text('Введите параметры для расчета:')],
        [sg.Text('Основание треугольника:'), sg.Input(key='triangle_base')],
        [sg.Text('Высота треугольника:'), sg.Input(key='triangle_height')],
        [sg.Button('Рассчитать площадь треугольника')],
        [sg.Output(size=(40, 10))],
        [sg.Button('Выход')]
    ]

    window = sg.Window('Геометрический калькулятор', layout)

    while True:
        event, values = window.read()
        
        if event == sg.WINDOW_CLOSED or event == 'Выход':
            break
        
        if event == 'Рассчитать площадь треугольника':
            base = float(values['triangle_base'])
            height = float(values['triangle_height'])
            area = calculate_triangle_area(base, height)
            print(f"Площадь треугольника: {area}")
    
    window.close()

if __name__ == '__main__':
    main()
