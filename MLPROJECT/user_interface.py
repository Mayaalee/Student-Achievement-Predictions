import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Title and Description
st.title("Student Achievement Prediction")
st.write("This app allows you to predict the target (Enrolled, Dropout, Graduate) based on your inputs.")

# Load the pre-trained model
clf = joblib.load('model.pkl')

# Extract feature names from the model 
if hasattr(clf, 'feature_names_in_'):
    columns = clf.feature_names_in_
else:
    st.error("The model does not contain feature information.")
    st.stop()

# User input for each column
user_input = {}

if "Marital status" in columns:
    st.write("### Personal Status Options:")
    st.write("1: Single\n2: Married\n3: Widower\n4: Divorced\n5: Common-law marriage\n6: Legally separated")

    marital_status_options = [
        "1: Single",
        "2: Married",
        "3: Widower",
        "4: Divorced",
        "5: Common-law marriage",
        "6: Legally separated"
    ]

    selected_status = st.selectbox("Select your marital status:", marital_status_options)
    marital_status_number = int(selected_status.split(":")[0])
    user_input["Marital status"] = marital_status_number

import streamlit as st

if "Application mode" in columns:
    application_mode_options = [
        "1: 1st phase—general contingent",
        "2: Ordinance No. 612/93",
        "3: 1st phase—special contingent (Azores Island)",
        "4: Holders of other higher courses",
        "5: Ordinance No. 854-B/99",
        "6: International student (bachelor)",
        "7: 1st phase—special contingent (Madeira Island)",
        "8: 2nd phase—general contingent",
        "9: 3rd phase—general contingent",
        "10: Ordinance No. 533-A/99, item b2) (Different Plan)",
        "11: Ordinance No. 533-A/99, item b3 (Other Institution)",
        "12: Over 23 years old",
        "13: Transfer",
        "14: Change in course",
        "15: Technological specialization diploma holders",
        "16: Change in institution/course",
        "17: Short cycle diploma holders",
        "18: Change in institution/course (International)"
    ]

    selected_mode = st.selectbox("Select your application mode:", application_mode_options)
    application_mode_number = int(selected_mode.split(":")[0])
    user_input["Application mode"] = application_mode_number

if "Application order" in columns:
    user_input["Application order"] = st.number_input("Enter the application order (e.g., 1 for first choice):", value=0, step=1)

import streamlit as st

if "Course" in columns:
    st.write("### Course Options:")
    course_options = [
        "1: Biofuel Production Technologies",
        "2: Animation and Multimedia Design",
        "3: Social Service (evening attendance)",
        "4: Agronomy",
        "5: Communication Design",
        "6: Veterinary Nursing",
        "7: Informatics Engineering",
        "8: Equiniculture",
        "9: Management",
        "10: Social Service",
        "11: Tourism",
        "12: Nursing",
        "13: Oral Hygiene",
        "14: Advertising and Marketing Management",
        "15: Journalism and Communication",
        "16: Basic Education",
        "17: Management (evening attendance)"
    ]

    selected_course = st.selectbox("Select your course:", course_options)
    course_number = int(selected_course.split(":")[0])
    user_input["Course"] = course_number

if "Daytime/evening attendance" in columns:
    st.write("### Attendance Options:")
    user_input["Daytime/evening attendance"] = st.radio("Select your attendance regime (Evening/ Daytime):", options=[0, 1], format_func=lambda x: "Evening" if x == 0 else "Daytime")

if "Previous qualification" in columns:
    qualification_options = [
        "1: Secondary education",
        "2: Higher education—bachelor’s degree",
        "3: Higher education—degree",
        "4: Higher education—master’s degree",
        "5: Higher education—doctorate",
        "6: Frequency of higher education",
        "7: 12th year of schooling—not completed",
        "8: 11th year of schooling—not completed",
        "9: Other—11th year of schooling",
        "10: 10th year of schooling",
        "11: 10th year of schooling—not completed",
        "12: Basic education 3rd cycle (9th/10th/11th year) or equivalent",
        "13: Basic education 2nd cycle (6th/7th/8th year) or equivalent",
        "14: Technological specialization course",
        "15: Higher education—degree (1st cycle)",
        "16: Professional higher technical course",
        "17: Higher education—master’s degree (2nd cycle)"
    ]

    selected_qualification = st.selectbox("Select your previous qualification:", qualification_options)
    qualification_number = int(selected_qualification.split(":")[0])
    user_input["Previous qualification"] = qualification_number

if "Nacionality" in columns:
    st.write("### Nationality Options:")
    nationality_options = [
        "1: Portuguese",
        "2: German",
        "3: Spanish",
        "4: Italian",
        "5: Dutch",
        "6: English",
        "7: Lithuanian",
        "8: Angolan",
        "9: Cape Verdean",
        "10: Guinean",
        "11: Mozambican",
        "12: Santomean",
        "13: Turkish",
        "14: Brazilian",
        "15: Romanian",
        "16: Moldova (Republic of)",
        "17: Mexican",
        "18: Ukrainian",
        "19: Russian",
        "20: Cuban",
        "21: Colombian"
    ]

    selected_option = st.selectbox("Select your nationality:", nationality_options)

    # Extract the nationality number from the selected option string
    nationality_number = int(selected_option.split(":")[0]) 

    user_input["Nacionality"] = nationality_number 

if "Mother's qualification" in columns or "Father's qualification" in columns:
    st.write("### Parent's Qualification Options:")
    qualification_options = [
        "1: Secondary Education—12th Year of Schooling or Equivalent",
        "2: Higher Education—bachelor’s degree",
        "3: Higher Education—degree",
        "4: Higher Education—master’s degree",
        "5: Higher Education—doctorate",
        "6: Frequency of Higher Education",
        "7: 12th Year of Schooling—not completed",
        "8: 11th Year of Schooling—not completed",
        "9: 7th Year (Old)",
        "10: Other—11th Year of Schooling",
        "11: 2nd year complementary high school course",
        "12: 10th Year of Schooling",
        "13: General commerce course",
        "14: Basic Education 3rd Cycle (9th/10th/11th Year) or Equivalent",
        "15: Complementary High School Course",
        "16: Technical-professional course",
        "17: Complementary High School Course—not concluded",
        "18: 7th year of schooling",
        "19: 2nd cycle of the general high school course",
        "20: 9th Year of Schooling—not completed",
        "21: 8th year of schooling",
        "22: General Course of Administration and Commerce",
        "23: Supplementary Accounting and Administration",
        "24: Unknown",
        "25: Cannot read or write",
        "26: Can read without having a 4th year of schooling",
        "27: Basic education 1st cycle (4th/5th year) or equivalent",
        "28: Basic Education 2nd Cycle (6th/7th/8th Year) or equivalent",
        "29: Technological specialization course",
        "30: Higher education—degree (1st cycle)",
        "31: Specialized higher studies course",
        "32: Professional higher technical course",
        "33: Higher Education—master’s degree (2nd cycle)",
        "34: Higher Education—doctorate (3rd cycle)"
    ]

    if "Mother's qualification" in columns:
        mother_qualification = st.selectbox("Select your mother's qualification:", qualification_options)
        mother_qualification_number = int(mother_qualification.split(":")[0])
        user_input["Mother's qualification"] = mother_qualification_number

    if "Father's qualification" in columns:
        father_qualification = st.selectbox("Select your father's qualification:", qualification_options)
        father_qualification_number = int(father_qualification.split(":")[0])
        user_input["Father's qualification"] = father_qualification_number

if "Mother's occupation" in columns or "Father's occupation" in columns:
    st.write("### Parent's Occupation Options:")
    occupation_options = [
        "1: Student",
        "2: Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",
        "3: Specialists in Intellectual and Scientific Activities",
        "4: Intermediate Level Technicians and Professions",
        "5: Administrative staff",
        "6: Personal Services, Security and Safety Workers, and Sellers",
        "7: Farmers and Skilled Workers in Agriculture, Fisheries, and Forestry",
        "8: Skilled Workers in Industry, Construction, and Craftsmen",
        "9: Installation and Machine Operators and Assembly Workers",
        "10: Unskilled Workers",
        "11: Armed Forces Professions",
        "12: Other Situation",
        "13: Armed Forces Officers",
        "14: Armed Forces Sergeants",
        "15: Other Armed Forces personnel",
        "16: Directors of administrative and commercial services",
        "17: Hotel, catering, trade, and other services directors",
        "18: Specialists in the physical sciences, mathematics, engineering, and related techniques",
        "19: Health professionals",
        "20: Teachers",
        "21: Specialists in finance, accounting, administrative organization, and public and commercial relations",
        "22: Intermediate level science and engineering technicians and professions",
        "23: Technicians and professionals of intermediate level of health",
        "24: Intermediate level technicians from legal, social, sports, cultural, and similar services",
        "25: Information and communication technology technicians",
        "26: Office workers, secretaries in general, and data processing operators",
        "27: Data, accounting, statistical, financial services, and registry-related operators",
        "28: Other administrative support staff",
        "29: Personal service workers",
        "30: Sellers",
        "31: Personal care workers and the like",
        "32: Protection and security services personnel",
        "33: Market-oriented farmers and skilled agricultural and animal production workers",
        "34: Farmers, livestock keepers, fishermen, hunters and gatherers, and subsistence",
        "35: Skilled construction workers and the like, except electricians",
        "36: Skilled workers in metallurgy, metalworking, and similar",
        "37: Skilled workers in electricity and electronics",
        "38: Workers in food processing, woodworking, and clothing and other industries and crafts",
        "39: Fixed plant and machine operators",
        "40: Assembly workers",
        "41: Vehicle drivers and mobile equipment operators",
        "42: Unskilled workers in agriculture, animal production, and fisheries and forestry",
        "43: Unskilled workers in extractive industry, construction, manufacturing, and transport",
        "44: Meal preparation assistants",
        "45: Street vendors (except food) and street service providers"
    ]

    if "Mother's occupation" in columns:
        mother_occupation = st.selectbox("Select your mother's occupation:", occupation_options)
        mother_occupation_number = int(mother_occupation.split(":")[0])
        user_input["Mother's occupation"] = mother_occupation_number

    if "Father's occupation" in columns:
        father_occupation = st.selectbox("Select your father's occupation:", occupation_options)
        father_occupation_number = int(father_occupation.split(":")[0])
        user_input["Father's occupation"] = father_occupation_number

if "Displaced" in columns:
    user_input["Displaced"] = st.radio("Are you displaced? (0 for No, 1 for Yes):", options=[0, 1])

if "Educational special needs" in columns:
    user_input["Educational special needs"] = st.radio("Do you have educational special needs? (0 for No, 1 for Yes):", options=[0, 1])

if "Debtor" in columns:
    user_input["Debtor"] = st.radio("Are you a debtor? (0 for No, 1 for Yes):", options=[0, 1])

if "Tuition fees up to date" in columns:
    user_input["Tuition fees up to date"] = st.radio("Are your tuition fees up to date? (0 for No, 1 for Yes):", options=[0, 1])

if "Gender" in columns:
    st.write("### Gender Options:")
    user_input["Gender"] = st.radio("Select your gender:", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")

if "Scholarship holder" in columns:
    user_input["Scholarship holder"] = st.radio("Are you a scholarship holder?:", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

if "Age at enrollment" in columns:
    user_input["Age at enrollment"] = st.number_input("Enter your age at enrollment:", value=0, step=1)

if "International" in columns:
    user_input["International"] = st.radio("Are you an international student?:", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

if "Curricular units 1st sem (credited)" in columns:
    user_input["Curricular units 1st sem (credited)"] = st.number_input("Enter the number of credited curricular units in the 1st semester:", value=0, step=1)

if "Curricular units 1st sem (enrolled)" in columns:
    user_input["Curricular units 1st sem (enrolled)"] = st.number_input("Enter the number of enrolled curricular units in the 1st semester:", value=0, step=1)

if "Curricular units 1st sem (evaluations)" in columns:
    user_input["Curricular units 1st sem (evaluations)"] = st.number_input("Enter the number of evaluations in the 1st semester:", value=0, step=1)

if "Curricular units 1st sem (approved)" in columns:
    user_input["Curricular units 1st sem (approved)"] = st.number_input("Enter the number of approved curricular units in the 1st semester:", value=0, step=1)

if "Curricular units 1st sem (grade)" in columns:
    user_input["Curricular units 1st sem (grade)"] = st.number_input("Enter the grade of curricular units in the 1st semester:", value=0.0, step=0.1)

if "Curricular units 1st sem (without evaluations)" in columns:
    user_input["Curricular units 1st sem (without evaluations)"] = st.number_input("Enter the number of curricular units without evaluations in the 1st semester:", value=0, step=1)

if "Curricular units 2nd sem (credited)" in columns:
    user_input["Curricular units 2nd sem (credited)"] = st.number_input("Enter the number of credited curricular units in the 2nd semester:", value=0, step=1)

if "Curricular units 2nd sem (enrolled)" in columns:
    user_input["Curricular units 2nd sem (enrolled)"] = st.number_input("Enter the number of enrolled curricular units in the 2nd semester:", value=0, step=1)

if "Curricular units 2nd sem (evaluations)" in columns:
    user_input["Curricular units 2nd sem (evaluations)"] = st.number_input("Enter the number of evaluations in the 2nd semester:", value=0, step=1)

if "Curricular units 2nd sem (approved)" in columns:
    user_input["Curricular units 2nd sem (approved)"] = st.number_input("Enter the number of approved curricular units in the 2nd semester:", value=0, step=1)

if "Curricular units 2nd sem (grade)" in columns:
    user_input["Curricular units 2nd sem (grade)"] = st.number_input("Enter the grade of curricular units in the 2nd semester:", value=0.0, step=0.1)

if "Curricular units 2nd sem (without evaluations)" in columns:
    user_input["Curricular units 2nd sem (without evaluations)"] = st.number_input("Enter the number of curricular units without evaluations in the 2nd semester:", value=0, step=1)

if "Unemployment rate" in columns:
    user_input["Unemployment rate"] = st.number_input("Enter the unemployment rate:", value=0.0, step=0.1)

if "Inflation rate" in columns:
    user_input["Inflation rate"] = st.number_input("Enter the inflation rate:", value=0.0, step=0.1)

if "GDP" in columns:
    user_input["GDP"] = st.number_input("Enter the GDP:", value=0.0, step=0.1)

# Convert user input to a DataFrame
input_df = pd.DataFrame([user_input])

# Prediction using the pre-trained model
st.subheader("Prediction")
if st.button("Predict Target"):
    try:
        input_df = pd.DataFrame([user_input])  # Ensure `user_input` is populated correctly
        predicted_target = clf.predict(input_df)[0]
        st.write(f"The predicted target is: **{predicted_target}**")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")