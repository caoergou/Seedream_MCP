# Seedream 4.0 MCP 工具

[![uvx](https://img.shields.io/badge/uvx-ready-brightgreen.svg)](https://github.com/astral-sh/uv)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![MCP](https://img.shields.io/badge/MCP-compatible-orange.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

🚀 **基于火山引擎 Seedream 4.0 API 的现代化 MCP 工具，一键安装，开箱即用！**

## ⚡ 一键安装（仅需 30 秒）

### 方法 1：直接运行（推荐）

```bash
uvx run seedream-mcp
```

### 方法 2：从 GitHub 仓库运行

```bash
uvx run git+https://github.com/caoergou/Seedream_MCP
```

### 方法 3：Docker 运行

```bash
# 直接运行
docker run -e ARK_API_KEY=your_api_key_here caoergou/seedream-mcp

# 使用 Docker Compose（推荐）
curl -O https://raw.githubusercontent.com/caoergou/Seedream_MCP/main/docker-compose.yml
echo "ARK_API_KEY=your_api_key_here" > .env
docker-compose up -d
```

### 方法 4：本地运行（开发用）

```bash
git clone https://github.com/caoergou/Seedream_MCP
cd Seedream_MCP
uvx run .
```

> ✨ **uvx** 是现代 Python 应用运行器，类似于 Node.js 的 `npx`。它会自动：
> - 下载项目依赖
> - 创建隔离环境
> - 运行应用程序
> - 无需手动安装 Python 包！

## 🎯 快速开始

### 第一步：获取 API 密钥

1. 访问 [火山引擎控制台](https://console.volcengine.com/)
2. 注册/登录账号
3. 进入 API 密钥管理页面
4. 创建新的 API 密钥

### 第二步：配置环境变量

在项目根目录创建 `.env` 文件：

```bash
# 方法1：复制配置模板
uvx run --copy-env git+https://github.com/caoergou/Seedream_MCP cp .env.example .env

# 方法2：手动创建
echo "ARK_API_KEY=your_api_key_here" > .env
```

**编辑 `.env` 文件：**
```bash
# 必需：将 your_api_key_here 替换为实际密钥
ARK_API_KEY=your_api_key_here
```

### 第三步：运行 MCP 服务器

```bash
# ✅ 零配置运行
uvx run seedream-mcp

# 或者指定配置文件路径
uvx --env-file .env run seedream-mcp
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

重启 Claude Desktop 即可开始使用！

## 🎨 功能特性

- **🖼️ 文生图**：根据文本描述生成高质量图像
- **🎨 图生图**：基于参考图像和文本指令生成新图像
- **🎭 多图融合**：融合多张参考图的特征生成新图像
- **📚 组图生成**：生成一组内容关联的图像序列
- **💾 自动保存**：自动下载图片到本地，解决 URL 过期问题
- **📝 Markdown 支持**：自动生成图片的 Markdown 引用格式
- **🚀 零配置运行**：uvx 自动处理依赖和环境

## 💬 使用示例

### 在 Claude 中直接对话

```
我：帮我生成一只可爱的小猫咪，卡通风格，2K分辨率

我：将这张图片转换为油画风格，保持人物不变 [上传图片]

我：将这三张图片融合成一个艺术作品，突出科幻风格 [上传多张图片]

我：生成一个科幻城市景观系列，包含4张连续的场景图片
```

### Python 代码调用

```python
import asyncio
from seedream_mcp import SeedreamClient, SeedreamConfig

async def main():
    config = SeedreamConfig.from_env()
    client = SeedreamClient(config)

    try:
        # 一句话生成图片
        result = await client.text_to_image(
            prompt="一只可爱的小猫咪，卡通风格",
            auto_save=True  # 自动保存到本地
        )
        print(f"图片已保存到: {result['local_path']}")
    finally:
        await client.close()

asyncio.run(main())
```

## ⚙️ 环境配置

### 最简配置（仅需一个参数）

```bash
# 必需配置
ARK_API_KEY=your_api_key_here
```

### 可选配置（推荐设置）

```bash
# 默认图像质量
SEEDREAM_DEFAULT_SIZE=2K  # 1K/2K/4K

# 自动保存功能
SEEDREAM_AUTO_SAVE_ENABLED=true  # 自动保存图片
SEEDREAM_AUTO_SAVE_BASE_DIR=./seedream_images  # 保存目录

# 日志级别
LOG_LEVEL=INFO  # DEBUG/INFO/WARNING/ERROR
```

## 🛠️ 可用工具

### 1. **文生图** - `seedream_text_to_image`
根据文本描述生成图像
- 支持中英文提示词
- 可选尺寸：1K/2K/4K
- 自动水印保护

### 2. **图生图** - `seedream_image_to_image`
基于参考图像编辑生成新图像
- 支持 URL 和本地图片
- 保持原图构图，改变风格

### 3. **多图融合** - `seedream_multi_image_fusion`
融合 2-5 张图片的特征
- 智能权重分配
- 艺术效果融合

### 4. **组图生成** - `seedream_sequential_generation`
生成连续的图像序列
- 支持 1-10 张图片
- 保持风格和主题一致

## 💾 自动保存功能

- ✅ **永久存储**：自动下载避免 URL 过期
- 📁 **智能分类**：按日期和功能自动组织
- 🔄 **并发处理**：支持批量高效下载
- 📝 **Markdown 友好**：自动生成引用格式

**保存目录结构：**
```
seedream_images/
├── 2024-01-15/
│   ├── text_to_image/
│   │   ├── cute_cat_20240115_143022_abc123_2K.png
│   │   └── landscape_20240115_143045_def456_4K.png
│   └── image_to_image/
│       └── oil_painting_20240115_144001_ghi789_2K.png
└── 2024-01-16/
```

## 🆘 常见问题

### Q: uvx 命令不存在？
```bash
# 安装 uv (包含 uvx)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 或者使用包管理器
pip install uv
# macOS
brew install uv
# Windows
winget install astral-sh.uv
```

### Q: API 密钥如何获取？
访问 [火山引擎控制台](https://console.volcengine.com/) → API密钥管理 → 创建密钥

### Q: 生成的图片链接过期了？
启用自动保存功能（默认开启），图片会自动保存到本地 `seedream_images/` 目录

### Q: MCP 服务器连接失败？
检查 `.env` 文件中的 `ARK_API_KEY` 是否正确设置

### Q: uvx 缓存占用空间过大？
```bash
# 清理 uvx 缓存
uvx cache clean

# 查看缓存使用情况
uvx cache info
```

## 🚀 高级用法

### 指定 Python 版本
```bash
uvx --python 3.11 run seedream-mcp
```

### 安装特定版本
```bash
uvx run 'seedream-mcp==1.0.0'
```

### 传递额外参数
```bash
uvx run seedream-mcp --log-level DEBUG
```

### 开发模式运行
```bash
git clone https://github.com/caoergou/Seedream_MCP
cd Seedream_MCP
uvx run -e .  # -e 表示可编辑模式
```

## 🧪 开发者指南

### 本地开发环境
```bash
git clone https://github.com/caoergou/Seedream_MCP
cd Seedream_MCP
uv sync  # 同步开发依赖
uv run python -m seedream_mcp.server
```

### 运行测试
```bash
uv run pytest
uv run python test_uvx.py  # 兼容性测试
```

### 代码格式化
```bash
uv run black .
uv run mypy .
```

### 发布新版本
```bash
# 更新版本号
# 编辑 pyproject.toml 中的 version 字段

# 创建发布标签
git tag v1.1.0
git push origin v1.1.0

# GitHub Actions 会自动处理后续发布流程
# 详细说明请查看 [RELEASE.md](https://github.com/caoergou/Seedream_MCP/blob/main/RELEASE.md)
```

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！请先阅读 [贡献指南](CONTRIBUTING.md)。

## 🙏 致谢

- [火山引擎](https://www.volcengine.com/) - 提供强大的 Seedream 4.0 AI 绘图服务
- [Astral](https://astral.sh/) - 开发现代化的 uv/uvx 工具
- [Anthropic](https://anthropic.com/) - 开创 MCP 协议标准

---

**🌟 如果这个项目对你有帮助，请给个 Star 支持一下！**

**💡 有任何问题或建议？欢迎 [提交 Issue](https://github.com/caoergou/Seedream_MCP/issues)**