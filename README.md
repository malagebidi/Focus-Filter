# Focus-Filter

**Focus Filter** is a custom filter list designed for **AdGuard**. Its primary goal is to remove recommended feeds, distracting elements, and "doom-scrolling" traps from various websites  (primarily Chinese platforms), allowing you to focus on the content you actually want to watch.

> **Note:** This filter utilizes advanced AdGuard scriptlets and extended CSS. It is best used with the AdGuard browser extension.

## 🎯 Features

- **Remove Algorithmic Recommendations:** Hides "Hot," "Trending," and "Recommended for you" feeds on homepages and sidebars.
- **Clean UI:** Removes distracting promotional banners, floating buttons, and red notification dots.
- **Search Focus:** Clears random/distracting placeholder text in search bars.

## 🚀 How to Use

Copy the raw link of the rule file and add it to AdGuard.

1. Open **AdGuard** Settings.
2. Go to **Filters** -> **Custom**.
3. Click **Add custom filter**.
4. Paste the following URL:
   
   ```text
   https://raw.githubusercontent.com/malagebidi/Focus-Filter/refs/heads/main/filter.txt
   ```
   *(⚠️ Please replace `rules.txt` with your actual filename if it's different)*

## 🛠️ Requirements

This list is optimized for **AdGuard**.
While it may work partially with **uBlock Origin**, some rules (specifically scriptlets like `set-attr`) are strictly AdGuard syntax and may not function on other blockers.

## 🤝 Contributing

Found a distracting element that needs to be removed?
- **Open an Issue:** Describe the website and the element you want to hide.
- **Submit a Pull Request:** Feel free to contribute your own rules!

## 📄 License

This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for details.

---

*Disclaimer: This project is not affiliated with AdGuard or any of the websites mentioned above. It is a community-maintained filter list for personal customization.*
```
