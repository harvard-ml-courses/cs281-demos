import plotly.graph_objs as go

def scatter(**kwargs):
    go.Scatter()
    f = go.FigureWidget()
    f.add_scatter(**kwargs)
    return f