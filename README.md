
# ViTaccidentDetection

## Project Setup

To get started with the ViTaccidentDetection project, follow these steps:

### 1. Create a Conda Environment

First, create a conda environment using the provided `environment.yml` file:

```bash
conda env create -f environment.yml
```

### 2. Download Model Weights

Next, download the model weights from the following [Google Drive link](https://drive.google.com/file/d/1FMyGcv0ICwDxROhaP0-G-hxd3oOiDyaA/view?usp=sharing). Create a `weights` directory in the project root and place the `.pth` and `.pt` files in this directory:

```bash
mkdir weights
# Add the downloaded .pth and .pt files here
```

## Running the Framework

### 1. Sample Videos

To test the framework, you can use the sample videos provided in the following directories:

- `/noacc` - Contains videos without accidents.
- `/inputsacc` - Contains videos with accidents.

### 2. Execute the Code

Navigate to the `/codes` directory and activate the conda environment:

```bash
cd codes
conda activate accident
```

Run the detection script with the desired video file path:

```bash
python run.py 'filepath'
```

Replace `'filepath'` with the path to the video file you want to analyze.

## Project Flowchart

Below is the flowchart of the ViTaccidentDetection project:

<img src="https://drive.google.com/uc?id=1rwKqou3WE0tmrKBsCWzuV7eI2UUMRcwM&export=view" alt="Project Flowchart" width="600"/>

## Processing Flow

This image shows the processing flow of the project:

<img src="https://drive.google.com/uc?id=1h9Uwbql1RZrZF2fi3ZgXf4GBz57UToCk&export=view" alt="Processing Flow" width="600"/>

## Results

The following image presents the results of our experiments, including False Alarm Rate (FAR) and Detection Rate (DAR):

<img src="https://drive.google.com/uc?id=19uxbV3ml92DXTb_NwARbp8zvTpBV48pY&export=view" alt="Results with FAR and DAR" width="600"/>

## Learn More

If you would like to know more about our project, you can read our paper [here](https://dx.doi.org/10.21203/rs.3.rs-3903862/v1).
