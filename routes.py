import logging
from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db
from models import User

main = Blueprint('main', __name__)
logger = logging.getLogger(__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/users')
def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@main.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    email = request.form.get('email')
    
    if name and email:
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        logger.info(f"User added: {email}")
    return redirect(url_for('main.list_users'))

@main.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user_to_delete = User.query.get_or_404(user_id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        logger.info(f"User Deleted: ID {user_id}")
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error deleting user {user_id}: {str(e)}")

    return redirect(url_for('main.list_users'))
