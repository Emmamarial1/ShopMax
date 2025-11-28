from app import app, db, Order

def final_check():
    print("✅ FINAL VERIFICATION")
    print("=" * 30)
    
    with app.app_context():
        # Check Order model
        print("📋 Order Model Columns:")
        for column in Order.__table__.columns:
            print(f"   - {column.name}")
        
        # Check if we can count orders without error
        try:
            count = Order.query.count()
            print(f"📊 Orders in database: {count}")
            print("🎉 SUCCESS! No more 'no such column' error!")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == '__main__':
    final_check()