import IPython

def configure_plotly_browser_state():
  display(IPython.core.display.HTML('''
        <script src="/static/components/requirejs/require.js"></script>
        <script>
          requirejs.config({
            paths: {
              base: '/static/base',
              plotly: 'https://cdn.plot.ly/plotly-latest.min.js?noext',
            },
          });
        </script>
        '''))

from plotly.offline import init_notebook_mode
import plotly.graph_objs as go
IPython.get_ipython().events.register('pre_run_cell', configure_plotly_browser_state)
init_notebook_mode()


def plot(x, y, **kwargs):
    "A simple plotting function"
    return [go.Scatter(dict(x = x.detach().numpy(),
                            y = y.detach().numpy(),
                            **kwargs))]
