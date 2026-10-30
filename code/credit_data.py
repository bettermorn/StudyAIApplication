"""信用卡违约数据：读取、划分，以及风控常用的 KS 指标。

数据集：UCI "Default of Credit Card Clients"
下载后保存为本目录下的 default_of_credit_card_clients.xls
"""
from pathlib import Path

import pandas as pd
from sklearn.metrics import roc_curve
from sklearn.model_selection import train_test_split

DATA_FILE = Path(__file__).parent / "default_of_credit_card_clients.xls"
TARGET = "default payment next month"


def load_train_test(test_size=0.3, random_state=42):
    """读取数据并按违约标签分层划分训练集与测试集。"""
    df = pd.read_excel(DATA_FILE, header=1)
    y = df[TARGET]
    X = df.drop(columns=["ID", TARGET])
    return train_test_split(
        X, y, test_size=test_size, stratify=y, random_state=random_state
    )


def ks_statistic(y_true, score):
    """KS：好、坏客户累计分布的最大差距，越大区分能力越强。"""
    fpr, tpr, _ = roc_curve(y_true, score)
    return (tpr - fpr).max()
