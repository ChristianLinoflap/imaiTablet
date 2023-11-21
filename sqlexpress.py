import tkinter as tk
import pypyodbc as odbc

def search_username():
    username = entry.get()
    cursor.execute(f"SELECT * FROM [cart].[users].[Login] WHERE user_name='{username}'")
    rows = cursor.fetchall()
    for widget in root.winfo_children():
        widget.destroy()
    for i, row in enumerate(rows):
        label = tk.Label(root, text=f"Username: {row[1]}, Password: {row[2]}")
        label.grid(row=i, column=0)

# Set up the connection parameters
DRIVER_NAME = 'SQL Server'
SERVER_NAME = 'LAPTOP-771CLPE3\SQLEXPRESS'  # Replace this with your server name
DATABASE_NAME = 'cart'  # Replace this with your database name

# Establish a connection
connection_string = f"DRIVER={{{DRIVER_NAME}}};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};Trusted_Connection=yes;"
conn = odbc.connect(connection_string)
cursor = conn.cursor()

# Create GUI
root = tk.Tk()
root.title("Data from SQL Server")

# Add a label and entry for username search
tk.Label(root, text="Enter Username: ").grid(row=0, column=0)
entry = tk.Entry(root)
entry.grid(row=0, column=1)
search_button = tk.Button(root, text="Search", command=search_username)
search_button.grid(row=0, column=2)

root.mainloop()

# Close the cursor and connection
cursor.close()
conn.close()




# import pypyodbc as odbc

# # Set up the connection parameters
# DRIVER_NAME = 'SQL SERVER'
# SERVER_NAME = 'LAPTOP-771CLPE3\SQLEXPRESS'  # Replace this with your server name
# DATABASE_NAME = 'cart'  # Replace this with your database name

# # Establish a connection
# connection_string = f"DRIVER={{{DRIVER_NAME}}};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};Trust_Connection=yes;"
# conn = odbc.connect(connection_string)

# # Create a cursor from the connection
# cursor = conn.cursor()

# # Sample data for insertion
# sample_data = [('0070177118563','TWININGS','THIS SPICY INFUSION WILL WARM YOU UP','200.00')]

# # Inserting data into the table
# for data in sample_data:
#     cursor.execute("INSERT INTO [cart].[products].[Items] (barcode,pname,description,price) VALUES (?, ?, ?, ?)", data)

# # Commit the transaction
# conn.commit()

# # Close the cursor and connection
# cursor.close()
# conn.close()
