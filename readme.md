# 16-bit Gradient Image Generator from color pallette

Useful for gradient backgrounds in squarespace, when you dont want to inject css code.

This project contains a Python script for generating linear gradient images between two (out of five) random colors in 16-bit quality. The direction and midpoint of the gradients are also randomly chosen, making each gradient unique.

## Features

- Generation of 16-bit linear gradients. (8bits is easier but yields strong banding)
- Random choice of two colors out of defined pallette for the gradient.
- Randomly selected direction and midpoint for the gradient creation.
- Ability to generate multiple gradient images at once.

## Installation

To run this script, you need to have Python installed on your machine. Additionally, you'll require the following Python libraries:

- NumPy
- OpenCV-Python

You can install these libraries using pip:

```
pip install numpy opencv-python
```

## Usage

Simply clone or download the repository, and run the script `generate_gradient.py`:

```
python generate_gradient.py
```

By default, the script will generate 10 images of 1500x1000 pixels. You can modify the script to change the number of images, their dimensions, and the colors used for gradients.

## Contributing

Contributions are always welcome! Feel free to fork this repository, make changes, and submit pull requests.

## License

This project is open-source and available under the MIT License.
```

Adjust the filenames and paths as needed to align with your actual project structure and details.