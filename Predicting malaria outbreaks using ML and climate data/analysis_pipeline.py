"""Detailed Python analysis scaffold for: Predicting malaria outbreaks using ML and climate data."""

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
    topic: str = "Predicting malaria outbreaks using ML and climate data"
    random_seed: int = 707
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
        n = 84
        half = n // 2
        group_a = np.random.normal(loc=38, scale=11, size=half)
        group_b = np.random.normal(loc=38 + (7), scale=11, size=n - half)
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
        """Render climate covariates against malaria case counts."""
        fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

        months = np.arange(1, 13)
        rainfall = 60 + 90 * np.clip(np.sin((months - 3) / 12 * 2 * np.pi), 0, None) + np.random.normal(0, 8, 12)
        cases = np.clip(20 + 1.8 * np.roll(rainfall, 1) + np.random.normal(0, 15, 12), 0, None)

        ax1 = axes[0]
        ax1.bar(months, rainfall, color="#42A5F5", alpha=0.7, label="Rainfall (mm)")
        ax2 = ax1.twinx()
        ax2.plot(months, cases, color="#C62828", marker="o", linewidth=2, label="Malaria cases")
        ax1.set_xlabel("Month")
        ax1.set_ylabel("Rainfall (mm)", color="#1565C0")
        ax2.set_ylabel("Malaria Cases", color="#C62828")
        ax1.set_title(f"{self.config.topic}\nClimate vs. Case Counts (simulated, 1-month lag)")
        ax1.set_xticks(months)

        axes[1].scatter(rainfall, cases, alpha=0.75, color="#2E7D32")
        coeffs = np.polyfit(rainfall, cases, 1)
        trend_x = np.linspace(rainfall.min(), rainfall.max(), 50)
        axes[1].plot(trend_x, np.polyval(coeffs, trend_x), color="black", linestyle="--")
        corr = np.corrcoef(rainfall, cases)[0, 1]
        axes[1].set_title(f"Rainfall\u2013Case Correlation: r = {corr:.2f}")
        axes[1].set_xlabel("Rainfall (mm)")
        axes[1].set_ylabel("Malaria Cases")
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
