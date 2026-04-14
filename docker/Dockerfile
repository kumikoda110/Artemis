# Artemis - 测试镜像
# 使用 podman 构建: podman build -t artemis-test -f docker/Dockerfile .

FROM 192.168.1.3:8088/artemis/docker.xuanyuan.run/library/python:latest

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

# 生成 lockfile 并安装依赖
RUN uv lock && uv sync

# 复制源代码
COPY src/ ./src/
COPY tests/ ./tests/

# 默认命令: 运行所有测试
CMD ["python", "-m", "pytest", "tests/", "-v", "--tb=short"]
