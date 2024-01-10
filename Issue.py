# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:35:28 2024

@author: Oussama AKENNAF
"""

import pandas as pd

def import_data_from_excel(file_path):
    try:
        data = pd.read_excel(file_path)
        # Process the imported data
        return data
    

import_data_from_excel('records.xlsx')