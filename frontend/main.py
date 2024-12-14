import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests

# Create the Dash app
app = dash.Dash(__name__)
server = app.server  # Needed for deployment compatibility

# App layout
app.layout = html.Div([
    html.H1("Meme Generator", style={"textAlign": "center"}),

    # User input for meme text
    dcc.Input(
        id="meme-input",
        type="text",
        placeholder="Enter your meme text here",
        style={"marginRight": "10px", "width": "300px"}
    ),

    # Generate button
    html.Button("Generate Meme", id="generate-button", n_clicks=0),

    # Meme display area
    html.Div(
        id="meme-container",
        children=html.Img(
            id="meme-image",
            src="http://localhost:8000/home",  # Default image URL from your API
            style={"maxWidth": "500px", "marginTop": "20px"}
        ),
        style={"textAlign": "center"}
    )
])

# Callback to handle meme generation
@app.callback(
    [Output("meme-image", "src"),
     Output("generate-button", "n_clicks")],
    Input("generate-button", "n_clicks"),
    Input("meme-input", "value"),
    prevent_initial_call=True
)
def update_meme(n_clicks, user_input):
    if n_clicks and user_input:
        print(f"Button clicked: {n_clicks}, User input: {user_input}")

        # Send the user input to the API
        api_url = "http://localhost:8000/generate_meme"
        response = requests.post(api_url, json={"user_input": user_input})

        if response.status_code == 200:
            # Return the URL for the newly generated meme
            return "http://localhost:8000/generated_images/" + response.json()["meme"], 0
        else:
            print("Error generating meme:", response.text)
            return "http://localhost:8000/home", 0

    # Return default image when no input or button not clicked
    return "http://localhost:8000/home", 0


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
