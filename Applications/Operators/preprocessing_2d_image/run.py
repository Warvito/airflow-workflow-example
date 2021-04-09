import numpy as np
import torch
from PIL import Image
from torchvision import transforms


def preprocess_image():
    print(f"Loading image: ")
    img = np.random.rand(256, 256, 3)
    img = Image.fromarray((img * 255).astype('uint8'), 'RGB')

    transform = transforms.Compose(
        [
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ]
    )

    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)
    path_preprocessed = "/tmp/preprocessed-img.pt"
    # torch.save(batch_t, path_preprocessed)
    print(f"Preprocessing done! Image save  at {path_preprocessed}")


if __name__ == '__main__':
    preprocess_image()
