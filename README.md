# Artemis

> 基于 Hermes-Agent 最佳实践的新一代 AI 助手框架

## 项目概述

使用 Python 3.12+ 重写 OpenClaw (TypeScript/Node.js)，参考 Hermes-Agent 实现：

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
| 端口 | 18088 (WebSocket), 18080 (HTTP) |

## 项目结构

```
Artemis/
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
└── docker/                 # Dockerfile
```

## 开发环境

```bash
# 安装依赖
uv sync

# 类型检查
uv run mypy src/

# 运行测试
uv run pytest tests/
```

## Docker 测试

```bash
# 构建镜像
podman build -t artemis-test -f docker/Dockerfile .

# 运行测试容器
podman run --rm artemis-test pytest tests/
```

## CI/CD

- **Jenkins**: 192.168.1.3:8080
- **测试服务器**: 192.168.3.64
- **测试路径**: /home/kodakumi/projects/Artemis/

## 版本

- v0.1: MVP (Phase 1 完成)
- v0.2: Phase 2 完成
- ...

## 参考资料

- [Hermes-Agent](https://github.com/NousResearch/hermes-agent)
- [OpenClaw](https://github.com/openclaw/openclaw)
- [feishu-oapi](https://open.feishu.cn/)

---

*更新时间: 2026-04-14*
