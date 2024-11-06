FROM python:3.12-bookworm AS base

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Working directory
WORKDIR /app

# Copy python declarative requirement with modern pyproject.toml
COPY ./pyproject.toml /app
COPY ./uv.lock /app

# Sync the project with pyproject.toml and make virtual environtment
RUN uv sync --frozen --no-cache --compile-bytecode


FROM scratch

# Copy uv binary to scratch
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy virtual environment to scratch
COPY --from=base .venv /app

# Copy all project file to scratch
COPY . /app