import streamlit as st
import pandas as pd
import plotly.express as px


#ui configuration
st.set_page_config(
    page_title = "pokemon app",
    page_icon = "🫏",
    layout="wide",

)
#load data 
@st.cache_data
def load_data():
    return pd.read_csv("pokemon.csv")
#ui integration
with st.spinner("loading dataset..."):
    df = load_data()
    st.balloons()

st.title("pokemon data analytics")
st.subheader("A simple data app to analyze pokemon data")

st.sidebar.title("menu")
choice = st.sidebar.radio("options",["view data","visualize data"])

if choice == 'view data':
    st.header("view dataset")
    st.dataframe(df)
else if:
    st.header("visualization")
    cat_cols = df.select_dtypes(imclude='object').columns.tolist()
    num_cols = df.select_dtypes(exclude='object').columns.tolist()
    cat_cols.remove("NAME")
    num_cols.remove("generation")
    num_cols.remove("legendary")
    cat_cols.append("generatiom")
    cat_cols.eppend("legendary")
    snum_col = st.sidebar.selectbox("select a numeric column",num_cols)
    scat_col = st.sidebar.selectbox("select a categorical column",cat_cols)

    c1,c2 = st .columns (2)
    #visulaize numberical column 
    fig1 = px.histogram(df,
                        x=snum_col,
                        title=f"distribution of {snum_col}")
    # visualize categorical column
    fig2= px.pie(df,
                names=scat_col,
                title=f"distribution of {scat_col}",
                hole=0.3
                )
    c1.plotly_chart(fig1)
    c1.plotly_chart(fig2)

    fig3=px.box(df,x=scat_col,y=snum_col,title=f"{snum_col} by {scat_col}")
    st.plotly_chart(fig3)
    df['type 2'] = df['type 2'].fillna('None')
    fig4= px.sunburst(
        df,
        path=['type1','type2','generation'],
        title=f"pokemon type distribution"
    )
    st.plotly_chart(fig4)
elif choice == ( 'column analysis'):
    columns=df.columns.tolist()
    scol = st.sidebar.selectbox("select a colun", columns)
    if df[scol].dtype=='object':
        vc = df[scol].value_counts()
        most_common = vc.idmax()   
        c1,c2 = st.columns([3,1])
        # visulaize
        figg = px.funnel_area(name = vc.index , values = vc.values)
        c1.plotly_chart(fig1)
        #value counts
        c2.subheader("total data")
        c2.write(vc)
        c2.metric("most commom",most_common,int(vc[most_common]))
    else :
        tab1,tab2 = st.tabs(['univariant','bivariate'])
        with tab1:
            score = df[scol].describe()
            fig1 = px.histogram(df,x = scol,title=f' distribution of {scol}')
            fig2 = px.histogram(df,x = scol,title=f'{scol} by {scol}')
            c1,c2,c3 = st.columns([1,3,3])
            c1.dataframe(score)
            c2.plotly_chart(fig1)
            c3.plotly_chart(fig2)
        with tab2:
            c1,c2= st.columns(2)
            col2 = c1.selectbox("select a column",df.select_dtypes(include='number').columns.tolist())
            color = c1.selectbox("select a column",df.select_dtypes(exclude='number').columns.tolist())
            fig3= px.scatter(df, x = scol , y = col2,color = color,
                             title = f'{scol} vs{col2}', height = 600)
            st.plotly_chart(fig3 , use_container_width=True,)


#to run this program , open terminal and run thr following command
# streamlit run app.pyst
