# 🚀 发布指南

## 📋 发布流程概览

本项目使用 GitHub Actions 实现自动化发布，支持以下功能：

- ✅ 自动化测试（Python 3.8-3.12）
- 📦 PyPI 包发布
- 🐳 Docker 镜像发布
- 🏷️ GitHub Release 创建
- 📝 自动更新文档

## 🎯 如何发布新版本

### 1. 准备发布

```bash
# 确保代码是最新的
git pull origin main

# 检查测试是否通过
uv sync --dev
uv run python test_uvx.py
```

### 2. 更新版本号

在 `pyproject.toml` 中更新版本号：

```toml
[project]
version = "1.1.0"  # 修改这里
```

或者使用命令行工具：
```bash
# 更新版本号（示例）
uv run python -c "
import re
content = open('pyproject.toml').read()
content = re.sub(r'version = "[\d.]+"', 'version = "1.1.0"', content)
open('pyproject.toml', 'w').write(content)
print('版本号已更新为 1.1.0')
"
```

### 3. 创建发布标签

```bash
# 提交版本号变更
git add pyproject.toml
git commit -m "🔖 Bump version to 1.1.0"

# 创建并推送标签
git tag v1.1.0
git push origin v1.1.0
```

### 4. 触发发布

推送标签后，GitHub Actions 会自动：
1. 在所有 Python 版本上运行测试
2. 构建 Python 包（wheel 和 sdist）
3. 创建 GitHub Release
4. 发布到 PyPI
5. 构建 Docker 镜像
6. 更新文档

## 🔧 必需的 Secrets

在 GitHub 仓库设置中配置以下 Secrets：

### PyPI API Token
1. 访问 [PyPI](https://pypi.org/)
2. 进入 Account Settings → API tokens
3. 创建新的 API token
4. 在 GitHub 仓库设置中添加：
   - Name: `PYPI_API_TOKEN`
   - Value: 你的 PyPI API token

### GitHub Container Registry
- **自动认证**：使用 `GITHUB_TOKEN` 自动认证
- **无需额外配置**：GitHub Actions 自动处理 GHCR 权限
- **仓库地址**：`ghcr.io/caoergou/seedream-mcp`

## 📦 发布产物

### GitHub Release
- 自动生成变更日志
- 包含安装说明
- 附带 Python 包文件

### PyPI 包
```bash
# 安装发布版本
pip install seedream-mcp

# 安装特定版本
pip install seedream-mcp==1.1.0
```

### Docker 镜像（GitHub Container Registry）
```bash
# 拉取最新版本
docker pull ghcr.io/caoergou/seedream-mcp:latest

# 拉取特定版本
docker pull ghcr.io/caoergou/seedream-mcp:v1.1.0

# 拉取语义版本标签
docker pull ghcr.io/caoergou/seedream-mcp:v1.1

# 使用 Docker Compose
curl -O https://raw.githubusercontent.com/caoergou/Seedream_MCP/main/docker-compose.yml
# 编辑 .env 文件设置 ARK_API_KEY
docker-compose up -d
```

## 🏷️ 版本号规范

遵循 [语义化版本](https://semver.org/lang/zh-CN/)：

- **主版本号 (MAJOR)**：不兼容的 API 修改
- **次版本号 (MINOR)**：向下兼容的功能性新增
- **修订号 (PATCH)**：向下兼容的问题修正

### 预发布版本
- `v1.1.0-alpha.1` - Alpha 版本
- `v1.1.0-beta.1` - Beta 版本
- `v1.1.0-rc.1` - Release Candidate

## 🚨 发布检查清单

发布前确认：
- [ ] 所有测试通过
- [ ] 版本号已更新
- [ ] CHANGELOG 已更新
- [ ] 文档是最新的
- [ ] 示例代码可正常工作

发布后确认：
- [ ] GitHub Release 创建成功
- [ ] PyPI 包发布成功
- [ ] Docker 镜像构建成功
- [ ] 文档链接正确
- [ ] 示例命令有效

## 🔄 回滚流程

如果发现问题需要回滚：

1. **GitHub Release**
   - 删除错误的 Release
   - 删除错误的标签
   - 重新创建正确的标签

2. **PyPI 包**
   - 联系 PyPI 支持删除包
   - 或者发布新版本修复问题

3. **Docker 镜像**
   ```bash
   # 拉取之前的版本
   docker pull caoergou/seedream-mcp:v1.0.0

   # 重新标签
   docker tag caoergou/seedream-mcp:v1.0.0 caoergou/seedream-mcp:latest
   docker push caoergou/seedream-mcp:latest
   ```

## 📊 监控发布

发布后可以通过以下方式监控：

1. **GitHub Release**
   - 查看下载量
   - 监控 Issues 和 PR

2. **PyPI**
   - 查看下载统计
   - 监控版本使用情况

3. **GitHub Container Registry**
   - 查看 [Packages 页面](https://github.com/caoergou/Seedream_MCP/pkgs/container/seedream-mcp)
   - 监控镜像拉取次数
   - 查看使用统计

## 🆘 常见问题

### Q: 发布失败怎么办？
A: 检查 GitHub Actions 日志，确认：
- Secrets 配置是否正确
- 版本号格式是否正确
- 测试是否全部通过

### Q: 如何撤销发布？
A: 立即联系平台支持：
- PyPI: support@pypi.org
- GitHub: 删除 Release 和标签
- GitHub Container Registry: 删除包版本

### Q: 如何手动发布？
A: 本地构建和发布：
```bash
# 构建包
uv build --wheel --sdist

# 发布到 PyPI
uv publish

# 构建 Docker 镜像
docker build -t ghcr.io/caoergou/seedream-mcp:v1.1.0 .
docker push ghcr.io/caoergou/seedream-mcp:v1.1.0
```

---

💡 **提示**: 首次发布需要配置 PyPI 的认证信息。GitHub Container Registry 会自动使用 GITHUB_TOKEN 认证。建议先在测试仓库验证流程无误后再进行正式发布。