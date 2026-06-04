# Real-Time Smile Detection with OpenCV

A simple and effective **real-time face and smile detection system** built using **Python** and **OpenCV**. This project uses Haar Cascade classifiers to detect faces and smiles from a webcam feed and automatically captures images when a smile is detected.

---

## Features

- Real-time webcam video processing
- Face detection using Haar Cascades
- Smile detection with adjustable sensitivity
- Automatic image capture when a smile is detected
- Lightweight and fast execution

---

## Technologies Used

- Python 3
- OpenCV (cv2)
- NumPy

---

## Project Structure

```
.
├── main.py
├── haarcascades/
│   ├── haarcascade_frontalface_default.xml
│   └── haarcascade_smile.xml
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/smile-detection-opencv.git
cd smile-detection-opencv
```

### 2. Install dependencies

```bash
pip install opencv-python numpy
```

### 3. Download Haar Cascade Files

Make sure you have the following files inside a `haarcascades/` directory:

- `haarcascade_frontalface_default.xml`
- `haarcascade_smile.xml`

You can download them from the official OpenCV GitHub repository:
https://github.com/opencv/opencv/tree/master/data/haarcascades

---

## Usage

Run the script:

```bash
python main.py
```

### Controls:

- Press `q` to quit the application

---

## How It Works

### 1. Face Detection

- Converts each frame to grayscale
- Uses Haar Cascade classifier to detect faces
- Draws bounding boxes around detected faces

### 2. Smile Detection

- Runs detection within each detected face region
- Uses stricter parameters to reduce false positives

### 3. Image Capture Logic

- When a smile is detected:
  - Saves an image every 5 detections
  - Prevents excessive duplicate captures

---

## Output

Captured images are saved in the root directory as:

```
smile_0.jpg
smile_5.jpg
smile_10.jpg
...
```

---

## Notes & Limitations

- Smile detection accuracy depends on lighting and camera quality
- Haar Cascades are fast but less accurate than modern deep learning models
- May produce false positives depending on facial features or expressions

---

## Future Improvements

- Replace Haar Cascades with deep learning models (e.g., CNNs, DNNs)
- Add logging or analytics for smile frequency
- Build a web interface for remote monitoring
- Improve smile detection accuracy using trained datasets

---

## Acknowledgements

- OpenCV for providing pre-trained Haar Cascade classifiers
- The open-source community for continuous inspiration

---

## License

This project is open-source and available under the MIT License.

---

## Author

Nelson Antonini

Software Developer

---

If you found this project useful, consider giving it a star.
