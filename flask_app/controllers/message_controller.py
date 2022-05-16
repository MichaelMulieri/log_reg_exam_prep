from crypt import methods
from flask import render_template, session,flash,redirect, request
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User
from flask_app.models.message import Message

@app.route('/post_message', methods=["POST"])
def post_message():
    if 'user_id' not in session:
        return redirect('/')

    data = {
        "sender_id": request.form['sender_id'],
        "receiver_id": request.form['receiver_id'],
        "content": request.form['content']
    }
    if len(data['content']) < 5:
        flash("Message must be at least 5 characters")
        return redirect('/dashboard')
    Message.save_message(data)
    return redirect('/dashboard')



@app.route('/destroy/message/<int:id>')
def destroy_message(id):
    data={
        "id": id
    }
    Message.destroy_message(data)
    return redirect('/dashboard')