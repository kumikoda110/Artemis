# OpenClaw Python 重写 - 测试镜像
# 使用 podman 构建: podman build -t openclaw-test .

FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# 安装 uv (快速 Python 包管理)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# 复制依赖文件
COPY pyproject.toml ./

# 安装 Python 依赖
RUN uv sync

# 复制源代码
COPY src/ ./src/
COPY tests/ ./tests/

# 安装 uvloop (高性能异步)
RUN uv pip install uvloop

# 默认命令: 运行所有测试
CMD ["pytest", "tests/", "-v", "--tb=short"]
