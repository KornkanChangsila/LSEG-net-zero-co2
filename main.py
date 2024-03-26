import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df_carbon = pd.read_csv('./data_new/carbon_result.csv')
df_temp = pd.read_csv('./data_new/temp_result.csv')
df_return = pd.read_csv('./data_new/return_result.csv')
df_w_2020 = pd.read_csv('./data_new/w_2020.csv')
df_w_2021 = pd.read_csv('./data_new/w_2021.csv')
df_w_2022 = pd.read_csv('./data_new/w_2022.csv')
df_w_2023 = pd.read_csv('./data_new/w_2023.csv')

# Page icon: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title='Net Zero Carbon Portfolio',
                   page_icon=':house_with_garden:',
                   layout='wide')

st.title('Net-Zero Carbon Portfolio🌍🌱')

st.write('🏜️ Climate change poses risks to financial portfolios through physical and transition impacts. Extreme weather events and policy changes can harm assets and industries, affecting returns. To manage these risks and align with global climate goals, investors need to allocate capital toward companies and projects working towards net-zero emissions. This strategy not only reduces exposure to climate risks but also capitalizes on opportunities in sustainable sectors, ensuring long-term resilience and financial performance.')
st.image('./data/Screenshot 2024-03-08 170343.png')
st.write('🎯 In applying net-zero alignment to the portfolio, we focus on constructing a portfolio that targets carbon budget reduction while minimizing tracking error risk. To achieve this, we invest in **Thai stocks** of companies that are actively reducing their carbon footprint and transitioning towards a low-carbon economy.')

st.markdown("""---""")

st.write('Benchmark = SET100')
st.write('CI-GMBCTS = Carbon Intensity - Climate Transition Score')
st.write('CI-GMBE = Carbon Intensity - Environmental Pillar Score')
st.write('NE-GMBCTS = Normalised Emission - Climate Transition Score')

st.markdown("""---""")

# Set color for chart
color_benchmark = '#EA4335'
color_ci_gmbcts = '#34A853'
color_ci_gmbe = '#4285F4'
color_ne_gmbcts = '#FBBC05'

data = {
    'year': [2020, 2021, 2022, 2023],
    'Benchmark': [5724576.00, 6019068.00, 5723520.00, 5561550.00],
    'CI-GMBCTS': [5319455.00, 4504747.00, 433735.00, 1223356.00],
    'CI-GMBE': [5412049.00, 5816127.00, 6221760.00, 7164297.00],
    'NE-GMBCTS': [4957856.00, 4329931.00, 421002.00, 1144883.00]
}
df_temp = pd.DataFrame(data)

fig_carbon = px.line(
    df_temp,
    x='year',
    y=['Benchmark', 'CI-GMBCTS', 'CI-GMBE', 'NE-GMBCTS'],
    title="<b>Carbon Footprint (Scope1 + Scope2)</b>",
    template="plotly_white",
    color_discrete_map={
        "Benchmark": color_benchmark,  
        "CI-GMBCTS": color_ci_gmbcts,
        'CI-GMBE': color_ci_gmbe,
        'NE-GMBCTS': color_ne_gmbcts
    }
)
fig_carbon.update_layout(
    legend_title_text='Asset',
    xaxis_title="Year",  
    yaxis_title="Carbon Footprint (tCO2e)",
    title_x=0.35,
    showlegend=True,
    xaxis=dict(
        tickmode='array',
        tickvals=[2020, 2021, 2022, 2023]
    )
)

st.plotly_chart(fig_carbon, use_container_width=True)

data = {
    'year': [2020, 2021, 2022, 2023],
    'Benchmark': [2.97, 2.89, 2.85, 2.95],
    'CI-GMBCTS': [2.34, 2.19, 2.50, 2.76],
    'CI-GMBE': [2.52, 2.34, 2.75, 2.82],
    'NE-GMBCTS': [2.48, 2.32, 2.60, 2.78]
}
df_temp = pd.DataFrame(data)

fig_temp = px.line(
    df_temp,
    x='year',
    y=['Benchmark', 'CI-GMBCTS', 'CI-GMBE', 'NE-GMBCTS'],
    title="<b>Implied Temperature Rise</b>",
    template="plotly_white",
    color_discrete_map={
        "Benchmark": color_benchmark,  
        "CI-GMBCTS": color_ci_gmbcts,
        'CI-GMBE': color_ci_gmbe,
        'NE-GMBCTS': color_ne_gmbcts
    }
)
fig_temp.update_layout(
    legend_title_text='Asset',
    xaxis_title="Year",  
    yaxis_title="Degrees Celsius",
    title_x=0.4,
    showlegend=True,
    xaxis=dict(
        tickmode='array',
        tickvals=[2020, 2021, 2022, 2023]
    )
)

st.plotly_chart(fig_temp, use_container_width=True)

# # Cumulative return
# fig_return = px.line(
#     df_return,
#     x='year',
#     y=df_return.columns[1:5],
#     title="<b>Cumulative return</b>",
#     template="plotly_white",
#     color_discrete_map={
#         "Benchmark": color_benchmark,  
#         "CI-GMBCTS": color_ci_gmbcts,
#         'CI-GMBE': color_ci_gmbe,
#         'NE-GMBCTS': color_ne_gmbcts
#     }
# )
# fig_return.update_layout(
#     legend_title_text='Asset',
#     xaxis_title="Date", 
#     yaxis_title="Cumulative Return (%)", 
#     title_x=0.4,
#     showlegend=True,
#     height=1000, 
#     width=800,
# )

# # Plot cumulative return
# st.plotly_chart(fig_return, use_container_width=True)


# df_weight_long = df_w_2020.melt(id_vars='Sector', var_name='Asset', value_name='Weight')

# # Create the histogram
# fig_weight = px.bar(
#     df_weight_long, 
#     x='Weight', 
#     y='Sector', 
#     color='Asset', 
#     barmode='group',
#     height=700, 
#     title="<b>Weight in each Sector 2020</b>",
#     color_discrete_map={
#         "Benchmark": color_benchmark,  
#         "CI-GMBCTS": color_ci_gmbcts,
#         'CI-GMBE': color_ci_gmbe,
#         'NE-GMBCTS': color_ne_gmbcts
#     }
# )

# fig_weight.update_layout(
#     legend_title_text='Asset',
#     xaxis_title="%", 
#     yaxis_title="Sector", 
#     title_x=0.4,
#     showlegend=True
# )

# # Weight 2020
# df_weight_long = df_w_2020.melt(id_vars='Sector', var_name='Asset', value_name='Weight')

# # Create the histogram
# fig_weight = px.bar(
#     df_weight_long, 
#     x='Weight', 
#     y='Sector', 
#     color='Asset', 
#     barmode='group',
#     height=700, 
#     title="<b>Weight in each Sector 2020</b>",
#     color_discrete_map={
#         "Benchmark": color_benchmark,  
#         "CI-GMBCTS": color_ci_gmbcts,
#         'CI-GMBE': color_ci_gmbe,
#         'NE-GMBCTS': color_ne_gmbcts
#     }
# )

# fig_weight.update_layout(
#     legend_title_text='Asset',
#     xaxis_title="%", 
#     yaxis_title="Sector", 
#     title_x=0.4,
#     showlegend=True
# )

# # Plot histogram
# st.plotly_chart(fig_weight, use_container_width=True)

# # Weight 2021
# df_weight_long = df_w_2021.melt(id_vars='Sector', var_name='Asset', value_name='Weight')

# # Create the histogram
# fig_weight = px.bar(
#     df_weight_long, 
#     x='Weight', 
#     y='Sector', 
#     color='Asset', 
#     barmode='group',
#     height=700, 
#     title="<b>Weight in each Sector 2021</b>",
#     color_discrete_map={
#         "Benchmark": color_benchmark,  
#         "CI-GMBCTS": color_ci_gmbcts,
#         'CI-GMBE': color_ci_gmbe,
#         'NE-GMBCTS': color_ne_gmbcts
#     }
# )

# fig_weight.update_layout(
#     legend_title_text='Asset',
#     xaxis_title="%", 
#     yaxis_title="Sector", 
#     title_x=0.4,
#     showlegend=True
# )

# # Plot histogram
# st.plotly_chart(fig_weight, use_container_width=True)

# # Weight 2022
# df_weight_long = df_w_2022.melt(id_vars='Sector', var_name='Asset', value_name='Weight')

# # Create the histogram
# fig_weight = px.bar(
#     df_weight_long, 
#     x='Weight', 
#     y='Sector', 
#     color='Asset', 
#     barmode='group',
#     height=700, 
#     title="<b>Weight in each Sector 2022</b>",
#     color_discrete_map={
#         "Benchmark": color_benchmark,  
#         "CI-GMBCTS": color_ci_gmbcts,
#         'CI-GMBE': color_ci_gmbe,
#         'NE-GMBCTS': color_ne_gmbcts
#     }
# )

# fig_weight.update_layout(
#     legend_title_text='Asset',
#     xaxis_title="%", 
#     yaxis_title="Sector", 
#     title_x=0.4,
#     showlegend=True
# )

# # Plot histogram
# st.plotly_chart(fig_weight, use_container_width=True)

# # Weight 2023
# df_weight_long = df_w_2023.melt(id_vars='Sector', var_name='Asset', value_name='Weight')

# # Create the histogram
# fig_weight = px.bar(
#     df_weight_long, 
#     x='Weight', 
#     y='Sector', 
#     color='Asset', 
#     barmode='group',
#     height=700, 
#     title="<b>Weight in each Sector 2023</b>",
#     color_discrete_map={
#         "Benchmark": color_benchmark,  
#         "CI-GMBCTS": color_ci_gmbcts,
#         'CI-GMBE': color_ci_gmbe,
#         'NE-GMBCTS': color_ne_gmbcts
#     }
# )

# fig_weight.update_layout(
#     legend_title_text='Asset',
#     xaxis_title="%", 
#     yaxis_title="Sector", 
#     title_x=0.4,
#     showlegend=True
# )

# # Plot histogram
# st.plotly_chart(fig_weight, use_container_width=True)

# Create a multiselect for asset selection
selected_assets = st.multiselect("Select Assets", df_return.columns[1:])

# Function to plot cumulative return chart for selected assets
def plot_cumulative_return(df, assets):
    fig_return = px.line(
        df,
        x='year',
        y=assets,
        title="<b>Cumulative return</b>",
        template="plotly_white",
        color_discrete_map={
            "Benchmark": color_benchmark,  
            "CI-GMBCTS": color_ci_gmbcts,
            'CI-GMBE': color_ci_gmbe,
            'NE-GMBCTS': color_ne_gmbcts
        }
    )
    fig_return.update_layout(
        legend_title_text='Asset',
        xaxis_title="Date",
        yaxis_title="Cumulative Return (%)",
        title_x=0.4,
        showlegend=True,
        height=1000,
        width=800,
    )
    st.plotly_chart(fig_return, use_container_width=True)

# Function to plot histogram for selected assets and year
def plot_histogram(df, assets, year):
    df_weight_long = df.melt(id_vars='Sector', var_name='Asset', value_name='Weight')
    fig_weight = px.bar(
        df_weight_long[df_weight_long['Asset'].isin(assets)],
        x='Weight',
        y='Sector',
        color='Asset',
        barmode='group',
        height=700,
        title=f"<b>Weight in Sector {year}</b>",
        color_discrete_map={
            "Benchmark": color_benchmark,  
            "CI-GMBCTS": color_ci_gmbcts,
            'CI-GMBE': color_ci_gmbe,
            'NE-GMBCTS': color_ne_gmbcts
        }
    )
    fig_weight.update_layout(
        legend_title_text='Asset',
        xaxis_title="%",
        yaxis_title="Sector",
        title_x=0.4,
        showlegend=True
    )
    st.plotly_chart(fig_weight, use_container_width=True)

# Plot charts based on selected assets
if selected_assets:
    plot_cumulative_return(df_return, selected_assets)
    plot_histogram(df_w_2020, selected_assets, 2020)
    plot_histogram(df_w_2021, selected_assets, 2021)
    plot_histogram(df_w_2022, selected_assets, 2022)
    plot_histogram(df_w_2023, selected_assets, 2023)

