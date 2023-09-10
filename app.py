from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('offer')
def handle_offer(offer):
    # Broadcast the offer to all connected clients (you may need to modify this logic)
    socketio.emit('offer', offer, broadcast=True)

@socketio.on('answer')
def handle_answer(answer):
    # Broadcast the answer to all connected clients (you may need to modify this logic)
    socketio.emit('answer', answer, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
