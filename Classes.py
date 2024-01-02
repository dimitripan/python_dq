import os.path


class Publication:
    news = '1'
    ad = '2'
    weather = '3'

    def __init__(self):
        self.i_type = None
        self.content = []

    def ask_type(self):
        while str(self.i_type) not in ('1', '2', '3'):
            self.i_type = input('Pick publication type: 1 News | 2 Private ad | 3 Weather report\nType 1, 2 or 3\n')

    def get_new(self):
        print("Enter/Paste your content. Press Enter twice to save it.")
        while True:
            line = input()
            if line:
                self.content.append(line)
            else:
                break
        print(self.content)

    def publish(self):
        file_name = 'published.txt'
        with open(file_name, 'a' if os.path.exists(file_name) else 'w') as file:
            for line in self.content:
                file.write(f"{line}\n")


class News(Publication):
    def __init__(self):
        super().__init__()
        self.title = 'News ------------------------------'
        self.divider = '-----------------------------------\n'

    def get_new(self):
        import datetime
        self.content.append(self.title)
        Publication.get_new(self)
        location = input("Enter/Paste city where that happened.\n")
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")
        self.content.append(location + ', ' + timestamp)
        self.content.append(self.divider)


class Ad(Publication):
    def __init__(self):
        super().__init__()
        self.title = 'AD --------------------------------'
        self.divider = '-----------------------------------\n'

    def get_new(self):
        import datetime
        self.content.append(self.title)
        Publication.get_new(self)
        while True:
            actual_until = input('Enter a date in YYYY-MM-DD format\n')
            year, month, day = map(int, actual_until.split('-'))
            actual_until = datetime.date(year, month, day)
            if actual_until > datetime.date.today():
                days_left = (actual_until - datetime.date.today()).days
                ending = 'Actual until: ' + str(actual_until) + ', ' + str(days_left) + ' days left'
                break
        self.content.append(ending)
        self.content.append(self.divider)


class Weather(Publication):
    def __init__(self):
        super().__init__()
        self.title = 'Weather ---------------------------'
        self.divider = '-----------------------------------\n'

    def get_new(self):
        import random
        self.content.append(self.title)
        Publication.get_new(self)
        weather = ['bad', 'ok', 'good']
        ending = f'Overall the weather is {random.choice(weather)}'
        self.content.append(ending)
        self.content.append(self.divider)


print(Publication.news)

a = Publication()
a.ask_type()

if a.i_type == Publication.news:
    b = News()
elif a.i_type == Publication.ad:
    b = Ad()
elif a.i_type == Publication.weather:
    b = Weather()

b.get_new()
b.publish()
