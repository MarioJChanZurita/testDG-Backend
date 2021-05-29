from src import initApp
from config import config

configuration = config['development']

app = initApp(configuration)

if __name__ == '__main__':
    app.run()
