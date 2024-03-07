import streamlit as st
import pandas as pd
import plotly.express as px

df_temp = pd.read_csv('./data/temperature.csv')
df_co2 = pd.read_csv('./data/co2.csv')
df_return = pd.read_csv('./data/return.csv')
df_table = pd.read_csv('./data/table_summary.csv')

# Page icon: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title='Net Zero Carbon Portfolio',
                   page_icon=':house_with_garden:',
                   layout='wide')

st.title('Net Zero Carbon Portfolio')
st.write('1. How do temperatures and carbon affect the Earth?')
st.write('2. How can financial innovation help to solve this problem?')
st.write('3. Add some picture to grab attention')
st.write('4. What we do?')
st.write("(Maybe P'Boss is probably the best at writing this haha)")

st.markdown("""---""")

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Reduce Temperature:")
    st.subheader('2.3°C')
with right_column:
    st.subheader("Reduce CO2:")
    st.subheader('52%')

st.markdown("""---""")

fig_temp = px.line(
    df_temp,
    x='year',
    y=['portfolio', 'benchmark'],
    title="<b>Temperature</b>",
    template="plotly_white",
    color_discrete_map={
    "portfolio": "green",  
    "benchmark": "red"  
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
    "portfolio": "green",  
    "benchmark": "red"   
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
                <div style="display: inline-block; border: 2px solid green; width: 50px;"></div> Portfolio
            </div>
            <br>
            <div>
                <div style="display: inline-block; border: 2px solid red; width: 50px;"></div> Benchmark
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
    "portfolio": "green",  
    "benchmark": "red" 
    }
)

fig_return.update_layout(
    legend_title_text='Asset',
    xaxis_title="Year", 
    yaxis_title="%", 
    #title_x=0.4,
    showlegend=False
)

# Plot cumulative return
st.plotly_chart(fig_return, use_container_width=True)