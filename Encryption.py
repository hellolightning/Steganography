import cv2
import numpy as np

# Read the image
img = cv2.imread("myimg.png")

if img is None:
    print("Error: Image not found!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Append a NULL terminator to indicate the end of the message
msg += "\0"
msg_bytes = msg.encode("utf-8")

flat_img = img.flatten()

if len(msg_bytes) > len(flat_img):
    print("Error: Message too long to hide in the image!")
    exit()

# Embed the message bytes into the image
flat_img[:len(msg_bytes)] = np.frombuffer(msg_bytes, dtype=np.uint8)

encrypted_img = flat_img.reshape(img.shape) # Reshape image

# Save the encrypted image
cv2.imwrite("encryptedImage.png", encrypted_img)
print("Encryption done. Saved as 'encryptedImage.png'.")

# Open the encrypted image
cv2.imshow("Encrypted Image", encrypted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
