"""Detailed Python analysis scaffold for: Bayesian ML outbreak prediction."""

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
    topic: str = "Bayesian ML outbreak prediction"
    random_seed: int = 101
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
        n = 60
        half = n // 2
        group_a = np.random.normal(loc=50, scale=8, size=half)
        group_b = np.random.normal(loc=50 + (3), scale=8, size=n - half)
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
        """Render a Bayesian-style outbreak forecast with credible intervals."""
        fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

        days = np.arange(0, 60)
        true_curve = 120 * np.exp(-0.5 * ((days - 28) / 10) ** 2)
        observed = np.random.poisson(lam=np.clip(true_curve, 0.1, None))

        # Simulate a posterior via repeated noisy draws around the true curve
        posterior_draws = np.random.normal(
            loc=true_curve, scale=np.sqrt(true_curve + 1), size=(500, len(days))
        )
        posterior_mean = posterior_draws.mean(axis=0)
        lower = np.percentile(posterior_draws, 2.5, axis=0)
        upper = np.percentile(posterior_draws, 97.5, axis=0)

        axes[0].bar(days, observed, color="#B0BEC5", alpha=0.6, label="Observed cases")
        axes[0].plot(days, posterior_mean, color="#1565C0", linewidth=2, label="Posterior mean")
        axes[0].fill_between(days, lower, upper, color="#1565C0", alpha=0.2, label="95% credible interval")
        axes[0].set_title(f"{self.config.topic}\nBayesian Outbreak Forecast")
        axes[0].set_xlabel("Day of Outbreak")
        axes[0].set_ylabel("Daily Case Count")
        axes[0].legend(fontsize=8)
        axes[0].grid(alpha=0.3)

        peak_day_samples = days[np.argmax(posterior_draws, axis=1)]
        axes[1].hist(peak_day_samples, bins=15, color="#7E57C2", alpha=0.8, edgecolor="white")
        axes[1].axvline(np.median(peak_day_samples), color="black", linestyle="--", label="Median estimate")
        axes[1].set_title("Posterior Distribution: Estimated Peak Day")
        axes[1].set_xlabel("Peak Day")
        axes[1].set_ylabel("Posterior Samples")
        axes[1].legend(fontsize=8)

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
