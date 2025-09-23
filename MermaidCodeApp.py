import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="侯良语面试Demo", layout="wide")

# Mermaid 图代码
mermaid_code1 = """
graph TD
    A[客户满意度] --> B[解决率 35%]
    B --> B1[首问解决率 40%]
    B --> B2[24/72小时内解决率 30%]
    B --> B3[转接率 30%]
    B3 --> BB1[高频转接路径]

    A --> C[时效指标 20%]
    C --> C1[平均通话/live chat时长 35%]
    C --> C3[等待时长 65%] -->CC1[客服资源调配]

    A --> D[服务质量主观评分 25%] 
    D --> DD1[是否友好耐心 33%]
    D --> DD2[专业知识是否充足 33%]
    D --> DD3[客服语言能力 33%]
    DD1 & DD2 & DD3--> DDD[统计分析]

    A --> E[投诉与异常 20%]
    E --> E2[重复来电率/跨渠道联系率 60%] --> EE2[UID Tracking]
    E --> E3[差评率 20%] --> EE3[指标权重设计]
    E --> E1[投诉率 20%] --> EE3[指标权重设计]

    subgraph 衍生分析
    BB1--> BBB1[联系方式不准确]
    CC1[客服资源调配] --> CCC1[过长:人力短缺 过短：人力浪费]
    DDD[统计分析]
    EE2[UID Tracking]
    EE3 --> EEE3[用户没有渠道/精力打差评投诉]
    end
"""

mermaid_code2 = """
graph TD
    A[服务渠道升级] --> B[电话 14%] --> BB[全球18个客服中心超1000人]
    A --> C[在线客服 80%] --> CC
    A --> F[In-App Call 5%] --> FF[忠实客户]
    A --> D[电子邮件 1%] --> DD[非紧急事项]

    subgraph AI
    CC[LLM AI Agent：传统Chatbot的升级]
    end
"""

mermaid_code3 = """
graph TD
    A[Trip.com全球客服中心23年度总成本<br/>估算 8-12 亿美元]

    A --> B[全球多中心人力成本<br/>占比约 65%<br/>优化方向: 全球人力套利, 提升高端技能人效]
    A --> C[外包与采购成本<br/>占比约 15%<br/>优化方向: 建立全球外包网络, 引入竞争]
    A --> D[技术与基础设施成本<br/>占比约 20%<br/>优化方向: 投资AI与自动化, 降低单位互动成本]

    B --> B1[多区域中心人力成本<br/>爱丁堡, 首尔, 新加坡<br>优化: 覆盖多语言与高端客群, 提升满意度溢价]
    B --> B2[全球外包人力成本<br/>马尼拉, 里斯本, 波哥大<br>优化: 利用时区/语言/成本优势, 提供24/7服务]

    C --> C1[全球云通信与SaaS服务费<br/>优化: 与大型云服务商签全球框架协议, 统一管理]
    C --> C2[本地化合作供应商采购<br/>优化: 各地区采购本地化服务如支付/短信, 降低成本]

    D --> D1[AI与自动化研发摊销<br/>优化: 投资多语言LLM大模型, 持续提升自助解决率]
    D --> D2[全球系统license与云资源<br/>优化: 统一技术栈, 利用云服务弹性伸缩, 避免浪费]

    E[根本性优化: <br/>优化UI/UX减少咨询, 主动通知, 本地化政策]
    D1-.->E
    C1-.->E
    B2-.->E
    D2-.->E
    C2-.->E
    B1-.->E

    subgraph 优化策略
    B1
    B2
    C1
    C2
    D1
    D2
    E
    end


"""

# Mermaid 渲染 HTML 模板，用 f-string 插入
def render_mermaid(code: str, height: int = 500):
    html_code = f"""
    <script type="module">
      import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";
      mermaid.initialize({{ startOnLoad: true }});
    </script>
    <div class="mermaid">
    {code}
    </div>
    """
    components.html(html_code, height=height, scrolling=True)


st.title("侯良语面试Demo：携程国际业务机酒业务-客户满意度")
st.subheader("以下涉及到的数据大部分为虚构，部分来源携程公开财报/新闻，仅用于面试展示使用")
st.subheader("业务指标体系")
render_mermaid(mermaid_code1, height=400)
st.subheader("客服渠道组合升级")
render_mermaid(mermaid_code2, height=400)
st.subheader("客服成本拆解")
render_mermaid(mermaid_code3, height=500)

