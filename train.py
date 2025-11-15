from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8n.pt")

    model.train(
        data=r"E:\Helmet detection\data.yaml",
        epochs= 30,
        imgsz=416,

        # ↓ FIX GPU OOM ERRORS ↓
        batch=4,               # reduce batch size
        workers=2,             # reduce dataloader memory
        device=0,
        amp=False,             # disable mixed precision (solves CUDA errors)
        cache=False,

        # other settings
        augment=True,
        save_period=1,
        project=r"E:\Helmet detection\results",
        name="model_training3",
        pretrained=True
    )
    print("Training complete.")
