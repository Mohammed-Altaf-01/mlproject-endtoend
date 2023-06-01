import os,sys,pickle,dill  # built in imports 

 # third party imports
from sklearn.metrics import r2_score 
from sklearn.model_selection import GridSearchCV

# custom imports
from src.exception import CustomException   
from src.logger import logging


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    


def evaluate_models(X_train,y_train,X_test,y_test,models,param):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]
            logging.info("searching for best parameters for our model")

            gs = GridSearchCV(model,para,cv=5)
            gs.fit(X_train,y_train)
            logging.info(f"got parameters for {list(models.values())[i]} as {gs.best_params_}")

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)


            y_test_pred = model.predict(X_test)
            test_model_score = r2_score(y_test,y_test_pred)
            logging.info(f"r2 score calculated as {test_model_score}")

            report[list(models.keys())[i]] = test_model_score
        return report 

    except Exception as e:
        raise CustomException(e,sys)


def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        return CustomException(e,sys)