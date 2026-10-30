"""贷前尽调风控智能体：工作流（对应课件“动手看 2/2”）。

流程：规划 -> 逐步调用工具并留痕 -> 代码计算 PD -> 大模型写摘要 -> 高风险转人工。
课件里的 llm 对象和 log 函数是示意；这里用 MockLLM 和 print 补齐，便于直接运行。
接入真实大模型时，只需让 llm 提供 plan() 与 write() 两个方法。

运行：python credit_agent_due_diligence.py
"""
from credit_agent_tools import TOOLS, score_pd

HUMAN_REVIEW_PD = 0.05  # PD 超过该阈值必须转人工（示意阈值）


class MockLLM:
    """示意用的假大模型：固定规划步骤，摘要只复述已给出的证据与 PD。"""

    def plan(self, goal, tools):
        return list(tools)

    def write(self, prompt):
        return f"（模拟摘要）{prompt}"


def log(company, step, result):
    """全程留痕：真实场景应写入可审计的日志系统。"""
    print(f"[log] {company} | {step} | {result}")


def due_diligence(company, llm):
    plan = llm.plan(f"评估 {company} 的授信风险", tools=list(TOOLS))  # 大模型规划
    evidence = {}
    for step in plan:  # 逐步执行
        if step in TOOLS:
            evidence[step] = TOOLS[step](company)
            log(company, step, evidence[step])  # 全程留痕
    pd_est = score_pd(evidence["财务"], evidence["司法"])  # 代码计算 PD
    text = llm.write(f"依据证据写摘要，不得编造数字：{evidence}, PD={pd_est}")
    need_human = pd_est > HUMAN_REVIEW_PD  # 高风险必须人工
    return {
        "company": company,
        "pd": pd_est,
        "summary": text,
        "evidence": evidence,
        "need_human": need_human,
    }


if __name__ == "__main__":
    report = due_diligence("示例科技有限公司", MockLLM())
    print("PD:", report["pd"], "| 需人工复核:", report["need_human"])
