# 🎯 Focus-Filter
**Focus Filter** 是一个专为 **AdGuard** 设计的自定义过滤列表，其主要目标是移除来自各种网站的推荐内容、干扰元素和“信息流陷阱”，让您专注于真正想看的内容。

> [!NOTE]
> 本过滤器采用了 AdGuard 高级脚本和扩展 CSS 技术，建议搭配 AdGuard 浏览器扩展使用效果最佳。

## 💡 动机
多年来，互联网逐渐演变为一种**注意力经济**。这不仅体现在令人上瘾的推荐信息流上，杂乱的界面和冗余的设计元素同样分散着我们的注意力，淹没了我们的视野。

Focus Filter 最初是我基于日常使用经验总结的个人规则集，如今我将其开源，诚邀社区共同协作完善。

## 🛡️ 范围
主要覆盖平台包括：

| 类别 | 网站 |
| :--- | :--- |
| AI | Poe |
| Social Media | 微博, 豆瓣电影 |
| Tech | V2EX |
| Video & Live | 哔哩哔哩, 芒果TV, 腾讯视频, 斗鱼, 快手直播 |
| Adult | Pornhub, 91porn, MissAV, Jable.TV, Jav.Guru |

## ⚙️ Setup
### 1. Choose an Edition

* **Standard Edition (Recommended)**  
Removes ads, feeds, and major distractions while keeping core functionality intact.
  ```text
  https://raw.githubusercontent.com/malagebidi/Focus-Filter/main/filter.txt
  ```

* **Zen Mode Edition**  
**Aggressive.** Includes all Standard rules plus removes gift bars, decorative headers, and floating widgets for a minimalist experience.
  ```text
  https://raw.githubusercontent.com/malagebidi/Focus-Filter/main/filter_zen.txt
  ```

### 2. Installation
1. Open AdGuard Settings
2. Go to **Filters** -> **Custom**
3. Click **Add custom filter**
4. Paste the URL you copied above and click **Next**
5. **Check** the "Trusted" checkbox

> [!TIP]  
> Websites change frequently. If you notice broken features or missing content, try disabling this filter temporarily to check if that resolves the issue.

## 🧩 Best With
While Focus Filter covers a wide range of websites, highly complex platforms often require specialized tools. Using dedicated extensions alongside our rules ensures the best possible experience.

*   GIF: [Animation Policy](https://chromewebstore.google.com/detail/animation-policy/ncigbofjfbodhkaffojakplpmnleeoee)
*   YouTube: [RYS — Remove YouTube Suggestions](https://chromewebstore.google.com/detail/rys-%E2%80%94-remove-youtube-sugg/cdhdichomdnlaadbndgmagohccgpejae)
*   Twitch: [BetterTTV](https://chromewebstore.google.com/detail/betterttv/ajopnjidmegmdimjlfnijceegpefgped)
*   X: [Control Panel for Twitter](https://chromewebstore.google.com/detail/control-panel-for-twitter/kpmjjdhbcfebfjgdnpjagcndoelnidfj)

## 🤝 Contributing
Read [Contributing Guide](CONTRIBUTING.md) for details on how to report issues or submit new rules.

## 📄 License
This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for details.
