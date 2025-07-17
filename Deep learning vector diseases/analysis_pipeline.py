"""Detailed Python analysis scaffold for: Deep learning vector diseases."""

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
    topic: str = "Deep learning vector diseases"
    random_seed: int = 303
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
        n = 66
        half = n // 2
        group_a = np.random.normal(loc=48, scale=9, size=half)
        group_b = np.random.normal(loc=48 + (1), scale=9, size=n - half)
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
        """Render a training loss curve and ROC curve for the vector-disease risk classifier scaffold."""
        fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

        epochs = np.arange(1, 31)
        train_loss = 0.9 * np.exp(-epochs / 8) + 0.05 + np.random.normal(0, 0.01, size=len(epochs))
        val_loss = 0.9 * np.exp(-epochs / 10) + 0.08 + np.random.normal(0, 0.015, size=len(epochs))

        axes[0].plot(epochs, train_loss, marker="o", markersize=3, label="Train loss", color="#C62828")
        axes[0].plot(epochs, val_loss, marker="s", markersize=3, label="Validation loss", color="#455A64")
        axes[0].set_title(f"{self.config.topic}\nTraining Loss Curve (simulated)")
        axes[0].set_xlabel("Epoch")
        axes[0].set_ylabel("Loss")
        axes[0].legend(fontsize=8)
        axes[0].grid(alpha=0.3)

        fpr = np.linspace(0, 1, 100)
        tpr = np.clip(np.sqrt(fpr) * 0.9 + fpr * 0.1, 0, 1)
        auc = np.trapezoid(tpr, fpr)
        axes[1].plot(fpr, tpr, color="#1565C0", linewidth=2, label=f"ROC curve (AUC = {auc:.2f})")
        axes[1].plot([0, 1], [0, 1], linestyle="--", color="gray", label="Chance")
        axes[1].set_title("ROC Curve (simulated risk classifier)")
        axes[1].set_xlabel("False Positive Rate")
        axes[1].set_ylabel("True Positive Rate")
        axes[1].legend(fontsize=8, loc="lower right")
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
