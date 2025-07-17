"""Detailed Python analysis scaffold for: ML infectious disease review."""

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
    topic: str = "ML infectious disease review"
    random_seed: int = 606
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
        n = 48
        half = n // 2
        group_a = np.random.normal(loc=65, scale=7, size=half)
        group_b = np.random.normal(loc=65 + (2), scale=7, size=n - half)
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
        """Render a comparative bar chart of reviewed ML methods and studies over time."""
        fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

        methods = ["Logistic\nRegression", "Random\nForest", "XGBoost", "SVM", "Neural\nNetwork"]
        accuracy = np.array([0.78, 0.85, 0.88, 0.81, 0.90])
        f1 = np.array([0.75, 0.83, 0.86, 0.79, 0.89])

        x = np.arange(len(methods))
        width = 0.35
        axes[0].bar(x - width / 2, accuracy, width, label="Accuracy", color="#1565C0")
        axes[0].bar(x + width / 2, f1, width, label="F1-score", color="#EF6C00")
        axes[0].set_xticks(x)
        axes[0].set_xticklabels(methods, fontsize=8)
        axes[0].set_ylim(0, 1)
        axes[0].set_title(f"{self.config.topic}\nReviewed Method Comparison (illustrative)")
        axes[0].set_ylabel("Score")
        axes[0].legend(fontsize=8)
        axes[0].grid(alpha=0.3, axis="y")

        study_years = np.array([2018, 2019, 2020, 2021, 2022, 2023, 2024])
        study_counts = np.array([3, 5, 9, 14, 18, 22, 27])
        axes[1].bar(study_years, study_counts, color="#6A1B9A", alpha=0.85)
        axes[1].set_title("Reviewed Publications by Year (illustrative)")
        axes[1].set_xlabel("Year")
        axes[1].set_ylabel("Number of Studies")
        axes[1].grid(alpha=0.3, axis="y")

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
