from flask import Flask, request
import requests

# ✅ ここにあなたのWebhook URLを貼ってください
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1386981212844724384/631eU3_tF-XAuNxRhsRhCMvHiCy1za-f6mcp0omD64wRI-48HCDwcIz0Qomdl8IYlj6m"

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def github_webhook():
    data = request.json

    # PRが作成されたときだけ反応する
    if data.get("action") == "opened" and "pull_request" in data:
        pr = data["pull_request"]
        title = pr["title"]
        url = pr["html_url"]
        user = pr["user"]["login"]
        repo = data["repository"]["full_name"]

        # Discordに送るメッセージ
        message = {
            "content": f"🆕 **新しいプルリクエストが作成されました！**\n"
                       f"📂 リポジトリ: `{repo}`\n"
                       f"📝 タイトル: `{title}`\n"
                       f"🙋 作成者: `{user}`\n"
                       f"🔗 [PRリンクはこちら]({url})"
        }

        # Discordへ送信
        requests.post(DISCORD_WEBHOOK_URL, json=message)

    return "", 204

if __name__ == "__main__":
    app.run(port=5000)
