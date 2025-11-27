#!/usr/bin/env python3
"""
Database initialization script
Run this after first deployment
"""
from app import app, db
from models import User

def init_database():
    """Initialize database and create admin user"""
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✓ Database tables created")
        
        # Check if admin exists
        admin = User.query.filter_by(email='admin@afimperiya.uz').first()
        if not admin:
            # Create admin user
            admin = User(
                full_name='Administrator',
                email='admin@afimperiya.uz',
                role='admin',
                is_active=True,
                department='IT',
                position='System Administrator'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("✓ Admin user created")
            print("\n=== LOGIN CREDENTIALS ===")
            print("Email: admin@afimperiya.uz")
            print("Password: admin123")
            print("=========================\n")
        else:
            print("✓ Admin user already exists")
        
        print("Database initialization completed successfully!")

if __name__ == '__main__':
    init_database()
