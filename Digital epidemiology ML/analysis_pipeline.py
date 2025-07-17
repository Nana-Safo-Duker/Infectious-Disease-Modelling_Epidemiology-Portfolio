"""Detailed Python analysis scaffold for: Digital epidemiology ML."""

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
    topic: str = "Digital epidemiology ML"
    random_seed: int = 404
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
        n = 90
        half = n // 2
        group_a = np.random.normal(loc=42, scale=15, size=half)
        group_b = np.random.normal(loc=42 + (4), scale=15, size=n - half)
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
        """Render digital signal vs. reported cases and their correlation."""
        fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

        days = np.arange(0, 60)
        cases = np.clip(30 + 25 * np.sin(days / 10) + np.random.normal(0, 4, size=len(days)), 0, None)
        digital_signal = np.clip(0.8 * cases + np.random.normal(0, 6, size=len(days)) + 10, 0, None)

        ax1 = axes[0]
        ax2 = ax1.twinx()
        ax1.plot(days, cases, color="#1565C0", linewidth=2, label="Reported cases")
        ax2.plot(days, digital_signal, color="#EF6C00", linewidth=2, alpha=0.8, label="Digital signal index")
        ax1.set_xlabel("Day")
        ax1.set_ylabel("Reported Cases", color="#1565C0")
        ax2.set_ylabel("Digital Signal Index", color="#EF6C00")
        ax1.set_title(f"{self.config.topic}\nDigital Signal vs. Reported Cases")
        ax1.grid(alpha=0.3)

        axes[1].scatter(digital_signal, cases, alpha=0.7, color="#6A1B9A")
        coeffs = np.polyfit(digital_signal, cases, 1)
        trend_x = np.linspace(digital_signal.min(), digital_signal.max(), 50)
        axes[1].plot(trend_x, np.polyval(coeffs, trend_x), color="black", linestyle="--")
        corr = np.corrcoef(digital_signal, cases)[0, 1]
        axes[1].set_title(f"Correlation: r = {corr:.2f}")
        axes[1].set_xlabel("Digital Signal Index")
        axes[1].set_ylabel("Reported Cases")
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
