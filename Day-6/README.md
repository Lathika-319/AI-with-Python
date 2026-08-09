#  Object Detection and Tracking Based on Color

## 🎯 Objectives

- Learn how to detect objects based on their color.
- Understand the HSV color space.
- Create a color mask using `cv2.inRange()`.
- Remove unwanted noise using erosion and dilation.
- Detect objects using contours.
- Find the center and size of the detected object.
- Draw a circle around the detected object.
- Identify the object's position as **Left, Right, Front, or Stop**.

## 🔄 Workflow

```text
🎥 Camera
   │
   ▼
📸 Capture Frame
   │
   ▼
🌫️ Gaussian Blur
   │
   ▼
🎨 Convert BGR → HSV
   │
   ▼
🎯 Select Required Color
   │
   ▼
⚪ Create Color Mask
   │
   ▼
🧹 Erosion + Dilation
   │
   ▼
🔍 Find Contours
   │
   ▼
⭕ Find Center & Radius
   │
   ▼
📍 Check Object Position
   │
   ▼
⬅️ Left / ➡️ Right / ⬆️ Front / 🛑 Stop
   │
   ▼
🖥️ Display Output
```
