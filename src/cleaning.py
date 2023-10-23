import pandas as pd
import re
from src import functions

def formatt_hour(string):
    if 'h' in string:
        string = string.split('h')
        if len(string[0]) == 1:
            string[0] += '0'
        return ":".join(string)
    elif 'j' in string:
        return string.replace('j', ':')
    elif string.isdigit():
        string = string[:len(string)//2] + ':' + string[len(string)//2:]
    else:
        return string
    
def class_by_string(string):
    string_pattern = r'\d{1,2}\w\d{2}|>\d{1,2}:\d{2}|(0?\d|1[0-2]):\d{2}j|Before (0?\d|1[0-2]):\d{2}|Between (0?\d|1[0-2]):\d{2} and (0?\d|1[0-2]):\d{2}|\d{1,2}:\d{2}|\d{1,2}:\d{2}'
    if 'morning' in str(string).lower():
        return 'Morning'
    elif 'afternoon' in str(string).lower() or 'midday' in str(string).lower() or 'noon' in str(string).lower():
        return "Afternoon"
    elif 'evening' in str(string).lower():
        return "Evening"
    elif 'night' in str(string).lower() or 'dusk' in str(string).lower():
        return "Night"
    elif re.search(string_pattern, str(string)):
        str_ = re.search(string_pattern, str(string))
        return formatt_hour(str_.group())
    else:
        return "Unknown"
    
def class_by_time(string):
    """
    This function receives a string in the format '12:00' and determines whether this time is 'Morning', 'Afternoon', 'Evening' or 'Night'.
    """
    morning_pattern = r'0[6-9]:[0-5][0-9]|1[0-1]:[0-5][0-9]'
    afternoon_pattern = r'1[2-7]:[0-5][0-9]'
    evening_pattern = r'1[8-9]:[0-5][0-9]|20:[0-5][0-9]|21:[0-5][0-9]'
    night_pattern = r'22:[0-5][0-9]|23:[0-5][0-9]|0[0-5]:[0-5][0-9]'

    if re.search(morning_pattern, str(string)):
        return 'Morning'
    elif re.search(afternoon_pattern, str(string)):
        return "Afternoon"
    elif re.search(evening_pattern, str(string)):
        return "Evening"
    elif re.search(night_pattern, str(string)):
        return "Night"
    else:
        return 'Unknown'
    
def extract_age(x):
    if pd.isna(x):
        return 'Unknown'
    if x in ['teen', 'Teen', 'Teens']:
        return '15'
    if x in ['adult', '(adult)', 'middle-aged']:
        return '50'
    if 'months' in x:
        x = x.split(' ')[0]
        if int(x) < 12:
            return '< 1'
        else:
            return '2'
    age_av = re.findall(r'(\d{1,2})\s*(&|or|to)\s*(\d{1,2})', str(x))
    if age_av:
        average_ages = [(int(match[0]) + int(match[2])) // 2 for match in age_av]
        return str(average_ages[0])
    age_match = re.search(r'\d{1,2}', str(x))
    if age_match:
        return age_match.group()
    return 'Unknown'

def clean_year(year):
    pattern_year = r'\d{4}'
    str_pattern = r'\d{4}\.'
    if re.match(str_pattern, str(year)):
        return re.match(pattern_year, str(year)).group()
    else:
        return 'Unknown'
    
def sex_clean(x):
    """
    This function standarizes all the values found in the dataframe sex column.
    Params:
        x (str): Value of the sex
    Returns:
        string (str): Standarized sex
    """
    if x != 'M' and x != 'F' and x != 'M ':
        return 'Unknown'
    elif x == 'M ':
        return 'M'
    else:
        return x
    
def replace_activities(activity):
    """
    Takes the original activity in the dataframe and classifies it in a category according to key words.
    Returns the category that contains any keyword.
    Params:
        x (str): Value of the original activity
    Returns:
        string (str): Standarized activity (category that contains any keyword)
    """
    activities = {
        'Sailing': ['boat', 'boating', 'racing', 'barqued', 'sinking', 'ship', 'wreck', 'dhow', 'kayak', 'canoa', 'raft', 'cutter', 'bark', 'submarine'],
        'Fishing': ['fishing', 'fish', 'spearfishing', 'netting', 'wade-fishing', 'hunting', 'fishingat', 'shrimping', 'gigging', 'picking'],
        'Air accident': ['aircraft', 'airliner', 'constellation', 'parachute'],
        'Swimming': ['swimming', 'riding'],
        'Diving': ['diving', 'diver', 'photographing', 'dive', 'skidiving'],
        'Surfing': ['surfing', 'surf', 'boogie', 'surf-skiing', 'paddeling', 'boarding', 'board', 'overboard', 'treading'],
        'Dangerous': ['explosives', 'anesthesize', 'investigating', 'pulling', 'filming', 'defecating', 'chumming', 'wrangling', 'murder', 'searching'],
        'Bathing': ['playing', 'bath', 'bathing', 'crouching', 'floating', 'standing', 'sitting', 'dangling'],
        'Natural disaster': ['hurricane', 'natural']
    }

    for key, word_list in activities.items():
        if any(keyword in str(activity).lower() for keyword in word_list):
            return key
    return 'Unknown'
    

def clean_dataframe(df: pd.DataFrame):
    df = functions.rename_columns(df)
    df = functions.drop_null_rows(df)
    ignore_col = ['case_number', 'original_order']
    df = functions.drop_null_row_exclude_col(df, ignore_col)
    columns = ['pdf', 'href_formula', 'href', 'case_number.1', 'case_number.2', 'original_order', 'unnamed:_22', 'unnamed:_23']
    df = functions.drop_columns(df, columns)

    # Transforming 'type' column
    pattern = r'\w*[Bb]oat\w*'
    df = functions.replace_pattern_by_string(df, 'type', pattern, 'Boat')

    # Transforming 'time' column
    df['clean_time'] = df['time'].apply(class_by_string)
    pattern = r'\d{1,2}:\d{1,2}'
    df.loc[:, 'clean_time'] = df['clean_time'].apply(lambda x: class_by_time(x) if pd.notna(x) and pd.Series(x).str.contains(pattern).any() else x)

    # Transforming 'age' column
    df['clean_age'] = df.loc[:, 'age'].apply(extract_age)

    # Transforming 'year' column
    df['clean_year'] = df.loc[:, 'year'].apply(clean_year)

    # Transforming 'sex' column
    df['clean_sex'] = df.loc[:, 'sex_'].apply(sex_clean)

    # Transforming 'activity' column
    df['clean_activity'] = df.loc[:, 'activity'].apply(replace_activities)
    
    return df



