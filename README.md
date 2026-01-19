# 🎯 Focus-Filter
**Focus Filter** is a custom filter list designed for **AdGuard**, its primary goal is to remove recommended feeds, distracting elements, and "doom-scrolling" traps from various websites, allowing you to focus on the content you actually want to watch.

> [!NOTE]
> This filter utilizes advanced AdGuard scriptlets and extended CSS. It is best used with the AdGuard browser extension.

## 💡 Motivation
Over the years, the internet has gradually evolved into an **Attention Economy**. It is not just about addictive recommendation feeds; cluttered interfaces and superfluous design elements also scatter our focus and overwhelm our vision.

Focus Filter originated as a personal collection of rules built from my daily use, and now I am open-sourcing it to invite community collaboration.

## 🛡️ Coverage
Major platforms covered include:

| Category | Websites |
| :--- | :--- |
| Social Media | 微博, 豆瓣电影 |
| Video | 哔哩哔哩, 芒果TV, 斗鱼, 快手直播 |
| Tech | V2EX |
| Adult | Pornhub, 91porn, MissAV, Jable.TV, Jav.Guru |

## ⚙️ Setup
1. Open AdGuard Settings
2. Go to Filters -> Custom
3. Click Add custom filter
4. Paste the following URL and click Next
    ```text
    https://raw.githubusercontent.com/malagebidi/Focus-Filter/refs/heads/main/filter.txt
    ```
5. Check the trusted checkbox

> [!TIP]  
> Websites change frequently. If you notice broken features or missing content, try disabling this filter temporarily to check if that resolves the issue.

## 🧩 Best With
While Focus Filter covers a wide range of websites, highly complex platforms often require specialized tools. Using dedicated extensions alongside our rules ensures the best possible experience.

*   GIF: [Animation Policy](https://chromewebstore.google.com/detail/animation-policy/ncigbofjfbodhkaffojakplpmnleeoee)
*   YouTube: [RYS — Remove YouTube Suggestions](https://chromewebstore.google.com/detail/rys-%E2%80%94-remove-youtube-sugg/cdhdichomdnlaadbndgmagohccgpejae)
*   Twitch: [BetterTTV](https://chromewebstore.google.com/detail/betterttv/ajopnjidmegmdimjlfnijceegpefgped)

## 🤝 Contributing
Read [Contributing Guide](CONTRIBUTING.md) for details on how to report issues or submit new rules.

## 📄 License
This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for details.
