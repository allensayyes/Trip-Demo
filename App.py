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
    
    # 各平台AI客服部署进度（基于实际验证调整）
    booking_ai = [10, 25, 45, 65, 75, 75, 75]  # 2017年推出但当前入口不明显
    expedia_ai = [5, 20, 40, 60, 80, 90, 95]   # 双端多模态AI客服表现最佳
    airbnb_ai = [15, 30, 50, 70, 70, 70, 70]   # 未发现AI聊天功能
    trip_ai = [8, 18, 35, 55, 75, 85, 90]      # TripGenie仅APP端支持多模态
    
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
    
    # 添加重要事件标注（基于实际验证调整）
    events = [
        {'year': 2017, 'y': 15, 'text': 'Booking小助手推出', 'color': '#FF6B6B'},
        {'year': 2020, 'y': 25, 'text': '疫情加速AI部署', 'color': '#FF6B6B'},
        {'year': 2021, 'y': 45, 'text': 'Expedia AI客服上线', 'color': '#4ECDC4'},
        {'year': 2022, 'y': 65, 'text': 'Airbnb社区化客服', 'color': '#45B7D1'},
        {'year': 2023, 'y': 80, 'text': 'Expedia多模态AI', 'color': '#4ECDC4'},
        {'year': 2023, 'y': 75, 'text': 'Trip.com TripGenie', 'color': '#0066CC'},
        {'year': 2024, 'y': 85, 'text': 'LLM多模态AI客服双端应用', 'color': '#FFEAA7'}
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
    
    # 各指标数据（基于实际验证调整）
    languages = [43, 25, 30, 20]  # 多语言支持（Booking 43种，其他保守估计）
    response_speed = [75, 85, 70, 80]  # 响应速度（Expedia双端表现最佳）
    resolution_rate = [70, 80, 75, 75]  # 解决率（基于AI客服可用性）
    cost_efficiency = [75, 90, 70, 80]  # 成本效率（多模态AI成本更高）
    
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
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📋 项目说明", "📊 竞品分析", "🚀 AI升级路线", "👥 人力资源优化", "📋 工单数据分析", "📈 思维导图"])

with tab1:
    st.markdown(f"""
    ### 📝 项目说明
    - 该 Demo 旨在直观呈现候选人以Senior Business Analyst的角色对携程国际业务（客服支持）的快速学习理解，并以此为切入点，激发正式面试中更深入的探讨与交流
    - 行业/竞对/历史数据来源于互联网公开信息，公开财报以及Trip.com 官方网站，存在一定误差，图表使用Plotly + HTML/CSS制作
    - 思维导图中大部分数字/权重为推断假设，使用基于JavaScript的代码可视化工具 - Mermaid制作，Draw.io美化 
    - 候选人相关过往项目经历请点击以下链接下载
    
    ### 📎 附件下载
    """, unsafe_allow_html=True)
    
    # 下载过往项目经历PDF文件
    col1, col2 = st.columns(2)
    
    with col1:
        with open("亚马逊项目 - 配送站评分系统.pdf", "rb") as f:
            pdf_bytes1 = f.read()
        
        st.download_button(
            label="📥 下载亚马逊配送站评分系统项目",
            data=pdf_bytes1,
            file_name="亚马逊配送站评分系统项目.pdf",
            mime="application/pdf"
        )
    
    with col2:
        with open("亚马逊项目 - 实时数据报表.pdf", "rb") as f:
            pdf_bytes2 = f.read()
        
        st.download_button(
            label="📥 下载亚马逊实时数据报表项目",
            data=pdf_bytes2,
            file_name="亚马逊实时数据报表项目.pdf",
            mime="application/pdf"
        )
    
    st.markdown("""
    ### 📋 开发日志
    <details>
    <summary><strong>点击展开查看开发历史</strong></summary>
    
    **v3.0 (2025-09-27 更新)**
    - ✨ 新增模拟客服工单系统：工单列表、数据分析、高频问题识别
    - ✨ 新增用户数字旅程分析：基于Shapley Value归因模型的双端对比分析
    - 🔧 数据准确性优化：基于实际验证调整各平台AI客服数据
    - 🎨 界面结构优化：标签页重新排序，思维导图拆分为两个SVG文件
    
    **v2.0 (2025-09-25 更新)**
    - ✨ 新增竞品分析模块：市场份额趋势、客服系统发展大事记、能力对比
    - ✨ 新增预测性人力资源优化模块：智能排班系统、优化模型展示
    - ✨ 新增AI客服升级路线图：项目进度管理、里程碑展示
    - 🎨 界面优化：多标签页布局、统一配色方案、响应式设计
    - 🔧 技术升级：从Mermaid迁移到Plotly，支持交互式图表
    
    **v1.0 (初始版本2025-09-23)**
    - 基础思维导图展示
    - 客服指标体系 + 客服渠道拆解 + 客服成本分析
    
    </details>
    """, unsafe_allow_html=True)

with tab2:
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
        <p><strong>AI客服验证:</strong> 基于2025年1月实际测试各平台网页端和APP端AI客服入口可用性</p>
        <p><strong>多模态功能:</strong> Expedia双端支持, Trip.com TripGenie仅APP端支持多模态</p>
        <p><strong>语言支持:</strong> Booking.com官方43种语言, 其他平台基于实际测试估算</p>
        <p><strong>数据标注:</strong> 部分数据为示例展示，实际数据以官方最新公布为准</p>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    show_ai_roadmap()

with tab4:
    show_predictive_staffing()

with tab5:
    # st.header("📋 模拟客服工单系统 - 数据分析界面")
    
    # 创建标签页
    ticket_tab1, ticket_tab2, ticket_tab3 = st.tabs(["📝 模拟工单数据", "📊 探索性数据分析EDA", "🎯 用户数字旅程分析"])
    
    with ticket_tab1:
        # st.subheader("📝 模拟客服工单数据")
        
        # 模拟工单数据
        import pandas as pd
        import random
        from datetime import datetime, timedelta
        
        # 生成模拟工单数据
        random.seed(42)
        n_tickets = 50
        
        user_ids = [f"U{random.randint(10000, 99999)}" for _ in range(n_tickets)]
        member_levels = random.choices(['普通会员', '银卡会员', '金卡会员', '钻石会员'], weights=[40, 30, 20, 10], k=n_tickets)
        ticket_numbers = [f"TK{random.randint(100000, 999999)}" for _ in range(n_tickets)]
        
        # 咨询原因分类
        inquiry_reasons = random.choices([
            '机票改签', '酒店预订', '支付问题', '账户登录', '退票申请',
            '行程变更', '会员权益', '发票申请', '密码重置', '订单查询'
        ], weights=[30, 20, 15, 10, 8, 7, 5, 3, 1, 1], k=n_tickets)
        
        # 机票改签的详细原因
        flight_change_reasons = [
            '改签费用不明确', '改签流程复杂', '无法在线改签', '改签规则不清晰',
            '改签时间限制', '改签条件不符合', '改签失败', '改签后座位问题'
        ]
        
        # 生成咨询原因
        inquiry_details = []
        for i in range(n_tickets):
            reason = random.choice(inquiry_reasons)
            if reason == '机票改签':
                detail = random.choice(flight_change_reasons)
            else:
                detail = f"{reason}相关问题"
            inquiry_details.append(detail)
        
        # 创建工单DataFrame
        tickets_df = pd.DataFrame({
            '用户ID': user_ids,
            '会员等级': member_levels,
            '工单号': ticket_numbers,
            '咨询原因': inquiry_reasons,
            '详细问题': inquiry_details,
            '创建时间': [datetime.now() - timedelta(days=random.randint(0, 30)) for _ in range(n_tickets)],
            '状态': random.choices(['待处理', '处理中', '已解决'], weights=[20, 30, 50], k=n_tickets)
        })
        
        # 显示工单表格
        st.dataframe(tickets_df, use_container_width=True)
        
        # 工单统计
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("总工单数", len(tickets_df))
        with col2:
            st.metric("待处理", len(tickets_df[tickets_df['状态'] == '待处理']))
        with col3:
            st.metric("处理中", len(tickets_df[tickets_df['状态'] == '处理中']))
        with col4:
            st.metric("已解决", len(tickets_df[tickets_df['状态'] == '已解决']))
    
    with ticket_tab2:
        # st.subheader("📊 探索性数据分析EDA")
        
        # 咨询原因分析
        st.markdown("### 🔍 咨询原因分布分析")
        
        # 统计咨询原因
        reason_counts = tickets_df['咨询原因'].value_counts()
        
        # 创建饼图
        fig_pie = go.Figure(data=[go.Pie(
            labels=reason_counts.index,
            values=reason_counts.values,
            hole=0.3,
            textinfo='label+percent',
            textfont_size=12
        )])
        
        fig_pie.update_layout(
            title="咨询原因分布",
            height=400
        )
        
        st.plotly_chart(fig_pie, use_container_width=True)
        
        # 高频问题分析
        st.markdown("### 📈 高频问题分析")
        
        # 统计详细问题
        detail_counts = tickets_df['详细问题'].value_counts().head(10)
        
        # 创建柱状图
        fig_bar = go.Figure(data=[go.Bar(
            x=detail_counts.values,
            y=detail_counts.index,
            orientation='h',
            marker_color='#0066CC',
            text=detail_counts.values,
            textposition='auto'
        )])
        
        fig_bar.update_layout(
            title="高频问题TOP10",
            xaxis_title="工单数量",
            yaxis_title="问题类型",
            height=500
        )
        
        st.plotly_chart(fig_bar, use_container_width=True)
        
        # 机票改签问题深度分析
        st.markdown("### ✈️ 机票改签问题深度分析")
        
        # 筛选机票改签相关工单
        flight_tickets = tickets_df[tickets_df['咨询原因'] == '机票改签']
        
        if len(flight_tickets) > 0:
            # 改签问题细分
            change_reason_counts = flight_tickets['详细问题'].value_counts()
            
            # 创建改签问题分析图
            fig_change = go.Figure(data=[go.Bar(
                x=change_reason_counts.index,
                y=change_reason_counts.values,
                marker_color='#FF6B6B',
                text=change_reason_counts.values,
                textposition='auto'
            )])
            
            fig_change.update_layout(
                title="机票改签问题细分分析",
                xaxis_title="问题类型",
                yaxis_title="工单数量",
                height=400,
                xaxis_tickangle=-45
            )
            
            st.plotly_chart(fig_change, use_container_width=True)
            
            # 改签问题根本原因分析
            st.markdown("#### 🎯 根本原因分析")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                **🔍 问题识别**
                - 改签费用不明确：用户不知道具体费用
                - 改签流程复杂：步骤过多，用户容易放弃
                - 无法在线改签：系统限制，必须人工处理
                - 改签规则不清晰：用户不理解政策
                """)
            
            with col2:
                st.markdown("""
                **💡 优化建议**
                - 优化改签费用展示：实时计算并清晰显示
                - 简化改签流程：减少步骤，提高成功率
                - 开放在线改签：允许用户自助操作
                - 优化规则说明：用通俗语言解释政策
                """)
            
            # 会员等级分析
            st.markdown("#### 👥 会员等级分析")
            
            member_analysis = flight_tickets['会员等级'].value_counts()
            
            fig_member = go.Figure(data=[go.Bar(
                x=member_analysis.index,
                y=member_analysis.values,
                marker_color=['#FFEAA7', '#DDA0DD', '#98FB98', '#F0E68C'],
                text=member_analysis.values,
                textposition='auto'
            )])
            
            fig_member.update_layout(
                title="改签问题会员等级分布",
                xaxis_title="会员等级",
                yaxis_title="工单数量",
                height=300
            )
            
            st.plotly_chart(fig_member, use_container_width=True)
        
        # 数据洞察总结
        st.markdown("---")
        st.markdown("### 💡 数据洞察总结")
        
        st.markdown("""
        **🔍 关键发现**
        - 机票改签是最高频问题，占工单总量的30%
        - 改签费用不明确和流程复杂是主要痛点
        - 普通会员改签问题最多，说明产品易用性有待提升
        
        **🎯 优化机会**
        - 优化改签流程，减少人工介入
        - 提升产品易用性，降低客服依赖
        - 加强自助服务，提高问题解决率
        
        **💰 预期效果**
        - 改签相关工单减少60%
        - 客服成本降低25%
        - 客户满意度提升15%
        """)
    
    with ticket_tab3:
        st.subheader("🎯 博弈论视角的Shapley Value归因模型")
        
        st.markdown("""
        ### 🔍 分析目标
        通过Shapley Value归因模型，分析用户在双端（网页端/APP端）的完整数字旅程，
        识别导致用户最终联系客服的关键页面和交互环节。
        """)
        
        # 用户旅程数据模拟
        st.markdown("### 📱 用户数字旅程数据")
        
        # 模拟用户旅程数据
        journey_data = {
            '用户ID': ['U12345', 'U12345', 'U12345', 'U12345', 'U12345', 'U12345'],
            '时间戳': ['09:00:00', '09:02:15', '09:05:30', '09:08:45', '09:12:00', '09:15:30'],
            '页面/功能': ['首页', '机票搜索', '航班选择', '改签页面', '改签失败', '联系客服'],
            '端类型': ['APP', 'APP', 'APP', 'APP', 'APP', 'APP'],
            '操作类型': ['浏览', '搜索', '选择', '点击改签', '系统错误', '人工客服'],
            '停留时长(秒)': [45, 120, 180, 300, 60, 0],
            '是否成功': [True, True, True, False, False, True]
        }
        
        journey_df = pd.DataFrame(journey_data)
        st.dataframe(journey_df, use_container_width=True)
        
        # Shapley Value归因分析
        st.markdown("### 🎯 Shapley Value归因分析")
        
        # 模拟Shapley Value结果
        shapley_data = {
            '页面/功能': ['改签页面', '航班选择', '机票搜索', '首页', '其他'],
            'Shapley Value': [0.45, 0.25, 0.15, 0.10, 0.05],
            '归因解释': [
                '改签页面设计复杂，用户无法完成操作',
                '航班信息展示不清晰，用户选择困难',
                '搜索条件设置复杂，用户容易出错',
                '首页引导不明确，用户路径混乱',
                '其他因素影响'
            ]
        }
        
        shapley_df = pd.DataFrame(shapley_data)
        
        # 创建Shapley Value归因图
        fig_shapley = go.Figure(data=[go.Bar(
            x=shapley_df['Shapley Value'],
            y=shapley_df['页面/功能'],
            orientation='h',
            marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'],
            text=shapley_df['Shapley Value'],
            textposition='auto',
            hovertemplate='<b>%{y}</b><br>Shapley Value: %{x}<br>%{customdata}<extra></extra>',
            customdata=shapley_df['归因解释']
        )])
        
        fig_shapley.update_layout(
            title="Shapley Value归因分析 - 导致客服咨询的关键因素",
            xaxis_title="Shapley Value (归因权重)",
            yaxis_title="页面/功能",
            height=400
        )
        
        st.plotly_chart(fig_shapley, use_container_width=True)
        
        # 双端对比分析
        st.markdown("### 📱 双端对比分析")
        
        # 模拟双端数据
        platform_data = {
            '端类型': ['APP端', '网页端', 'APP端', '网页端', 'APP端', '网页端'],
            '问题页面': ['改签页面', '改签页面', '航班选择', '航班选择', '支付页面', '支付页面'],
            '问题类型': ['流程复杂', '按钮不明显', '信息不清晰', '加载缓慢', '支付失败', '支付失败'],
            '影响权重': [0.35, 0.30, 0.20, 0.15, 0.10, 0.08]
        }
        
        platform_df = pd.DataFrame(platform_data)
        
        # 创建双端对比图
        fig_platform = go.Figure()
        
        # APP端数据
        app_data = platform_df[platform_df['端类型'] == 'APP端']
        fig_platform.add_trace(go.Bar(
            name='APP端',
            x=app_data['问题页面'],
            y=app_data['影响权重'],
            marker_color='#0066CC',
            text=app_data['影响权重'],
            textposition='auto'
        ))
        
        # 网页端数据
        web_data = platform_df[platform_df['端类型'] == '网页端']
        fig_platform.add_trace(go.Bar(
            name='网页端',
            x=web_data['问题页面'],
            y=web_data['影响权重'],
            marker_color='#FF6B6B',
            text=web_data['影响权重'],
            textposition='auto'
        ))
        
        fig_platform.update_layout(
            title="双端问题页面对比分析",
            xaxis_title="问题页面",
            yaxis_title="影响权重",
            barmode='group',
            height=400
        )
        
        st.plotly_chart(fig_platform, use_container_width=True)
        
        # 具体问题分析
        st.markdown("### 🔧 具体问题分析")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **📱 APP端主要问题**
            - **改签页面流程复杂** (权重35%)
              - 步骤过多，用户容易放弃
              - 界面元素过多，用户困惑
            - **航班选择信息不清晰** (权重20%)
              - 价格信息展示不突出
              - 时间信息对比困难
            - **支付页面失败率高** (权重10%)
              - 支付流程中断
              - 错误提示不明确
            """)
        
        with col2:
            st.markdown("""
            **💻 网页端主要问题**
            - **改签按钮不明显** (权重30%)
              - 按钮位置不突出
              - 颜色对比度不够
            - **航班选择加载缓慢** (权重15%)
              - 页面响应时间长
              - 用户体验差
            - **支付页面失败率高** (权重8%)
              - 兼容性问题
              - 网络连接不稳定
            """)
        
        # 优化建议
        st.markdown("### 💡 基于归因分析的优化建议")
        
        st.markdown("""
        **🎯 高优先级优化 (Shapley Value > 0.3)**
        1. **改签页面重构**
           - 简化改签流程，减少步骤
           - 优化界面设计，突出关键信息
           - 增加进度指示器
        
        2. **航班选择页面优化**
           - 重新设计信息展示布局
           - 增加价格对比功能
           - 优化时间选择交互
        
        **🔧 中优先级优化 (Shapley Value 0.1-0.3)**
        3. **搜索页面改进**
           - 简化搜索条件设置
           - 增加智能推荐
           - 优化搜索结果展示
        
        4. **首页引导优化**
           - 增加改签功能入口
           - 优化用户路径引导
           - 增加帮助提示
        
        **📊 预期效果**
        - 改签成功率提升40%
        - 客服咨询量减少50%
        - 用户满意度提升25%
        - 双端体验一致性提升
        """)
        
        # 技术实现说明
        st.markdown("---")
        st.markdown("### 🔬 技术实现说明")
        
        st.markdown("""
        **Shapley Value归因模型原理**
        - 基于博弈论，公平分配每个因素对最终结果的贡献
        - 考虑因素间的交互效应，避免简单线性归因
        - 适用于多因素复杂系统的归因分析
        
        **数据收集维度**
        - 用户行为轨迹：页面访问、点击、停留时间
        - 交互事件：按钮点击、表单填写、错误发生
        - 系统状态：页面加载时间、错误日志、性能指标
        - 用户属性：设备类型、网络环境、使用习惯
        
        **模型优势**
        - 客观性：基于数学原理，避免主观判断
        - 完整性：考虑所有可能的影响因素组合
        - 可解释性：每个因素的贡献度清晰可量化
        """)

with tab6:
    st.markdown(f"""
    ### 📊 客户满意度指标 + 客服渠道拆解 + 客服成本分析与优化
    """, unsafe_allow_html=True)
    # 加载两个SVG文件
    with open("pic1.svg","r",encoding="utf-8") as f:
        svg_code1 = f.read()
    st.components.v1.html(svg_code1, height=350, scrolling=True)
    
    with open("pic2.svg","r",encoding="utf-8") as f:
        svg_code2 = f.read()
    st.components.v1.html(svg_code2, height=550, scrolling=True)




