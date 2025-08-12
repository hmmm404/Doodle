# Doodle Recognition System

This project implements a convolutional neural network (CNN) to identify and classify hand-drawn doodles using The Quick, Draw! Dataset. The system trains and validates the model to recognize patterns across diverse categories of drawings.

---

## Contributors

24m0857 (Skarma Yangskit)
24m0855 (Ritika Jaiswal)
24m0856 (Pratik Man Shah)
24m0789 (Omi Kakadiya)

## Requirements

The following dependencies are necessary to run the project:

- Python 3.7 or higher
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Requests
- Urllib
- Glob
- Random

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone <https://github.com/hmmm404/Doodle>
   cd <Doodle>
   ```
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Data Preparation

- 1. Download the dataset from The Quick, Draw! Dataset.
- 2. Place the dataset in the data/ directory within the project folder.

## Running the Project

1. **Launch the Jupyter Notebook environment**:
   ```bash
   jupyter notebook
   ```
2. **Open the notebook file**:
   ```bash
   pred.ipynb
   ```
3. **Run all cells sequentially to**:
   - Preprocess data.
   - Train and validate the CNN model.
   - Evaluate model performance.

## Parameters

| Parameter       | Description                                    | Default Value |
| --------------- | ---------------------------------------------- | ------------- |
| `batch_size`    | Number of samples processed per training batch | 32            |
| `epochs`        | Number of training epochs                      | 10            |
| `learning_rate` | Learning rate for the optimizer                | 0.001         |
| `input_shape`   | Dimensions of input images                     | (28, 28, 1)   |
| `num_classes`   | Number of doodle categories                    | 345           |
| `train_split`   | Percentage of data used for training           | 80%           |
| `val_split`     | Percentage of data used for validation         | 20%           |

## Model summary

| Layer (Type)             | Output Shape       | Param #       |
| ------------------------ | ------------------ | ------------- |
| `conv2d_9` (Conv2D)      | (None, 28, 28, 16) | 160           |
| `max_pooling2d_9`        | (None, 14, 14, 16) | 0             |
| `conv2d_10` (Conv2D)     | (None, 14, 14, 32) | 4,640         |
| `max_pooling2d_10`       | (None, 7, 7, 32)   | 0             |
| `conv2d_11` (Conv2D)     | (None, 7, 7, 64)   | 18,496        |
| `max_pooling2d_11`       | (None, 3, 3, 64)   | 0             |
| `flatten_3` (Flatten)    | (None, 576)        | 0             |
| `dense_6` (Dense)        | (None, 128)        | 73,856        |
| `dense_7` (Dense)        | (None, 345)        | 44,505        |
| **Total params**         | **141,657**        | **553.35 KB** |
| **Trainable params**     | **141,657**        | **553.35 KB** |
| **Non-trainable params** | **0**              | **0.00 Byte** |

## Acknowledgments

- Dataset: The Quick, Draw! Dataset
- Libraries Used: TensorFlow, Keras, NumPy, Matplotlib
