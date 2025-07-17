# Detailed R analysis scaffold for: Spatiotemporal epidemic ML

suppressPackageStartupMessages({
  library(dplyr)
  library(ggplot2)
  library(readr)
})

set.seed(909)
data_path <- file.path("data", "dataset.csv")
output_dir <- "outputs"
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

if (file.exists(data_path)) {
  df <- read_csv(data_path, show_col_types = FALSE)
} else {
  n <- 75
  half <- floor(n / 2)
  group_a <- rnorm(half, mean = 52, sd = 9)
  group_b <- rnorm(n - half, mean = 52 + (-3), sd = 9)
  df <- tibble(
    time = 1:n,
    signal = c(group_a, group_b),
    group = c(rep("A", half), rep("B", n - half))
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
cat("Completed R analysis for topic: Spatiotemporal epidemic ML\n")
