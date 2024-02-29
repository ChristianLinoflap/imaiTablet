import pyodbc
import logging
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from PyQt5 import QtWidgets

class EnvironmentLoader:
    @staticmethod
    def load_env_variables():
        load_dotenv()

        # Access the variables
        db_server_name = os.getenv('DB_SERVER_NAME')
        db_name = os.getenv('DB_NAME')
        db_username = os.getenv('DB_USERNAME')
        db_password = os.getenv('DB_PASSWORD')

        return db_server_name, db_name, db_username, db_password

class DatabaseManager:
    # Database Initializations
    def __init__(self, server_name, database_name, username, password):
        self.server_name = server_name
        self.database_name = database_name
        self.username = username
        self.password = password

    # Database Connection
    def connect(self):
        driver_name = 'ODBC Driver 17 for SQL Server'
        connection_string = f"DRIVER={{{driver_name}}};SERVER={self.server_name};DATABASE={self.database_name};UID={self.username};PWD={self.password}"
        
        try:
            with pyodbc.connect(connection_string, timeout=5) as conn: 
                return conn
        except pyodbc.OperationalError as e:
            logging.error(f"Error connecting to the database: {e}")
            raise

    # LOGINMEMBER - Database User Authentication
    def authenticate_user(self, cursor, username, password):
        query = "SELECT UserClientId, FirstName, LastName FROM [dbo].[UserClient] WHERE Email = ? AND Password = ?"
        cursor.execute(query, username, password)
        return cursor.fetchone()
    
    # LOGINMEMBER - Get transaction id
    def get_transaction_id(self, user_client_id, reference_number):
        query = "SELECT TransactionId FROM [dbo].[Transaction] WHERE UserClientId = ? AND ReferenceNumber = ?;"
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, user_client_id, reference_number)
                result = cursor.fetchone()
                if result:
                    return result[0]
                else:
                    return None
    
    # LOGINMEMBER - Insert new transaction
    def insert_transaction(self, user_client_id, reference_number):
        try:
            japan_time = datetime.utcnow() + timedelta(hours=9)
            query = "INSERT INTO [dbo].[Transaction] (UserClientId, CreatedAt, UpdatedAt, TransactionStatus, ReferenceNumber) VALUES (?, ?, ?, 'On-going', ?);"
            with self.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, user_client_id, japan_time, japan_time, reference_number)
                    conn.commit()
        except Exception as e:
            error_message = f"An unexpected error occurred during transaction insertion: {e}"
            print(error_message)
            QtWidgets.QMessageBox.critical(None, "Error", error_message)

    # LOGINMEMBER - Update transaction details
    def update_transaction(self, user_client_id, reference_number):
        try:
            japan_time = datetime.utcnow() + timedelta(hours=9) 
            query = "UPDATE [dbo].[Transaction] SET UpdatedAt = ? WHERE UserClientId = ? AND ReferenceNumber = ?;"
            with self.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, japan_time, user_client_id, reference_number)
                    conn.commit()
        except Exception as e:
            error_message = f"An unexpected error occurred during transaction update: {e}"
            print(error_message)
            QtWidgets.QMessageBox.critical(None, "Error", error_message)


    # ITEMVIEW - Select Query for Product
    def get_product_details_by_barcode(self, cursor, barcode):
        try:
            query = """
                SELECT * FROM Fn_Products_BranchProducts (?)
            """
            cursor.execute(query, barcode)
            return cursor.fetchone()
        except Exception as e:
            error_message = f"An unexpected error occurred while fetching product details: {e}"
            print(error_message)
            return None
 
    # ITEMVIEW - Select Query for Advertisement Videos
    def get_advertisement_video_details_by_id(self, cursor, video_id):
        try:
            query = """
                SELECT AdvertisementVideoName, AdvertisementVideoURL
                FROM AdvertisementVideos
                WHERE AdvertisementVideoId = ?
            """
            cursor.execute(query, video_id)
            return cursor.fetchone()
        except Exception as e:
            error_message = f"An unexpected error occurred while fetching advertisement video details: {e}"
            print(error_message)
            return None
 
    # ITEMVIEW - Select Query for Products in Shopping List
    def checkProductInShoppingList(self, product_id):
        try:
            query = "SELECT TOP 1 * FROM ShoppingListDetail WHERE ProductId = ?"
            with self.connect() as conn, conn.cursor() as cursor:
                cursor.execute(query, product_id)
                return cursor.fetchone()
        except Exception as e:
            error_message = f"An unexpected error occurred while checking product in shopping list: {e}"
            print(error_message)
            return None

    # ITEMVIEW - Select Query and Update for Shopping List Detail
    def updateCartQuantity(self, product_id):
        try:
            query_select = "SELECT CartQuantity FROM ShoppingListDetail WHERE ProductId = ?"
            with self.connect() as conn, conn.cursor() as cursor:
                cursor.execute(query_select, product_id)
                current_cart_quantity = cursor.fetchone()[0]

                query_update = "UPDATE ShoppingListDetail SET CartQuantity = ? WHERE ProductId = ?"
                new_cart_quantity = current_cart_quantity + 1 
                cursor.execute(query_update, (new_cart_quantity, product_id))
                conn.commit()
        except Exception as e:
            error_message = f"An unexpected error occurred while updating cart quantity: {e}"
            print(error_message)


    # ITEMVIEW - Select Query for Save Transaction Detail
    def saveTransactionDetail(self, item_name, item_price, item_barcode, sales_trans, transaction_text):
        try:
            with self.connect() as conn, conn.cursor() as cursor:
                cursor.execute(
                    "{CALL sp_SaveTransDetail (?, ?, ?, ?, ?)}",
                    item_name, item_price, item_barcode, sales_trans, transaction_text
                )
                conn.commit()
                print(f"Transaction details for {item_name} saved successfully.")
        except pyodbc.Error as e:
            print(f"Error executing the stored procedure: {e}")
            conn.rollback()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            conn.rollback()

    # ITEMVIEW - Delete Query for Transaction Detail
    def deleteTransactionDetail(self, reference_number, barcode):
        try:
            query = "EXEC sp_DeleteTransDetailV2 @ReferenceNumber = ?, @BarcodeNumber = ?"
            with self.connect() as conn, conn.cursor() as cursor:
                cursor.execute(query, reference_number, barcode)
                conn.commit()
                print(f"Transaction detail with ReferenceNumber {reference_number} and Barcode {barcode} deleted successfully.")
        except pyodbc.Error as e:
            logging.error(f"Error executing the stored procedure to delete transaction detail: {e}")
            conn.rollback()
            raise 
        except Exception as e:
            logging.error(f"An unexpected error occurred while deleting transaction detail: {e}")
            conn.rollback()
            raise

    # SHOPPINGLIST - Populate Shopping List
    def populate_shopping_list(self, cursor, user_client_id):
        query = f"SELECT Name, Quantity, CartQuantity FROM dbo.vw_ProductShoppingListDetail WHERE UserClientID = {user_client_id}"

        try:
            cursor.execute(query)
            result = cursor.fetchall()

            shopping_list = []
            for item in result:
                name, quantity, cart_quantity = item.Name, item.Quantity, item.CartQuantity
                shopping_list.append({"name": name, "quantity": quantity, "cart_quantity": cart_quantity})

            return shopping_list

        except pyodbc.Error as e:
            print(f"Error fetching shopping list items: {e}")
            return None
    
    # ADVERTISEMENTVIDEOS - Get Advertisement Videos 
    def get_advertisement_videos_from_database(self):
        try:
            with self.connect() as conn, conn.cursor() as cursor:
                query = "SELECT AdvertisementVideoURL FROM AdvertisementVideos"
                cursor.execute(query)
                return [row.AdvertisementVideoURL for row in cursor.fetchall()]
        except Exception as e:
            logging.error(f"Error retrieving advertisement videos from the database: {e}")
            return []

    # SEARCH - Search Items
    def search_products(self, cursor, keyword):
        try:
            query = "SELECT Name, ProductWeight, Price FROM dbo.vw_Products_BranchProducts WHERE Name LIKE ?"
            cursor.execute(query, f"{keyword}%")
            return cursor.fetchall()
        except pyodbc.Error as e:
            logging.error(f"Error searching for products: {e}")
            return []
        except Exception as e:
            logging.error(f"An unexpected error occurred while searching for products: {e}")
            return []
        
    # SEARCH - Get All Times 
    def get_all_products(self, cursor):
        try:
            query = "SELECT Name, ProductWeight, Price FROM dbo.vw_Products_BranchProducts"
            cursor.execute(query)
            return cursor.fetchall()
        except pyodbc.Error as e:
            logging.error(f"Error fetching all products: {e}")
            return []
        except Exception as e:
            logging.error(f"An unexpected error occurred while fetching all products: {e}")
            return []