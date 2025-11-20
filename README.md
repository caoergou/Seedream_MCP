# Seedream 4.0 MCP 工具

[![uvx](https://img.shields.io/badge/uvx-ready-brightgreen.svg)](https://github.com/astral-sh/uv)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![MCP](https://img.shields.io/badge/MCP-compatible-orange.svg)

基于火山引擎 Seedream 4.0 API 的 MCP 工具，支持 AI 图像生成。

## ⚡ 快速启动

```bash
# 直接传递 API 密钥
uvx run seedream-mcp --api-key your_api_key_here

# 配置 Claude Desktop
{
  "mcpServers": {
    "seedream": {
      "command": "uvx",
      "args": [
        "seedream-mcp",
        "--api-key", "your_api_key_here"
      ]
    }
  }
}
```

## 🔧 启动参数

```bash
--api-key TEXT        # API 密钥（必需）
--config-file PATH    # 配置文件路径
--default-size [1K|2K|4K]  # 图像尺寸 (默认: 2K)
--watermark                 # 启用水印
--log-level [DEBUG|INFO|WARNING|ERROR]  # 日志级别
```

## 🎨 功能

- **文生图**：文本生成图像
- **图生图**：图像转换风格
- **多图融合**：融合多张图片
- **组图生成**：生成图像序列
- **自动保存**：图片本地存储

## 🛠️ 可用工具

1. `seedream_text_to_image`
2. `seedream_image_to_image`
3. `seedream_multi_image_fusion`
4. `seedream_sequential_generation`

## 🆘 常见问题

**Q: uvx 命令不存在？**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Q: 如何获取 API 密钥？**
访问 [火山引擎控制台](https://console.volcengine.com/) 创建密钥

## 🧪 开发

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