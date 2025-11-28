from app import app, db, Order

def verify_fix():
    print("✅ VERIFYING FIX")
    print("=" * 30)
    
    with app.app_context():
        try:
            # This should now work without errors
            order_count = Order.query.count()
            print(f"📊 Orders in database: {order_count}")
            print("🎉 SUCCESS! Admin dashboard should work now!")
            
            # Show the actual columns in the orders table
            print("\n📋 Orders table columns:")
            for column in Order.__table__.columns:
                print(f"   - {column.name}")
                
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == '__main__':
    verify_fix()