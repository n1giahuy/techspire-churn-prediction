RAW_DATA_PATH = '../data/raw/dataset.csv'
PROCESSED_DATA_PATH = '../data/processed/'
MODEL_PATH = '../models/'
FIGURES_PATH = '../reports/figures/'

TARGET_VARIABLE = 'churn_label'
RANDOM_STATE = 42

DROP_FEATURES = ['user_id']

NUMERICAL_FEATURES = [
    'age',
    'reg_days',
    'sessions_30d',
    'sessions_90d',
    'avg_session_duration_90d',
    'median_pages_viewed_30d',
    'search_queries_30d',
    'device_mix_ratio',
    'orders_30d',
    'orders_90d',
    'orders_2024',
    'aov_2024',
    'gmv_2024',
    'category_diversity_2024',
    'days_since_last_order',
    'discount_rate_2024',
    'refunds_count_2024',
    'refund_rate_2024',
    'support_tickets_2024',
    'avg_csat_2024',
    'emails_open_rate_90d',
    'emails_click_rate_90d',
    'review_count_2024',
    'avg_review_stars_2024',
    'rfm_recency',
    'rfm_frequency',
    'rfm_monetary'
]

CATEGORICAL_OHE_FEATURES = [
    'marketing_source',
    'app_version_major'
]

CATEGORICAL_TE_FEATURES = [
    'country',
    'city'
]
