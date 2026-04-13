# OpenClaw-Python 重写项目

> 基于 Hermes-Agent 最佳实践的新一代 AI 助手框架

## 项目概述

将 OpenClaw (TypeScript/Node.js) 使用 Python 3.12+ 完全重写，参考 Hermes-Agent 实现：

- 智能模型路由
- 自动上下文压缩
- SQLite 持久化记忆
- 飞书 + Telegram 渠道支持

## 技术栈

| 组件 | 选择 |
|------|------|
| 语言 | Python 3.12+ |
| Web 框架 | FastAPI |
| 数据库 | SQLite + FTS5 |
| 协议 | 100% ACP 兼容 |
| Channel | 飞书 (feishu-oapi) + Telegram |

## 项目结构

```
openclaw-rewrite/
├── src/                    # 源代码
│   ├── gateway/            # 网关层
│   ├── protocol/           # 协议层
│   ├── session/            # 会话层
│   ├── agent/              # Agent 核心
│   ├── channels/           # 渠道层
│   └── tools/              # 工具系统
├── tests/
│   ├── unit/               # 单元测试
│   └── integration/        # 集成测试
├── docker/                 # Dockerfile
└── scripts/                # 工具脚本
```

## 开发环境

```bash
# 安装依赖
uv sync

# 类型检查
uv run mypy src/

# 运行测试
uv run pytest tests/

# 本地运行
uv run python -m src.gateway.server
```

## Docker 测试

```bash
# 构建镜像
cd docker && podman build -t openclaw-test .

# 运行测试容器
podman run --rm openclaw-test pytest tests/

# 交互式开发
podman run -it --rm openclaw-test bash
```

## CI/CD

- Jenkins: `192.168.1.3:8080`
- 测试服务器: `192.168.3.64`
- 测试路径: `/home/kodakumi/projects/openclaw-rewrite/`

## 参考资料

- [Hermes-Agent](https://github.com/NousResearch/hermes-agent)
- [OpenClaw](https://github.com/openclaw/openclaw)

---

*更新时间: 2026-04-13*
