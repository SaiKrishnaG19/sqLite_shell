import random
from datetime import datetime, timedelta
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Product, Customer, Order, OrderItem
from custom_schema import User

db_path = r"sqlite:'enter db path here !"
engine =create_engine(db_path)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

def random_product(num_records):
    for _ in range(num_records):
        product = Product(
            product_name=fake.word(),
            description=fake.sentence(),
            price=round(random.uniform(10.0,1000.0),2),
            stock=random.randint(1,100)
        )
        session.add(product)
        session.commit()

def random_customer(num_records):
    user_ids = [user.user_id for user in session.query(User).all()]
    for _ in range(num_records):
        customer = Customer(
            user_id=random.choice(user_ids),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone_number=fake.phone_number(),
            address=fake.address(),           
        )
        session.add(customer)
        session.commit()

def random_order(num_records):
        customer_ids = [customer.customer_id for customer in session.query(Customer).all()]
        for _ in range(num_records):
            order = Order (
                customer_id=random.choice(customer_ids),
                order_date=fake.date_this_year(),
                status=random.choice(['Processing','Shipped','Delivered','Cancelled'])
            )
            session.add(order)
            session.commit()

def random_orderitem(num_records):
    order_ids = [order.order_id for order in session.query(Order).all()]
    product_ids = [product.product_id for product in session.query(Product).all()]
    for _ in range(num_records):
        order_item = OrderItem(
            order_id=random.choice(order_ids),
            product_id=random.choice(product_ids),
            quantity=random.randint(1,10),
            price=round(random.uniform(10.0,1000.0),2)
        )
        session.add(order_item)
        session.commit()

def main():
    table_map = {
        'products': random_product,
        'customers': random_customer,
        'orders': random_order,
        'order_items': random_orderitem,
    }

    print("Available tables: users, products, customers, orders,order_items")
    table = input("Enter tha table name you want to add data for: ").strip().lower()
    num_records = int(input(f"How many records do you want to generate for {table}: "))

    if table in table_map:
        table_map[table](num_records)
        print(f"{num_records} records have been generated for the {table} table.")
    else:
        print(f"Table {table} is not available in the database.")

if __name__=="__main__":
    main()
