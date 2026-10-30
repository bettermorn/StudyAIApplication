"""异常检测：孤立森林（对应课件“异常检测：没有坏样本时怎么办？”）。

没有欺诈标签时，用正常样本训练，给新样本打“异常分”。
异常不等于欺诈，只是线索，仍需结合业务规则与人工核实。

运行：python anomaly_detection_isolation_forest.py
课件里的 X_normal、X_new 是示意变量，这里用随机数据演示。
"""
import numpy as np
from sklearn.ensemble import IsolationForest


def anomaly_scores(X_normal, X_new, contamination=0.01, random_state=42):
    """返回 X_new 的异常分，越大越异常。"""
    iso = IsolationForest(contamination=contamination, random_state=random_state)
    iso.fit(X_normal)
    return -iso.score_samples(X_new)


def main():
    rng = np.random.default_rng(42)
    X_normal = rng.normal(0, 1, size=(1000, 3))
    X_new = np.vstack([rng.normal(0, 1, size=(3, 3)), [[8, 8, 8]]])  # 最后一行是明显离群点

    for i, s in enumerate(anomaly_scores(X_normal, X_new)):
        print(f"样本 {i}: 异常分 {s:.3f}")


if __name__ == "__main__":
    main()
