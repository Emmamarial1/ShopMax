# recreate_database.py
import os
from app import app, db

def recreate_database():
    print("🔄 RECREATING DATABASE WITH FIXED MODELS")
    
    # Delete existing database
    if os.path.exists('shopmax.db'):
        os.remove('shopmax.db')
        print("🗑️  Deleted old database")
    
    with app.app_context():
        # Create all tables with updated models
        db.create_all()
        print("✅ Created new database with updated schema")
        
        # Initialize data
        from app import create_admin_user, initialize_delivery_persons, create_sample_products
        create_admin_user()
        initialize_delivery_persons()
        create_sample_products()
        
        print("🎉 Database recreation completed!")
        print("👉 Run: python app.py")

if __name__ == '__main__':
    recreate_database()