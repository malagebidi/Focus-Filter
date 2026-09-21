# 🎯 Focus-Filter
**Focus Filter** 是一个专为 **AdGuard** 设计的自定义过滤器，其主要目标是移除来自各种网站的推荐内容、干扰元素和“信息流陷阱”，让您专注于真正想看的内容。

> [!NOTE]
> 本过滤器采用了 AdGuard 高级脚本和扩展 CSS 技术，建议搭配 AdGuard 浏览器扩展使用效果最佳。

## 💡 动机
多年来，互联网逐渐演变为一种**注意力经济**。这不仅体现在令人上瘾的推荐信息流上，杂乱的界面和冗余的设计元素同样分散着我们的注意力，淹没了我们的视野。

Focus Filter 源于我日常使用中积累的一套个人规则。现在我将其开源，诚邀社区共同参与协作与完善。

## 🛡️ 范围
主要覆盖平台包括：

| 类别 | 网站 |
| :--- | :--- |
| AI | Poe |
| Social Media | 微博，豆瓣电影 |
| Tech | V2EX，cnBeta |
| Video & Live | 哔哩哔哩，YouTube，芒果TV，腾讯视频，斗鱼 |
| Adult | Pornhub，91porn，MissAV，Jable.TV，Jav.Guru |

## ⚙️ 设置
### 1. 选择一个版本

* **标准版（推荐）**  
移除推荐流和主要干扰项，同时保持网站核心功能完整。
  ```text
  https://raw.githubusercontent.com/malagebidi/Focus-Filter/main/filter.txt
  ```

* **禅模式版**  
包含标准规则，并进一步移除网站的功能性部件，页脚甚至其他主观不喜欢的内容，以提供极简体验。
  ```text
  https://raw.githubusercontent.com/malagebidi/Focus-Filter/main/filter_zen.txt
  ```

### 2. 安装
1. 打开 AdGuard 设置
2. 前往**过滤器**->**自定义**
3. 点击**添加自定义过滤器**
4. 粘贴您上面复制的 URL，然后点击**下一步**
5. **勾选**“受信任”复选框

> [!TIP]  
> 网站经常发生变动。如遇功能失效或内容显示不全，请尝试暂时关闭此过滤器以排查问题。

## 🧩 最佳搭档
虽然 Focus Filter 覆盖了广泛的网站，但高度复杂的平台通常需要专门的工具。将专用扩展与我们的规则一同使用，可确保获得最佳体验。

*   GIF: [Animation Policy](https://chromewebstore.google.com/detail/animation-policy/ncigbofjfbodhkaffojakplpmnleeoee)
*   Twitch: [BetterTTV](https://chromewebstore.google.com/detail/betterttv/ajopnjidmegmdimjlfnijceegpefgped)

## 🤝 贡献
阅读[贡献指南](CONTRIBUTING.md)以了解如何报告问题或者提交新的规则。

## 📄 许可证
本项目根据 **GNU 通用公共许可证 v3.0** 获得许可。有关详细信息，请参阅[LICENSE](LICENSE)文件。
