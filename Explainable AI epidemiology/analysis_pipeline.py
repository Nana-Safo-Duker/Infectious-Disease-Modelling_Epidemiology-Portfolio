"""Detailed Python analysis scaffold for: Explainable AI epidemiology."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats


@dataclass
class Config:
    topic: str = "Explainable AI epidemiology"
    random_seed: int = 505
    data_path: Path = Path("data") / "dataset.csv"
    output_dir: Path = Path("outputs")
    assets_dir: Path = Path("assets")


class ResearchReviewPipeline:
    def __init__(self, config: Config) -> None:
        self.config = config
        np.random.seed(self.config.random_seed)
        self.config.output_dir.mkdir(parents=True, exist_ok=True)
        self.config.assets_dir.mkdir(parents=True, exist_ok=True)

    def load_data(self) -> pd.DataFrame:
        if self.config.data_path.exists():
            return pd.read_csv(self.config.data_path)
        n = 54
        half = n // 2
        group_a = np.random.normal(loc=60, scale=10, size=half)
        group_b = np.random.normal(loc=60 + (-5), scale=10, size=n - half)
        return pd.DataFrame(
            {
                "time": np.arange(1, n + 1),
                "signal": np.concatenate([group_a, group_b]),
                "group": np.array(["A"] * half + ["B"] * (n - half)),
            }
        )

    def summarize_data(self, df: pd.DataFrame) -> pd.DataFrame:
        summary = df.describe(include="all").transpose()
        summary.to_csv(self.config.output_dir / "summary_statistics.csv", index=True)
        return summary

    def run_t_test(self, df: pd.DataFrame) -> Dict[str, float]:
        a = df.loc[df["group"] == "A", "signal"]
        b = df.loc[df["group"] == "B", "signal"]
        t_stat, p_val = stats.ttest_ind(a, b, equal_var=False)
        result = {"t_statistic": float(t_stat), "p_value": float(p_val)}
        pd.DataFrame([result]).to_csv(
            self.config.output_dir / "t_test_result.csv", index=False
        )
        return result

    def create_visualization(self, df: pd.DataFrame) -> Path:
        """Render SHAP-style feature importances and a partial-dependence-style curve."""
        fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

        features = [
            "Population density", "Prior case rate", "Vaccination coverage",
            "Temperature anomaly", "Travel volume", "Healthcare access", "Age >65 (%)",
        ]
        importances = np.array([0.28, 0.24, 0.19, 0.13, 0.09, 0.05, 0.02])
        order = np.argsort(importances)
        axes[0].barh(np.array(features)[order], importances[order], color="#00897B")
        axes[0].set_title(f"{self.config.topic}\nFeature Importance (simulated SHAP)")
        axes[0].set_xlabel("Mean |SHAP value|")

        feature_values = np.linspace(0, 100, 50)
        predicted_risk = 1 / (1 + np.exp(-0.08 * (feature_values - 50)))
        axes[1].plot(feature_values, predicted_risk, color="#D84315", linewidth=2)
        axes[1].fill_between(
            feature_values, predicted_risk - 0.05, predicted_risk + 0.05, color="#D84315", alpha=0.15
        )
        axes[1].set_title("Partial Dependence: Top Feature (Population Density)")
        axes[1].set_xlabel("Population Density (percentile)")
        axes[1].set_ylabel("Predicted Outbreak Risk")
        axes[1].grid(alpha=0.3)

        fig.tight_layout()
        output_path = self.config.assets_dir / "overview.png"
        fig.savefig(output_path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        return output_path

    def run(self) -> None:
        df = self.load_data()
        summary = self.summarize_data(df)
        ttest = self.run_t_test(df)
        chart_path = self.create_visualization(df)
        print(f"Topic: {self.config.topic}")
        print(f"T-test: t={ttest['t_statistic']:.4f}, p={ttest['p_value']:.4f}")
        print(f"Visualization saved to: {chart_path}")
        print(summary.head())


if __name__ == "__main__":
    ResearchReviewPipeline(Config()).run()
