# watsonx Orchestrate Hello Agent CI/CD

このプロジェクトは IBM watsonx Orchestrate エージェントを GitHub Actions で自動デプロイするためのサンプルです。

## セットアップ

### 必要な GitHub Secrets

以下の Secrets を GitHub リポジトリに設定してください：

1. `WO_API_KEY` - watsonx Orchestrate API キー
2. `WO_URL` - watsonx Orchestrate サービスインスタンス URL (例: https://api.us-south.watson-orchestrate.cloud.ibm.com/instances/xxx)

### GitHub Secrets の設定方法

1. GitHub リポジトリの「Settings」タブを開く
2. 左メニューの「Secrets and variables」→「Actions」を選択
3. 「New repository secret」をクリック
4. 上記の各 Secret を追加

### watsonx Orchestrate の認証情報取得

watsonx Orchestrate の認証情報は以下の方法で取得できます：

1. IBM Cloud コンソールにログイン
2. watsonx Orchestrate インスタンスを選択
3. 「サービス資格情報」から API キーを取得
4. サービスインスタンス URL を確認（`https://api.us-south.watson-orchestrate.cloud.ibm.com/instances/your-instance-id` の形式）

## デプロイ

main ブランチにプッシュまたはプルリクエストを作成すると、GitHub Actions が自動的に：

1. Python と dependencies をインストール
2. watsonx Orchestrate にツールをインポート
3. エージェントをデプロイ

## ローカルでのテスト

```bash
# watsonx Orchestrate ADKをインストール
pip install ibm-watsonx-orchestrate

# 環境設定
orchestrate env add -n local -u YOUR_URL
orchestrate env activate local --api-key YOUR_API_KEY

# ツールをインポート
orchestrate tools import -f tools/

# エージェントをインポート
orchestrate agents import -f agents/hello-agent.yaml
```

## プロジェクト構造

```text
.
├── .github/workflows/
│   └── deploy.yml          # GitHub Actions ワークフロー
├── agents/
│   └── hello-agent.yaml    # エージェント定義
├── tools/
│   └── return_hello.py     # ツール実装
└── README.md
```
