from sklearn.externals import joblib
from django.core.cache import cache

clf = joblib.load('filename.pkl') 