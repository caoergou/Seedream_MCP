# 发布指南

## 🚀 发布流程

### 1. 更新版本号
```bash
# 编辑 pyproject.toml
version = "1.1.0"
```

### 2. 创建标签
```bash
git tag v1.1.0
git push origin v1.1.0
```

GitHub Actions 会自动：
- 测试代码
- 构建包
- 发布到 PyPI
- 构建 Docker 镜像
- 创建 GitHub Release

## ⚙️ 必需配置

在 GitHub 仓库设置中添加：
- `PYPI_API_TOKEN`：PyPI 发布令牌

## 📦 发布产物

- **PyPI**: `pip install seedream-mcp`
- **Docker**: `docker pull ghcr.io/caoergou/seedream-mcp`
- **GitHub Release**: 包含二进制文件和文档

## 🔄 版本号规范

- `v1.0.0`：主版本
- `v1.1.0`：功能更新
- `v1.0.1`：修复版本
- `v1.0.0-alpha.1`：预发布版本