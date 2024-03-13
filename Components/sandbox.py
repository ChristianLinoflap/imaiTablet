from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_receipt(file_path, products, total_price):
    c = canvas.Canvas(file_path, pagesize=letter)
    
    # Draw receipt header
    c.setFont("Helvetica", 16)
    c.drawString(100, 750, "Receipt")
    
    # Draw product list
    c.setFont("Helvetica", 12)
    y_position = 700
    for product, price in products:
        c.drawString(100, y_position, f"{product}: ${price:.2f}")
        y_position -= 20
    
    # Draw total price
    c.drawString(100, y_position - 20, f"Total: ${total_price:.2f}")
    
    c.save()

# Example usage:
products = [("Product 1", 10.00), ("Product 2", 20.00)]
total_price = sum(price for _, price in products)

# Debugging: Print the calculated total price
print("Total price:", total_price)

# Debugging: Check if products list is empty
print("Products:", products)

generate_receipt("receipt.pdf", products, total_price)
