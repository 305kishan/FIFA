# Core Package
import streamlit as st

# EDA Packages
import pandas as pd
import numpy as np

# Visualization Packages
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")
import seaborn as sns

# Visulaization Packages 2
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as py

# Other Required Packages
import string
import webbrowser

@st.cache(suppress_st_warning=True)

def main_page():
    st.title("FIFA Video Games")

    st.markdown(
        """
        <style>
        .reportview-container {
            background: url("")
        }
        .sidebar .sidebar-content {
            background: url("")
        }
        </style>
        """,
        unsafe_allow_html=True)

    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

def create_list(data):
    club_list = data['club_name'].to_list()
    club_list = np.unique(club_list).tolist()

    country_list = data['nationality_name'].to_list()
    country_list = np.unique(country_list).tolist()
    
    player_list = data['short_name'].to_list()
    player_list = np.unique(player_list).tolist()

    return club_list, country_list, player_list

def select_edition(x):
    if x == "FIFA15":
        url = "https://raw.githubusercontent.com/305kishan/FIFA/main/data/FIFA15.csv"
        data = pd.read_csv(url,sep=',')
    elif x == "FIFA16":
        url = "https://raw.githubusercontent.com/305kishan/FIFA/main/data/FIFA16.csv"
        data = pd.read_csv(url,sep=',')
    elif x == "FIFA17":
        url = "https://raw.githubusercontent.com/305kishan/FIFA/main/data/FIFA17.csv"
        data = pd.read_csv(url,sep=',')
    elif x == "FIFA18":
        url = "https://raw.githubusercontent.com/305kishan/FIFA/main/data/FIFA18.csv"
        data = pd.read_csv(url,sep=',')
    elif x == "FIFA19":
        url = "https://raw.githubusercontent.com/305kishan/FIFA/main/data/FIFA19.csv"
        data = pd.read_csv(url,sep=',')
    elif x == "FIFA20":
        url = "https://raw.githubusercontent.com/305kishan/FIFA/main/data/FIFA20.csv"
        data = pd.read_csv(url,sep=',')
    elif x == "FIFA21":
        url = "https://raw.githubusercontent.com/305kishan/FIFA/main/data/FIFA21.csv"
        data = pd.read_csv(url,sep=',')
    else:
        url = "https://raw.githubusercontent.com/305kishan/FIFA/main/data/FIFA22.csv"
        data = pd.read_csv(url,sep=',')

    return data

def selectbox_edition():
    option = st.selectbox('Select a FIFA editon',('FIFA22', 'FIFA21', 'FIFA20', 'FIFA19', 'FIFA18', 'FIFA17', 'FIFA16', 'FIFA15'))
    data = select_edition(option)
    return data

def radiobutton_analysisof():
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: space-evenly;} </style>', unsafe_allow_html=True)
    st.write('<style>div.st-bf{flex-direction:row;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)
    analysisof=st.radio("What Would you like to Analyse",("Club","Country"))
    return analysisof

def nav_page(club_list, country_list, player_list):

    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    if st.sidebar.button("Show Club Names"):
        st.sidebar.write(club_list)
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    if st.sidebar.button("Show Country Names"):
        st.sidebar.write(country_list)
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    if st.sidebar.button("Show Player Names"):
        st.sidebar.write(player_list)
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    
    st.sidebar.write("Reach Me Here!")
    link = '[GitHub](https://github.com/305kishan)'
    st.sidebar.markdown(link, unsafe_allow_html=True)
    link = '[Kaggle](https://www.kaggle.com/kishan305)'
    st.sidebar.markdown(link, unsafe_allow_html=True)
    link = '[LinkedIn](https://www.linkedin.com/in/305kishan/)'
    st.sidebar.markdown(link, unsafe_allow_html=True)
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)


def club_value(x):
    squadvalue = 0
    for i in range(0, len(x)):
        squadvalue+=x.iloc[i]['value_eur']
    
    squadvalue = squadvalue/1000000
    return squadvalue

def club_wage(x):
    squadwage = 0
    for i in range(0, len(x)):
        squadwage+=x.iloc[i]['wage_eur']
    
    squadwage = squadwage/1000000
    return squadwage

def average_age(x):
    avg_age = x["age"].mean()
    avg_age = round(avg_age,1)
    return avg_age

def average_ovr(x):
    avg_ovr = x["overall"].mean()
    avg_ovr = int(avg_ovr)
    return avg_ovr

def playerscount(x):
    r,c = x.shape
    return r

def plot_age(data1):
    plt.figure(figsize= (15,7))
    ax = sns.countplot(x='age', data=data1, palette='bright')
    ax.set_title(label='Count of Players having Age of', fontsize=18)
    ax.set_xlabel(xlabel='Age', fontsize=16)
    ax.set_ylabel(ylabel='Count', fontsize=16)
    st.pyplot()

def plot_ovr(data1):
    plt.figure(figsize= (15,7))
    ax = sns.countplot(x='overall', data=data1, palette='bright')
    ax.set_title(label='Count of Players having OVR of', fontsize=18)
    ax.set_xlabel(xlabel='OVR', fontsize=16)
    ax.set_ylabel(ylabel='Count', fontsize=16)
    st.pyplot()

def plot_nationality(data1):
    plt.figure(figsize= (15,7))
    ax = sns.countplot(x='nationality_name', data=data1, palette='bright')
    ax.set_title(label='Count of Players on Basis of NATIONALITY', fontsize=18)
    ax.set_xlabel(xlabel='Nationality', fontsize=16)
    ax.set_ylabel(ylabel='Count', fontsize=16)
    plt.xticks(rotation=30, fontsize=12)
    st.pyplot()

def plot_contractexp(data1): 
    plt.figure(figsize= (15,7))
    ax = sns.countplot(x='club_contract_valid_until', data=data1, palette='bright')
    ax.set_title(label='Count of Players on Basis of Contract Expiration', fontsize=18)       
    ax.set_xlabel(xlabel='Contract Expiration', fontsize=16)
    ax.set_ylabel(ylabel='Count', fontsize=16)
    plt.xticks(rotation=30, fontsize=12)
    st.pyplot()
 
def plot_position(data1):
    plt.figure(figsize= (15,7))
    ax = sns.countplot(x='player_positions', data=data1, palette='bright')
    ax.set_title(label='Count of Players on Basis of Positions', fontsize=18)          
    ax.set_xlabel(xlabel='Positions', fontsize=16)
    ax.set_ylabel(ylabel='Count', fontsize=16)
    plt.xticks(rotation=60, fontsize=12)           
    st.pyplot()

def display_ovr_name(data1):
    # DISPLAYING PLAYERS NAME & OVR
    tempdf = data1.sort_values(by='overall')
    fig = px.bar(tempdf, x='short_name', y='overall', color='overall')
    fig['layout']['yaxis1'].update(title='', range=[45, 95], dtick=5, autorange=False)
    fig.update_layout(title='OVR of Players',xaxis_title="Player's Name",yaxis_title="OVR")
    st.plotly_chart(fig)

def display_potential_name(data1):
    # DISPLAYING PLAYERS NAME & POTENTIAL
    tempdf = data1.sort_values(by='potential')
    fig = px.bar(tempdf, x='short_name', y='potential', color='potential')
    fig['layout']['yaxis1'].update(title='', range=[60, 100], dtick=5, autorange=False)
    fig.update_layout(title='Potential of Players',xaxis_title="Player's Name",yaxis_title=" Potential")
    st.plotly_chart(fig) 

def display_wages_name(data1):
    # DISPLAYING PLAYERS NAME & WAGES
    tempdf = data1.sort_values(by='wage_eur')
    fig = px.bar(tempdf, x='short_name', y='wage_eur', color='wage_eur')
    fig.update_layout(title='Weekly wages of Players',xaxis_title="Player's Name",yaxis_title="Wage in Euro")
    st.plotly_chart(fig)

def display_value_name(data1):           
    # DISPLAYING PLAYERS NAME & VALUES
    tempdf = data1.sort_values(by='value_eur')
    fig = px.bar(tempdf, x='short_name', y='value_eur', color='value_eur')
    fig.update_layout(title='Values of Players', xaxis_title="Player's Name",yaxis_title="Value in Euro")
    st.plotly_chart(fig)

def display_contract_name(data1):            
    # DISPLAYING PLAYERS NAME & CONTRACT VALIDITY
    tempdf = data1.sort_values(by='club_contract_valid_until')
    fig = px.bar(tempdf, x='short_name', y='club_contract_valid_until', color='club_contract_valid_until')
    fig['layout']['yaxis1'].update(title='', range=[2019, 2026], dtick=5, autorange=False)
    fig.update_layout(title='Contract of Players',xaxis_title="Player's Name",yaxis_title="Contract Expiration")
    st.plotly_chart(fig)

def CLUB(data,club_list):
    st.header("CLUB ANALYSIS")
    st.markdown("<br>", unsafe_allow_html=True)

    input_club = st.text_input("Enter A Club Name","Real Madrid CF")
    data1 = data[(data['club_name']).str.lower() == input_club.lower()][["short_name","overall","player_positions","potential", "value_eur", "wage_eur", "age", "dob", "height_cm", "weight_kg", "club_name", "league_name", "league_level", "club_position", "club_jersey_number", "club_loaned_from", "club_joined", "club_contract_valid_until", "nationality_name", "preferred_foot", "weak_foot", "skill_moves", "body_type", "real_face", "release_clause_eur", "goalkeeping_speed", "player_face_url", "club_logo_url", "club_flag_url"]]
    data1 = data1.reset_index(drop=True)
    club_list_lower = [item.lower() for item in club_list]
    
    if input_club.lower() not in club_list_lower:
        st.text("Club Name Not Found in Database, please refer to navigation panel for club list")
        
    elif st.button("SUBMIT"):
        col1, col2 = st.columns(2)
        col1.write("Club's Logo")
        col2.image(data1.iloc[0]['club_logo_url'])
        st.markdown("<br>", unsafe_allow_html=True)

        number_of_players = playerscount(data1)
        st.write('Current Squad Strength of ',input_club, 'is', number_of_players, ' Players')

        input_club_value = club_value(data1)
        st.write('Current Squad Value of', input_club, 'is',input_club_value, ' Millions Euro')

        input_club_wage = club_wage(data1)
        st.write(input_club, 'Spends ',input_club_wage,' Millions Euros Per week as Wages to its Players')

        input_club_average_age = average_age(data1)
        st.write(input_club,'Squad\'s have an average age of',input_club_average_age,'Years')

        input_club_average_ovr = average_ovr(data1)
        st.write(input_club, 'Squad\'s have an average OVR of ',input_club_average_ovr)    

        st.subheader('PLOTS')
        st.set_option('deprecation.showPyplotGlobalUse', False)

        display_ovr_name(data1)
        display_potential_name(data1)
        display_wages_name(data1)
        display_value_name(data1)
        display_contract_name(data1)

        plot_age(data1)
        plot_ovr(data1)
        plot_nationality(data1)
        plot_contractexp(data1)
        plot_position(data1)


def country_value(x):
    squadvalue = 0
    x['value_eur'] = x['value_eur'].fillna(0)
    x['value_eur'] = x['value_eur'].astype(int)
    for i in range(0, len(x)):
        squadvalue+=x.iloc[i]['value_eur']
    
    squadvalue = squadvalue/1000000
    return squadvalue

def COUNTRY(data,country_list):
    st.header("COUNTRY ANALYSIS")
    st.markdown("<br>", unsafe_allow_html=True)

    input_country = st.text_input("Enter A Country Name","India")
    data1 = data[(data['nationality_name']).str.lower() == input_country.lower()][["short_name", "overall", "potential", "value_eur", "wage_eur", "age", "dob", "height_cm", "weight_kg", "nationality_name", "player_positions", "nation_jersey_number", "preferred_foot", "weak_foot", "skill_moves", "international_reputation", "body_type", "real_face", "player_tags", "player_face_url", "nation_logo_url", "nation_flag_url"]]
    data1 = data1.reset_index(drop=True)
    country_list_lower = [item.lower() for item in country_list]
    
    if input_country.lower() not in country_list_lower:
        st.text("Country Name Not Found in Database, please refer to navigation panel for country list")
        
    elif st.button("SUBMIT"):

        col1, col2 = st.columns(2)
        col1.write("National Team's Logo")
        col2.image(data1.iloc[0]['nation_logo_url'])
        st.markdown("<br>", unsafe_allow_html=True)

        # COUNT OF PLAYERS FROM A COUNTRY
        input_country_playerscount = playerscount(data1)
        st.write('Number of Players from ',input_country, 'is', input_country_playerscount, ' Players')
            
        # COMBINED PLAYERS VALUE
        input_country_value = country_value(data1)
        st.write('Current Combined Player\'s Value of', input_country,' is ',input_country_value, ' Millions Euro')
            
        # AVG AGE OF SQUAD
        input_country_avg_age = average_age(data1)
        st.write(input_country, 'Player\'s have an average age of ',input_country_avg_age, ' Years')
            
        # AVG OVR
        input_country_avg_ovr = average_ovr(data1)
        st.write(input_country, 'Player\'s have an average OVR of ',input_country_avg_ovr)

        plot_age(data1)
        plot_ovr(data1)

    

def main():
    main_page()
    data = selectbox_edition()
    analysisof = radiobutton_analysisof()
    club_list, country_list, player_list = create_list(data)
    nav_page(club_list, country_list, player_list)
    
    if analysisof == "Club":
        CLUB(data,club_list)
    elif analysisof =="Country":
        COUNTRY(data,country_list) 


if __name__=="__main__":
    main()