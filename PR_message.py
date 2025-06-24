from flask import Flask, request
import requests

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1386981212844724384/631eU3_tF-XAuNxRhsRhCMvHiCy1za-f6mcp0omD64wRI-48HCDwcIz0Qomdl8IYlj6m"

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def github_pr_notification():
    data = request.json
    if data.get("action") == "opened" and "pull_request" in data:
        pr = data["pull_request"]
        msg = {
            "content": f"📌 新しいPRが作成されました！\n"
                       f"タイトル: `{pr['title']}`\n"
                       f"作成者: {pr['user']['login']}\n"
                       f"🔗 {pr['html_url']}"
        }
        requests.post(DISCORD_WEBHOOK_URL, json=msg)
    return "", 204

if __name__ == "__main__":
    app.run(port=5000)
