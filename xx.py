import torch

# Dosya yolunu doğru şekilde yaz
model_path = "C:/Users/Batuhan/PycharmProjects/face_reaging/model/best_unet_model.pth"

# Modeli yükle
model = torch.load(model_path)

# Modeli yükledikten sonra, gerekli işleme ve işlemleri yapabilirsin.
