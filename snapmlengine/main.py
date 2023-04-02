from linear_regression import linear_regression_analysis, create_graphs

ans = linear_regression_analysis('data.xlsx', ['AT', 'V', 'AP', 'RH'], ['PE'])
g_data = create_graphs(ans)