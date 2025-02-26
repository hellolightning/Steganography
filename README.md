# SECURE DATA HIDING IN IMAGES USING STEGANOGRAPHY

This project implements image-based steganography to securely hide secret messages within images. The encryption process embeds message bytes by modifying pixel values without noticeable changes. The hidden message can later be extracted using a decryption script. This technique ensures secure data transmission while keeping the message undetectable. It provides a simple yet effective approach to concealing sensitive information within digital images.


## Features

* Secure data transmission: Encrypts and conceals data within images for safe communication.
* Minimal Image Distortion: Image quality remains almost unchanged after embedding data. 
* User friendly: Simple interface for easy encoding and decoding. 
* Support multiple formats: Works with various image file types like PNG, JPG, BMP. 
* Real-time steganography: Instantly encodes and decodes messages within images for quick and efficient data hiding.
* Simple and lightweight implementation using Python and OpenCV.



## Requirements

Make sure you have the following dependencies installed before running the scripts:

```sh
pip install opencv-python
```

## Usage

### 1. Encrypting a Message

To hide a secret message in an image:

```sh
python Encryption.py
```

#### Steps:

1. The script will ask for the image file (`myimg.png`).
2. Enter the secret message you want to hide.
3. Provide a password for security.
4. The encrypted image is saved as `encryptedImage.png`.
5. The password is stored in `passcode.txt`.

### 2. Decrypting a Message

To retrieve the hidden message from the encrypted image:

```sh
python Decryption.py
```

#### Steps:

1. The script reads `encryptedImage.png`.
2. You must enter the correct password.
3. If the password matches, the hidden message is displayed.
4. If the password is incorrect, access is denied.

## File Descriptions

- **Encryption.py** - Script to embed a secret message into an image.
- **Decryption.py** - Script to extract the secret message from the image.
- **encryptedImage.png** - Image containing the hidden message.
- **passcode.txt** - Stores the password required for decryption.
- **myimg.png** - Original image used for encryption.



## Example

### Encrypting:

```sh
Enter secret message: This is My Project
Enter a passcode: 4567
Encryption done. Saved as 'encryptedImage.png'.
```

### Decrypting:

```sh
Enter the passcode to decrypt: 4567
Enter the original passcode used: 4567
Secret message: This is My Project
```

## Notes

- The encryption process replaces pixel values with message bytes.
- The message length should not exceed the image size.
- A NULL (`\0`) byte is used as an end marker to detect the message termination.





## Author

**YASH G JADHAV**




