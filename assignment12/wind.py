import plotly.express as px
import plotly.data as pldata

def main():
    # Load the Plotly wind dataset
    df = pldata.wind(return_type="pandas")

    # Print the first and last 10 lines of the DataFrame.
    print("FIRST 10 ROWS:")
    print(df.head(10))
    print("\nLAST 10 ROWS:")
    print(df.tail(10))

    # Clean the data. You need to convert the 'strength' column to a float. 
    df["strength"] = (
        df["strength"]
        .astype(str)
        .str.replace(r"[^0-9.]", "", regex=True)
        .astype(float)
    )

    # Create an interactive scatter plot of strength vs. frequency
    fig = px.scatter(
        df,
        x="strength",
        y="frequency",
        color="direction",
        title="Wind: Strength vs Frequency by Direction",
        hover_data=["direction", "strength", "frequency"]
    )

    # Save and load the HTML file
    fig.write_html("wind.html", auto_open=True)

if __name__ == "__main__":
    main()