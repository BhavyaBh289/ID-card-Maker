import qrcode
import os

# Function to create QR codes from a text file
def create_qr_codes_from_file(file_path, output_dir):
    # Read the file and extract values
    with open(file_path, 'r') as file:
        values = file.readlines()

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Generate QR codes for each value
    for i, value in enumerate(values):
        value = value.strip()  # Remove any extra whitespace or newlines

        # Skip empty lines
        if not value:
            continue

        # Create and save the QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(value)
        qr.make(fit=True)

        # Generate the QR code image
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image with a unique name
        img_name = os.path.join(output_dir, f"QR_{i+1}_{value}.png")
        img.save(img_name)

    print(f"QR codes saved to {output_dir}")

# Specify the input file and output directory
file_path = "1.csv"  # Replace with your file path
output_dir = "qr_codes"

# Generate QR codes
create_qr_codes_from_file(file_path, output_dir)
