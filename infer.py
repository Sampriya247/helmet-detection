from ultralytics import YOLO
from pathlib import Path

model = YOLO(r"E:\Helmet detection\results\model_training 15e\weights\best.pt")

results = model.predict(
    source = r"E:\Helmet detection\detect",
    save=True,       
    imgsz=640,
    iou = 0.4,
    conf = 0.6,   
)

# Process and display results
for result in results:
    print("Bounding Boxes:")
    for box in result.boxes:
        # Extract details for each bounding box
        x1, y1, x2, y2 = box.xyxy[0]  
        conf = box.conf[0]            
        cls = box.cls[0]              
        print(f"Class: {cls}, Confidence: {conf:.2f}, Bounding Box: [{x1:.2f}, {y1:.2f}, {x2:.2f}, {y2:.2f}]")

save_dir = Path(results[0].save_dir) 
print(f"Predicted results saved at: {save_dir}")














# from ultralytics import YOLO

# # Load the trained model
# model = YOLO(r'C:\Users\Saksh\ultralytics\yoloenv\OK_NOTOK\yolo_mrp_training4\weights\best.pt')

# # Perform inference
# results = model.predict(
#     source=r'C:\Users\Saksh\ultralytics\yoloenv\OK_NOTOK\Dataset\test\images\test',
#     save=True,
#     imgsz=640
# )

# # Display results
# for result in results:
#     print(result.boxes)

