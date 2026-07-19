import shap
import pandas as pd
class ModelExplainer:
  def __init__(self,model):
    self.explainer=shap.TreeExplainer(model)

  def explain(self,input_df):
    shap_values=self.explainer.shap_values(input_df)

    return shap_values