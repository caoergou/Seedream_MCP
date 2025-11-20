# Seedream 4.0 MCP 工具

[![uvx](https://img.shields.io/badge/uvx-ready-brightgreen.svg)](https://github.com/astral-sh/uv)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![MCP](https://img.shields.io/badge/MCP-compatible-orange.svg)

基于火山引擎 Seedream 4.0 API 的 MCP 工具，支持 AI 图像生成。

## ⚡ 快速安装

### 方法 1：uvx 一键启动（推荐）

```bash
# 直接从 GitHub 仓库启动
uvx run git+https://github.com/caoergou/Seedream_MCP --api-key your_api_key_here

# 或者先克隆再启动
git clone https://github.com/caoergou/Seedream_MCP
cd Seedream_MCP
uvx . --api-key your_api_key_here
```

### 方法 2：Docker Compose

```bash
# 下载 docker-compose.yml
curl -O https://raw.githubusercontent.com/caoergou/Seedream_MCP/main/docker-compose.yml

# 启动服务
ARK_API_KEY=your_api_key_here docker-compose up -d
```

## 🔧 Claude Desktop 配置

在 `claude_desktop_config.json` 中添加：

```json
{
  "mcpServers": {
    "seedream": {
      "command": "uvx",
      "args": [
        "git+https://github.com/caoergou/Seedream_MCP",
        "--api-key", "your_api_key_here"
      ]
    }
  }
}
```

重启 Claude Desktop 即可使用。

## ⚙️ 启动参数

```bash
--api-key TEXT        # API 密钥（必需）
--default-size [1K|2K|4K]  # 图像尺寸 (默认: 2K)
--watermark                 # 启用水印
--log-level [DEBUG|INFO|WARNING|ERROR]  # 日志级别
```

### 使用示例

```bash
# 基础使用
uvx run git+https://github.com/caoergou/Seedream_MCP \
  --api-key your_key

# 高质量图像 + 调试模式
uvx run git+https://github.com/caoergou/Seedream_MCP \
  --api-key your_key --default-size 4K --log-level DEBUG
```

## 🎨 功能特性

- **文生图**：文本生成图像
- **图生图**：图像转换风格
- **多图融合**：融合多张图片
- **组图生成**：生成图像序列
- **自动保存**：图片本地存储

## 🛠️ 可用工具

1. `seedream_text_to_image` - 文生图
2. `seedream_image_to_image` - 图生图
3. `seedream_multi_image_fusion` - 多图融合
4. `seedream_sequential_generation` - 组图生成

## 🆘 常见问题

**Q: uvx 命令不存在？**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Q: 如何获取 API 密钥？**
访问 [火山引擎控制台](https://console.volcengine.com/) 创建密钥

**Q: Docker 服务无法启动？**
确保设置了环境变量：
```bash
export ARK_API_KEY=your_key
docker-compose up -d
```

## 🧪 本地开发

```bash
git clone https://github.com/caoergou/Seedream_MCP
cd Seedream_MCP
uv sync --dev
uv run python -m seedream_mcp.server --api-key your_key
```

## 📄 许可证

MIT License

## 🙏 致谢

- [火山引擎](https://www.volcengine.com/) - Seedream 4.0 AI 绘图服务
- [原项目仓库](https://github.com/tengmmvp/Seedream_MCP) - 初始代码基础

**🌟 如果这个项目有帮助，请给个 Star！**