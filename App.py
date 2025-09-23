import streamlit as st
import streamlit.components.v1 as components
import base64


# ========== 页面设置 ==========
st.set_page_config(
    page_title="侯良语面试Demo",
    layout="wide"
)

# ========== 标题 ==========
st.title("✏️ 侯良语面试Demo - 携程国际业务 客服支持业务 《指标体系与成本分析》")

# ========== 附件下载 ==========
def pdf_download_link(pdf_path, link_text="📄 点此下载"):
    with open(pdf_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f'{link_text}'




# ========== 说明 ==========
st.markdown(f"""
---
### 📝 说明
- 该 Demo 旨在直观呈现候选人代入Senior Business Analyst的角色后对携程国际业务（客服支持体系）的快速学习理解，并以此为切入点，激发正式面试中更深入的探讨与交流
- 大部分数字/权重为推断假设，部分数据来源于Trip.com 官网和公开财报，已以红字显示
- 图表使用基于JavaScript的代码可视化工具 - Mermaid制作，Draw.io美化 
- 候选人相似过往项目经历请点击以下链接下载
""", unsafe_allow_html=True)

# 假设你的 PDF 文件叫 "resume.pdf" 放在项目根目录
with open("亚马逊项目 - 配送站评分系统.pdf", "rb") as f:
    pdf_bytes = f.read()

st.download_button(
    label="📥 下载候选人相似过往项目经历",
    data=pdf_bytes,
    file_name="候选人项目经历.pdf",
    mime="application/pdf"
)

# ========== 三张图展示 ==========
st.header("📊 客户满意度指标 + 客服渠道拆解 + 客服成本分析与优化")
st.markdown(f"""

""")
with open("pic.svg","r",encoding="utf-8") as f:
    svg_code = f.read()
components.html(svg_code,height=1000,width = 2500, scrolling=True)

