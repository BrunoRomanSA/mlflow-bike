import mlflow
import mlflow.sklearn
import optuna
from optuna.pruners import HyperbandPruner
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Configure MLflow
mlflow.set_tracking_uri("http://98.81.184.50:5000/")
mlflow.set_experiment("RandomForest_Classification")

with mlflow.start_run():
  mlflow.log_param("max_deph",10)

  mlflow.log_metric("rmse", 0.35)