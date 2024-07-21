# data wrangling libraries
import pandas as pd
import numpy as np
import scipy.stats
import math

# data preprocessing libraries
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import scale
from sklearn.metrics.pairwise import cosine_similarity

# ML model libraries
import statsmodels.api as sm

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier

from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import BaggingClassifier

from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import GradientBoostingClassifier

from xgboost import XGBRegressor
from xgboost import XGBClassifier

from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans

# model tuning and performance libraries
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_auc_score

# data visualization libraries
import seaborn as sns
import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap
from cartopy import mpl

# NLP libraries
import re
import string
from nltk.corpus import stopwords
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer

# Deep Learning libraries
from keras.api.models import Sequential
from keras.api.layers import Dense
from keras.api.layers import LSTM
from keras.api.layers import Dropout
from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier