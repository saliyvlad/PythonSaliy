import PySimpleGUI as sg
import random

class TournamentApp:
    def __init__(self):
        self.teams = []
        self.layout = self.create_layout()
        self.window = sg.Window("Футбольный турнир", self.layout)

    def create_layout(self):
        layout = [
            [sg.Button("Добавить команду"), sg.Button("Удалить команду")],
            [sg.Button("Экспорт в файл"), sg.Button("Импорт из файла")],
            [sg.Button("Создать турнир"), sg.Button("Эмуляция турнира")],
            [sg.Listbox(values=self.teams, size=(30, 10), key="-TEAM_LIST-", enable_events=True)],
            [sg.Button("Выход")]
        ]
        return layout

    def run(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED or event == "Выход":
                break
            elif event == "Добавить команду":
                self.add_team()
            elif event == "Удалить команду":
                self.remove_team()
            elif event == "Экспорт в файл":
                self.export_to_file()
            elif event == "Импорт из файла":
                self.import_from_file()
            elif event == "Создать турнир":
                self.create_tournament()
            elif event == "Эмуляция турнира":
                self.simulate_tournament()

        self.window.close()

    def add_team(self):
        team_name = sg.popup_get_text("Введите название команды:")
        if team_name and team_name not in self.teams:
            self.teams.append(team_name)
            self.update_team_list()
        else:
            sg.popup_error("Ошибка: такая команда уже есть или название пустое.")

    def remove_team(self):
        selected_team = values["-TEAM_LIST-"]
        if selected_team:
            self.teams.remove(selected_team[0])
            self.update_team_list()
        else:
            sg.popup_error("Ошибка: выберите команду для удаления.")

    def export_to_file(self):
        file_name = sg.popup_get_file("Сохранить как", save_as=True, no_window=True)
        if file_name:
            with open(file_name, 'w') as f:
                for team in self.teams:
                    f.write(team + '\n')
            sg.popup("Команды экспортированы в файл.")

    def import_from_file(self):
        file_name = sg.popup_get_file("Выберите файл для импорта", no_window=True)
        if file_name:
            confirm = sg.popup_yes_no("Вы уверены, что хотите загрузить список команд из файла? Все несохраненные команды будут удалены.")
            if confirm == "Yes":
                with open(file_name, 'r') as f:
                    self.teams = [line.strip() for line in f.readlines()]
                self.update_team_list()

    def create_tournament(self):
        tournament_name = sg.popup_get_text("Введите название турнира:")
        num_teams = sg.popup_get_text("Введите количество команд:")
        
        try:
            num_teams = int(num_teams)
            if num_teams > len(self.teams):
                sg.popup_error("Ошибка: недостаточно команд для турнира.")
                return

            matches = []
            random_teams = random.sample(self.teams, num_teams)
            for i in range(0, num_teams, 2):
                if i + 1 < num_teams:
                    matches.append(f"{random_teams[i]} - {random_teams[i + 1]}")

            with open(f"{tournament_name}.txt", 'w') as f:
                f.write(f"{tournament_name}\n")
                for match in matches:
                    f.write(match + '\n')
            sg.popup(f"Турнир '{tournament_name}' создан.")
        except ValueError:
            sg.popup_error("Ошибка: введите корректное число.")

    def simulate_tournament(self):
        tournament_name = sg.popup_get_text("Введите название турнира:")
        num_teams = sg.popup_get_text("Введите количество команд:")
        
        try:
            num_teams = int(num_teams)
            if num_teams > len(self.teams):
                sg.popup_error("Ошибка: недостаточно команд для турнира.")
                return

            matches = []
            scores = {}
            random_teams = random.sample(self.teams, num_teams)
            for i in range(0, num_teams, 2):
                if i + 1 < num_teams:
                    score1 = random.randint(0, 5)
                    score2 = random.randint(0, 5)
                    matches.append(f"{random_teams[i]} - {random_teams[i + 1]} Счет: {score1} - {score2}")
                    scores[random_teams[i]] = scores.get(random_teams[i], 0) + score1
                    scores[random_teams[i + 1]] = scores.get(random_teams[i + 1], 0) + score2

            with open(f"{tournament_name}.txt", 'w') as f:
                f.write(f"{tournament_name}\n")
                for match in matches:
                    f.write(match + '\n')

                max_goals = max(scores.values(), default=0)
                winners = [team for team, score in scores.items() if score == max_goals]
                f.write("Победители: " + ', '.join(winners) + '\n')
            sg.popup(f"Эмуляция турнира '{tournament_name}' завершена.")
        except ValueError:
            sg.popup_error("Ошибка: введите корректное число.")

    def update_team_list(self):
        self.window["-TEAM_LIST-"].update(self.teams)


if __name__ == "__main__":
    app = TournamentApp()
    app.run()