# 🎯 Crowd Monitoring System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Latest-red.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A real-time crowd monitoring system using YOLOv8 for person detection, featuring heatmap visualization, zone-based crowd density analysis, and intelligent movement recommendations.

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api-documentation)

</div>

---

## 📋 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Customization](#-customization)
- [Troubleshooting](#-troubleshooting)

---

## ✨ Features

- 🎥 **Real-time Person Detection** - Powered by YOLOv8 for accurate person detection
- 🗺️ **Interactive Heatmap** - Smooth gradient visualization showing crowd activity zones
- 📊 **Zone-based Analysis** - Customizable zones with individual crowd density monitoring
- 💡 **Smart Recommendations** - AI-driven suggestions for optimal crowd redistribution
- 📹 **Multiple Sources** - Support for webcam, uploaded videos, and IP cameras
- 🔌 **RESTful API** - Easy integration with external systems
- 📱 **Responsive Design** - Works on desktop and mobile devices
- ⚡ **Real-time Updates** - Live streaming with minimal latency

---


## 📁 Project Structure

```
crowd-monitoring-system/
│
├── 📄 app.py                          # Main Flask application entry point
├── ⚙️ config.py                       # Configuration settings
├── 📋 requirements.txt                # Python dependencies
├── 📖 README.md                       # This file
│
├── 🧠 models/
│   ├── __init__.py
│   └── yolo_detector.py              # YOLO model wrapper
│
├── 🛠️ utils/
│   ├── __init__.py
│   ├── heatmap.py                    # Heatmap generation logic
│   ├── zone_manager.py               # Zone management & density calculations
│   └── video_processor.py            # Video frame processing
│
├── 🌐 routes/
│   ├── __init__.py
│   ├── main_routes.py                # Main page routes
│   ├── video_routes.py               # Video feed routes
│   └── api_routes.py                 # API endpoints
│
├── 🎨 templates/
│   └── index.html                    # Frontend template
│
├── 📦 static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── 📂 uploads/                        # Uploaded videos directory (auto-created)
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Webcam or video files for monitoring
- (Optional) CUDA-capable GPU for better performance

### Step 1: Clone the Repository

```bash
git clone https://github.com/Dev-saurabhraj/Crowd-sense.git
cd Crowd-sense
```

### Step 2: Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```


## ⚙️ Configuration

Edit `config.py` to customize the system:

### Basic Settings

```python
# Crowd density thresholds
LOW_THRESHOLD = 8      # Below this = Low density
MEDIUM_THRESHOLD = 12  # Below this = Medium density
HIGH_THRESHOLD = 14    # Above this = High density

# Heatmap resolution (higher = smoother but slower)
GRID_ROWS = 32
GRID_COLS = 32
```

### Zone Configuration

```python
ZONES = {
    'A': {
        'coords': [0.0, 0.0, 0.33, 1.0],  # [x1, y1, x2, y2] normalized
        'color': (0, 0, 255),              # BGR color
        'count': 0,
        'density': 'low'
    },
    # Add more zones...
}
```

### Upload Settings

```python
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv', 'webm'}
MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB max
```

---

## 💻 Usage

### Start the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Using Webcam

1. Open your browser to `http://localhost:5000`
2. Click "Use Webcam" button
3. Allow camera access when prompted
4. View real-time detection and heatmap

### Using Video Files

1. Click "Upload Video" button
2. Select a video file (MP4, AVI, MOV, MKV, WEBM)
3. Wait for upload to complete
4. Video will start playing automatically

### Switching Between Sources

- **Webcam**: Click "Use Webcam" button
- **Video**: Upload a new video file

---

## 📡 API Documentation

### Get Zone Data

**Endpoint:** `GET /zone_data`

**Description:** Returns real-time zone statistics and recommendations

**Response:**
```json
{
  "zones": {
    "A": {
      "coords": [0.0, 0.0, 0.33, 1.0],
      "color": [0, 0, 255],
      "count": 5,
      "density": "low"
    },
    "B": {
      "coords": [0.33, 0.0, 0.66, 1.0],
      "color": [0, 255, 0],
      "count": 12,
      "density": "medium"
    },
    "C": {
      "coords": [0.66, 0.0, 1.0, 1.0],
      "color": [255, 0, 0],
      "count": 3,
      "density": "low"
    }
  },
  "total_people": 20,
  "recommendations": [
    "Move from Zone B to Zone C",
    "Move from Zone B to Zone A"
  ]
}
```

### Get Heatmap Data

**Endpoint:** `GET /heatmap_data`

**Description:** Returns heatmap grid data and overall density

**Response:**
```json
{
  "grid": [
    [0.0, 0.5, 1.2, ...],
    [0.3, 0.8, 0.6, ...],
    ...
  ],
  "people_count": 20,
  "density_level": "medium"
}
```

### Update Zones

**Endpoint:** `POST /update_zones`

**Description:** Update zone configuration dynamically

**Request Body:**
```json
{
  "zones": {
    "A": {
      "coords": [0.0, 0.0, 0.5, 1.0],
      "color": [0, 0, 255]
    },
    "B": {
      "coords": [0.5, 0.0, 1.0, 1.0],
      "color": [0, 255, 0]
    }
  }
}
```

**Response:**
```json
{
  "success": true,
  "zones": { ... }
}
```

### Video Feeds

**Live Video:** `GET /video_feed`  
**Heatmap Stream:** `GET /heatmap_feed`

Both endpoints return `multipart/x-mixed-replace` MJPEG streams.

---

## 🎨 Customization

### Modify Number of Zones

Edit `config.py`:

```python
ZONES = {
    'Zone1': {'coords': [0.0, 0.0, 0.25, 1.0], 'color': (255, 0, 0)},
    'Zone2': {'coords': [0.25, 0.0, 0.5, 1.0], 'color': (0, 255, 0)},
    'Zone3': {'coords': [0.5, 0.0, 0.75, 1.0], 'color': (0, 0, 255)},
    'Zone4': {'coords': [0.75, 0.0, 1.0, 1.0], 'color': (255, 255, 0)},
}
```

### Adjust Detection Sensitivity

Modify YOLO confidence threshold in `models/yolo_detector.py`:

```python
def detect(self, frame, conf_threshold=0.5):
    return self.model(frame, conf=conf_threshold)
```

### Change Heatmap Colors

Modify color gradient in `utils/heatmap.py`:

```python
def _get_gradient_color(self, intensity):
    # Customize your color scheme here
    if intensity < 0.33:
        return (255, 0, 0)      # Blue
    elif intensity < 0.66:
        return (0, 255, 255)    # Yellow
    else:
        return (0, 0, 255)      # Red
```

### Add New Features

The modular structure makes it easy to extend:

1. **Add new detectors**: Create new class in `models/`
2. **Add new visualizations**: Add functions to `utils/`
3. **Add new routes**: Create new route file in `routes/`

---

## 🐛 Troubleshooting

### Webcam Not Working

**Problem:** Camera not detected or black screen

**Solutions:**
- Check if webcam is properly connected
- Try different camera index in `config.py`:
  ```python
  WEBCAM_INDEX = 1  # Try 0, 1, 2...
  ```
- Grant camera permissions to browser
- Close other applications using the webcam

### Slow Performance

**Problem:** Low FPS or laggy video

**Solutions:**
- Reduce grid resolution in `config.py`:
  ```python
  GRID_ROWS = 16
  GRID_COLS = 16
  ```
- Use GPU acceleration (install CUDA + cuDNN)
- Close unnecessary applications
- Use a faster YOLO model variant

### Module Import Errors

**Problem:** `ModuleNotFoundError`

**Solutions:**
```bash
# Reinstall all dependencies
pip install -r requirements.txt --force-reinstall

# Check Python version
python --version  # Should be 3.8+

# Verify virtual environment is activated
which python  # Should point to venv
```

### Upload Not Working

**Problem:** Video upload fails

**Solutions:**
- Check file size (max 100MB by default)
- Verify file format is supported
- Check permissions on `uploads/` folder:
  ```bash
  chmod 755 uploads/
  ```
- Increase max upload size in `config.py`:
  ```python
  MAX_CONTENT_LENGTH = 200 * 1024 * 1024  # 200MB
  ```

### Port Already in Use

**Problem:** `Address already in use` error

**Solutions:**
```bash
# Find process using port 5000
lsof -i :5000  # macOS/Linux
netstat -ano | findstr :5000  # Windows

# Kill the process or use different port
# Edit app.py:
app.run(host='0.0.0.0', port=5001)
```



## 👏 Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) - Object detection model
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [OpenCV](https://opencv.org/) - Computer vision library
- [COCO Dataset](https://cocodataset.org/) - Training dataset

---

## 📞 Contact

**Your Name** - [@saurabhrajput]([https://twitter.com/yourtwitter](https://www.linkedin.com/in/saurabh-rajput-06b1a32b8/)) - saurabhraj2509@example.com

**Project Link:** [https://github.com/Dev-saurabhraj/Crowd-sense](https://github.com/Dev-saurabhraj/Crowd-sense)

---

<div align="center">

**Made with ❤️ by Saurabh Rajput**
**contributers - saubhagya sharma, paarth gupta, saurya thripathi**

If you found this project helpful, please consider giving it a ⭐!

</div>
