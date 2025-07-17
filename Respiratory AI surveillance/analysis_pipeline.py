"""Detailed Python analysis scaffold for: Respiratory AI surveillance."""

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
    topic: str = "Respiratory AI surveillance"
    random_seed: int = 808
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
        n = 96
        half = n // 2
        group_a = np.random.normal(loc=45, scale=13, size=half)
        group_b = np.random.normal(loc=45 + (0.5), scale=13, size=n - half)
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
        """Render a surveillance signal with anomaly alerts and a weekly alert summary."""
        fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

        days = np.arange(0, 90)
        baseline = 40 + 8 * np.sin(days / 12)
        spike = 60 * np.exp(-0.5 * ((days - 55) / 6) ** 2)
        counts = np.clip(baseline + spike + np.random.normal(0, 4, size=len(days)), 0, None)
        threshold = baseline + 2 * counts.std()
        alerts = counts > threshold

        axes[0].plot(days, counts, color="#37474F", linewidth=1.5, label="Daily respiratory visits")
        axes[0].plot(days, threshold, color="#EF6C00", linestyle="--", label="Alert threshold")
        axes[0].scatter(days[alerts], counts[alerts], color="#C62828", zorder=5, label="Flagged anomaly")
        axes[0].set_title(f"{self.config.topic}\nSurveillance Signal with Anomaly Alerts")
        axes[0].set_xlabel("Day")
        axes[0].set_ylabel("Daily Visit Count")
        axes[0].legend(fontsize=8)
        axes[0].grid(alpha=0.3)

        weeks = np.arange(1, 13)
        alerts_per_week = np.random.poisson(lam=np.where(weeks > 7, 2.5, 0.3))
        axes[1].bar(weeks, alerts_per_week, color="#C62828", alpha=0.85)
        axes[1].set_title("Weekly Alert Counts (simulated)")
        axes[1].set_xlabel("Week")
        axes[1].set_ylabel("Number of Alerts")
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
