import simpleDOE as doe
import streamlit as st

# app
st.title('Designing Experiments')
st.text('''This tool is meant to help in the process of crafting a DOE
and measure the results of an experiment using test of proportions.
Test of proportions are widely used in marketing efforts such as in A/B
tests.''')

st.subheader('Calculating the test group sizes given expected proportions')
st.text('''Ex.: A marketing manager has a population of 50000 people to mail a letter
with a bonus offer for a marketing experiment. How should he split his 
test/control groups knowing that he expects a response rate of 3% for his
test group and 2% for his control based on his past learnings? He wants
a power of 90% for this experiment.''')

population = st.number_input(
    'Total population available', min_value=1, value=50000)
exp_conversion_a = st.number_input('Expected conversions for group A',
                                   min_value=0.0, max_value=1.0, value=0.03)
exp_conversion_b = st.number_input('Expected conversions for group B',
                                   min_value=0.0, max_value=1.0, value=0.02)
alpha = st.slider('Confidence level', min_value=0.0,
                  max_value=1.0, value=0.05)
power = st.slider('Desired statistical power', min_value=0.0, max_value=1.0,
                  value=0.9)
if st.button('Compute'):
    with st.spinner('Computing results...'):
        total_pop, sample_a, sample_b, pval, power = doe.optimal_experiment_test_prop(
            population, exp_conversion_a, exp_conversion_b, alpha, power)
        try:
            if pval <= 0.05:
                st.success(f"""The experiment can yield significant results with the inputed parameters.
                \nSample size for group A can be {sample_a};
                \nSample size for group B can be {sample_b};
                \nThe expected p-value for this experiment is {round(pval,4)}""")
            else:
                st.warning(f"""The experiment may not yield significant results with the inputed parameters.
                \nSample size for group A can be {sample_a};
                \nSample size for group B can be {sample_b};
                \nThe expected p-value for this experiment is {round(pval,4)}""")
        except:
            st.error("Please review your parameters and try again.")


st.subheader('Calculating the test group sizes given expected proportions')
