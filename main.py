import streamlit as st
import pandas as pd
import plotly.express as px

df_temp = pd.read_csv('./data/temperature.csv')
df_co2 = pd.read_csv('./data/co2.csv')
df_return = pd.read_csv('./data/return.csv')
df_table = pd.read_csv('./data/table_summary.csv')
df_weight = pd.read_csv('./data/weight.csv')

# Page icon: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title='Net Zero Carbon Portfolio',
                   page_icon=':house_with_garden:',
                   layout='wide')

st.title('Net-Zero Carbon Portfolio🌍🌱')
st.write('🏜️ Climate change poses risks to financial portfolios through physical and transition impacts. Extreme weather events and policy changes can harm assets and industries, affecting returns. To manage these risks and align with global climate goals, investors need to allocate capital toward companies and projects working towards net-zero emissions. This strategy not only reduces exposure to climate risks but also capitalizes on opportunities in sustainable sectors, ensuring long-term resilience and financial performance.')
st.write('🎯 In applying net-zero alignment to the portfolio, we focus on constructing a portfolio that targets carbon budget reduction while minimizing tracking error risk. To achieve this, we invest in **Thai stocks** of companies that are actively reducing their carbon footprint and transitioning towards a low-carbon economy.')
st.write('[Image]')
st.write('Note: This project will be completed on 26 Mar 2024. Some results are currently being simulated for illustrative purposes only.')

st.markdown("""---""")

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Reduce Temperature🌡️:")
    st.subheader('2.3°C')
with right_column:
    st.subheader("Reduce Carbon Footprint👣:")
    st.subheader('52%')

st.markdown("""---""")

# Set color for chart
color_benchmark = '#458ccc'
color_portfolio = '#0fac03'

fig_temp = px.line(
    df_temp,
    x='year',
    y=['portfolio', 'benchmark'],
    title="<b>Temperature</b>",
    template="plotly_white",
    color_discrete_map={
    "portfolio": color_portfolio,  
    "benchmark": color_benchmark  
    }
)
fig_temp.update_layout(
    legend_title_text='Asset',
    xaxis_title="Year",  
    yaxis_title="Degrees Celsius",
    #title_x=0.4,
    showlegend=False
)

#st.plotly_chart(fig_temp, use_container_width=True)

fig_co2 = px.line(
    df_co2,
    x='year',
    y=['portfolio', 'benchmark'],
    title="<b>Carbon Footprint</b>",
    template="plotly_white",
    color_discrete_map={
    "portfolio": color_portfolio,  
    "benchmark": color_benchmark   
    }
)
fig_co2.update_layout(
    legend_title_text='Asset',
    xaxis_title="Year",  
    yaxis_title="Megatons CO2e", 
    #title_x=0.4,
    showlegend=False,
)

#st.plotly_chart(fig_co2, use_container_width=True)

# Plot Temperature and CO2
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_temp, use_container_width=True)
right_column.plotly_chart(fig_co2, use_container_width=True)


col1, col2 = st.columns(2)

# Display summary table
with col2:
    st.dataframe(df_table, hide_index=True)

# Display Legend
with col1:
    st.markdown(
        """
        <div style="text-align:center">
            <p><strong>Asset</strong></p>
            <div>
                <div style="display: inline-block; border: 4px solid #0fac03; width: 50px;"></div> Portfolio
            </div>
            <br>
            <div>
                <div style="display: inline-block; border: 4px solid #458ccc; width: 50px;"></div> Benchmark
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# Cumulative return
fig_return = px.line(
    df_return,
    x='year',
    y=['portfolio', 'benchmark'],
    title="<b>Cumulative return</b>",
    template="plotly_white",
    color_discrete_map={
    "portfolio": color_portfolio,  
    "benchmark": color_benchmark 
    }
)
fig_return.update_layout(
    legend_title_text='Asset',
    xaxis_title="Year", 
    yaxis_title="%", 
    title_x=0.45,
    showlegend=False
)

# Plot cumulative return
st.plotly_chart(fig_return, use_container_width=True)

fig_weight = px.histogram(df_weight, y="sector", x=['benchmark', 'portfolio'],
            barmode='group', height=700, title="<b>Weight in each Sector</b>",
             color_discrete_map={
             "portfolio": color_portfolio,  
             "benchmark": color_benchmark
 }   
)
fig_weight.update_layout(
     legend_title_text='Asset',
     xaxis_title="%", 
     yaxis_title="Sector", 
     title_x=0.45,
     showlegend=True
 )

st.plotly_chart(fig_weight, use_container_width=True)

# Hide Streamlit Style
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)
