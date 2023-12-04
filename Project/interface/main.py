from Project.ml_logic.roboflow_load import load_data_from_roboflow
from Project.ml_logic.train import train_model
from Project.ml_logic.augmentation import augmentation_training_set, augmentation_validation_set
from Project.params import *
from epicureai.params import *


def main():
    # load_data_from_roboflow()
    # Need to update the paths to our data in data.yaml
    # augmentation_training_set()
    # print('✅ done with augmenting training set')
    # augmentation_validation_set()
    # print('✅ done with augmenting validation set')
    train_model(epochs=NUM_EPOCHS)

if __name__ == "__main__":
    main()
