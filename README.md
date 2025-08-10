# 🛡️ SECURE DATA HIDING IN IMAGES USING STEGANOGRAPHY



#  OVERVIEW

This project implements image-based steganography to securely hide secret messages within digital images. It modifies pixel values to embed the message without noticeable distortion, ensuring secure and undetectable data transmission.


With this tool, users can:

* Encrypt messages into images.
* Decrypt hidden messages from images using a password.
* Ensure minimal distortion to the image quality.



# FEATURES


* Secure Data Transmission – Hide sensitive information within images.

* Minimal Image Distortion – The original image remains visually unchanged.

* Password Protection – Only users with the correct passcode can retrieve the message.

* Simple & Lightweight – Easy to use with a minimalistic approach.

* Supports Multiple Image Formats – Works with PNG, JPG, BMP, etc.

* Fast Encoding & Decoding – Real-time message encryption and decryption.



# TECHNOLOGIES USED

* Programming Language: Python
* Libraries: OpenCV (cv2), NumPy
* Platform: Windows
* Tools: Visual Studio Code



# INSTALLATION

Before running the scripts, make sure Python is installed on your system.

1) Install Dependencies

Run the following command to install the required Python libraries:
pip install opencv-python numpy



# USAGE

1) Encrypt a Message

To hide a secret message inside an image:

Encryption.py

Steps:

1) The script will ask for the image file (myimg.png).

2) Enter the secret message you want to hide.

3) Provide a password to encrypt the message securely.

4) The encrypted image will be saved as encryptedImage.png.


2) Decrypt the Message

To retrieve the hidden message from the encrypted image:

Decryption.py

Steps:

1) The script will read encryptedImage.png.

2) You must enter the correct password.

3) If the password matches, the hidden message will be displayed.



# EXAMPLE

Encryption Process:
Enter secret message: This is My project.
Enter a passcode: 4567
Encryption done. Saved as 'encryptedImage.png'.


Decryption Process:
Enter the passcode to decrypt: 4567
Enter the original passcode used: 4567
Decrypted Message: This is My project.



# PROJECT STRUCTURE

1. Secure Data Hiding in Images Using Steganography
2. Encryption.py      # Script to embed a secret message into an image
3. Decryption.py      # Script to extract the secret message from an image
4. encryptedImage.png # Image containing the hidden message
5. myimg.png          # Original image used for encryption
6. README.md          # Project documentation (this file)



# HOW IT WORKS (TECHNICAL EXPLANATION)

* The encryption script modifies the pixel values of an image to embed the message.
* The decryption script extracts the pixel-modified values and reconstructs the hidden message.
* A NULL (\0) terminator is added at the end of the message to mark the stopping point.



# FUTURE ENHANCEMENTS

1. Implement AES/DES encryption for added security.
2. Create a GUI interface for user-friendly interactions.
3. Support steganography for audio, video, and documents.



# LICENSE

This project is open-source and free to use.



# AUTHOR

Yash G Jadhav







