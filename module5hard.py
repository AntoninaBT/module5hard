# Teplova// Свой YouTube
#
#
#
#словарь с данными, в который будут добавляться имя пользователя и пароль, а также метод для добавления данных в этот словарь
from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.age = int(age)
        self.password = hash(password)
    def __str__(self):
        return self.nickname
    def __eq__(self, other):
        return self.nickname == other.nickname
    def get_info(self):
        return self.nickname, self.password
class Video:
    def __init__(self, title, duration, adult_mode=False):
         self.title = title
         self.duration = duration
         self.adult_mode = adult_mode
         self.time_now = 0

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title
class UrTube:
    def __init__(self):
         self.user = []
         self.videos = []
         self.current_user = None
    def log_in(self, login, password):
        for i in self.user:
            if i.nickname == login and i.password == password:
                self.current_user = i
                return
    print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        for user in self.user:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.user.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None
    def add(self, *videos):
        for i in videos:
            if i.title not in self.videos:
                self.videos.append(i)
    def get_videos(self, title):
        self.title = title.lower()
        return [video.title for video in self.videos if self.title in video.title.lower()]
    def watch_videos(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            print("Видео не найдено")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for second in range(video.time_now, video.duration):
            print(f"Секунда: {second + 1}")
            sleep(1)

        video.time_now = 0
        print("Конец видео")

#Код для проверки:

ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)



# Добавление видео

ur.add(v1, v2)



# Проверка поиска

print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))



# Проверка на вход пользователя и возрастное ограничение

ur.watch_videos('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_videos('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_videos('Для чего девушкам парень программист?')



# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)



# Попытка воспроизведения несуществующего видео

ur.watch_videos('Лучший язык программирования 2024 года!')