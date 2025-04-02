import cv2
import torch
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")  # Ensure this model file is in your working directory

# Input video path
video_path = "C:/Users/hp/Downloads/traffic.mp4"

# Open video file
cap = cv2.VideoCapture(video_path)

# Get video properties
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for output video
fps = int(cap.get(cv2.CAP_PROP_FPS))  # Get FPS of input video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Output video writer
output_video_path = "C:/Users/hp/OneDrive/Desktop/2/output.mp4"
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# Check if video is opened
if not cap.isOpened():
    print("Error: Cannot open video file!")
    exit()

frame_count = 0  # Counter for frames

while True:
    ret, frame = cap.read()
    if not ret:
        print("🚀 Video processing completed!")
        break  # Exit when the video ends

    # Run YOLO detection
    results = model(frame)

    # Draw bounding boxes and labels on the frame
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get bounding box coordinates
            cls = int(box.cls[0])  # Get class ID
            conf = box.conf[0]  # Confidence score

            # Get class name
            label = model.names[cls]
            text = f"{label} ({conf:.2f})"

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Save the processed frame as an image (only first frame for reference)
    if frame_count == 0:
        cv2.imwrite("C:/Users/hp/OneDrive/Desktop/2/detected_frame.jpg", frame)

    # Write the frame to the output video
    out.write(frame)

    frame_count += 1

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Video saved at: {output_video_path}")
print(f"First detected frame saved at: C:/Users/hp/OneDrive/Desktop/2/detected_frame.jpg")
