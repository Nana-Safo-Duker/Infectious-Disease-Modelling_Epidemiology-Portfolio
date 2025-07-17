"""Detailed Python analysis scaffold for: Spatiotemporal epidemic ML."""

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
    topic: str = "Spatiotemporal epidemic ML"
    random_seed: int = 909
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
        n = 75
        half = n // 2
        group_a = np.random.normal(loc=52, scale=9, size=half)
        group_b = np.random.normal(loc=52 + (-3), scale=9, size=n - half)
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
        """Render multi-region case trends and a space-time intensity heatmap."""
        fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

        regions = ["North", "East", "South", "West", "Central"]
        weeks = np.arange(0, 20)
        intensity = np.zeros((len(regions), len(weeks)))
        for i, _ in enumerate(regions):
            peak_week = 4 + i * 2.5
            intensity[i] = 40 * np.exp(-0.5 * ((weeks - peak_week) / 3) ** 2) + np.random.normal(0, 2, len(weeks))
        intensity = np.clip(intensity, 0, None)

        for i, region in enumerate(regions):
            axes[0].plot(weeks, intensity[i], marker="o", markersize=3, label=region)
        axes[0].set_title(f"{self.config.topic}\nCase Trends by Region")
        axes[0].set_xlabel("Week")
        axes[0].set_ylabel("Cases")
        axes[0].legend(fontsize=7, ncol=2)
        axes[0].grid(alpha=0.3)

        im = axes[1].imshow(intensity, aspect="auto", cmap="magma")
        axes[1].set_yticks(np.arange(len(regions)))
        axes[1].set_yticklabels(regions)
        axes[1].set_xlabel("Week")
        axes[1].set_title("Spatiotemporal Case Intensity Heatmap")
        fig.colorbar(im, ax=axes[1], fraction=0.046, pad=0.04, label="Cases")

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
