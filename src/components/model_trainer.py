# built in imports 
import os, sys 
from dataclasses import dataclass

# third party boosting libraries
from catboost import CatBoostRegressor
from xgboost import XGBRegressor

# third party libraries
from sklearn.ensemble import AdaBoostRegressor,GradientBoostingRegressor,RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

#custom imports 
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifact','model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_arr,test_arr):
        try:
            logging.info("splitting trainig and test input data")

            X_train,y_train,X_test,y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
            models = {
                "Random Forest":RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradinet Boosting": GradientBoostingRegressor(),
                "Ada Boosting":AdaBoostRegressor(),
                'Linear Regressor':LinearRegression(),
                "K neaerest neighbours regressor":KNeighborsRegressor(),}
            
            model_report:dict = evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model Found")
            logging.info(" Best model foudn on both training and testing data")

            save_object(file_path=self.model_trainer_config.trained_model_file_path,obj=best_model)

            prediction = best_model.predict(X_test)

            return r2_score(y_test,prediction)

        except Exception as e:
            raise CustomException(e,sys)
