import pandas as pd

UPPERBOUND_DEFAULT: float = 0.9
LOWERBOUND_DEFAULT: float = 0.0
OUTLIER_FENCE_FACTOR: float = 1.5 # IQR inspired

def filter_outliers(
    dataframe: pd.DataFrame,
    column: str,
    upper_bound: float = UPPERBOUND_DEFAULT,
    lower_bound: float = LOWERBOUND_DEFAULT,
    factor: float = OUTLIER_FENCE_FACTOR,
) -> pd.DataFrame:
    """Return a `dataframe` with rows kept whose `column` values lie
    within the computed bounds.

    Bounds are computed from the specified lower and upper quantiles and a
    multiplicative factor on the inter-quantile range.

    Args:
        dataframe: DataFrame to filter.
        column: Name of the numeric column to use for outlier detection.
        upper_bound: Upper quantile (0 <= upper_bound <= 1).
        lower_bound: Lower quantile (0 <= lower_bound <= 1).
        factor: Multiplier applied to the inter-quantile range.

    Returns:
        A filtered `dataframe`.

    Raises:
        ValueError: If the column is missing or not numeric.
    """
    if column not in dataframe.columns:
        raise ValueError(f"Column {column!r} not found in the DataFrame.")

    col: pd.Series = dataframe[column]
    if not pd.api.types.is_numeric_dtype(col):
        raise ValueError(f"Column {column!r} must have a numeric dtype.")

    q_low, q_high = col.quantile([lower_bound, upper_bound])
    quantile_range: float = q_high - q_low
    lower_cutoff: float = q_low - factor * quantile_range
    upper_cutoff: float = q_high + factor * quantile_range

    filtered_df: pd.DataFrame = dataframe[(col >= lower_cutoff) & (col <= upper_cutoff)]
    return filtered_df