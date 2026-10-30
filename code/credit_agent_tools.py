"""贷前尽调风控智能体：工具箱（对应课件“动手看 1/2”）。

设计原则：数字由确定性代码计算，不让大模型心算。
工具表只提供“读”的能力，不提供放款、改额度等危险动作。
示例数字为教学虚构，真实场景需对接财报库、司法/工商接口和已上线的评分模型。
"""


def get_financials(company):
    """真实场景：对接财报库。"""
    return {"debt_ratio": 0.78, "current_ratio": 0.9, "net_margin": -0.02}


def get_legal_risk(company):
    """真实场景：对接司法/工商接口。"""
    return {"lawsuits_12m": 5, "dishonest_executor": False}


def score_pd(fin, legal):
    """真实场景：调用已上线的评分模型。这里用简单规则示意违约概率 PD。"""
    pd_ = 0.02 + 0.08 * (fin["debt_ratio"] > 0.7) + 0.03 * (legal["lawsuits_12m"] > 3)
    return round(pd_, 3)


# 只给“读”，不给“放款”
TOOLS = {"财务": get_financials, "司法": get_legal_risk}
