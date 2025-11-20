# Seedream 4.0 MCP 工具

[![uvx](https://img.shields.io/badge/uvx-ready-brightgreen.svg)](https://github.com/astral-sh/uv)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![MCP](https://img.shields.io/badge/MCP-compatible-orange.svg)

基于火山引擎 Seedream 4.0 API 的 MCP 工具，支持 AI 图像生成。

## ⚡ 快速安装

### uvx 安装（推荐）
```bash
uvx run seedream-mcp
```

### Git 仓库安装
```bash
uvx run git+https://github.com/caoergou/Seedream_MCP
```

### Docker 安装
```bash
# 直接运行
docker run -e ARK_API_KEY=your_api_key_here ghcr.io/caoergou/seedream-mcp

# Docker Compose
curl -O https://raw.githubusercontent.com/caoergou/Seedream_MCP/main/docker-compose.yml
echo "ARK_API_KEY=your_api_key_here" > .env
docker-compose up -d
```

## 🎯 快速开始

### 1. 获取 API 密钥
访问 [火山引擎控制台](https://console.volcengine.com/) → API 密钥管理 → 创建密钥

### 2. 配置环境变量
创建 `.env` 文件：
```bash
ARK_API_KEY=your_api_key_here
```

### 3. 运行 MCP 服务器
```bash
uvx run seedream-mcp
```

## 🔧 Claude Desktop 配置

在 `claude_desktop_config.json` 中添加：
```json
{
  "mcpServers": {
    "seedream": {
      "command": "uvx",
      "args": ["seedream-mcp"]
    }
  }
}
```

重启 Claude Desktop 即可使用。

## 🎨 功能特性

- **文生图**：根据文本描述生成图像
- **图生图**：基于参考图像生成新图像
- **多图融合**：融合多张图片的特征
- **组图生成**：生成连续的图像序列
- **自动保存**：自动下载图片到本地

## 💬 使用示例

### 在 Claude 中直接对话
```
我：生成一只可爱的小猫咪，卡通风格
我：将这张图片转换为油画风格 [上传图片]
我：融合这三张图片的艺术风格 [上传多张图片]
```

## ⚙️ 环境配置

### 必需配置
```bash
ARK_API_KEY=your_api_key_here
```

### 可选配置
```bash
SEEDREAM_DEFAULT_SIZE=2K          # 图像尺寸：1K/2K/4K
SEEDREAM_AUTO_SAVE_ENABLED=true   # 自动保存图片
LOG_LEVEL=INFO                    # 日志级别
```

## 🛠️ 可用工具

1. **文生图** - `seedream_text_to_image`
2. **图生图** - `seedream_image_to_image`
3. **多图融合** - `seedream_multi_image_fusion`
4. **组图生成** - `seedream_sequential_generation`

## 🆘 常见问题

### Q: uvx 命令不存在？
A: 安装 uv：
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Q: 获取 API 密钥？
A: 访问 [火山引擎控制台](https://console.volcengine.com/) 创建密钥

### Q: 图片链接过期？
A: 启用自动保存功能，图片会保存到 `seedream_images/` 目录

## 🧪 开发者

### 本地开发
```bash
git clone https://github.com/caoergou/Seedream_MCP
cd Seedream_MCP
uv sync --dev
uv run python -m seedream_mcp.server
```

### 发布新版本
```bash
# 更新版本号
git tag v1.1.0
git push origin v1.1.0
# GitHub Actions 自动发布
```

## 📄 许可证

MIT License

## 🙏 致谢

- [火山引擎](https://www.volcengine.com/) - Seedream 4.0 AI 绘图服务
- [原项目仓库](https://github.com/tengmmvp/Seedream_MCP) - 初始代码基础和灵感

**🌟 如果这个项目有帮助，请给个 Star！**