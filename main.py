# Updated main.py

# Import necessary libraries
import barcode
from barcode.writer import ImageWriter
import sys

# Function to generate barcode

def generate_barcode(data):
    try:
        # Validate input data
        if not data:
            raise ValueError("Input data for the barcode cannot be empty.")

        # Generate barcode
        code128 = barcode.get('code128', data, writer=ImageWriter())
        file_path = code128.save('barcode')
        print(f"Barcode generated and saved to {file_path}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Main input validation before calling the barcode generation function

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <data>")
        sys.exit(1)
    data = sys.argv[1]
    generate_barcode(data)

if __name__ == '__main__':
    main()