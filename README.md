# Sinhala TTS -  Training Pipeline

Sinhala Text-to-Speech (TTS) training pipeline built using Coqui TTS and the VITS architecture.

This project includes:

* Dataset preprocessing
* Sinhala vocabulary integration
* Model training
* Inference/testing pipeline

---

# Project Structure

```text
Sinhala-TTS/
│
├── data/
│   ├── train_final.txt
│   ├── val_final.txt
│   └── wavs/
│
├── models/
│   └── best_model_272.pth
│
├── config/
│   └── config.json
│
├── notebooks/
│   └── training.ipynb
│
├── inference/
│   └── test_inference.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# About This Pipeline

This pipeline was developed for training a Sinhala TTS model using Coqui TTS.

The notebook contains:

* dataset preparation
* metadata generation
* audio preprocessing
* Sinhala vocabulary setup
* training workflow
* testing/inference experiments

---

# How To Use This Pipeline

## 1. Prepare Your Dataset

Go to:

```text
notebooks/training.ipynb
```

Update all directory paths according to your own dataset locations.

Example:

* audio dataset paths
* metadata paths
* output paths
* wav folders

Then run the notebook cells step-by-step.

The notebook will:

* preprocess the dataset
* generate train_final.txt
* generate val_final.txt
* prepare audio paths
* configure Sinhala vocabulary
* generate config.json

---

# Dataset Format

Audio files should be placed inside:

```text
data/wavs/
```

Metadata style example:

```text
sample_001|මම සිංහලෙන් කතා කරනවා|මම සිංහලෙන් කතා කරනවා
```

Format:

```text
audio_file_name|transcription|normalized_transcription
```

---

# Sinhala Vocabulary Support

This project uses a manually defined Sinhala character vocabulary because Coqui TTS does not include full Sinhala grapheme support by default.

The vocabulary includes:

* Sinhala vowels
* Sinhala consonants
* Sinhala vowel modifiers
* Sinhala special characters
* English characters
* punctuation symbols

---

# Create Virtual Environment(in main directory)

## Windows

```bash
python -m venv tts_env
tts_env\Scripts\activate
```

---

# Install Dependencies

Install all required packages using:

```bash
pip install -r requirements.txt
```

---

# Start Training

Run the following command:

```bash
python -m TTS.bin.train_tts --config_path config/config.json
```

Training outputs will be saved inside:

```text
output/
```

Example trained model:

```text
best_model_272.pth
```

---

# Run Inference

To test the trained model:

```bash
python inference/test_inference.py
```

Generated audio will be saved as:

```text
output.wav
```

---

# Notes

* Developed using Coqui TTS VITS architecture
* Sinhala custom vocabulary manually integrated
* Supports Sinhala + English characters
* formatter style is important (sample_001|මම සිංහලෙන් කතා කරනවා|මම සිංහලෙන් කතා කරනවා).

---

# Output Files

Important output files:

```text
best_model_XXX.pth
```

Other temporary checkpoint/log files can be ignored or removed.

---

# Dependencies

All dependencies are listed in:

```text
requirements.txt
```

Install them before training.

---

# Author

Duovate
