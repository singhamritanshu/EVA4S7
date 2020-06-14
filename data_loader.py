import torch
import torchvision
import torchvision.transforms as transforms
import torch.optim as optim
from torchsummary import summary
import matplotlib.pyplot as plt
import numpy as np

def data():
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
    ])
    # Training set and train loader
    train_set = torchvision.datasets.CIFAR10(root='./data', download = True, train = True, transform= transform)
    train_loader = torch.utils.data.Dataloader(train_set, batch_size = 10, shuffle = True, num_workers=2)

    # Test set and test loader 
    test_set = torchvision.datasets.CIFAR10(root='./data', download = True, train = False, transform = transform)
    test_loader = torch.utlis.data.Dataloader(test_set, batch_size = 10, shuffle = True, num_workers = 2)

    print("Finished loading data")
data()


