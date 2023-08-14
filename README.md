# Image to PDF Converter
A simple command-line tool to combine multiple images into a single PDF file. We don't need any more unnecessary apps on our machines!

## Requirements
- Python 3.x
- Pillow

## Installation (Conda virtual environment)
1. Clone the repository: `git clone https://github.com/YourGitHubUsername/YourRepositoryName.git`
2. Navigate to the repository's directory: `cd image2pdf`
3. Create a virtual environment using Anaconda or Miniconda (recommended):
``` bash
conda create --name image2pdf python=3.8
conda activate image2pdf
```
4. Install the required package: `pip install Pillow`

## Installation (Standard Python)
1. Clone the repository: `git clone https://github.com/YourGitHubUsername/YourRepositoryName.git`
2. Navigate to the repository's directory: `cd image2pdf`
3. Install the required package: `pip install Pillow`
# Usage
Run the script using the following command, replacing the image paths with your own:
``` bash
python image2pdf.py -i image1.png image2.jpg -o output.pdf
```
## Recommendations
I recommend using [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) to manage dependencies and environments. They provide a simple way to create isolated Python environments that can be easily set up and torn down. This is entirely optional.

## License
Licensed under the MIT License. See `LICENSE.txt` in the project root for license information.