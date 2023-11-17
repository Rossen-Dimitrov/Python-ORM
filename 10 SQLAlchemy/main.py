from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import DATABASE_URL

from models import User, Order

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

# create user
# with Session() as session:
#     new_user = User(username='john_doe', email='john@example.com')
#     session.add(new_user)
#     session.commit()


# retrieve all users
# with Session() as session:
#     users = session.query(User).all()
#     for user in users:
#         print(user.username, user.email)


# Query the user you want to update
# with Session() as session:
#     user_to_update = session.query(User).filter_by(username='john_doe').first()
# # Update the user's information
#     if user_to_update:
#         user_to_update.email = 'new_email@example.com'
#         session.commit()
#         print("User updated successfully")
#     else:
#         print("User not found")


# # Query the user you want to delete
# with Session() as session:
#     user_to_delete = session.query(User).filter_by(username='john_doe').first()
#     # Delete the user
#     if user_to_delete:
#         session.delete(user_to_delete)
#         session.commit()
#         print("User deleted successfully")
#     else:
#         print("User not found")

# with Session() as session:
#
#     new_user = User(username='john_doe', email='john@example.com')
#     new_user2 = User(username='doe_john', email='doe@example.com')
#     session.add(new_user)
#     session.add(new_user2)
#     session.commit()
#     print(f'import completed.')

# def populate_order_table():
#     with Session() as session:
#         session.add_all((Order(user_id=1), Order(user_id=2)))
#         session.commit()
#
# populate_order_table()

# def relationship_query():
#     with Session() as session:
#         orders = session.query(Order).order_by(Order.user_id.desc()).all()
#         if not orders:
#             print("No orders yet.")
#             return
#         for order in orders:
#             user = order.user
#             print(f'Order number {order.id}, Is completed: {order.is_completed}, Username: {user.username}')
#
# relationship_query()