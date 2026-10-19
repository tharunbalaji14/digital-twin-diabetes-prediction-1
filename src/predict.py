
import joblib
import pandas as pd
import shap
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "models" / "risk_model.pkl"
TRAIN_SCRIPT = ROOT / "src" / "train.py"

if not MODEL_PATH.exists():
    subprocess.run(
        [sys.executable, str(TRAIN_SCRIPT)],
        cwd=str(ROOT),
        check=True
    )

saved_data = joblib.load(MODEL_PATH)

model = saved_data["model"]
features = saved_data["features"]
explainer = shap.TreeExplainer(model)


def predict_risk(patient_data):
    input_df = pd.DataFrame([patient_data], columns=features)
    probability = float(model.predict_proba(input_df)[0][1])

    if probability >= 0.7:
        risk_level = "High"
    elif probability >= 0.4:
        risk_level = "Moderate"
    else:
        risk_level = "Low"

    shap_values = explainer.shap_values(input_df)

    if isinstance(shap_values, list):
        values = shap_values[1][0]
    elif len(shap_values.shape) == 3:
        values = shap_values[0, :, 1]
    else:
        values = shap_values[0]

    contributions = sorted(
        zip(features, values),
        key=lambda item: abs(float(item[1])),
        reverse=True
    )

    top_factors = [
        {
            "feature": feature,
            "contribution": float(value),
            "direction": (
                "increases model output"
                if value > 0
                else "decreases model output"
            )
        }
        for feature, value in contributions[:3]
    ]

    return {
        "risk_prediction": int(probability >= 0.5),
        "risk_probability": probability,
        "risk_level": risk_level,
        "top_factors": top_factors
    }
