import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboardfrom flask import Flask, render_template
import csv
import os

app = Flask(__name__)
def read_leaderboard():
    leaderboard = []
    with open(‘leaderboard.csv’, ‘r’) as file:
        reader = csv.reader(file)
        for row in reader:
            leaderboard.append(row)
    return leaderboard
@app.route(‘/’)
def leaderboard():
    leaderboard_data = read_leaderboard()
    return render_template(‘leaderboard.html’, leaderboard_data=leaderboard_data)
if __name__ == ‘__main__‘:
    app.run()
def write_leaderboard(leaderboard):
    with open(‘leaderboard.csv’, ‘w’, newline=‘’) as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)
def read_leaderboard():
    leaderboard = []
    if not os.path.isfile(‘leaderboard.csv’):
        initial_data = [
            [‘Ryan’, ‘1000’, ‘00:45’],
            [‘Aniket’, ‘800’, ‘01:15’],
            [‘Max’, ‘650’, ‘00:55’],
            [‘Evan’, ‘500’, ‘01:21’],
            [‘Nathan’, ‘650’, ‘00:47’],
            [‘Kalani’, ‘0’, ‘10:32’],
            [‘Jaden’, ‘1100’, ‘00:31’]
        ]
        write_leaderboard(initial_data)
        leaderboard = initial_data
    else:
        with open(‘leaderboard.csv’, ‘r’) as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
    return leaderboard