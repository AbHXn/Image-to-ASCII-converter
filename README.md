# ASCII Image Converter

This Python script converts an image into ASCII art and saves it as a `.txt` file. The conversion process includes resizing the image, converting it to grayscale, and mapping pixel intensities to ASCII characters.

---

## Features

* Converts images to grayscale.
* Resizes images to a fixed size for consistent ASCII output.
* Maps pixel intensities to a set of 20 ASCII characters.
* Supports square kernel averaging for better detail in ASCII representation.
* Automatically opens the resulting text file (Linux only).

---

## Requirements

* Python 3.x
* [NumPy](https://numpy.org/)
* [Pillow (PIL)](https://pillow.readthedocs.io/)
* [Matplotlib](https://matplotlib.org/)

Install dependencies with:

```bash
pip install numpy pillow matplotlib
```

---

## Usage

Run the script from the command line:

```bash
python ascii_converter.py <image_file>
```

* `<image_file>`: Path to the input image (e.g., `image.jpg`).

The output will be saved as a `.txt` file with the same name as the input image.

Example:

```bash
python ascii_converter.py photo.png
# Output: photo.txt
```

---

## Configuration

* `PIXEL_SIZE`: Size of the resized image (default: 512). Must be divisible by `KERNEL_SIZE`.
* `KERNEL_SIZE`: Size of the block used to calculate the average pixel value (default: 2).
* `ASCII_CODES`: List of ASCII characters used to map pixel intensities.

---

## Notes

* The script currently opens the output file using `xdg-open`, which works on Linux. On Windows or macOS, you may need to open the `.txt` file manually.
* Ensure that `PIXEL_SIZE % KERNEL_SIZE == 0`, otherwise the program will not run.

---

## License

This project is open-source and free to use.
