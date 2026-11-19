import pandas as pd
import numpy as np
import re

# Load the raw data
raw_df = pd.read_csv('./data/raw/bridge_data_raw.csv')

# Filter for Bridges only
processed_df = raw_df[raw_df['CATEGORY'] == 'Bridge']

# Rename to use snake case for consistency
rename_map = {
    "ID (SITE Ndeg)": "site_id",
    "STRUCTURE NAME": "structure_name",
    "FRENCH NAME": "french_name",
    "HIGHWAY NAME": "highway_name",
    "LATITUDE": "latitude",
    "LONGITUDE": "longitude",
    "CATEGORY": "category",
    "SUBCATEGORY 1": "subcategory",
    "TYPE 1": "structure_type",
    "MATERIAL 1": "material",
    "YEAR BUILT": "year_built",
    "LAST MAJOR REHAB": "last_major_rehab",
    "LAST MINOR REHAB": "last_minor_rehab",
    "NUMBER OF SPAN / CELLS": "num_spans_cells",
    "SPAN DETAILS (m)": "span_details_m",
    "DECK / CULVERTS LENGTH (m)": "length_m",
    "WIDTH TOTAL (m)": "width_m",
    "REGION": "region",
    "COUNTY": "county",
    "OPERATION STATUS": "operation_status",
    "OWNER": "owner",
    "LAST INSPECTION DATE": "last_inspection_date",
    "CURRENT BCI": "current_bci",
}

processed_df = processed_df.rename(columns=rename_map)

# Drop rows that don't have a CURRENT_BCI (target), 52 rows
processed_df = processed_df.dropna(subset=['current_bci'])

# Create target variable
processed_df['rehab_soon'] = (processed_df['current_bci'] < 70).astype(int)

# Parse span_details_m into total, count, max, mean, and std
def extract_span_summary(val):
    """Helper function to parse span details into total,
    count, max, mean, and std span
    """
    txt = str(val).strip()
    t_match = re.search(r"Total\s*=\s*([+-]?\d+(?:\.\d+)?)", txt, re.IGNORECASE)
    spans = [
        float(m.group(2))
        for m in re.finditer(r"\(\s*(\d+)\s*\)\s*=\s*([+-]?\d+(?:\.\d+)?)", txt)
    ]

    if spans:
        arr = np.array(spans, dtype=float)
        total_val = (
            float(t_match.group(1))
            if t_match and float(t_match.group(1)) > 0
            else float(arr.sum())
        )
        return pd.Series(
            [total_val, float(len(arr)), float(arr.max()), float(arr.mean()), float(arr.std(ddof=0))]
        )

    try:
        num = float(txt.rstrip("mM "))
        return pd.Series([num, 1.0, num, num, 0.0])
    except ValueError:
        total_val = float(t_match.group(1)) if t_match else np.nan
        return pd.Series([total_val, 0.0, np.nan, np.nan, np.nan])


processed_df[['span_total_m', 'span_count', 'span_max_m', 'span_mean_m', 'span_std_m']] = (
    processed_df['span_details_m'].apply(extract_span_summary)
)

# Group together materials
low_count_materials = [
    'Unknown',
    'Engineered Wood (Psl, etc.)',
    'Mass Concrete',
    'Plastic/Geogrid/Geocell',
    'Glue Laminated Wood',
    'Masonry/Block/Rock'
]
processed_df['material'] = processed_df['material'].replace(low_count_materials, 'Other')

# Feature Engineering
processed_df['age'] = 2020 - processed_df['year_built']

processed_df['years_since_last_rehab_major'] = 2020 - processed_df['last_major_rehab'].fillna(processed_df['year_built'])
processed_df['years_since_last_rehab_minor'] = 2020 - processed_df['last_minor_rehab'].fillna(processed_df['year_built'])


# Columns to drop
drop_columns = [
    'category',
    '_id',
    'site_id',
    'structure_name',
    'french_name',
    'highway_name',
    'latitude',
    'longitude',
    '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012',
    '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004', '2003',
    '2002', '2001', '2000',
    'year_built',
    'last_major_rehab',
    'last_minor_rehab',
    'num_spans_cells',
    'span_details_m',
    'last_inspection_date'
]
processed_df = processed_df.drop(columns=drop_columns)
# Save the processed dataframe
processed_df.to_csv('./data/processed/bridge_data_processed.csv', index=False)