from flask import Flask, render_template, request
import requests

app = Flask(__name__)
base_url = "https://api.github.com/users/"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        github_name = request.form.get("githubname")
        response = requests.get(base_url + github_name)
        user_repos = requests.get(f"https://api.github.com/users/{github_name}/repos")
        github_user_datas = response.json()
        repos = user_repos.json()
        if "message" in github_user_datas:
            return render_template("index.html", error="No found any github thing...")
        else:
            return render_template("index.html", profile=github_user_datas, repos=repos)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
