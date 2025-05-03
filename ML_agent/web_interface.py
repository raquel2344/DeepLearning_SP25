from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        api_key = request.form.get("api_key")
        
        # Save the API key to a .env file or use it directly
        with open(".env", "w") as f:
            f.write(f"OPENAI_API_KEY={api_key}\n")
        
        return "✅ API Key saved successfully! You can now close this window and interact with the agent."
    
    return """
    <!doctype html>
    <html>
        <head><title>Enter OpenAI API Key</title></head>
        <body>
            <h1>OpenAI API Key Setup</h1>
            <form method="POST">
                <label for="api_key">Enter your OpenAI API Key:</label><br>
                <input type="text" id="api_key" name="api_key" required><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """

if __name__ == "__main__":
    # Automatically open the browser
    import webbrowser
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)
