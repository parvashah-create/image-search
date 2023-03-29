import torch
import torchvision.models as models
import torchvision.transforms as transforms
import numpy as np
from PIL import Image

class FeatureExtractor:
    def __init__(self):
        self.model = models.vgg16(weights='DEFAULT')
        self.model.classifier = self.model.classifier[:-1] # Remove the last layer (fc2) to get fc1 layer output
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)), # VGG must take a 224x224 img as an input
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

    def extract(self, img):
        """
        Extract a deep feature from an input image
        Args:
            img: from PIL.Image.open(path) or torchvision.datasets.ImageFolder

        Returns:
            feature (np.ndarray): deep feature with the shape=(4096, )
        """
        img_tensor = self.transform(img)
        img_tensor = torch.unsqueeze(img_tensor, 0) # (C, H, W) -> (1, C, H, W)
        with torch.no_grad():
            feature = self.model(img_tensor).squeeze() # (1, 4096) -> (4096, )
        return feature.numpy() / np.linalg.norm(feature.numpy()) # Normalize



