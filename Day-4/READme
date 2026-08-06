
---

# 🌫️ Gaussian Blur

## 🎯 Objective

Gaussian Blur is used to **reduce image noise** and **smooth images** by applying a Gaussian filter. It is commonly used before edge detection, thresholding, and object detection to improve processing accuracy.

### ✨ Key Learning Outcomes

- ✅ Learn image smoothing using Gaussian Blur.
- ✅ Understand the effect of different kernel sizes.
- ✅ Reduce unwanted image noise.
- ✅ Prepare images for further image processing.

### 🔄 Workflow

```text
📷 Input Image
      │
      ▼
📂 Read Image
      │
      ▼
🌫️ Apply Gaussian Blur
      │
      ▼
🖥️ Display Blurred Image
      │
      ▼
💾 Save Output Image
```

### 🛠️ Function Used

```python
cv2.GaussianBlur(src, (kernel_width, kernel_height), sigmaX)
```

---

# ⚫ Binary Thresholding

## 🎯 Objective

Binary Thresholding converts a grayscale image into a **black-and-white image** by comparing each pixel against a threshold value. It is widely used in image segmentation and object detection.

### ✨ Key Learning Outcomes

- ✅ Learn Binary Thresholding.
- ✅ Understand threshold values.
- ✅ Convert grayscale images into binary images.
- ✅ Prepare images for contour detection.

### 🔄 Workflow

```text
📷 Input Image
      │
      ▼
📂 Read Image
      │
      ▼
⚫ Convert to Grayscale
      │
      ▼
⚪ Apply Binary Threshold
      │
      ▼
🖥️ Display Threshold Image
      │
      ▼
💾 Save Output Image
```

### 🛠️ Function Used

```python
cv2.threshold(src, threshold_value, max_value, cv2.THRESH_BINARY)
```

---

# 🎥 Motion Detection using OpenCV

## 🎯 Objective

This project detects **moving objects** from a live webcam feed by comparing the current frame with a reference frame. It uses Gaussian Blur, Binary Thresholding, Dilation, and Contour Detection to identify and highlight moving objects.

### ✨ Key Learning Outcomes

- ✅ Capture live video using a webcam.
- ✅ Convert frames to grayscale.
- ✅ Apply Gaussian Blur to reduce noise.
- ✅ Detect frame differences using `absdiff()`.
- ✅ Apply Binary Thresholding.
- ✅ Use Dilation to remove gaps.
- ✅ Detect contours of moving objects.
- ✅ Draw bounding rectangles around detected objects.
- ✅ Display real-time motion detection status.

### 🔄 Workflow

```text
🎥 Start Webcam
      │
      ▼
📸 Capture Video Frame
      │
      ▼
⚫ Convert to Grayscale
      │
      ▼
🌫️ Apply Gaussian Blur
      │
      ▼
🔍 Compare with First Frame (absdiff)
      │
      ▼
⚪ Apply Binary Threshold
      │
      ▼
🧱 Dilate Image
      │
      ▼
📐 Find Contours
      │
      ▼
📏 Check Contour Area
      │
      ▼
🟢 Draw Bounding Rectangle
      │
      ▼
📝 Display Motion Detection Status
      │
      ▼
🖥️ Show Live Video Feed
```


