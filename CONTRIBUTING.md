# Contributing to Focus-Filter

First off, thank you for considering contributing to Focus-Filter! 
Whether you are reporting a missing rule, fixing a broken website, or submitting a new filter, your help is appreciated.

Since this repository focuses primarily on **Chinese platforms**, issues and pull requests in both **English** and **Chinese (中文)** are welcome.

## 🐛 Reporting Issues

If you find a website where the filter is not working, or if a rule is breaking a website's functionality, please open an Issue.

**Please include the following details:**

1.  **URL:** The exact link where the issue occurs.
2.  **Description:** 
    - What is not being blocked? (e.g., "The recommended video feed on the right sidebar")
    - Or what is broken? (e.g., "The login button disappeared")
3.  **Screenshot (Highly Recommended):** A screenshot showing the distracting element helps us identify the correct CSS selector much faster.
4.  **Environment:** Which browser and AdGuard version are you using?

## 💡 Submitting New Rules (Pull Requests)

If you know how to write AdGuard/uBlock rules and want to contribute directly:

1.  **Fork** the repository.
2.  **Edit** the rules file (e.g., `filter.txt`).
3.  **Submit** a Pull Request.

### Rule Guidelines

To maintain the quality of this list, please adhere to the following guidelines:

*   **Scope:** The goal is to remove **recommendations, ads, and distractions**. Do not remove essential functional elements (like navigation bars, video players, or login inputs) unless they are strictly promotional.
*   **Syntax:**
    *   Use **AdGuard-compatible syntax** (Standard CSS, Extended CSS, or Scriptlets).
    *   Avoid generic rules (e.g., `##.banner`). Always limit rules to specific domains (e.g., `example.com##.banner`) to prevent false positives on other sites.
*   **Comments:** Please add a comment above your rule explaining what it does.
    ```adblock
    ! Correct
    ! Bilibili - Remove homepage recommended feed
    bilibili.com##.feed-card

    ! Incorrect (No explanation)
    bilibili.com##.feed-card
    ```
*   **Grouping:** Keep rules for the same website grouped together.

## ⚠️ Philosophy

This is a **Focus Filter**, not a privacy strip-miner.
*   ✅ **Do remove:** "Hot Search", "Guess you like", "Infinite feeds", "Red notification dots (fake ones)", "App download banners".
*   ❌ **Do not remove:** Comments sections (unless they are spammy), search bars, or core navigation, as these are often needed for normal usage.
