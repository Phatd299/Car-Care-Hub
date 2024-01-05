import streamlit as st
from streamlit_app.car_brand_classification_app import run_module1_app
from streamlit_app.car_acceptability_testing_app import run_module2_app
from streamlit_app.car_engine_prediction_app import run_module3_app
from streamlit_app.car_maintenance_app import run_module4_app

def main():
    st.set_page_config(
        page_title="Car Care Platform",
        page_icon="🚗",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title('Integrated Car Care Platform')
    st.sidebar.title('Modules')

    app_options = {
        "Car Brand Classification": run_module1_app,
        "Car Acceptability Testing": run_module2_app,
        "Car Engine Maintenance Prediction": run_module3_app,
        "Car Maintenance Cost Prediction": run_module4_app
    }

    choice = st.sidebar.selectbox("Select Module", list(app_options.keys()))
    app_func = app_options[choice]

    st.sidebar.markdown("---")
    st.sidebar.info("👈 Select a module from the sidebar")

    st.subheader(choice)
    app_func()

if __name__ == "__main__":
    main()