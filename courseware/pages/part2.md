---
layout: section
---

# 2 智能风控建模

从评分卡到机器学习，一次完整的信用风险建模

---

# 评分卡：风控领域的“经典艺术”

<div class="grid grid-cols-2 gap-6">

<div>

**思路**

1. 把连续变量**分箱**（如年龄分成 4 段）
2. 用 **WOE** 把每一箱换成“风险度量”
3. 用 **逻辑回归** 拟合违约概率
4. 把概率换算成**分数**（越高越好）

**为什么银行爱用？**

- 每个变量的贡献一目了然
- 监管要求可解释
- 稳定、好上线、好审计

</div>

<div>

**WOE 与 IV**

$$
WOE_i = \ln\frac{\text{好客户占比}_i}{\text{坏客户占比}_i}
$$

$$
IV = \sum_i (\text{好占比}_i-\text{坏占比}_i)\times WOE_i
$$

| IV 值 | 变量预测力 |
|---|---|
| 0.02 以下 | 几乎没用 |
| 0.02 ~ 0.1 | 弱 |
| 0.1 ~ 0.3 | 中等 |
| 0.3 以上 | 强 |

</div>

</div>

---

# 一张小例子：看懂 WOE

假设 1000 个客户（好 900，坏 100），按“近 6 个月逾期次数”分组：

| 分箱 | 好客户 | 坏客户 | 好占比 | 坏占比 | WOE |
|---|---|---|---|---|---|
| 0 次 | 600 | 30 | 66.7% | 30% | **+0.80** |
| 1 次 | 200 | 30 | 22.2% | 30% | **−0.30** |
| 2 次及以上 | 100 | 40 | 11.1% | 40% | **−1.28** |

<v-click>

<div class="mt-4 p-3 bg-yellow-50 rounded">

**读法**：WOE 为正 → 这一箱比平均水平“更好”；为负 → 更差。<br/>
逾期越多，WOE 越负，评分越低，结论符合业务直觉。

</div>

</v-click>

<!--
【25:00】用计算器验证：ln(0.667/0.30)=0.80；ln(0.222/0.30)=-0.30；ln(0.111/0.40)=-1.28。让学生自己心算一格。
-->

---

# 从概率到分数

逻辑回归输出违约概率 $p$，评分卡把它线性映射为分数：

$$
\text{Score} = A - B\ln\left(\frac{p}{1-p}\right)
$$

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

**约定三个参数**

- 基准分：如 600 分
- 基准好坏比：如 20:1 时 600 分
- **PDO**（Points to Double the Odds）：好坏比翻倍所需加分，如 50

</div>

<div class="p-3 bg-blue-50 rounded">

**直观理解**

每多 50 分，客户“更好”的可能性翻一倍。<br/>
600 分 → 好:坏 = 20:1<br/>
650 分 → 好:坏 = 40:1<br/>
700 分 → 好:坏 = 80:1

</div>

</div>

---

# 机器学习升级：从线性走向非线性

<div class="grid grid-cols-2 gap-6">

<div>

| 对比 | 评分卡 | 梯度提升树 |
|---|---|---|
| 代表 | 逻辑回归 | XGBoost / LightGBM |
| 特征 | 几十个 | 成百上千个 |
| 非线性/交叉 | 需手工 | 自动学习 |
| 效果 | 稳 | 通常更高 |
| 可解释 | **天然强** | 需 SHAP 等工具 |
| 上线门槛 | 低 | 较高 |

</div>

<div>

**现实中的做法**

- 评分卡与树模型**并存**：核心准入用评分卡，其他场景用树模型
- 树模型做特征筛选，再喂给评分卡
- 用 SHAP 给出“拒绝原因码”，满足监管要求

<div class="mt-4 p-3 bg-orange-50 rounded text-sm">
没有“最好”的模型，只有<b>在收益、稳定性、可解释性之间取得平衡</b>的模型。
</div>

</div>

</div>

---

# 怎么评价一个风控模型？

<div class="grid grid-cols-2 gap-6">

<div>

**区分能力**

- **AUC**：随机抽一个坏客户和一个好客户，模型给坏客户打更高风险分的概率。0.5 = 瞎猜，1 = 完美
- **KS**：好、坏客户累计分布的最大差距。行业经验：0.3 以上可用，0.4 以上较好

**稳定性**

- **PSI**：新旧样本分数分布差多少

$$
PSI = \sum_i (A_i - E_i)\ln\frac{A_i}{E_i}
$$

</div>

<div>

**PSI 经验阈值**

| PSI | 含义 |
|---|---|
| 小于 0.1 | 稳定 |
| 0.1 ~ 0.25 | 有变化，关注 |
| 大于 0.25 | 显著漂移，需重训 |

<div class="mt-4 p-3 bg-red-50 rounded text-sm">

**为什么不用准确率？**<br/>
违约率只有 2% 时，“全部预测不违约”准确率就是 98%，却一个坏人也没抓到。

</div>

</div>

</div>

---

# 案例：信用卡违约预测

<div class="grid grid-cols-2 gap-6">

<div>

**数据集**：UCI *Default of Credit Card Clients*

- 台湾某银行信用卡客户，约 3 万条
- 目标：下个月是否违约（约 22% 违约）
- 特征：额度、性别、学历、婚姻、年龄、前 6 个月还款状态/账单/还款额

**我们要做的事**

1. 读数据、检查违约率
2. 按时间/随机划分训练集与测试集
3. 训练逻辑回归 与 LightGBM
4. 对比 AUC、KS
5. 看哪些变量最重要

</div>

<div class="p-3 bg-gray-50 rounded text-sm">

**业务问题**

<br/>

银行想在客户**下个月违约之前**识别出高风险客户，提前降额或提醒还款。

<br/>

**你要思考**

- 漏掉一个坏客户 vs 误伤一个好客户，哪个更贵？
- 阈值怎么选？

</div>

</div>

<!--
【31:00】进入代码演示。如果现场网络不稳定，直接展示下一页代码和课前跑好的结果。
-->

---

# 演示：基线模型代码

```python {all|1-4|6-12|14-19|all}
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, roc_curve

df = pd.read_excel("default_of_credit_card_clients.xls", header=1)
y = df["default payment next month"]
X = df.drop(columns=["ID", "default payment next month"])

X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42
)

lr = LogisticRegression(max_iter=1000)
lr.fit(X_tr, y_tr)
p = lr.predict_proba(X_te)[:, 1]

def ks(y_true, score):
    fpr, tpr, _ = roc_curve(y_true, score)
    return (tpr - fpr).max()

print("AUC:", roc_auc_score(y_te, p), " KS:", ks(y_te, p))
```

<div class="text-sm opacity-70 mt-2">
基线结果通常 AUC 约 0.70~0.72（具体以现场运行为准）。
</div>

---

# 演示：升级为树模型，并解释它

```python {all|1-12|14-20}
import lightgbm as lgb
import shap

gbm = lgb.LGBMClassifier(
    n_estimators=300,
    learning_rate=0.05,
    num_leaves=31,
    class_weight="balanced",
    random_state=42,
)
gbm.fit(X_tr, y_tr)
p2 = gbm.predict_proba(X_te)[:, 1]
print("AUC:", roc_auc_score(y_te, p2), " KS:", ks(y_te, p2))

# 可解释：每个特征对风险分的贡献
explainer = shap.TreeExplainer(gbm)
sv = explainer.shap_values(X_te)
shap.summary_plot(sv[1] if isinstance(sv, list) else sv, X_te)
```

<div class="mt-3 p-3 bg-blue-50 rounded text-sm">
通常你会看到：<b>最近一两个月的还款状态（PAY_0、PAY_2）</b>最重要。这符合直觉：越近的逾期，越能预示下个月违约。
</div>

<!--
【35:00】关键不是 AUC 提升多少，而是让学生看到 SHAP 能给出“为什么”。强调：提升不大不代表树模型没用，在特征很多的真实业务中差距会拉大。
-->

---

# 四个最常见的陷阱

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="p-3 rounded bg-red-50 border border-red-200">
<b>1. 数据泄露</b><br/>
用了“事后才知道”的信息做特征（如催收结果）。线下指标漂亮，上线就崩。
</div>

<div class="p-3 rounded bg-red-50 border border-red-200">
<b>2. 随机划分代替时间划分</b><br/>
风控必须用<b>时间外样本（OOT）</b>验证：用过去训练，用未来检验。
</div>

<div class="p-3 rounded bg-red-50 border border-red-200">
<b>3. 样本偏差（拒绝推断）</b><br/>
只有被批准的人才有还款表现；被拒绝的人没有标签，模型只见过“幸存者”。
</div>

<div class="p-3 rounded bg-red-50 border border-red-200">
<b>4. 只盯 AUC</b><br/>
业务看的是：在通过率 X% 下，坏账率降了多少？带来多少收益？
</div>

</div>

---

# 随堂小测（1 分钟）

<div class="text-lg leading-loose">

**Q1.** 某变量 IV = 0.45，说明什么？

A. 几乎无用　B. 弱　C. 预测力强，但需检查是否泄露

<v-click>
<div class="text-green-700 ml-4">✅ 答案：C。IV 特别高时，要先怀疑是不是“未来信息”混进来了。</div>
</v-click>

**Q2.** 模型上线半年，PSI = 0.31，应当怎么办？

A. 继续用　B. 排查数据与客群变化，考虑重训

<v-click>
<div class="text-green-700 ml-4">✅ 答案：B。PSI 超过 0.25 说明分布显著漂移。</div>
</v-click>

**Q3.** 坏客户只占 1%，应主要看哪个指标？

A. 准确率　B. KS / AUC / 召回

<v-click>
<div class="text-green-700 ml-4">✅ 答案：B。</div>
</v-click>

</div>

---
layout: center
---

# 💬 提问环节

<div class="text-xl mt-8 opacity-80">
关于风险、数据、评分卡和机器学习建模，有什么想问的？
</div>

<div class="mt-8 text-left inline-block text-base opacity-80">

**如果一时想不到问题，可以先想想：**

- 评分卡和树模型，实际工作中怎么选？
- 如果训练数据里的好坏标签本身有偏差，模型会出什么问题？
- 为什么 IV 特别高的变量反而要警惕？

</div>

<div class="mt-8 opacity-60">
接下来：图计算与反欺诈 → 金融智能体
</div>

<!--
【40:00】提问环节，约 5 分钟。先给学生 1 分钟思考，冷场时用页面上的三个问题预热。把没来得及回答的问题记下来，放到后面智能体部分或课后答疑。
-->
