# 金融智能风险管理代码

本目录存放讲座课件 `fdirm.md` 中全部 Python 示例代码，已整理成可独立运行的文件。

## 文件一览

| 课件位置 | 文件 | 说明 |
|---|---|---|
| 演示：基线模型代码 | `credit_default_baseline_logistic.py` | 逻辑回归基线，输出 AUC 与 KS |
| 演示：升级为树模型，并解释它 | `credit_default_lightgbm_shap.py` | LightGBM 加 SHAP 汇总图 |
| 图计算的基本工具箱 | `fraud_ring_graph_components.py` | 用图的连通分量找可疑团伙 |
| 异常检测：没有“坏样本”时怎么办？ | `anomaly_detection_isolation_forest.py` | 孤立森林给新样本打异常分 |
| 动手看（1/2）：智能体的“工具箱” | `credit_agent_tools.py` | 财务、司法、PD 评分三个函数和 `TOOLS` 表 |
| 动手看（2/2）：智能体的“工作流” | `credit_agent_due_diligence.py` | 尽调智能体：规划、调用工具、留痕、转人工 |

辅助文件：

| 文件 | 说明 |
|---|---|
| `credit_data.py` | 读取信用卡数据、分层划分训练/测试集、计算 KS。基线模型与树模型两个脚本共用 |
| `requirements.txt` | 依赖清单 |

## 运行前准备

1. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

2. 信用卡违约预测（两个 `credit_default_*.py`）需要先准备数据：
   - 数据集：UCI Machine Learning Repository，*Default of Credit Card Clients*
   - 下载后保存为本目录下的 `default_of_credit_card_clients.xls`

其余脚本不需要外部数据。

## 运行方法

在本目录下执行：

```bash
python credit_default_baseline_logistic.py     # 基线模型，约 AUC 0.70~0.72（以实际运行为准）
python credit_default_lightgbm_shap.py         # 树模型 + SHAP 解释
python fraud_ring_graph_components.py          # 输出：可疑团伙
python anomaly_detection_isolation_forest.py   # 输出各样本异常分，最后一个明显离群
python credit_agent_due_diligence.py           # 输出留痕日志、PD 与是否需人工复核
```

`credit_agent_tools.py` 与 `credit_data.py` 是被其他脚本导入的模块，不需要单独运行。

## 与课件的差异

代码逻辑与课件一致，为了能独立运行做了以下补充：

- **补齐示意变量。**
  - 智能体工作流里的 `llm` 与 `log`，用 `MockLLM` 和打印日志代替。接入真实大模型时，只需让对象提供 `plan()` 与 `write()` 两个方法。
  - 异常检测里的 `X_normal`、`X_new`，改用随机数据演示。
- **抽取公共模块。**课件中树模型页直接使用基线页的变量，独立文件里这部分数据读取与 KS 计算统一放在 `credit_data.py`。
- **增加入口函数。**各脚本都有 `main()`；图团伙脚本把查找逻辑拆成 `find_suspicious_rings()`，便于复用。
- **阈值提成常量。**人工复核阈值为 `HUMAN_REVIEW_PD = 0.05`，为示意值。

## 验证情况

| 脚本 | 状态 |
|---|---|
| `credit_agent_due_diligence.py` | 已运行：PD 0.13，需人工复核 |
| `fraud_ring_graph_components.py` | 已运行：输出由设备A与账户1~3组成的可疑团伙 |
| `credit_default_baseline_logistic.py` | 仅通过语法编译，未实际运行 |
| `credit_default_lightgbm_shap.py` | 仅通过语法编译，未实际运行 |
| `anomaly_detection_isolation_forest.py` | 仅通过语法编译，未实际运行 |

安装 scikit-learn、LightGBM、SHAP后可以实测。示例数字为教学虚构，不代表真实机构数据。

## 说明

- `slides.md` 中的代码块保持原样，没有改成引用外部文件，课件可单独使用。
- 如需让课件与代码文件保持同步，可改用 Slidev 的文件引入语法，例如在 `slides.md` 中写 `<<< ./code/credit_agent_tools.py`。



