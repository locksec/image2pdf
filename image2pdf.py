"""
Image2PDF
Author: Ray Heffer (GitHub: rayheffer)
Description: A command-line tool to combine multiple images into a single PDF file
License: MIT
"""

import argparse
from PIL import Image

def images_to_pdf(image_files, output_pdf):
    """Combines given image files into a PDF

    :param image_files: List of image file paths
    :param output_pdf: Output PDF file name
    """
    print("Reading images:")
    images = [Image.open(image_file) for image_file in image_files]
    for image_file in image_files:
        print(f"  - {image_file}")

    # Convert images to RGB mode
    print("Converting images to RGB mode...")
    images_rgb = [image.convert('RGB') for image in images]

    # Save the first image and append the rest
    print(f"Combining images into {output_pdf}...")
    images_rgb[0].save(output_pdf, save_all=True, append_images=images_rgb[1:])
    print_ganbate()
    print(f"Successfully saved {output_pdf}!")

def main():
    """Main function to handle command-line arguments and call images_to_pdf"""
    parser = argparse.ArgumentParser(description="Combine images into a PDF.")
    parser.add_argument('-i', '--images', nargs='+', required=True, help='Paths to the images to combine')
    parser.add_argument('-o', '--output', default='output.pdf', help='Output PDF file name')
    args = parser.parse_args()

    images_to_pdf(args.images, args.output)

def print_ganbate():
    ganbate_ascii = """
 _____
/     \\
vvvvvvv  /|__/|
   I   /O,O   |
   I /_____   |      /|/|
  J|/^ ^ ^ \\  |    /00  |    _//|
   |^ ^ ^ ^ |W|   |/^^\\ |   /oo |
    \\m___m__|_|    \\m_m_|   \\mm_|
"""
    print(ganbate_ascii)

if __name__ == "__main__":
    main()