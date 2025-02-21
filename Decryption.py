import cv2
import numpy as np

# Load the encrypted image
img = cv2.imread("encryptedImage.png")

if img is None:
    print("Error: Encrypted image not found!")
    exit()

flat_img = img.flatten()

msg_bytes = []
for byte in flat_img:
    if byte == 0:  
        break
    msg_bytes.append(byte)

# Convert extracted bytes to a string
hidden_message = bytes(msg_bytes).decode("utf-8")

# Prompt user for passcode (for additional security)
password_input = input("Enter the passcode to decrypt: ")

# Check passcode (if stored securely elsewhere)
correct_password = input("Enter the original passcode used: ")  # In practice, store securely

if password_input == correct_password:
    print("\nDecrypted Message:", hidden_message)
else:
    print("\nError: Incorrect passcode! Decryption failed.")
