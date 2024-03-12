import numpy as np  
import cv2  
import random

def generate_gradient_16bit_cv2(color1, color2, width, height):  
    """  
    Generates a linear gradient between two colors,
    positioned randomly by choice of direction and midpoint, in 16-bit.  
    """

    # Create gradient image  
    gradient = np.zeros((height, width, 3), dtype=np.uint16)

    # Randomly determine the direction and position of the gradient  
    dir_x = random.choice([-1, 1]) * random.random()  # Random X direction  
    dir_y = random.choice([-1, 1]) * random.random()  # Random Y direction

    # Normalize the direction  
    length = np.sqrt(dir_x**2 + dir_y**2)  
    dir_x /= length  
    dir_y /= length

    # Center of the gradient  
    center_x, center_y = width / 2, height / 2

    # Calculating the maximum distance from the center to the edge  
    max_dist = np.sqrt(center_x**2 + center_y**2)

    # Calculate color transitions  
    for y in range(height):  
        for x in range(width):  
            # Distance from point (x, y) to the center  
            dx, dy = x - center_x, y - center_y

            # Calculate position in the gradient  
            position = (dx * dir_x + dy * dir_y) / max_dist + 0.5  # Normalize to 0-1  
            
            # Limit position to stay within color transitions  
            position = max(min(position, 1), 0)

            # Determine the gradient color  
            color = [0, 0, 0]  
            for i in range(3):  
                # Now calculate for 16 Bit (0 to 65535)  
                color[i] = int((color1[i] * (1 - position) + color2[i] * position))

            # Add color to the gradient image  
            gradient[y, x, :] = color

    return gradient

def hex_to_rgb(hex_color):  
    """  
    Converts hexadecimal color code to an RGB tuple.  
    """  
    hex_color = hex_color.lstrip('#')  
    # Multiply by 257 for 16-bit adjustment  
    return tuple(int(hex_color[i:i+2], 16) * 257 for i in (0, 2, 4))

# Color palette  
colors_hex = ["FFFFFF", "8AB28A", "F15D51", "2E3C44", "000000"]  
colors_rgb = [hex_to_rgb(color) for color in colors_hex]

width, height = 1500, 1000  
num_images = 10

for i in range(num_images):  
    color1, color2 = random.sample(colors_rgb, 2)  
    img_data = generate_gradient_16bit_cv2(color1, color2, width, height)  
    # Save the gradient as an image  
    cv2.imwrite(f'gradient_background_16bit_{i+1:03d}.png', cv2.cvtColor(img_data, cv2.COLOR_RGB2BGR))

print(f'{num_images} 16-bit gradient images have been created.')