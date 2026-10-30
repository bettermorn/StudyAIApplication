"""信用卡违约预测：逻辑回归基线模型（对应课件“演示：基线模型代码”）。

运行：python credit_default_baseline_logistic.py
基线结果通常 AUC 约 0.70~0.72，具体以实际运行为准。
"""
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

from credit_data import ks_statistic, load_train_test


def main():
    X_tr, X_te, y_tr, y_te = load_train_test()

    lr = LogisticRegression(max_iter=1000).fit(X_tr, y_tr)
    p = lr.predict_proba(X_te)[:, 1]

    print("AUC:", roc_auc_score(y_te, p), " KS:", ks_statistic(y_te, p))


if __name__ == "__main__":
    main()
