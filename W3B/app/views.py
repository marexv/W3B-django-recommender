"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import UserInfo 
from sklearn.externals import joblib
import pandas as pd
import numpy as np
import sklearn



#Our view
clf1 = joblib.load('app/MLmodels/model1/clf1.pkl') 
clf2 = joblib.load('app/MLmodels/model2/clf2.pkl') 
clf3 = joblib.load('app/MLmodels/model3/clf3.pkl') 
clf4 = joblib.load('app/MLmodels/model4/clf4.pkl') 
clf5 = joblib.load('app/MLmodels/model5/clf5.pkl') 
clf6 = joblib.load('app/MLmodels/model6/clf6.pkl') 
clf7 = joblib.load('app/MLmodels/model7/clf7.pkl') 
clf8 = joblib.load('app/MLmodels/model8/clf8.pkl') 

df = pd.DataFrame(np.zeros((1,23)),columns=['Sex_Female', 'Sex_Male', 'typeOfResidence_City or urban area',
       'typeOfResidence_Rural area', 'typeOfResidence_Suburban area',
       'Employment_Disabled', 'Employment_Homemaker', 'Employment_Military',
       'Employment_None', 'Employment_Self', 'Employment_Student',
       'Employment_Wages', 'Employment_lookingFor', 'Employment_notLookingFor',
       'Education_Bachelor', 'Education_Doctor', 'Education_HighShool',
       'Education_Masters', 'Education_None', 'Education_Proffesional',
       'Education_Tehnical', 'Education_someCollege', 'Age'])

#w3b form try
def w3b(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # this worked form = NameForm(request.POST)
        form = UserInfo(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            threshold = 50
            sex = form.cleaned_data.get('sex')
            age = form.cleaned_data.get('age')
            employment = form.cleaned_data.get('employment')
            education = form.cleaned_data.get('education')
            residence = form.cleaned_data.get('residence')
            threshold = form.cleaned_data.get('threshold')

            if sex == 'male':
                df['Sex_Male'] = 1
            else:
                df['Sex_Female'] = 1

            df['Age'] = age

            if employment == 'self':
                df['Employment_Self'] = 1
            elif  employment == 'unemployedLooking':
                df['Employment_lookingFor'] = 1
            elif  employment == 'unemployedNotLooking':
                df['Employment_notLookingFor'] = 1
            elif  employment == 'homemaker':
                df['Employment_Homemaker'] = 1
            elif  employment == 'student':
                df['Employment_Student'] = 1
            elif  employment == 'military':
                df['Employment_Military'] = 1
            elif  employment == 'retired':
                df['Employment_None'] = 1
            elif  employment == 'wages':
                df['Employment_Wages'] = 1
            else:
                df['Employment_Disabled'] = 1
            
            if education == 'bachelor':
                df['Education_Bachelor'] = 1
            elif education == 'doctor':
                df['Education_Doctor'] = 1
            elif education == 'high':
                df['Education_HighShool'] = 1
            elif education == 'master':
                df['Education_Masters'] = 1
            elif education == 'lessThanHigh':
                df['Education_None'] = 1
            elif education == 'professional':
                df['Education_Proffesional'] = 1
            elif education == 'tehnical':
                df['Education_Tehnical'] = 1
            else:
                df['Education_someCollege'] = 1

            if residence == 'rural':
                df['typeOfResidence_Rural area'] = 1
            elif residence == 'suburban':
                df['typeOfResidence_Suburban area'] = 1
            else:
                df['typeOfResidence_City or urban area'] = 1
            
                      

            prob1 = round(clf1.predict_proba(df)[0][0]*100 , 2) 
            prob2 = round(clf2.predict_proba(df)[0][0]*100 , 2) 
            prob3 = round(clf3.predict_proba(df)[0][0]*100 , 2)
            prob4 = round(clf4.predict_proba(df)[0][0]*100 , 2)  
            prob5 = round(clf5.predict_proba(df)[0][0]*100 , 2) 
            prob6 = round(clf6.predict_proba(df)[0][0]*100 , 2) 
            prob7 = round(clf7.predict_proba(df)[0][0]*100 , 2)         
            prob8 = round(clf8.predict_proba(df)[0][0]*100 , 2) 
        

            return render(request, 'app/index.html', {'form':form,
                                                    'prob1':prob1,
                                                    'prob2':prob2,
                                                    'prob3':prob3,
                                                    'prob4':prob4,
                                                    'prob5':prob5,
                                                    'prob6':prob6,
                                                    'prob7':prob7,
                                                    'prob8':prob8,
                                                    'threshold':threshold,
                                                    })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserInfo()

    return render(request, 'app/index.html', {'form':form,
                                            'prob1':0,
                                            'prob2':0,
                                            'prob3':0,
                                            'prob4':0,
                                            'prob5':0,
                                            'prob6':0,
                                            'prob7':0,
                                            'prob8':0,
                                            'threshold':50,
})