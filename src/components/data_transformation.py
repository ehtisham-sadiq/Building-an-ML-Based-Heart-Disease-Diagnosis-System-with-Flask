import sys 
from dataclasses import dataclass 

import numpy as np 
import pandas as pd 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, RobustScaler

from src.exception import CustomException
from src.logger import logging
from sklearn.preprocessing import LabelEncoder
import os


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")
    
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        '''
        
        try:
            categorical_columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
            numerical_columns = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
            
            #for numeric columns

            numeric_transformer = Pipeline(steps=[
                ('numeric_imputer', SimpleImputer(strategy='median')),
                ('scaling', RobustScaler())
                    ])

            #for categorical columns 
            categorical_transformer = Pipeline(steps=[
                ('cat_imputer', SimpleImputer(strategy='most_frequent')),
                ('encoder', OneHotEncoder(handle_unknown='ignore')),
                ("cat_scalar",RobustScaler())
            ])
            
            
            logging.info(f"Categoical Columns :{categorical_columns}")
            logging.info(f"Numerical Columns :{numerical_columns }")
            
            preprocessor = ColumnTransformer(
                transformers=[
                ('num', numeric_transformer, numerical_columns),
                ('cat', categorical_transformer, categorical_columns),
                ])

            return preprocessor
        
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read.read(test_path)
            
            logging.info(f"Read train and test data completed")
            
            
            logging.info(f"Obtaining preprocessing object")
            
            preprocessing_obj = self.get_data_transformer_object()
            
            
            ## encoding of target column
            target_column = "target"
            le = LabelEncoder()
            train_df[target_column] = le.fit_transform(train_df[target_column])
            test_df[target_column] = le.fit_transform(test_df[target_column])
            
            
            ## data transformation of chol column
            #mood of the column
            column_name = "chol"
            train_value = train_df[column_name].mode()[0]
            test_value = test_df[column_name].mode()[0]
            
            

            train_df[column_name].replace({'nothing':train_value}, inplace=True)
            test_df[column_name].replace({'nothing':test_value}, inplace=True)
            
            train_df[column_name] = train_df[column_name].astype('float')
            test_df[column_name] = test_df[column_name].astype('float')
            
            
            
            ## separate train and test features
            
            input_features_train_df = train_df.drop(columns=[target_column], axis=1)
            target_feature_train_df = train_df[target_column]
            
            input_features_test_df = test_df.drop(columns=[target_column], axis=1)
            target_feature_test_df = test_df[target_column]
            
            
            
            logging.info(
                f"Applying preprocessing object on training and testing dataframes"
                )
            
            input_features_train_arr = preprocessing_obj.fit_transform(input_features_train_df)
            input_features_test_arr = preprocessing_obj.transform(input_features_test_df)
            
            

            
        except Exception as e:
            raise CustomException(e,sys)
    
            
        
         
