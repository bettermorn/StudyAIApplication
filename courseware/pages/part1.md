---
layout: section
---

# ① 金融风险与大数据

金融在做什么？风险从哪里来？数据怎样帮忙？

---

# 金融的本质：用今天的钱，换明天的承诺

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

**银行放一笔贷款**

- 今天：借出 10 万元
- 明天：对方是否还？还多少？何时还？
- **风险 = 未来的不确定性带来的损失**

<v-click>

**风控要回答三个问题**

1. 这个人/企业**会不会**违约？（概率 PD）
2. 违约了**会损失多少**？（损失率 LGD）
3. 当时**暴露了多少**？（风险敞口 EAD）

</v-click>

</div>

<div v-click>

**预期损失公式**

$$
EL = PD \times LGD \times EAD
$$

<div class="mt-6 p-3 bg-yellow-50 rounded text-sm">
例：PD = 2%，LGD = 60%，EAD = 10 万<br/>
EL = 0.02 × 0.6 × 100000 = <b>1200 元</b><br/>
利率里必须覆盖这 1200 元，否则就亏本。
</div>

</div>

</div>

<!--
【05:00】这页是整场数学基础。统计背景的同学对 PD 就是“二分类预测概率”应该很有感觉，直接点明：我们后面建模，建的就是 PD。
-->

---

# 四类核心风险

| 风险类型 | 一句话解释 | 生活里的例子 | 主要数据 |
|---|---|---|---|
| **信用风险** | 对方不还钱 | 信用卡逾期、网贷违约 | 征信、流水、行为 |
| **市场风险** | 价格波动造成损失 | 股价下跌、汇率变动 | 行情、利率、波动率 |
| **操作风险** | 人、系统、流程出错或欺诈 | 转账被骗、内部违规 | 日志、设备、交易 |
| **流动性风险** | 钱到期拿不出来 | 理财赎回潮、银行挤兑 | 资产负债期限结构 |

<div class="mt-6 p-3 bg-blue-50 rounded">
今天重点讲<b>信用风险</b>和<b>操作风险（反欺诈）</b>——数据最丰富，也最先被 AI 改变。
</div>

---

# 风控闭环：不是一次判断，而是持续管理

```mermaid {scale: 0.85}
flowchart LR
  A[贷前<br/>准入审批] --> B[贷中<br/>监控预警]
  B --> C[贷后<br/>催收处置]
  C --> D[复盘<br/>策略迭代]
  D --> A
  style A fill:#dbeafe,stroke:#3b82f6
  style B fill:#dcfce7,stroke:#22c55e
  style C fill:#fef9c3,stroke:#eab308
  style D fill:#fce7f3,stroke:#ec4899
```

<div class="grid grid-cols-3 gap-4 mt-4 text-sm">

<div class="p-2 bg-blue-50 rounded">
<b>贷前</b>：要不要放？放多少？什么利率？<br/>→ 评分卡、反欺诈
</div>

<div class="p-2 bg-green-50 rounded">
<b>贷中</b>：客户状况变坏了吗？<br/>→ 行为评分、预警信号
</div>

<div class="p-2 bg-yellow-50 rounded">
<b>贷后</b>：逾期了怎么办？<br/>→ 催收评分、处置策略
</div>

</div>

<!--
【08:00】强调：预警从“贷后补救”前移到“贷前、贷中”，这正是后面重庆银行案例的目标。
-->

---

# 什么是“金融大数据”？

<div class="grid grid-cols-2 gap-6">

<div>

**特点（教科书里的“多 V”）**

- **Volume 量大**：每天数亿笔交易
- **Velocity 快**：毫秒级实时决策
- **Variety 杂**：表格、文本、图像、图关系
- **Veracity 真实性**：噪声、缺失、造假
- **Value 价值密度低**：需要提炼

</div>

<div>

**主要数据源**

| 类别 | 例子 |
|---|---|
| 征信数据 | 央行征信、百行征信 |
| 交易数据 | 流水、支付、转账 |
| 行为数据 | App 点击、设备、定位 |
| 文本数据 | 年报、新闻、客服对话 |
| 工商司法 | 股权、诉讼、失信 |
| 供应链 | 发票、订单、物流 |

</div>

</div>

<div class="mt-4 p-3 bg-red-50 rounded text-sm">
⚠️ 数据不是“越多越好”。必须<b>合法、合规、最小必要</b>，并获得用户授权。
</div>

---

# 互动：给一位“白户”毕业生授信

<div class="text-xl mt-6">

小王，应届毕业，**没有任何信贷记录**，申请 5000 元额度。

</div>

<div class="mt-8 text-lg">

你会看哪些数据来判断他的还款意愿和能力？

</div>

<v-clicks>

- 📄 Offer 与工作单位（稳定性）
- 🏫 学历、学校、专业（能力预期）
- 📱 手机号使用时长、实名情况
- 💳 在支付平台的消费和还款历史
- 🔗 设备、联系人是否与高风险人群重合
- ⚖️ 但：哪些数据<b>不能</b>用？（如种族、宗教、非授权隐私）

</v-clicks>

<!--
【14:00】2 分钟互动。让学生先说，再逐条揭示。最后一条引出合规与公平，后面模块五回扣。
-->

---

# 传统量化风控的三个瓶颈

<div class="grid grid-cols-3 gap-4 mt-8">

<div class="p-4 rounded border-2 border-blue-300 bg-blue-50">
<div class="text-4xl">①</div>
<b>维度窄</b><br/><br/>
主要依赖十几个征信变量，对“白户”和小微企业几乎没有信息。
</div>

<div class="p-4 rounded border-2 border-green-300 bg-green-50">
<div class="text-4xl">②</div>
<b>只看个体</b><br/><br/>
线性模型难捕捉非线性；更难看到<b>团伙、关联、担保圈</b>这类关系型风险。
</div>

<div class="p-4 rounded border-2 border-orange-300 bg-orange-50">
<div class="text-4xl">③</div>
<b>读不懂文本</b><br/><br/>
合同、年报、尽调报告、新闻全靠人读，慢，而且容易漏。
</div>

</div>

<div class="mt-8 text-center text-lg">
→ 对应今天的三条解法：<b>机器学习</b> · <b>图计算</b> · <b>大模型智能体</b>
</div>

<!--
【19:00】过渡页。把瓶颈和后面三个模块一一对应。
-->