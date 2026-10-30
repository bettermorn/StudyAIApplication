---
layout: section
---

# 总结：你的成长路径

---

# 今天的知识地图与微专业课程

<div class="text-sm opacity-70">课程信息来源：《金融大数据与智能风险管理微专业 2026 年招生简章》</div>

| 今天讲的 | 对应课程 | 类型 |
|---|---|---|
| 风险、大数据、数据来源 | 《金融大数据分析》 | 核心课程 |
| PD/LGD、评分卡、模型评价 | 《金融统计与风险管理》 | 核心课程 |
| 结果呈现、SHAP 解释 | 《金融数据可视化分析建模》 | 核心课程 |
| 智能体、大模型金融应用 | 《数智金融》 | 企业实战训练营 |
| 反欺诈、预警、案例拆解 | 《智能风控案例分析》 | 企业实战训练营 |
| 把一切串起来做项目 | 行业项目实训（8 周） | 校企合作实习 |

<!--
<div class="mt-4 p-3 bg-blue-50 rounded text-sm">
总共 6 门课程、10 学分。已修读并通过的核心课程可申请学分认定。
</div>
-->

<!--
【86:00】课程名称和学分以招生简章为准；简章是扫描件，若学分/学期有疑问，课后以学院正式通知核对。
-->

---

# 三个可以立刻开始的行动

<div class="grid grid-cols-3 gap-4 mt-8">

<div class="p-4 rounded border-2 border-blue-300 bg-blue-50">
<div class="text-3xl">1️⃣</div>
<b>复现一个评分卡</b><br/><br/>
用 UCI 信用卡数据集，完成分箱 → WOE → 逻辑回归 → 分数映射，并算出 KS 和 PSI。
</div>

<div class="p-4 rounded border-2 border-green-300 bg-green-50">
<div class="text-3xl">2️⃣</div>
<b>拆解一个智能体案例</b><br/><br/>
选重庆银行或 FinRobot，画出架构图：它有哪些工具？哪里需要人工？风险在哪？
</div>

<div class="p-4 rounded border-2 border-orange-300 bg-orange-50">
<div class="text-3xl">3️⃣</div>
<b>做一个小原型</b><br/><br/>
结合实训项目，做一个只读的“尽调助手”：工具调用 + 留痕 + 转人工。
</div>

</div>

---


# 本讲小结

<v-clicks>

- 风控是**持续闭环**：贷前、贷中、贷后、复盘；核心量是 **EL = PD × LGD × EAD**
- **评分卡**稳定、可解释；**机器学习**更强但要配合解释工具；评价看 **AUC / KS / PSI**，验证要用时间外样本
- **图计算**让我们看见“关系型风险”，**异常检测**补上“没见过的套路”
- **智能体 = 大模型 + 工具 + 记忆 + 规划 + 护栏**；它不取代模型，而是把模型和流程**组织成闭环**
- 金融智能体的铁律：**数字由代码算、过程可追溯、权限最小化、高风险人工把关**
- 技术向善：守住风险底线，服务实体经济与普惠金融

</v-clicks>

---
layout: center
---

# 谢谢！Q & A

<!--
<div class="mt-8 opacity-70">
课后材料：课件源文件 · 信用卡违约预测示例数据 · 阅读清单
</div>
-->

---

# 参考资料与延伸阅读

<div class="text-sm leading-relaxed">

- 《金融大数据与智能风险管理微专业 2026 年招生简章》
- 央视网/中国金融信息网：《Token 消耗量激增、智能体批量上线 上市银行半年报里的“AI 竞赛”》，2026-09-03
- 中国新闻网上海站：《金融智能体迈入规模化落地周期 科技厂商竞逐生态共建赛道》，2026-07-29
- 金科创新社：《重庆银行：AI 智能体驱动的“重银晓警”风险智能预警平台》，鑫智奖 2026 第七届金融机构数智化转型优秀案例
- Yang, H. et al. *FinRobot: An Open-Source AI Agent Platform for Financial Applications using Large Language Models*. arXiv:2405.14767, 2024
- GitHub：AI4Finance-Foundation/FinRobot；TauricResearch/TradingAgents
- UCI Machine Learning Repository：*Default of Credit Card Clients* 数据集
- 经典：Siddiqi, N. *Credit Risk Scorecards*；周志华《机器学习》；Lundberg & Lee, *SHAP*, 2017

</div>

<div class="mt-4 p-3 bg-yellow-50 rounded text-xs">
说明：案例中的机构数据来自公开报道与公开项目主页；评分卡 WOE 小例子与“尽调智能体”代码为教学示意，非真实机构数据或生产代码。
</div>
