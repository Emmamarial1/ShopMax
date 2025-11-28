from app import app, db
from models import User

def verify_setup():
    with app.app_context():
        try:
            # Check if database is accessible
            users = User.query.all()
            print(f"✓ Database connected - Found {len(users)} users")
            
            # Check user types
            admins = User.query.filter_by(user_type='admin').count()
            sellers = User.query.filter_by(user_type='seller').count() 
            buyers = User.query.filter_by(user_type='buyer').count()
            
            print(f"✓ Admins: {admins}")
            print(f"✓ Sellers: {sellers}")
            print(f"✓ Buyers: {buyers}")
            
            # Check is_active functionality
            active_users = User.query.filter_by(is_active=True).count()
            print(f"✓ Active users: {active_users}")
            
            # Test individual user
            if users:
                user = users[0]
                print(f"✓ Sample user: {user.fullname} ({user.email}) - Active: {user.is_active}")
                
            print("✓ Database setup verified successfully!")
            
        except Exception as e:
            print(f"✗ Verification failed: {e}")

if __name__ == '__main__':
    verify_setup()