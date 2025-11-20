# Seedream 4.0 MCP 工具

[![uvx](https://img.shields.io/badge/uvx-ready-brightgreen.svg)](https://github.com/astral-sh/uv)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![MCP](https://img.shields.io/badge/MCP-compatible-orange.svg)

基于火山引擎 Seedream 4.0 API 的 MCP 工具，支持 AI 图像生成。

## ⚡ 极简启动

### 直接启动（无需配置文件）
```bash
# 最简单的方式 - 直接传递 API 密钥
uvx run seedream-mcp --api-key your_api_key_here

# 完整配置
uvx run seedream-mcp \
  --api-key your_key \
  --default-size 4K \
  --log-level DEBUG
```

### 其他启动方式
```bash
# Git 仓库安装
uvx run git+https://github.com/caoergou/Seedream_MCP \
  --api-key your_key

# Docker 运行
docker run -e ARK_API_KEY=your_key ghcr.io/caoergou/seedream-mcp

# 本地运行
python -m seedream_mcp.server --api-key your_key
```

## 🎯 一分钟上手

### 1. 获取 API 密钥
访问 [火山引擎控制台](https://console.volcengine.com/) → API 密钥管理 → 创建密钥

### 2. 直接运行
```bash
# 复制你的 API 密钥，直接运行
uvx run seedream-mcp --api-key paste_your_key_here
```

### 3. 配置 Claude Desktop
在 `claude_desktop_config.json` 中添加：
```json
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

## ⚙️ 启动参数

```bash
seedream-mcp --help

# 核心参数
--api-key TEXT        # 火山引擎 API 密钥（必需）
--config-file PATH    # 配置文件路径（可选）

# 图像设置
--default-size [1K|2K|4K]  # 默认图像尺寸 (默认: 2K)
--watermark                 # 启用默认水印
--model-id TEXT             # 模型 ID

# 调试设置
--log-level [DEBUG|INFO|WARNING|ERROR]  # 日志级别
--base-url TEXT                       # API 基础 URL
```

### 常用启动命令

```bash
# 基础使用
uvx run seedream-mcp --api-key your_key

# 高质量图像
uvx run seedream-mcp --api-key your_key --default-size 4K

# 启用水印
uvx run seedream-mcp --api-key your_key --watermark

# 调试模式
uvx run seedream-mcp --api-key your_key --log-level DEBUG
```

## 🛠️ 可用工具

1. **文生图** - `seedream_text_to_image`
2. **图生图** - `seedream_image_to_image`
3. **多图融合** - `seedream_multi_image_fusion`
4. **组图生成** - `seedream_sequential_generation`

## 🆘 常见问题

### Q: 如何获取 API 密钥？
A: 访问 [火山引擎控制台](https://console.volcengine.com/) 创建密钥

### Q: uvx 命令不存在？
A: 安装 uv：
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Q: 图片链接过期？
A: 自动保存功能会将图片保存到 `seedream_images/` 目录

### Q: 如何设置默认配置？
A: 创建配置文件：
```bash
# config.env
ARK_API_KEY=your_key
SEEDREAM_DEFAULT_SIZE=4K
LOG_LEVEL=DEBUG

# 使用配置文件
uvx run seedream-mcp --config-file config.env
```

## 🧪 开发者

### 本地开发
```bash
git clone https://github.com/caoergou/Seedream_MCP
cd Seedream_MCP
uv sync --dev
uv run python -m seedream_mcp.server --api-key your_key
```

### 客户端 API 使用（高级）
```python
import asyncio
from seedream_mcp import SeedreamClient, SeedreamConfig

async def demo():
    # 客户端方法（不包含 auto_save）
    config = SeedreamConfig(api_key="your_key")
    async with SeedreamClient(config) as client:
        result = await client.text_to_image(
            prompt="一只可爱的小猫咪",
            size="2K",
            watermark=False
        )
        print(f"图像URL: {result['data'][0]['url']}")

# MCP 工具方法（包含 auto_save）
# 通过 Claude Desktop 或 MCP 协议调用，支持完整的参数
```

**注意**: `auto_save` 等高级功能是 MCP 工具层面的，客户端 API 提供基础功能。

### 发布新版本
```bash
git tag v1.1.0
git push origin v1.1.0
```

## 📄 许可证

MIT License

## 🙏 致谢

- [火山引擎](https://www.volcengine.com/) - Seedream 4.0 AI 绘图服务
- [原项目仓库](https://github.com/tengmmvp/Seedream_MCP) - 初始代码基础和灵感

**🌟 如果这个项目有帮助，请给个 Star！**