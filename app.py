from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1 


winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  
    [0, 4, 8], [2, 4, 6]              
]


def check_win():
    for comb in winning_combinations:
        if xState[comb[0]] == xState[comb[1]] == xState[comb[2]] == 1:
            return 'X'
        elif zState[comb[0]] == zState[comb[1]] == zState[comb[2]] == 1:
            return '0'
    return None


@app.route('/')
def index():
    return render_template('index.html', xState=xState, zState=zState, turn=turn)


@app.route('/play', methods=['POST'])
def play():
    global turn
    position = int(request.form['position'])
    if turn == 1:
        xState[position] = 1
    else:
        zState[position] = 1
    winner = check_win()
    if winner:
        return redirect(url_for('game_over', winner=winner))
    elif all(x != 0 for x in xState + zState):
        return redirect(url_for('game_over', winner='Draw'))
    turn = 1 - turn
    return redirect(url_for('index'))


@app.route('/game_over/<winner>')
def game_over(winner):
    return render_template('game_over.html', winner=winner)

@app.route('/clear', methods=['POST'])
def clear_board():
    global xState, zState, turn
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
