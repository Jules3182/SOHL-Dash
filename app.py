from flask import Flask, render_template, request, redirect
import yaml


app = Flask(__name__)
# Pulls user config from YAML
with open("config/config_example.yaml") as f:
    config = yaml.safe_load(f)

# The main landing page for selecting the User
@app.route('/')
def landing():
    print("Welcome to the Significant Other HomeLab Dashboard!")

    # Loads in all users listed in the config
    users = config["users"]
    print("Users: ", config["users"].keys())

    # Render call for landiong page (passes in users as listed in the config)
    return render_template(
        "landing.html",
        users=users
    )

# The main dashboard of the app
@app.route("/dashboard")
def dashboard():

    # Gets the selected user and loads in their personalized config
    username = request.args.get("user")
    if username not in config["users"]:
        return "User couldn't be found", 404

    # Sets up variables for user
    user_config = config["users"][username]
    name = user_config["name"]
    icon = user_config["icon"]
    level = user_config["level"]
    pet_names = user_config["pet_names"]
    theme = user_config.get("theme")

    # Debugging Print
    print("Loaded User: ", username)
    print("User Settings: ", name, icon, level, pet_names, theme)

    # Render the dashboard with their settings
    return render_template(
        "dashboard.html",
        username=username,
        name=name,
        icon=icon,
        level=level,
        pet_names=pet_names,
        theme=theme
    )

# Main app run function
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=config["port"])