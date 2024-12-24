import os
from src.mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.mlProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    ## Note: You can add different data transformation techniques such as Scaler, PCA and You can perform . 
    # All kinds of EDA in ML cycle here before passing this data to the model

    # I'm only adding train_test_splittin since this data is already cleaned up

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        #Split the data into training and test. (0.75, 0.25) split
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splitted data into testing and training data")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
        
