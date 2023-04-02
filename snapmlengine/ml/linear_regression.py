import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.DataFrame()

def load_data(file_name):
    '''
    Given a file_name loads the file as pd.DataFrame()
    Parameters: file_name (Name of the file to be loaded)
    Return: data (pandas DataFrame containing the file)
    '''
    name_split = file_name.split('.')
    name_split = [name_split[-2], name_split[-1]]
    file_type = name_split[1]
    try:
        if file_type == 'xlsx':
            data = pd.read_excel(file_name)
            return data

        elif file_type == 'csv':
            data = pd.read_csv(file_name)
            return data
    except:
        raise Exception('File Not Found or File Type is not compatible for analysis')

def data_shape():
    '''
    Returns shape of the input DataFrame data
    Parameters: data (Input DataFrame)
    Return: shape of the DataFrame 'data'
    '''
    global data
    return data.shape

def fit_linear_regression(fts_x, fts_y):
    global data
    linear_regression = LinearRegression()
    model = linear_regression.fit(data[fts_x], data[fts_y])
    return linear_regression.coef_[0]


def linear_regression_analysis(file_name, fts_x, fts_y):
    global data
    analysis = {}
    
    data = load_data(file_name)
    
    data_X = data[fts_x]
    data_Y = data[fts_y]

    ## linear regression coeff
    lr_coeff = {}
    for fts in fts_x:
        lr_coeff[fts] = fit_linear_regression([fts], fts_y)[0]
    analysis['linear_regression_coefficients'] = lr_coeff
    
    ## multi regression
    multi_regression = LinearRegression()
    model = multi_regression.fit(data_X, data_Y)

    analysis['multi_regression_train_data_score'] = model.score(data_X, data_Y)
    analysis['multi_regression_intercept'] = model.intercept_
    mr_coeff = model.coef_[0]
    multi_regression_coeff_arr = []
    for c in mr_coeff:
        multi_regression_coeff_arr.append(c)
    analysis['multi_regression_coefficients'] = multi_regression_coeff_arr
    
    ## adding all features in analysis
    analysis['fts'] = fts_x
    analysis['file_name'] = file_name
    return analysis

def create_graphs(analysis):
    ## [graph_title, x_axis_name, y_axis_name, x_data, y_data]
    data = load_data(analysis['file_name'])
    input_fts = analysis['fts']
    graph_data = []

    ## type1 : graphs pairwise scatterplots
    for x in range(len(input_fts)-1):
        for y in range(x+1, len(input_fts)):
            new_graph = []
            new_graph.append("Pairwise Scatterplots : " + input_fts[x] + " vs " + input_fts[y])
            new_graph.append(input_fts[x])
            new_graph.append(input_fts[y])
            new_graph.append(list(data[input_fts[x]]))
            new_graph.append(list(data[input_fts[y]]))

            graph_data.append(new_graph)

    graph_data.append(new_graph)
    ## type2 graphs : linear regression coeff vs multi regression coeff
    new_graph = ['Coefficient Comparison', 'Simple Linear Regression Coefficient', 'Multiple Linear Regression Coefficient']
    x = []
    y = []
    for fts in input_fts:
        x.append(analysis['linear_regression_coefficients'][fts])

    y = (analysis['multi_regression_coefficients'])
    new_graph.append(x)
    new_graph.append(y)
    graph_data.append(new_graph)

    return graph_data

