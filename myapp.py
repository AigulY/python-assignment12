from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# The dataset to use is the Plotly built in gapminder dataset
df = px.data.gapminder()

# Create a Series called countries that is the list of countries with duplicates removed.
countries = df["country"].drop_duplicates()

# Initialize Dash app
app = Dash(__name__)
server = app.server

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": c, "value": c} for c in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth")
])

# Callback for dynamic updates
@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(country_name):
    # Filter rows for the selected country
    filtered_df = df[df["country"] == country_name]

    # Create a line plot for 'year' vs. 'gdpPercap`.
    fig = px.line(
        filtered_df,
        x="year",
        y="gdpPercap",
        title=f"GDP Per Capita Over Time: {country_name}"
    )
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)