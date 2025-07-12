# Watson Orchestrate Hello Agent CI/CD

このプロジェクトは IBM Watson Orchestrate エージェントを GitHub Actions で自動デプロイするためのサンプルです。

## セットアップ

### 必要なGitHub Secrets

以下のSecretsをGitHubリポジトリに設定してください：

1. `WATSON_ORCHESTRATE_API_KEY` - Watson Orchestrate API キー
2. `WATSON_ORCHESTRATE_INSTANCE_ID` - Watson Orchestrate インスタンス ID  
3. `WATSON_ORCHESTRATE_URL` - Watson Orchestrate URL (例: https://api.us-south.watson-orchestrate.cloud.ibm.com)

### GitHub Secretsの設定方法

1. GitHubリポジトリの「Settings」タブを開く
2. 左メニューの「Secrets and variables」→「Actions」を選択
3. 「New repository secret」をクリック
4. 上記の各Secretを追加

### Watson Orchestrateの認証情報取得

Watson Orchestrateの認証情報は以下の方法で取得できます：

1. IBM Cloud コンソールにログイン
2. Watson Orchestrate インスタンスを選択
3. 「サービス資格情報」から API キーを取得
4. インスタンス ID と URL を確認

## デプロイ

mainブランチにプッシュまたはプルリクエストを作成すると、GitHub Actionsが自動的に：

1. Pythonとdependenciesをインストール
2. Watson Orchestrateにツールをインポート
3. エージェントをデプロイ

## ローカルでのテスト

```bash
# Watson Orchestrate ADKをインストール
pip install ibm-watsonx-orchestrate

# 認証設定
orchestrate configure --api-key YOUR_API_KEY --instance-id YOUR_INSTANCE_ID --url YOUR_URL

# ツールをインポート
orchestrate tools import -f tools/

# エージェントをインポート
orchestrate agents import -f agents/hello-agent.yaml
```

## プロジェクト構造

```
.
├── .github/workflows/
│   └── deploy.yml          # GitHub Actions ワークフロー
├── agents/
│   └── hello-agent.yaml    # エージェント定義
├── tools/
│   └── return_hello.py     # ツール実装
└── README.md
```
