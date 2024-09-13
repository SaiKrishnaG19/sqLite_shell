import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_path= r"sqlite:///enter db path here !"
engine = create_engine(db_path)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    subscription = Column(Boolean, default=True)

class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)

class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    address = Column(String)

class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    order_date = Column(Date)
    status = Column(String)

class OrderItem(Base):
    __tablename__ = 'order_items'
    order_item_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(String, ForeignKey('orders.order_id'))
    product_id = Column(String, ForeignKey('products.product_id'))
    quantity = Column(Integer)
    price = Column(Float)

Base.metadata.create_all(engine)
