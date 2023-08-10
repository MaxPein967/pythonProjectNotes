import datetime
from controller import Controller
from action import Action
from note import Note
from view import View


def run():
    c = Controller(Action("notes.json"), View())

    while True:
        button = input(
                        'Сделайте Ваш выбор:\n' +
                        '1 - Создать заметку\n'
                        '2 - Показать заметку\n'
                        '3 - Изменить заметку\n'
                        '4 - Удалить заметку\n'
                        '5 - Удалить все заметки\n'
                        '6 - Показать все заметки\n'
                        '7 - Выход\n'
                        )
        if button == '7':
            print('\nВы вышли из программы')
            break

        if button == '1':
            print('\nСоздать заметку:')
            c.create_note(get_note_data())

        elif button == '2':
            print('\nПоказать заметку:')
            if c.notes_exist():
                c.show_note(int(get_number()))
        elif button == '3':
            if c.notes_exist():
                print('\nИзменить заметку:')
                updated_id = int(get_number())
                if c.note_id_exist(updated_id):
                    c.update_note(updated_id, get_note_data())

        elif button == '4':
            if c.notes_exist():
                print('\nУдалить заметку:')
                delete_id = int(get_number())
                if c.note_id_exist(delete_id):
                    c.delete_note(delete_id)

        elif button == '5':
            if c.notes_exist():
                print('\nУдалить все заметки:')
                if input('Вы точно хотите удалить все заметки? (Y/N): ').capitalize() == 'Y':
                    if c.notes_exist():
                        c.delete_all_notes()

        elif button == '6':
            if c.notes_exist():
                print('\nСписок всех заметок:')
                c.show_notes()
        else:
            print('Введите существующий пункт меню')


def get_note_data():
    note_id = 0
    date = datetime.datetime.now()
    title = input('Введите название заметки: ')
    text = input('Введите текст заметки: ')
    return Note(note_id, date, title, text)


def get_number():
    while True:
        get_choice = input('Введите id заметки: ')
        if get_choice.isdigit() and int(get_choice) > 0:
            return get_choice
        else:
            print('Введите целое положительное число!')