
# ViTAccidentDetection

## Project Setup

To get started with the ViTaccidentDetection project, follow these steps:

### 1. Create a Conda Environment

First, create a conda environment using the provided `environment.yaml` file:

```bash
conda env create -f environment.yaml
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

---

