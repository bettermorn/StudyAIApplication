"""信用卡违约预测：LightGBM 树模型 + SHAP 解释（对应课件“升级为树模型，并解释它”）。

运行：python credit_default_lightgbm_shap.py
通常最重要的特征是最近一两个月的还款状态（PAY_0、PAY_2）。
"""
import lightgbm as lgb
import shap
from sklearn.metrics import roc_auc_score

from credit_data import ks_statistic, load_train_test


def main():
    X_tr, X_te, y_tr, y_te = load_train_test()

    gbm = lgb.LGBMClassifier(
        n_estimators=300,
        learning_rate=0.05,
        num_leaves=31,
        class_weight="balanced",
        random_state=42,
    )
    gbm.fit(X_tr, y_tr)
    p = gbm.predict_proba(X_te)[:, 1]
    print("AUC:", roc_auc_score(y_te, p), " KS:", ks_statistic(y_te, p))

    # 可解释：每个特征对风险分的贡献
    explainer = shap.TreeExplainer(gbm)
    sv = explainer.shap_values(X_te)
    shap.summary_plot(sv[1] if isinstance(sv, list) else sv, X_te)


if __name__ == "__main__":
    main()
