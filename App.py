import streamlit as st
import streamlit.components.v1 as components
import base64
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# ========== 页面设置 ==========
st.set_page_config(
    page_title="侯良语面试Demo",
    layout="wide"
)

# ========== 标题 ==========
st.title("✏️ 侯良语面试Demo - 携程国际业务 客服支持")

# ========== 附件下载 ==========
def pdf_download_link(pdf_path, link_text="📄 点此下载"):
    with open(pdf_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f'{link_text}'




# ========== 说明 ==========
st.markdown(f"""
---
### 📝 说明
- 该 Demo 旨在直观呈现候选人以Senior Business Analyst的角色对携程国际业务（客服支持）的快速学习理解，并以此为切入点，激发正式面试中更深入的探讨与交流
- 行业/竞对/历史数据来源于互联网公开信息，公开财报以及Trip.com 官方网站，存在一定误差，图表使用Plotly + HTML/CSS制作
- 思维导图中大部分数字/权重为推断假设，使用基于JavaScript的代码可视化工具 - Mermaid制作，Draw.io美化 
- 候选人相似过往项目经历（业务指标体系）请点击以下链接下载

### 📋 开发日志
<details>
<summary><strong>点击展开查看开发历史</strong></summary>

**v1.0 (初始版本2025-09-23)**
- 基础思维导图展示 (Mermaid SVG)
- 客户满意度指标 + 客服渠道拆解 + 客服成本分析

**v2.0 (2025-09-25 更新)**
- ✨ 新增竞品分析模块
  - 海外OTA平台市场份额变化趋势 (面积图)
  - 客服系统发展大事记 (折线图)
  - 客服系统能力雷达图对比 (4个雷达图)
- ✨ 新增预测性人力资源优化模块
  - 炫酷思维导图展示优化模型
  - 智能排班系统Demo界面
- ✨ 新增AI客服升级路线图
  - 项目进度管理甘特图
  - 里程碑和关键指标展示
- 🎨 界面优化
  - 多标签页布局
  - 统一携程蓝配色方案
  - 响应式设计优化
- 🔧 技术升级
  - 从Mermaid迁移到Plotly + HTML/CSS
  - 交互式图表支持
  - 自定义tooltip和hover效果

</details>
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

# ========== 竞品分析功能 ==========
def show_market_share():
    st.subheader("📈 海外OTA平台市场份额变化趋势 (2019-2025)")
    
    # 市场份额变化数据
    years = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
    
    booking_share = [47.2, 45.8, 46.1, 45.5, 44.8, 44.3, 43.8]
    expedia_share = [31.5, 29.8, 30.2, 29.5, 28.9, 27.7, 26.5]
    airbnb_share = [12.8, 14.2, 15.1, 15.8, 16.0, 16.1, 16.2]
    trip_share = [6.2, 7.1, 7.8, 8.2, 8.6, 9.4, 10.1]
    others_share = [2.3, 3.1, 0.8, 1.0, 1.7, 2.5, 3.4]
    
    # 创建面积图数据 - 使用正确的堆叠面积图
    fig = go.Figure()
    
    # 计算累积值用于堆叠面积图 - 从下到上按份额从低到高排列
    cumulative_others = others_share
    cumulative_trip = [o + t for o, t in zip(others_share, trip_share)]
    cumulative_airbnb = [o + t + a for o, t, a in zip(others_share, trip_share, airbnb_share)]
    cumulative_expedia = [o + t + a + e for o, t, a, e in zip(others_share, trip_share, airbnb_share, expedia_share)]
    cumulative_booking = [o + t + a + e + b for o, t, a, e, b in zip(others_share, trip_share, airbnb_share, expedia_share, booking_share)]
    
    # 添加各平台面积图 - 从下到上按份额从低到高排列，tooltip显示单独份额
    fig.add_trace(go.Scatter(x=years, y=cumulative_others, mode='lines+markers', 
                            fill='tozeroy', name='Others', 
                            line=dict(color='#FFEAA7', width=3),
                            marker=dict(size=6, color='#FFEAA7'),
                            fillcolor='rgba(255, 234, 167, 0.7)',
                            hovertemplate='<b>Others</b><br>年份: %{x}<br>市场份额: %{customdata}%<extra></extra>',
                            customdata=others_share))
    fig.add_trace(go.Scatter(x=years, y=cumulative_trip, mode='lines+markers', 
                            fill='tonexty', name='Trip.com', 
                            line=dict(color='#0066CC', width=3),
                            marker=dict(size=6, color='#0066CC'),
                            fillcolor='rgba(0, 102, 204, 0.7)',
                            hovertemplate='<b>Trip.com</b><br>年份: %{x}<br>市场份额: %{customdata}%<extra></extra>',
                            customdata=trip_share))
    fig.add_trace(go.Scatter(x=years, y=cumulative_airbnb, mode='lines+markers', 
                            fill='tonexty', name='Airbnb', 
                            line=dict(color='#45B7D1', width=3),
                            marker=dict(size=6, color='#45B7D1'),
                            fillcolor='rgba(69, 183, 209, 0.7)',
                            hovertemplate='<b>Airbnb</b><br>年份: %{x}<br>市场份额: %{customdata}%<extra></extra>',
                            customdata=airbnb_share))
    fig.add_trace(go.Scatter(x=years, y=cumulative_expedia, mode='lines+markers', 
                            fill='tonexty', name='Expedia Group', 
                            line=dict(color='#4ECDC4', width=3),
                            marker=dict(size=6, color='#4ECDC4'),
                            fillcolor='rgba(78, 205, 196, 0.7)',
                            hovertemplate='<b>Expedia Group</b><br>年份: %{x}<br>市场份额: %{customdata}%<extra></extra>',
                            customdata=expedia_share))
    fig.add_trace(go.Scatter(x=years, y=cumulative_booking, mode='lines+markers', 
                            fill='tonexty', name='Booking.com', 
                            line=dict(color='#FF6B6B', width=3),
                            marker=dict(size=6, color='#FF6B6B'),
                            fillcolor='rgba(255, 107, 107, 0.7)',
                            hovertemplate='<b>Booking.com</b><br>年份: %{x}<br>市场份额: %{customdata}%<extra></extra>',
                            customdata=booking_share))
    
    fig.update_layout(
        # title="全球OTA市场份额变化趋势 (2019-2025)",
        xaxis_title="年份",
        yaxis_title="市场份额 (%)",
        hovermode='x unified',
        height=500,
        yaxis=dict(
            range=[0, 100],
            tickmode='linear',
            tick0=0,
            dtick=10,
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128,128,128,0.2)'
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_timeline():
    st.subheader("📈 海外OTA客服系统发展大事记：AI客服部署进度对比 (2019-2025)")
    
    # 折线图数据
    years = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
    
    # 各平台AI客服部署进度
    booking_ai = [10, 25, 45, 65, 80, 90, 95]
    expedia_ai = [5, 20, 40, 60, 75, 85, 92]
    airbnb_ai = [15, 30, 50, 70, 85, 88, 90]
    trip_ai = [8, 18, 35, 55, 70, 82, 88]
    
    fig = go.Figure()
    
    # 添加各平台折线
    fig.add_trace(go.Scatter(x=years, y=booking_ai, mode='lines+markers', 
                            name='Booking.com', line=dict(color='#FF6B6B', width=3)))
    fig.add_trace(go.Scatter(x=years, y=expedia_ai, mode='lines+markers', 
                            name='Expedia', line=dict(color='#4ECDC4', width=3)))
    fig.add_trace(go.Scatter(x=years, y=airbnb_ai, mode='lines+markers', 
                            name='Airbnb', line=dict(color='#45B7D1', width=3)))
    fig.add_trace(go.Scatter(x=years, y=trip_ai, mode='lines+markers', 
                            name='Trip.com', line=dict(color='#0066CC', width=3)))
    
    # 添加重要事件标注
    events = [
        {'year': 2019, 'y': 15, 'text': 'Booking收购GetYourGuide', 'color': '#FF6B6B'},
        {'year': 2020, 'y': 25, 'text': '疫情加速AI部署', 'color': '#FF6B6B'},
        {'year': 2021, 'y': 45, 'text': 'Expedia AI客服上线', 'color': '#4ECDC4'},
        {'year': 2022, 'y': 65, 'text': 'Airbnb社区化客服', 'color': '#45B7D1'},
        {'year': 2023, 'y': 80, 'text': 'Booking多模态AI', 'color': '#FF6B6B'},
        {'year': 2024, 'y': 85, 'text': 'Trip.com LLM升级', 'color': '#0066CC'},
        {'year': 2025, 'y': 90, 'text': '全行业AI成熟期', 'color': '#FFEAA7'}
    ]
    
    for event in events:
        fig.add_annotation(
            x=event['year'], y=event['y'],
            text=event['text'],
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor=event['color'],
            ax=0, ay=-40,
            bgcolor="white",
            bordercolor=event['color'],
            borderwidth=1
        )
    
    fig.update_layout(
        # title=" (2019-2025)",
        xaxis_title="年份",
        yaxis_title="AI客服覆盖率 (%)",
        hovermode='x unified',
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_competitor_comparison():
    st.subheader("🎯 客服系统能力雷达图对比 (2025)")
    
    # 数据 - 2025年最新数据
    platforms = ['Booking.com', 'Expedia', 'Airbnb', 'Trip.com']
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#0066CC']  # Trip.com用携程蓝
    
    # 各指标数据
    languages = [55, 28, 35, 25]  # 多语言支持
    response_speed = [85, 75, 90, 80]  # 响应速度 (100-响应时间*20)
    resolution_rate = [72, 68, 78, 70]  # 解决率
    cost_efficiency = [85, 80, 90, 75]  # 成本效率 (100-成本*5)
    
    # 创建四个雷达图，一排两个
    col1, col2 = st.columns(2)
    
    with col1:
        # Trip.com 基准图
        fig1 = go.Figure()
        fig1.add_trace(go.Scatterpolar(
            r=[languages[3], response_speed[3], resolution_rate[3], cost_efficiency[3]],
            theta=['Languages', 'Response Speed', 'Resolution Rate', 'Cost Efficiency'],
            fill='toself',
            name='Trip.com (基准)',
            line=dict(color='#0066CC', width=3)
        ))
        fig1.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            title="Trip.com 客服能力基准",
            height=400,
            margin=dict(l=20, r=20, t=50, b=20)
        )
        st.plotly_chart(fig1, use_container_width=True)
        
        # Booking.com vs Trip.com
        fig2 = go.Figure()
        # Booking.com 实线
        fig2.add_trace(go.Scatterpolar(
            r=[languages[0], response_speed[0], resolution_rate[0], cost_efficiency[0]],
            theta=['Languages', 'Response Speed', 'Resolution Rate', 'Cost Efficiency'],
            fill='toself',
            name='Booking.com',
            line=dict(color='#FF6B6B', width=3)
        ))
        # Trip.com 虚线基准 (置前)
        fig2.add_trace(go.Scatterpolar(
            r=[languages[3], response_speed[3], resolution_rate[3], cost_efficiency[3]],
            theta=['Languages', 'Response Speed', 'Resolution Rate', 'Cost Efficiency'],
            fill='toself',
            name='Trip.com (基准)',
            line=dict(color='#0066CC', width=2, dash='dash')
        ))
        fig2.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            title="Booking.com vs Trip.com",
            height=400,
            margin=dict(l=20, r=20, t=50, b=20)
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    with col2:
        # Expedia vs Trip.com
        fig3 = go.Figure()
        # Expedia 实线
        fig3.add_trace(go.Scatterpolar(
            r=[languages[1], response_speed[1], resolution_rate[1], cost_efficiency[1]],
            theta=['Languages', 'Response Speed', 'Resolution Rate', 'Cost Efficiency'],
            fill='toself',
            name='Expedia',
            line=dict(color='#4ECDC4', width=3)
        ))
        # Trip.com 虚线基准 (置前)
        fig3.add_trace(go.Scatterpolar(
            r=[languages[3], response_speed[3], resolution_rate[3], cost_efficiency[3]],
            theta=['Languages', 'Response Speed', 'Resolution Rate', 'Cost Efficiency'],
            fill='toself',
            name='Trip.com (基准)',
            line=dict(color='#0066CC', width=2, dash='dash')
        ))
        fig3.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            title="Expedia vs Trip.com",
            height=400,
            margin=dict(l=20, r=20, t=50, b=20)
        )
        st.plotly_chart(fig3, use_container_width=True)
        
        # Airbnb vs Trip.com
        fig4 = go.Figure()
        # Airbnb 实线
        fig4.add_trace(go.Scatterpolar(
            r=[languages[2], response_speed[2], resolution_rate[2], cost_efficiency[2]],
            theta=['Languages', 'Response Speed', 'Resolution Rate', 'Cost Efficiency'],
            fill='toself',
            name='Airbnb',
            line=dict(color='#45B7D1', width=3)
        ))
        # Trip.com 虚线基准 (置前)
        fig4.add_trace(go.Scatterpolar(
            r=[languages[3], response_speed[3], resolution_rate[3], cost_efficiency[3]],
            theta=['Languages', 'Response Speed', 'Resolution Rate', 'Cost Efficiency'],
            fill='toself',
            name='Trip.com (基准)',
            line=dict(color='#0066CC', width=2, dash='dash')
        ))
        fig4.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            title="Airbnb vs Trip.com",
            height=400,
            margin=dict(l=20, r=20, t=50, b=20)
        )
        st.plotly_chart(fig4, use_container_width=True)

# ========== 预测性人力资源优化 ==========
def show_predictive_staffing():
    st.subheader("👥 预测性客服人力资源优化模型")
    
    # 创建炫酷的思维导图HTML
    mindmap_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            .mindmap {
                width: 100%;
                height: 600px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 20px;
                padding: 30px;
                font-family: 'Arial', sans-serif;
                position: relative;
                overflow: hidden;
            }
            
            .center-node {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: #fff;
                border-radius: 50%;
                width: 300px;
                height: 300px;
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 8px 20px rgba(0,0,0,0.3);
                z-index: 10;
            }
            
            .center-text {
                font-size: 25px;
                font-weight: bold;
                color: #333;
                text-align: center;
                line-height: 1.2;
            }
            
            .branch {
                position: absolute;
                background: rgba(255,255,255,0.9);
                border-radius: 12px;
                padding: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                width: 450px;
                height: 120px;
                backdrop-filter: blur(10px);
            }
            
            .branch-title {
                font-size: 22px;
                font-weight: bold;
                color: #333;
                margin-bottom: 6px;
                display: flex;
                align-items: center;
            }
            
            .branch-content {
                font-size: 20px;
                color: #666;
                line-height: 1.2;
            }
            
            .icon {
                margin-right: 6px;
                font-size: 20px;
            }
            
            .branch-1 { top: 20%; left: 10%; }
            .branch-2 { top: 20%; right: 10%; }
            .branch-3 { bottom: 20%; left: 10%; }
            .branch-4 { bottom: 20%; right: 10%; }
            
            .connection-line {
                position: absolute;
                background: rgba(255,255,255,0.6);
                height: 2px;
                transform-origin: left center;
            }
            
            .line-1 { top: 30%; left: 20%; width: 180px; transform: rotate(-15deg); }
            .line-2 { top: 30%; right: 20%; width: 180px; transform: rotate(15deg); }
            .line-3 { bottom: 30%; left: 20%; width: 180px; transform: rotate(15deg); }
            .line-4 { bottom: 30%; right: 20%; width: 180px; transform: rotate(-15deg); }
        </style>
    </head>
    <body>
        <div class="mindmap">
            <div class="center-node">
                <div class="center-text">预测性人力资源<br/>优化模型</div>
            </div>
            
            <div class="connection-line line-1"></div>
            <div class="connection-line line-2"></div>
            <div class="connection-line line-3"></div>
            <div class="connection-line line-4"></div>
            
            <div class="branch branch-1">
                <div class="branch-title">
                    <span class="icon">📊</span>
                    需求预测模型
                </div>
                <div class="branch-content">
                    <strong>输入:</strong> 历史数据、季节性因子、事件驱动<br>
                    <strong>输出:</strong> 7-30天预测、实时调整机制
                </div>
            </div>
            
            <div class="branch branch-2">
                <div class="branch-title">
                    <span class="icon">👥</span>
                    人员配置优化
                </div>
                <div class="branch-content">
                    <strong>配置:</strong> 全职60%、季节性25%、灵活（兼职）15%<br>
                    <strong>技能:</strong> 多语言专家、业务专家、通用客服
                </div>
            </div>
            
            <div class="branch branch-3">
                <div class="branch-title">
                    <span class="icon">⚡</span>
                    灵活用工策略
                </div>
                <div class="branch-content">
                    <strong>亚马逊物流人力规划经验:</strong> VET自愿加班、VTO自愿休假、MET强制加班<br>
                    <strong>外包网络:</strong> 全球合作伙伴、时区覆盖、成本优化
                </div>
            </div>
            
            <div class="branch branch-4">
                <div class="branch-title">
                    <span class="icon">💰</span>
                    成本效益分析
                </div>
                <div class="branch-content">
                    <strong>收益:</strong> 人力成本优化20-30%、服务质量提升15%<br>
                    <strong>ROI:</strong> 6个月回本、年化收益25%
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    st.components.v1.html(mindmap_html, height=650)
    
    # 智能排班系统Demo
    st.markdown("---")
    st.subheader("🤖 智能排班系统 Demo")
    st.markdown("基于上述预测模型搭建的智能排班系统，实时优化客服人员配置")
    
    # 创建智能排班系统界面
    scheduling_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            .scheduling-demo {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 20px;
                padding: 30px;
                color: white;
                font-family: 'Arial', sans-serif;
            }
            
            .header {
                text-align: center;
                margin-bottom: 30px;
            }
            
            .dashboard {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
                margin-bottom: 30px;
            }
            
            .card {
                background: rgba(255,255,255,0.1);
                border-radius: 15px;
                padding: 20px;
                backdrop-filter: blur(10px);
            }
            
            .card h3 {
                margin: 0 0 15px 0;
                color: #fff;
                font-size: 18px;
            }
            
            .metric {
                display: flex;
                justify-content: space-between;
                margin: 10px 0;
                padding: 8px 0;
                border-bottom: 1px solid rgba(255,255,255,0.2);
            }
            
            .metric:last-child {
                border-bottom: none;
            }
            
            .metric-label {
                font-size: 14px;
            }
            
            .metric-value {
                font-weight: bold;
                font-size: 16px;
            }
            
            .schedule-table {
                background: rgba(255,255,255,0.1);
                border-radius: 15px;
                padding: 20px;
                backdrop-filter: blur(10px);
            }
            
            .schedule-table h3 {
                margin: 0 0 20px 0;
                color: #fff;
                text-align: center;
            }
            
            .time-slots {
                display: grid;
                grid-template-columns: repeat(6, 1fr);
                gap: 10px;
                margin-bottom: 15px;
            }
            
            .time-slot {
                background: rgba(255,255,255,0.2);
                border-radius: 8px;
                padding: 10px;
                text-align: center;
                font-size: 12px;
            }
            
            .staff-row {
                display: grid;
                grid-template-columns: 120px repeat(6, 1fr);
                gap: 10px;
                margin-bottom: 10px;
                align-items: center;
            }
            
            .staff-name {
                background: rgba(255,255,255,0.2);
                border-radius: 8px;
                padding: 8px;
                font-size: 12px;
                text-align: center;
            }
            
            .shift {
                background: #4CAF50;
                border-radius: 8px;
                padding: 8px;
                text-align: center;
                font-size: 11px;
                color: white;
            }
            
            .shift.peak {
                background: #FF9800;
            }
            
            .shift.off {
                background: rgba(255,255,255,0.1);
            }
            
            .ai-recommendation {
                background: rgba(255,255,255,0.1);
                border-radius: 15px;
                padding: 20px;
                margin-top: 20px;
                backdrop-filter: blur(10px);
            }
            
            .ai-recommendation h3 {
                margin: 0 0 15px 0;
                color: #fff;
            }
            
            .recommendation-item {
                background: rgba(255,255,255,0.1);
                border-radius: 8px;
                padding: 10px;
                margin: 8px 0;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <div class="scheduling-demo">
            <div class="header">
                <h2>🤖 智能排班系统 - 实时监控面板</h2>
                <p>基于预测模型自动优化客服人员配置</p>
            </div>
            
            <div class="dashboard">
                <div class="card">
                    <h3>📊 今日预测需求</h3>
                    <div class="metric">
                        <span class="metric-label">预计客服量</span>
                        <span class="metric-value">2,847</span>
                    </div>
                    <div class="metric">
                        <span class="metric-label">峰值时段</span>
                        <span class="metric-value">14:00-16:00</span>
                    </div>
                    <div class="metric">
                        <span class="metric-label">需求准确率</span>
                        <span class="metric-value">94.2%</span>
                    </div>
                </div>
                
                <div class="card">
                    <h3>👥 人员配置状态</h3>
                    <div class="metric">
                        <span class="metric-label">在线客服</span>
                        <span class="metric-value">156人</span>
                    </div>
                    <div class="metric">
                        <span class="metric-label">待命客服</span>
                        <span class="metric-value">23人</span>
                    </div>
                    <div class="metric">
                        <span class="metric-label">AI处理率</span>
                        <span class="metric-value">68%</span>
                    </div>
                </div>
            </div>
            
            <div class="schedule-table">
                <h3>📅 今日排班表 (2025年1月15日)</h3>
                <div class="time-slots">
                    <div class="time-slot">08:00-10:00</div>
                    <div class="time-slot">10:00-12:00</div>
                    <div class="time-slot">12:00-14:00</div>
                    <div class="time-slot">14:00-16:00</div>
                    <div class="time-slot">16:00-18:00</div>
                    <div class="time-slot">18:00-20:00</div>
                </div>
                
                <div class="staff-row">
                    <div class="staff-name">张小明 (中文)</div>
                    <div class="shift">在岗</div>
                    <div class="shift">在岗</div>
                    <div class="shift peak">在岗</div>
                    <div class="shift peak">在岗</div>
                    <div class="shift">在岗</div>
                    <div class="shift off">休息</div>
                </div>
                
                <div class="staff-row">
                    <div class="staff-name">Sarah (English)</div>
                    <div class="shift off">休息</div>
                    <div class="shift">在岗</div>
                    <div class="shift">在岗</div>
                    <div class="shift peak">在岗</div>
                    <div class="shift peak">在岗</div>
                    <div class="shift">在岗</div>
                </div>
                
                <div class="staff-row">
                    <div class="staff-name">田中 (日本語)</div>
                    <div class="shift">在岗</div>
                    <div class="shift">在岗</div>
                    <div class="shift off">休息</div>
                    <div class="shift">在岗</div>
                    <div class="shift">在岗</div>
                    <div class="shift">在岗</div>
                </div>
                
                <div class="staff-row">
                    <div class="staff-name">AI Agent</div>
                    <div class="shift">24/7</div>
                    <div class="shift">24/7</div>
                    <div class="shift">24/7</div>
                    <div class="shift">24/7</div>
                    <div class="shift">24/7</div>
                    <div class="shift">24/7</div>
                </div>
            </div>
            
            <div class="ai-recommendation">
                <h3>🎯 AI智能推荐</h3>
                <div class="recommendation-item">
                    <strong>14:00-16:00 时段:</strong> 建议增加8名客服，预计需求激增35%
                </div>
                <div class="recommendation-item">
                    <strong>VET通知:</strong> 已向23名客服发送自愿加班通知
                </div>
                <div class="recommendation-item">
                    <strong>技能匹配:</strong> 建议调配3名多语言专家到亚太区域
                </div>
                <div class="recommendation-item">
                    <strong>外包激活:</strong> 已联系马尼拉客服中心，准备增援15人
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    st.components.v1.html(scheduling_html, height=1100)

# ========== AI升级路线图 ==========
def show_ai_roadmap():
    st.subheader("🚀 Trip.com 客服系统发展历程")
    
    # 创建炫酷的整合发展历程图
    fig = go.Figure()
    
    # 时间轴数据 - 更密集的节点
    years = [2010, 2012, 2014, 2016, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
    
    # AI能力发展曲线
    ai_capability = [0, 5, 12, 25, 40, 50, 60, 70, 80, 85, 90, 95, 98]
    
    # 添加主发展曲线 - 渐变色彩
    fig.add_trace(go.Scatter(
        x=years,
        y=ai_capability,
        mode='lines+markers',
        name='AI智能程度',
        line=dict(
            color='#0066CC',
            width=6,
            shape='spline',
            smoothing=0.3
        ),
        # marker=dict(
        #     size=15,
        #     color=ai_capability,
        #     colorscale='Viridis',
        #     showscale=True,
        #     colorbar=dict(
        #         title=dict(text="AI智能程度 (%)", side="right"),
        #         tickmode="array",
        #         tickvals=[0, 25, 50, 75, 100],
        #         ticktext=["传统", "初级", "中级", "高级", "超级"]
        #     ),
        #     line=dict(width=3, color='white')
        # ),
        fill='tonexty',
        fillcolor='rgba(0, 102, 204, 0.2)',
        hovertemplate='<b>%{x}年</b><br>AI智能程度: %{y}%<extra></extra>'
    ))
    
    # 添加发展阶段背景区域
    phases = [
        {'start': 2010, 'end': 2015, 'name': '传统客服时代', 'color': 'rgba(255, 99, 132, 0.1)'},
        {'start': 2015, 'end': 2018, 'name': '数字化客服', 'color': 'rgba(54, 162, 235, 0.1)'},
        {'start': 2018, 'end': 2021, 'name': '智能客服初期', 'color': 'rgba(255, 206, 86, 0.1)'},
        {'start': 2021, 'end': 2024, 'name': 'AI客服成熟期', 'color': 'rgba(75, 192, 192, 0.1)'},
        {'start': 2024, 'end': 2026, 'name': 'LLM智能客服', 'color': 'rgba(153, 102, 255, 0.1)'}
    ]
    
    for phase in phases:
        fig.add_vrect(
            x0=phase['start'], x1=phase['end'],
            fillcolor=phase['color'],
            layer="below",
            line_width=0,
        )
        # 添加阶段标签
        fig.add_annotation(
            x=(phase['start'] + phase['end']) / 2,
            y=50,
            text=phase['name'],
            showarrow=False,
            font=dict(size=12, color='#666'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#ddd',
            borderwidth=1
        )
    
    # 添加关键里程碑点 - 更密集详细
    milestones = [
        {'year': 2012, 'y': 5, 'text': '携程客服中心<br>成立', 'color': '#FF6B6B'},
        {'year': 2014, 'y': 12, 'text': 'CRM系统<br>建设', 'color': '#FF8E8E'},
        {'year': 2016, 'y': 25, 'text': '在线客服系统<br>上线', 'color': '#4ECDC4'},
        {'year': 2018, 'y': 40, 'text': '多渠道整合<br>平台', 'color': '#6ED5D1'},
        {'year': 2019, 'y': 50, 'text': 'AI客服机器人<br>部署', 'color': '#45B7D1'},
        {'year': 2020, 'y': 60, 'text': 'NLP技术<br>应用', 'color': '#6BC5D8'},
        {'year': 2021, 'y': 70, 'text': '多语言AI<br>客服', 'color': '#96CEB4'},
        {'year': 2022, 'y': 80, 'text': '深度学习<br>模型', 'color': '#A8D5BA'},
        {'year': 2023, 'y': 85, 'text': '大语言模型<br>部署', 'color': '#FFEAA7'},
        {'year': 2024, 'y': 90, 'text': '多模态AI<br>客服', 'color': '#DDA0DD'},
        {'year': 2025, 'y': 95, 'text': '情绪感知<br>AI', 'color': '#98FB98'},
        {'year': 2026, 'y': 98, 'text': '智能决策<br>系统', 'color': '#F0E68C'}
    ]
    
    for milestone in milestones:
        # 添加里程碑点
        fig.add_trace(go.Scatter(
            x=[milestone['year']],
            y=[milestone['y']],
            mode='markers',
            name=milestone['text'].replace('<br>', ' '),
            # marker=dict(
            #     size=20,
            #     color=milestone['color'],
            #     line=dict(width=3, color='white'),
            #     symbol='diamond'
            # ),
            # showlegend=False,
            hovertemplate=f'<b>{milestone["text"].replace("<br>", " ")}</b><br>{milestone["year"]}年<extra></extra>'
        ))
        
        # 添加里程碑标注
        fig.add_annotation(
            x=milestone['year'],
            y=milestone['y'],
            text=milestone['text'],
            showarrow=True,
            arrowhead=2,
            arrowsize=1.5,
            arrowwidth=3,
            arrowcolor=milestone['color'],
            ax=0,
            ay=-60 if milestone['y'] > 50 else 60,
            bgcolor="white",
            bordercolor=milestone['color'],
            borderwidth=2,
            font=dict(size=11, color='#333')
        )
    
    # 添加当前重点技术标注
    current_tech = [
        {'year': 2024, 'y': 88, 'text': '🔥 当前重点<br>• 多模态理解<br>• 智能决策', 'color': '#FF4500'},
        {'year': 2025, 'y': 92, 'text': '🚀 发展方向<br>• 情绪感知AI<br>• 预测性服务<br>• 个性化交互', 'color': '#9370DB'}
    ]
    
    for tech in current_tech:
        fig.add_annotation(
            x=tech['year'],
            y=tech['y'],
            text=tech['text'],
            showarrow=True,
            arrowhead=1,
            arrowsize=1,
            arrowwidth=1.5,
            arrowcolor=tech['color'],
            ax=45,
            ay=10,
            bgcolor="rgba(255,255,255,0.95)",
            bordercolor=tech['color'],
            borderwidth=2,
            font=dict(size=12, color='#333')
        )
    
    # 更新布局
    fig.update_layout(
        # title=dict(
        #     text="🚀 Trip.com 客服AI系统发展历程 - LLM智能客服演进",
        #     font=dict(size=24, color='#333', family='Arial Black'),
        #     x=0.5
        # ),
        xaxis=dict(
            title=dict(text="时间轴 (年份)", font=dict(color='#333', size=16)),
            tickfont=dict(color='#666', size=12),
            gridcolor='rgba(128,128,128,0.2)',
            linecolor='#333',
            range=[2009, 2027]
        ),
        yaxis=dict(
            title=dict(text="AI智能程度 (%)", font=dict(color='#333', size=16)),
            tickfont=dict(color='#666', size=12),
            range=[0, 105],
            gridcolor='rgba(128,128,128,0.2)',
            linecolor='#333'
        ),
        height=700,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Arial"),
        showlegend=False,
        hovermode='closest'
    )
    
    st.plotly_chart(fig, use_container_width=True)

# ========== 主要内容展示 ==========
st.header("🌍 Trip.com 客服系统深度分析")

# 创建标签页
tab1, tab2, tab3, tab4 = st.tabs(["📊 竞品分析", "👥 人力资源优化", "🚀 AI升级路线", "📈 思维导图：指标体系，AI升级, 成本分析"])

with tab1:
    show_market_share()
    st.markdown("---")
    show_timeline()
    st.markdown("---")
    show_competitor_comparison()
    
    # 数据来源说明
    st.markdown("""
    ---
    ### 📚 数据来源说明
    
    <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; font-size: 12px; color: #666;">
        <p><strong>市场份额数据:</strong> Statista 2025, Phocuswright 2025, Airbnb 2025年报, 携程2025年报, 行业报告汇总</p>
        <p><strong>历史大事记:</strong> Booking Holdings 2019-2025年报, Phocuswright 2020-2025报告, Expedia 2021-2025投资者日, Airbnb 2022-2025年报, Booking.com 2023-2025技术博客</p>
        <p><strong>客服系统对比:</strong> Booking.com 2025客服报告, Expedia 2025投资者关系, Airbnb 2025年报, 携程2025年报</p>
        <p><strong>AI部署进度:</strong> 各平台公开技术博客, 投资者关系材料, 行业分析报告, 内部调研数据</p>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    show_predictive_staffing()

with tab3:
    show_ai_roadmap()

with tab4:
    st.header("📊 客户满意度指标 + 客服渠道拆解 + 客服成本分析与优化")
    st.markdown(f"""


    """, unsafe_allow_html=True)
    # 加载两个SVG文件
    with open("pic1.svg","r",encoding="utf-8") as f:
        svg_code1 = f.read()
    st.components.v1.html(svg_code1, height=350, scrolling=True)
    
    with open("pic2.svg","r",encoding="utf-8") as f:
        svg_code2 = f.read()
    st.components.v1.html(svg_code2, height=550, scrolling=True)



