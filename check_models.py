import os
import sys

# Add current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db

def check_all_models():
    with app.app_context():
        print("🔍 CHECKING ALL MODELS AND DATABASE SCHEMA")
        print("=" * 50)
        
        # Check Order model
        from app import Order
        print("📋 Order Model Columns:")
        for column in Order.__table__.columns:
            print(f"   - {column.name} ({column.type})")
        
        print("\n📊 Database Orders Table Columns:")
        try:
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            columns = inspector.get_columns('orders')
            for column in columns:
                print(f"   - {column['name']} ({column['type']})")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        # Check if they match
        print("\n🔍 COMPARISON:")
        model_columns = [col.name for col in Order.__table__.columns]
        try:
            db_columns = [col['name'] for col in inspector.get_columns('orders')]
            missing_in_db = set(model_columns) - set(db_columns)
            missing_in_model = set(db_columns) - set(model_columns)
            
            if missing_in_db:
                print(f"❌ Columns in model but NOT in database: {missing_in_db}")
            if missing_in_model:
                print(f"❌ Columns in database but NOT in model: {missing_in_model}")
            if not missing_in_db and not missing_in_model:
                print("✅ Model and database are synchronized!")
                
        except Exception as e:
            print(f"❌ Cannot compare: {e}")

if __name__ == '__main__':
    check_all_models()