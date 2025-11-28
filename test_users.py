from app import app, db
from models import User

def create_test_users():
    with app.app_context():
        # Create admin user
        admin = User(
            fullname="Admin User",
            email="admin@shopmax.com",
            user_type="admin",
            username="admin",
            is_active=True
        )
        admin.set_password("admin123")

        # Create seller user
        seller = User(
            fullname="Test Seller",
            email="seller@shopmax.com", 
            user_type="seller",
            username="testseller",
            business_name="UCU Campus Store",
            business_description="Selling quality products to UCU students",
            phone="+256700000000",
            is_active=True
        )
        seller.set_password("seller123")

        # Create buyer user
        buyer = User(
            fullname="Test Buyer",
            email="buyer@shopmax.com",
            user_type="buyer", 
            username="testbuyer",
            phone="+256711111111",
            is_active=True
        )
        buyer.set_password("buyer123")

        try:
            db.session.add(admin)
            db.session.add(seller)
            db.session.add(buyer)
            db.session.commit()
            print("✓ Test users created successfully!")
            print("  Admin: admin@shopmax.com / admin123")
            print("  Seller: seller@shopmax.com / seller123") 
            print("  Buyer: buyer@shopmax.com / buyer123")
        except Exception as e:
            db.session.rollback()
            print(f"✗ Error creating users: {e}")

if __name__ == '__main__':
    create_test_users()