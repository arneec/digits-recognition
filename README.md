# Digits Recognition

## Description

A simple python program and sklearn library for digits recognitions.

This program uses a dataset for training from sklearn.datasets.load_digits(). From this training, prediction of new digits in any image format of any image size can be done. Might not be perfectly accurate since only 1797 (rows) data are used for training. For more accuracy use more data for training.

## Requirements
**Python: 3.5+**

## How to run the code?
The code and images are placed inside 'code' directory.

> Install all the requirements required to run the program. On the root directory of this project.

``` pip install -r requirements.txt ```

> Navigate to code directory.

``` cd code```

> Run the program.

```python main.py```


## Configuration

Configure the test image to predict by changing the variable ```TEST_IMAGE``` in code/config.py.

### Steps
- First place your image to code/images directory.
- Change the ```TEST_IMAGE``` attribute in code/config.py to match your newly placed image full name ( with extension ).
- Then run the main.py file as described above.

For thorough explanation of logic, watch the video [here](https://www.youtube.com/watch?v=hB6IlpqHy-o).
