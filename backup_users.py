# backup_users.py
import json
from app import app, db
from models import User

def backup_users():
    with app.app_context():
        users = User.query.all()
        user_data = []
        for user in users:
            user_data.append({
                'fullname': user.fullname,
                'email': user.email,
                'password': user.password,  # Keep hashed passwords
                'phone': user.phone,
                'user_type': user.user_type,
                'username': user.username,
                'business_name': user.business_name,
                'business_description': user.business_description,
                'address': user.address
            })
        
        with open('user_backup.json', 'w') as f:
            json.dump(user_data, f, indent=2)
        print(f"✓ Backed up {len(user_data)} users to user_backup.json")

if __name__ == '__main__':
    backup_users()