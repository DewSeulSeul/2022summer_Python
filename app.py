import streamlit as st
import pandas as pd
import numpy as np

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

st.title('네이버 영화평')