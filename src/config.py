RAW_DATA_PATH = '../data/raw/dataset.csv'
PROCESSED_DATA_PATH = '../data/processed/'
MODEL_PATH = '../outputs/models/'            
FIGURES_PATH = '../outputs/reports/figures/' 

TARGET_VARIABLE = 'churn_label'
RANDOM_STATE = 42

TEST_SET_SIZE = 0.2
VALIDATION_SET_SIZE = 0.1875

INITIAL_COLS_TO_DROP = [
    'user_id',
    'marketing_source',
    'app_version_major'
]


COLS_TO_LOG_TRANSFORM = [
    'gmv_2024',
    'sessions_90d'
]

HIGH_CARDINALITY_COLS = [
    'country',
    'city'
]

NUMERICAL_COLS_FOR_OUTLIERS = [
    'age',
    'reg_days',
    'avg_session_duration_90d',
    'median_pages_viewed_30d',
    'search_queries_30d',
    'device_mix_ratio',
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
    'session_decay_ratio',
    'order_decay_ratio',
    'session_to_order_conversion',
    'gmv_per_session'
]

MODELS_TO_TRAIN = ['LogisticRegression', 'XGBoost', 'LightGBM']

MODEL_PARAM_GRIDS = {
    'LogisticRegression': {
        'C': [0.1, 1.0, 10.0],
        'class_weight': ['balanced'] 
    },
    'XGBoost': {
        'n_estimators': [100, 200],
        'max_depth': [5, 7],
        'learning_rate': [0.05, 0.1],
        'scale_pos_weight': [3] 
    },
    'LightGBM': {
        'n_estimators': [100, 200],
        'learning_rate': [0.05, 0.1],
        'num_leaves': [31, 50],
        'class_weight': ['balanced']
    }
}