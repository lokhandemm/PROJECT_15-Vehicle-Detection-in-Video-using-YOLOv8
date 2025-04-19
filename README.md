# 🚗 Vehicle Detection in Video using YOLOv8  
          
## 📌 Overview   
This project detects and tracks vehicles in a video using **YOLOv8** (You Only Look Once) and **OpenCV**. The detected objects are highlighted with bounding boxes, and the output video is saved.

- **Model Used:** YOLOv8  
- **Frameworks:** OpenCV, Ultralytics  
- **Output:** Processed video with vehicle detection  

---

## 📖 What is YOLO?  

**YOLO (You Only Look Once)** is a **deep learning-based object detection algorithm** known for its speed and accuracy. Unlike traditional object detection models that scan an image multiple times, YOLO processes the image in a **single forward pass** through a neural network, making it highly efficient.

### 🛠️ **Why We Used YOLOv8?**  
✅ **Speed:** YOLOv8 is optimized for real-time detection.  
✅ **Accuracy:** It provides high detection accuracy with minimal computation.  
✅ **Versatility:** Can detect multiple object classes, including vehicles, in a single frame.  
✅ **Efficiency:** Suitable for real-time applications like traffic surveillance and autonomous driving.  

In this project, **YOLOv8** allows us to efficiently detect vehicles in a video with high accuracy.

---

## ❓ What Does the `0.78` Above Each Vehicle Mean?  
Each detected object is labeled with a **confidence score**, like `0.78`.  

### 🔹 **Understanding the Confidence Score**  
- The number (`0.78`, for example) represents the **model's confidence** in its prediction.  
- It is a probability value ranging from **0 to 1** (or **0% to 100%**).  
- A higher confidence score means the model is more certain that the detected object belongs to a particular class (e.g., "car," "bus," "truck").  

Example interpretation:  
Car 0.78 → The model is 78% confident that the detected object is a car.

If the confidence is too low (e.g., `0.30`), it might be a **false detection**, and such objects can be filtered out.

---


# Install Required Libraries:

pip install ultralytics opencv-python torch torchvision

# Download YOLOv8 Model

The script automatically downloads yolov8n.pt, but you can manually download it from:
🔗 Ultralytics YOLOv8 Model



# WORKING:
Processed video saved at:
📍 C:/Users/hp/Downloads/output.mp4

First detected frame saved at:
📍 C:/Users/hp/Downloads/detected_frame.jpg

🎯 Features
✅ Detects vehicles (cars, buses, trucks, etc.)
✅ Draws bounding boxes with labels & confidence scores
✅ Saves the detected frame & processed video
✅ Uses YOLOv8 for fast and accurate detection

📸 Example Output is also provided for your understanding!
---

# 💡 To-Do / Future Improvements
🔹 Add real-time video detection using a webcam

🔹 Improve object tracking

🔹 Enhance accuracy with YOLOv8 fine-tuning

# 👨‍💻 Contributing
Feel free to fork this repo, make improvements, and submit a pull request!









