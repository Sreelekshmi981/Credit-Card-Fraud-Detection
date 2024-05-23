import streamlit as st
import pickle
from PIL import Image
def main():
    st.title("CREDIT CARD FRAUD DETECTION")
    image=Image.open("credit.jpg")
    st.image(image,width=650)
    CVV=st.text_input("CVV","Type here")
    CustomerAge=st.text_input("Customer Age","Type here")
    Gender= st.radio("Gender", ['Male', 'Female'])
    if Gender == 'Male':
        Gender = 1
    else:
        Gender = 0
    MaritalStatus = st.selectbox("Marital Status",('Divorced','Married','Single','Unknown'),index=None)
    if MaritalStatus == 'Divorced':
         MaritalStatus= 0
    elif MaritalStatus == 'Married':
        MaritalStatus = 1
    elif MaritalStatus == 'Single':
         MaritalStatus= 2
    else:
        MaritalStatus=3

    CardType = st.radio("Card Type",['MasterCard','Verve','Visa'])
    if CardType == 'MasterCard':
         CardType= 0
    elif CardType == 'Verve':
        CardType = 1
    elif CardType== 'Visa':
        CardType= 2

    Domain= st.radio("Domain",['International','Local' ])
    if Domain == 'International':
         Domain= 0
    elif Domain == 'Local':
        Domain = 1

    Amount=st.text_input("Amount", "Type here")
    AverageIncomeExpenditure = st.text_input("Average Income Expenditure", "Type here")

    Customer_City_Address = st.selectbox("City",('Abuja','Enugu','Ibadan','Kano','Lagos','Ota','Other','Port Harcourt'),index=None)
    if Customer_City_Address=='Abuja':
        Customer_City_Address=0
    elif Customer_City_Address=='Enugu':
        Customer_City_Address=1
    elif Customer_City_Address=='Ibadan':
        Customer_City_Address=2
    elif Customer_City_Address=='Kano':
        Customer_City_Address=3
    elif Customer_City_Address=='Lagos':
        Customer_City_Address=4
    elif Customer_City_Address=='Ota':
        Customer_City_Address=5
    elif Customer_City_Address=='Other':
        Customer_City_Address=6
    else:
        Customer_City_Address=7

    features=[CVV,CustomerAge,Gender,MaritalStatus,CardType,Domain,Amount,AverageIncomeExpenditure,Customer_City_Address]
    model=pickle.load(open('model3.sav','rb'))
    scaler=pickle.load(open('scaler3.sav','rb'))

    pred=st.button('PREDICT')
    if pred:
        prediction=model.predict(scaler.transform([features]))
        if prediction==0:
            st.write("## Not Fraud")
        else:
            st.write("## Fraud")
main()

