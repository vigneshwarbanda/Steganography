import cv2

img = cv2.imread("encryptedImage.jpg")

password = input("Enter passcode for Decryption:")
original_password = "your_password_here"

c = {}
for i in range(255):
    c[i] = chr(i)

n = 0
m = 0
z = 0

message = ""

if password == original_password:
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")
