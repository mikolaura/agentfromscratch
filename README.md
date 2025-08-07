# 👩‍🏫 Academic Helper

A simple agentic AI-powered academic assistant built with LangGraph and Streamlit.

> ⚠️ **Note:** This is a personal pet project. Feel free to reuse or build upon it, but do **not fully trust** the answers provided by the agent without verification.

---

## 🚀 Requirements

- [uv](https://github.com/astral-sh/uv)
- Python 3.10+

Install the required dependencies:

```bash
uv sync
```

---

## 🧪 How to Run

You can run the project in two different modes:

### 1. Using LangGraph Studio

To start the development environment with LangGraph Studio:

```bash
uvx --from "langgraph-cli[inmem]" --with-editable . langgraph dev
```

### 2. Using Streamlit

To run the app in your browser using Streamlit:

```bash
uv run streamlit run app.py
```

---

## 📌 Disclaimer

This project is experimental and not intended for production use. Always double-check the responses before relying on them in any academic setting.

---

## 📜 License

This project is released under the MIT License.