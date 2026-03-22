# VC 每日简报

每天早上 9 点（北京时间），自动发送一封结构化的科技投资日报到你的邮箱。

## 📬 简报内容

| 板块 | 内容 | 数据来源 |
|------|------|----------|
| 💰 **融资头条** | AI/科技公司最新融资交易，含金额、轮次、领投方 | Crunchbase, TechCrunch, Bloomberg, 36Kr, CB Insights 等 |
| 🚀 **技术突破** | 新模型发布、产品更新、研究进展 | OpenAI, Google AI, NVIDIA, DeepMind, Microsoft AI 等官方博客 |
| 🏛 **湾区顶级 VC 动态** | 最新投资观点、行业分析 | a16z, Sequoia, Greylock, Accel, Bessemer, Kleiner Perkins 等 14 家 VC 官网 |
| 📡 **科技媒体更新** | AI 行业重要报道 | TechCrunch, VentureBeat, The Verge, MIT Tech Review, Wired 等 |
| 🎙 **播客追踪** | 投资/科技播客新集速览 | Lex Fridman, All-In, 20VC, Acquired, BG2Pod 等 11 个频道 |
| 📰 **行业资讯** | 独立分析师与 newsletter | Stratechery, Not Boring, Lenny's Newsletter 等 |

所有内容均由 **Gemini AI 生成中文摘要**，详细到可以直接转发给同事。

## 🚀 快速部署（5 分钟）

### 1. Fork 本仓库

点击右上角 **Fork** 按钮。

### 2. 配置 Secrets

进入你 fork 的仓库 → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**，添加以下 4 个：

| Secret 名称 | 说明 | 获取方式 |
|---|---|---|
| `GMAIL_USER` | 发件 Gmail 地址 | 你的 Gmail，如 `yourname@gmail.com` |
| `GMAIL_APP_PASSWORD` | Gmail 应用密码（16 位） | [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords) 创建 |
| `GEMINI_API_KEY` | Gemini API 密钥（免费） | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) 创建 |
| `RECIPIENT_EMAIL` | 收件邮箱，多人用逗号分隔 | 如 `a@gmail.com,b@outlook.com` |

### 3. 启用 GitHub Actions

进入仓库 → **Actions** 标签页 → 点击 **I understand my workflows, go ahead and enable them**。

### 4. 测试发送

进入 **Actions** → 选择 **每日简报** workflow → 点击 **Run workflow** → **Run workflow**。

几分钟后检查收件箱，第一封简报就到了。

之后每天北京时间早上 9:00 自动发送，无需任何维护。

## ⚙️ 自定义

### 修改发送时间

编辑 `.github/workflows/daily-briefing.yml` 中的 cron 表达式：

```yaml
schedule:
  - cron: '0 1 * * *'  # UTC 1:00 = 北京时间 9:00
```

### 添加播客源

编辑 `config/default-sources.json`，在 `podcasts` 数组中添加：

```json
{
  "name": "播客名称",
  "type": "youtube_channel",
  "url": "https://www.youtube.com/@频道名",
  "channelId": "频道ID"
}
```

### 添加/修改 RSS 源或 VC 列表

直接编辑 `scripts/send_briefing.py` 中的 `FUNDING_SOURCES`、`TECH_SOURCES`、`MEDIA_SOURCES`、`VC_SCRAPE_SOURCES`、`BLOG_SOURCES` 列表。

## 📄 License

MIT
