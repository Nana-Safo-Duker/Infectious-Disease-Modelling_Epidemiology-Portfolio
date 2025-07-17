"""Detailed Python analysis scaffold for: Deep learning for malaria parasite detection."""

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
    topic: str = "Deep learning for malaria parasite detection"
    random_seed: int = 202
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
        n = 72
        half = n // 2
        group_a = np.random.normal(loc=55, scale=12, size=half)
        group_b = np.random.normal(loc=55 + (6), scale=12, size=n - half)
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
        """Render training curves and a confusion matrix for the CNN classifier scaffold."""
        fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

        epochs = np.arange(1, 31)
        train_acc = 0.99 - 0.45 * np.exp(-epochs / 6) + np.random.normal(0, 0.01, size=len(epochs))
        val_acc = 0.96 - 0.45 * np.exp(-epochs / 7) + np.random.normal(0, 0.015, size=len(epochs))

        axes[0].plot(epochs, train_acc, marker="o", markersize=3, label="Train accuracy", color="#2E7D32")
        axes[0].plot(epochs, val_acc, marker="s", markersize=3, label="Validation accuracy", color="#EF6C00")
        axes[0].set_title(f"{self.config.topic}\nCNN Training Curve (simulated)")
        axes[0].set_xlabel("Epoch")
        axes[0].set_ylabel("Accuracy")
        axes[0].set_ylim(0.4, 1.0)
        axes[0].legend(fontsize=8)
        axes[0].grid(alpha=0.3)

        confusion = np.array([[915, 35], [42, 908]])
        im = axes[1].imshow(confusion, cmap="Blues")
        axes[1].set_xticks([0, 1])
        axes[1].set_yticks([0, 1])
        axes[1].set_xticklabels(["Parasitized", "Uninfected"])
        axes[1].set_yticklabels(["Parasitized", "Uninfected"])
        axes[1].set_xlabel("Predicted label")
        axes[1].set_ylabel("True label")
        axes[1].set_title("Confusion Matrix (simulated test set)")
        for i in range(2):
            for j in range(2):
                axes[1].text(
                    j, i, f"{confusion[i, j]:,}", ha="center", va="center",
                    color="white" if confusion[i, j] > 500 else "black",
                )
        fig.colorbar(im, ax=axes[1], fraction=0.046, pad=0.04)

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
