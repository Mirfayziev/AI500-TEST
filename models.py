from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# User Model
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))
    telegram_username = db.Column(db.String(100))
    telegram_chat_id = db.Column(db.String(100))
    role = db.Column(db.String(50), default='user')  # admin, rahbar, xodim, user
    department = db.Column(db.String(100))
    position = db.Column(db.String(100))
    phone = db.Column(db.String(50))
    bio = db.Column(db.Text)
    photo = db.Column(db.String(200))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    assigned_modules = db.relationship('UserModule', foreign_keys='UserModule.user_id', backref='user', lazy=True)
    tasks_created = db.relationship('Task', foreign_keys='Task.created_by', backref='creator', lazy=True)
    tasks_assigned = db.relationship('TaskAssignment', foreign_keys='TaskAssignment.user_id', backref='assigned_user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def has_module_access(self, module_name):
        if self.role in ['admin', 'rahbar']:
            return True
        return any(um.module_name == module_name for um in self.assigned_modules)

# User Module Assignment
class UserModule(db.Model):
    __tablename__ = 'user_modules'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    module_name = db.Column(db.String(100), nullable=False)
    assigned_at = db.Column(db.DateTime, default=datetime.utcnow)
    assigned_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    assigner = db.relationship('User', foreign_keys=[assigned_by], backref='modules_assigned')

# 1. Topshriqlar Module
class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text)
    priority = db.Column(db.String(50), default='medium')  # low, medium, high, urgent
    status = db.Column(db.String(50), default='pending')  # pending, in_progress, review, completed, overdue
    start_date = db.Column(db.DateTime)
    due_date = db.Column(db.DateTime)
    completion_date = db.Column(db.DateTime)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    assignments = db.relationship('TaskAssignment', backref='task', lazy=True, cascade='all, delete-orphan')
    comments = db.relationship('TaskComment', backref='task', lazy=True, cascade='all, delete-orphan')
    attachments = db.relationship('TaskAttachment', backref='task', lazy=True, cascade='all, delete-orphan')

class TaskAssignment(db.Model):
    __tablename__ = 'task_assignments'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    assigned_at = db.Column(db.DateTime, default=datetime.utcnow)
    assigned_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    approved_by_rahbar = db.Column(db.Boolean, default=False)
    
    assigner = db.relationship('User', foreign_keys=[assigned_by], backref='assignments_created')

class TaskComment(db.Model):
    __tablename__ = 'task_comments'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='task_comments')

class TaskAttachment(db.Model):
    __tablename__ = 'task_attachments'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    filename = db.Column(db.String(300), nullable=False)
    filepath = db.Column(db.String(500), nullable=False)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

# 2. Avto Transport Module
class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    license_plate = db.Column(db.String(50), unique=True)
    vin_number = db.Column(db.String(100))
    color = db.Column(db.String(50))
    status = db.Column(db.String(50), default='active')  # active, maintenance, inactive
    last_maintenance = db.Column(db.DateTime)
    next_maintenance = db.Column(db.DateTime)
    driver_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    defects = db.Column(db.Text)
    notes = db.Column(db.Text)
    photo = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    driver = db.relationship('User', backref='vehicles')
    documents = db.relationship('VehicleDocument', backref='vehicle', lazy=True, cascade='all, delete-orphan')

class VehicleDocument(db.Model):
    __tablename__ = 'vehicle_documents'
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    document_type = db.Column(db.String(100))  # tech_passport, insurance, etc
    filename = db.Column(db.String(300))
    filepath = db.Column(db.String(500))
    expiry_date = db.Column(db.DateTime)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

# 3. Ijro Module (same as tasks but with extra features)
# Using Task model with additional features

# 4. Bino Module
class BuildingCategory(db.Model):
    __tablename__ = 'building_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.String(100))
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Building(db.Model):
    __tablename__ = 'buildings'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('building_categories.id'))
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.Text)
    area = db.Column(db.Float)
    floors = db.Column(db.Integer)
    rooms = db.Column(db.Integer)
    construction_year = db.Column(db.Integer)
    status = db.Column(db.String(50))
    description = db.Column(db.Text)
    photo = db.Column(db.String(200))
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    category = db.relationship('BuildingCategory', backref='buildings')
    documents = db.relationship('BuildingDocument', backref='building', lazy=True, cascade='all, delete-orphan')

class BuildingDocument(db.Model):
    __tablename__ = 'building_documents'
    id = db.Column(db.Integer, primary_key=True)
    building_id = db.Column(db.Integer, db.ForeignKey('buildings.id'), nullable=False)
    filename = db.Column(db.String(300))
    filepath = db.Column(db.String(500))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

# 5. Yashil Makon Module
class GreenSpaceCategory(db.Model):
    __tablename__ = 'greenspace_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.String(100))
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class GreenSpace(db.Model):
    __tablename__ = 'green_spaces'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('greenspace_categories.id'))
    name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.Text)
    area = db.Column(db.Float)
    plant_types = db.Column(db.Text)
    maintenance_schedule = db.Column(db.Text)
    status = db.Column(db.String(50))
    description = db.Column(db.Text)
    photo = db.Column(db.String(200))
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    category = db.relationship('GreenSpaceCategory', backref='green_spaces')

# 6. Quyosh Panellari Module
class SolarPanel(db.Model):
    __tablename__ = 'solar_panels'
    id = db.Column(db.Integer, primary_key=True)
    building_id = db.Column(db.Integer, db.ForeignKey('buildings.id'))
    panel_type = db.Column(db.String(100))
    capacity = db.Column(db.Float)  # kW
    installation_date = db.Column(db.DateTime)
    manufacturer = db.Column(db.String(200))
    model = db.Column(db.String(200))
    efficiency = db.Column(db.Float)
    status = db.Column(db.String(50))
    monitoring_url = db.Column(db.String(500))
    notes = db.Column(db.Text)
    photo = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    building = db.relationship('Building', backref='solar_panels')

# 7. Xodimlar Module (Using User model with additional info)

# 8. Tasks Module (Kanban style - using Task model)

# 9. Outsorsing Module
class OutsourcingService(db.Model):
    __tablename__ = 'outsourcing_services'
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(200), nullable=False)
    provider_name = db.Column(db.String(200))
    contract_number = db.Column(db.String(100))
    contract_date = db.Column(db.DateTime)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    service_description = db.Column(db.Text)
    cost = db.Column(db.Float)
    status = db.Column(db.String(50))
    contact_person = db.Column(db.String(200))
    contact_phone = db.Column(db.String(50))
    notes = db.Column(db.Text)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    documents = db.relationship('OutsourcingDocument', backref='service', lazy=True, cascade='all, delete-orphan')

class OutsourcingDocument(db.Model):
    __tablename__ = 'outsourcing_documents'
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('outsourcing_services.id'), nullable=False)
    filename = db.Column(db.String(300))
    filepath = db.Column(db.String(500))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

# 10. Tashkilotlar Module
class Organization(db.Model):
    __tablename__ = 'organizations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    logo = db.Column(db.String(200))
    employee_count = db.Column(db.Integer)
    building_area = db.Column(db.Float)
    description = db.Column(db.Text)
    address = db.Column(db.Text)
    phone = db.Column(db.String(50))
    email = db.Column(db.String(120))
    website = db.Column(db.String(200))
    vehicles = db.Column(db.Text)
    established_date = db.Column(db.DateTime)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# 11. Mehmonlar Module
class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(200), nullable=False)
    organization = db.Column(db.String(200))
    position = db.Column(db.String(200))
    arrival_date = db.Column(db.DateTime)
    departure_date = db.Column(db.DateTime)
    visit_purpose = db.Column(db.Text)
    reference_number = db.Column(db.String(100))
    services_provided = db.Column(db.Text)
    restaurant_expense = db.Column(db.Float)
    gift_expense = db.Column(db.Float)
    other_expenses = db.Column(db.Float)
    total_expense = db.Column(db.Float)
    notes = db.Column(db.Text)
    photo = db.Column(db.String(200))
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# 12. Tabriknomalar Module
class Celebration(db.Model):
    __tablename__ = 'celebrations'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))  # birthday, general
    title = db.Column(db.String(200), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date = db.Column(db.DateTime)
    gift_description = db.Column(db.Text)
    gift_value = db.Column(db.Float)
    message = db.Column(db.Text)
    status = db.Column(db.String(50))
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    recipient = db.relationship('User', foreign_keys=[recipient_id], backref='celebrations_received')
    creator = db.relationship('User', foreign_keys=[created_by], backref='celebrations_created')

# 13. Shartnomalar Module
class Contract(db.Model):
    __tablename__ = 'contracts'
    id = db.Column(db.Integer, primary_key=True)
    contract_number = db.Column(db.String(100), nullable=False)
    contract_date = db.Column(db.DateTime)
    company_name = db.Column(db.String(300))
    contract_amount = db.Column(db.Float)
    payment_date = db.Column(db.DateTime)
    status = db.Column(db.String(50))  # active, completed, pending, cancelled
    description = db.Column(db.Text)
    notes = db.Column(db.Text)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    documents = db.relationship('ContractDocument', backref='contract', lazy=True, cascade='all, delete-orphan')

class ContractDocument(db.Model):
    __tablename__ = 'contract_documents'
    id = db.Column(db.Integer, primary_key=True)
    contract_id = db.Column(db.Integer, db.ForeignKey('contracts.id'), nullable=False)
    filename = db.Column(db.String(300))
    filepath = db.Column(db.String(500))
    document_type = db.Column(db.String(50))  # pdf, excel, word
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

# Notifications
class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200))
    message = db.Column(db.Text)
    type = db.Column(db.String(50))  # task, reminder, alert
    is_read = db.Column(db.Boolean, default=False)
    link = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='notifications')

# User Activity Log
class ActivityLog(db.Model):
    __tablename__ = 'activity_logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    action = db.Column(db.String(200))
    module = db.Column(db.String(100))
    details = db.Column(db.Text)
    ip_address = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='activity_logs')
