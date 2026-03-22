import time
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role
admin = User("Janka", "admin")
user = User("Malika", "user")

def is_admin(func):
    def wrapper(user):
         if user.role == "admin":
             return func(user)
         else:
            print("У вас нету доступа")
    return wrapper
@is_admin
def delete_video(user):
    print("Видео удалено")

delete_video(admin)
delete_video(user)

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Время выполнения: {end - start} секунд' )
    return wrapper
@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")
download_video()