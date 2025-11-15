import pandas as pd 
import numpy as np 

def drop_weak_features(df, cols_to_drop): 
    """Drops specified columns from a Dataframe."""
    df = df.drop(columns = cols_to_drop, errors= 'ignore')
    print(f"Dropped {cols_to_drop}")
    return df 

def handle_skewness(df, cols_to_log_transform): 
    """
    Applies a log transformation (log1p) to specified columns to reduce right-skewness. s
    log1p is used to handle potential zero values gracefully.
    """
    for col in cols_to_log_transform: 
        df[col] = np.log1p(df[col])
    print(f"Applied log to transform to: {cols_to_log_transform}")
    return df

def create_interaction_features(df): 
    """
    Creates new features based on interactions between existing ones, inspired by hypotheses from the EDA.
    """
    # Hypothesis: Low satisfaction combined with high recency is a strong churn signal
    df['satisfaction_x_recency'] = df['avg_csat_2024'] * df['days_since_last_order']

    # Hypothesis: Value per session can indicate engagement quality
    df['gmv_per_session_90d'] = df['gmv_2024'] / (df['sessions_90d'] + 1)  

    print("Created interact features.")
    
    return df

def handle_outliers(df, column_list, lower_quantile = 0.01, upper_quantile= 0.99):
    """
    Caps outliers in specified columns using the quantile-based winsorizing method.
    """
    for col in column_list: 
        low = df[col].quantile(lower_quantile)
        high = df[col].quantile(upper_quantile)
        df[col] = np.clip(df[col], low, high)

    print(f"Handled outliers for {len(column_list)} columns.")
    return df 

def encode_categorical_features(train_df, test_df, high_cardinality_cols): 
    """Encodes high-cardinality categorical features using Frequency Encoding."""
    for col in high_cardinality_cols: 
        freq_map = train_df[col].value_counts(normalize=True).to_dict()

        train_df[col + '_freq'] = train_df[col].map(freq_map).fillna(0) 
        test_df[col + '_freq'] = test_df[col].map(freq_map).fillna(0)

        train_df = train_df.drop(columns = [col])
        test_df = test_df.drop(columns = [col])

    print(f"Applied Frequency Encoding to: {high_cardinality_cols}")
    return train_df, test_df