"""Detailed Python analysis scaffold for: TB transmission ML modeling."""

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
    topic: str = "TB transmission ML modeling"
    random_seed: int = 1010
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
        n = 68
        half = n // 2
        group_a = np.random.normal(loc=58, scale=10, size=half)
        group_b = np.random.normal(loc=58 + (5), scale=10, size=n - half)
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
        """Render simulated transmission compartments and risk-by-setting bars."""
        fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

        days = np.arange(0, 365)
        exposed = 500 * np.exp(-((days - 60) / 40) ** 2)
        infectious = 350 * np.exp(-((days - 110) / 50) ** 2)
        recovered = np.clip(np.cumsum(infectious) * 0.02, 0, 4000)

        axes[0].plot(days, exposed, label="Exposed (latent TB)", color="#F9A825")
        axes[0].plot(days, infectious, label="Infectious (active TB)", color="#C62828")
        axes[0].plot(days, recovered, label="Recovered/treated", color="#2E7D32")
        axes[0].set_title(f"{self.config.topic}\nSimulated Transmission Compartments")
        axes[0].set_xlabel("Day")
        axes[0].set_ylabel("Individuals")
        axes[0].legend(fontsize=8)
        axes[0].grid(alpha=0.3)

        settings = ["Household", "Healthcare\nfacility", "Workplace", "Community", "Congregate\nsetting"]
        risk = np.array([0.42, 0.31, 0.14, 0.09, 0.28])
        axes[1].bar(settings, risk, color="#6D4C41")
        axes[1].set_title("Estimated Transmission Risk by Setting (simulated)")
        axes[1].set_ylabel("Relative Transmission Risk")
        axes[1].tick_params(axis="x", labelsize=8)
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
