# Detailed R analysis scaffold for: Deep learning for malaria parasite detection

suppressPackageStartupMessages({
  library(dplyr)
  library(ggplot2)
  library(readr)
})

set.seed(42)
data_path <- file.path("data", "dataset.csv")
output_dir <- "outputs"
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

if (file.exists(data_path)) {
  df <- read_csv(data_path, show_col_types = FALSE)
} else {
  df <- tibble(
    time = 1:60,
    signal = rnorm(60, mean = 50, sd = 10),
    group = ifelse((1:60) %% 2 == 0, "A", "B")
  )
}

summary_tbl <- df %>%
  summarise(
    n = n(),
    mean_signal = mean(signal, na.rm = TRUE),
    median_signal = median(signal, na.rm = TRUE),
    sd_signal = sd(signal, na.rm = TRUE)
  )
write_csv(summary_tbl, file.path(output_dir, "summary_statistics_r.csv"))

ttest <- t.test(signal ~ group, data = df)
results <- tibble(
  t_statistic = unname(ttest$statistic),
  p_value = ttest$p.value
)
write_csv(results, file.path(output_dir, "t_test_result_r.csv"))

p <- ggplot(df, aes(x = time, y = signal, color = group)) +
  geom_line(alpha = 0.8) +
  geom_smooth(se = FALSE, method = "loess") +
  theme_minimal()

ggsave(file.path(output_dir, "signal_plot_r.png"), p, width = 9, height = 5, dpi = 150)
cat("Completed R analysis for topic: Deep learning for malaria parasite detection\n")
