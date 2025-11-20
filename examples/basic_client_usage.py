#!/usr/bin/env python3
"""
基础客户端使用示例

演示 SeedreamClient 的正确使用方法。
注意：客户端 API 不包含 auto_save 参数，这些功能在 MCP 工具层面处理。
"""

import asyncio
from seedream_mcp import SeedreamClient, SeedreamConfig


async def basic_text_to_image():
    """基础的文生图示例"""
    # 创建配置
    config = SeedreamConfig.from_env_with_api_key("your_api_key_here")

    # 创建客户端
    async with SeedreamClient(config) as client:
        # 客户端方法只支持基础参数
        result = await client.text_to_image(
            prompt="一只可爱的小猫咪",
            size="2K",
            watermark=False,
            response_format="url"
        )

        if result.get("success"):
            image_url = result["data"][0]["url"]
            print(f"✅ 生成成功!")
            print(f"🖼️ 图像URL: {image_url}")
            print(f"📊 使用情况: {result.get('usage', {})}")
        else:
            print(f"❌ 生成失败: {result}")


async def basic_image_to_image():
    """基础的图生图示例"""
    config = SeedreamConfig.from_env_with_api_key("your_api_key_here")

    async with SeedreamClient(config) as client:
        result = await client.image_to_image(
            prompt="将这张图片转换为油画风格",
            image="https://example.com/image.jpg",  # 替换为实际图片URL
            size="2K",
            watermark=False
        )

        if result.get("success"):
            image_url = result["data"][0]["url"]
            print(f"✅ 转换成功!")
            print(f"🖼️ 图像URL: {image_url}")
        else:
            print(f"❌ 转换失败: {result}")


# 🔧 辅助函数，创建包含 API 密钥的配置
def create_config_with_api_key(api_key: str) -> SeedreamConfig:
    """创建包含 API 密钥的配置对象"""
    import os

    # 临时设置环境变量
    os.environ["ARK_API_KEY"] = api_key

    # 从环境变量创建配置
    return SeedreamConfig.from_env()


# 为 SeedreamConfig 添加便捷方法
@classmethod
def from_env_with_api_key(cls, api_key: str):
    """从环境变量和给定的 API 密钥创建配置"""
    import os
    old_key = os.environ.get("ARK_API_KEY")
    try:
        os.environ["ARK_API_KEY"] = api_key
        return SeedreamConfig.from_env()
    finally:
        if old_key:
            os.environ["ARK_API_KEY"] = old_key
        else:
            os.environ.pop("ARK_API_KEY", None)


# 动态添加方法到类
SeedreamConfig.from_env_with_api_key = from_env_with_api_key


async def main():
    """主函数"""
    print("🎨 Seedream MCP 基础客户端使用示例")
    print("=" * 50)

    # 替换为你的实际 API 密钥
    API_KEY = "your_api_key_here"

    if API_KEY == "your_api_key_here":
        print("❌ 请先设置 API_KEY 变量")
        return

    try:
        print("\n1. 文生图示例:")
        print("-" * 30)
        await basic_text_to_image()

        print("\n2. 图生图示例:")
        print("-" * 30)
        # await basic_image_to_image()  # 需要有效的图片URL

    except Exception as e:
        print(f"❌ 错误: {e}")


if __name__ == "__main__":
    asyncio.run(main())