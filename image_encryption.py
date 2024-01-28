from PIL import Image
import os

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Create a new image to store the encrypted pixels
    encrypted_img = Image.new('RGBA', (width, height))

    # Encrypt each pixel in the image
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            if len(pixel) == 4:  # RGBA image
                r, g, b, a = pixel
                # Perform encryption using key
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                encrypted_img.putpixel((x, y), (r, g, b, a))
            else:  # RGB image
                r, g, b = pixel
                # Perform encryption using key
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                encrypted_img.putpixel((x, y), (r, g, b))

    return encrypted_img

def decrypt_image(encrypted_image, key):
    width, height = encrypted_image.size
    decrypted_img = Image.new('RGBA', (width, height))

    # Decrypt each pixel in the image
    for x in range(width):
        for y in range(height):
            pixel = encrypted_image.getpixel((x, y))
            if len(pixel) == 4:  # RGBA image
                r, g, b, a = pixel
                # Perform decryption using key
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                decrypted_img.putpixel((x, y), (r, g, b, a))
            else:  # RGB image
                r, g, b = pixel
                # Perform decryption using key
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                decrypted_img.putpixel((x, y), (r, g, b))

    return decrypted_img

if __name__ == "__main__":
    # Get the full path to the image file
    script_dir = os.path.dirname(os.path.realpath(__file__))
    image_filename = "your_image_here.jpg"
    image_path = os.path.join(script_dir, image_filename)

    key = 50

    # Encrypt the image
    encrypted_image = encrypt_image(image_path, key)
    encrypted_image_path = os.path.join(script_dir, "encrypted_image.png")
    encrypted_image.save(encrypted_image_path)
    print("Image encrypted and saved to:", encrypted_image_path)

    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image, key)
    decrypted_image_path = os.path.join(script_dir, "decrypted_image.png")
    decrypted_image.save(decrypted_image_path)
    print("Image decrypted and saved to:", decrypted_image_path)