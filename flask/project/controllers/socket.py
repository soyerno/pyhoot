from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from flask_socketio import emit, join_room, leave_room
from .. import socketio

socket = Blueprint('socket', __name__)

connected_users = {}
user_rooms = {}

@socket.route("/room/<string:id>")
@login_required
def room(id=None):
    props = {
        "id": id,
        "user": current_user.name
    }
    return render_template('pages/room.html', props=props)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    user = connected_users.pop(request.sid, None)
    if user:
        username = user.get('name')
        room = user.get('room')
        if room:
            leave_room(room)
            room_users = user_rooms.get(room, [])
            room_users = [u for u in room_users if u['name'] != username]
            user_rooms[room] = room_users
            emit('room_users', {'users': room_users}, room=room)
            emit('user-left', {"name": username, "sid": request.sid}, room=room)
            emit('message', {'text': f'{username} left room: {room}'}, room=room)
        print(f'User {username} disconnected')
    else:
        print('Unknown user disconnected')
    print('Client disconnected')

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    username = current_user.name
    sid = request.sid
    connected_users[sid] = {"name": username, "room": room, "sid": sid}
    room_data = user_rooms.get(room, []) 
    room_data.append({"name": username, "sid": sid})
    user_rooms[room] = room_data
    emit('room_users', {'users': room_data}, room=room)
    emit('user-join', {"name": username, "sid": sid}, room=room)
    emit('message', {'text': f'{username} joined room: {room}'}, room=room)

@socketio.on('leave')
def handle_leave(data):
    user = connected_users.pop(request.sid, None)
    if user:
        username = user.get('name')
        room = data.get('room')
        if room:
            leave_room(room)
            room_users = user_rooms.get(room, [])
            room_users = [u for u in room_users if u['sid'] != request.sid]
            user_rooms[room] = room_users
            emit('room_users', {'users': room_users}, room=room)
            emit('user-left', {"name": username, "sid": request.sid}, room=room)
            emit('message', {'text': f'{username} left room: {room}'}, room=room)
