# Probability Distributions

Gaussian and Binomial probability distributions

## Methods

### General distribution methods

- read_data_file(file_name)
- calculate_mean()
- calculate_stdev()
- pdf(x)
- __add__(other_distribution)
  other_distribution must be of the same type.
  
  Addition for binomials with different p values is not supported at the moment.
- __repr__()

### Gaussian distribution methods
- plot_histogram()

### Binomial distribution methods
- replace_stats_with_data()
- plot_bar()
