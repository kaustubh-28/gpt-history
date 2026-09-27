# GPT History 🔍

> **Semantic search for your personal ChatGPT conversations — right from your terminal.**

Ever found yourself scrolling endlessly through the ChatGPT sidebar trying to dig up that one conversation from four months ago? Maybe you wrote a clever regex, designed an API schema, or brainstormed a project outline, but finding it again in OpenAI's interface feels like searching for a needle in a haystack.

**`gpthistory`** solves this. It takes your exported ChatGPT data, embeds your chats locally with OpenAI vector embeddings, and gives you instant, semantic search from your command line. Best of all, every search result includes a direct, one-click link back to the exact conversation on ChatGPT.

---

## ✨ Features

- **🧠 Semantic Search**: Don't worry about remembering the exact keywords you used. Ask for "docker postgres setup" or "how we handled stripe webhooks", and embeddings (`text-embedding-ada-002`) will find the right conversation based on context and meaning.
- **⚡ Direct Web Links**: Jump directly to `https://chat.openai.com/c/<conversation-id>` straight from your terminal output.
- **💰 Smart Incremental Indexing**: Saves your OpenAI API credits. When you re-export your history in the future, `gpthistory` detects conversations you've already indexed and only generates embeddings for new ones.
- **🔒 Local & Private**: Your index file is stored locally on your machine at `~/.gpthistory/chatindex.csv`.

---

## 🚀 Quickstart

### 1. Installation

Clone the repository and install it in editable mode:

```bash
git clone git@github.com:kaustubh-28/gpt-history.git
cd gpt-history
pip install -e .
```

### 2. Export Your ChatGPT Data

Because OpenAI doesn't provide an open public API to fetch your personal chat history directly, export it from their web interface:

1. Go to [chatgpt.com](https://chatgpt.com) and click your profile icon (bottom-left) → **Settings**.
2. Navigate to **Data Controls** → **Export Data**.
3. Confirm the export. OpenAI will email you a download link within a few minutes.
4. Download and unzip the archive. You'll see a file called `conversations.json`.

### 3. Set Your OpenAI API Key

`gpthistory` uses OpenAI embeddings to index and search your chats. Set your API key in your shell:

```bash
export OPENAI_API_KEY="sk-..."
```

*(You can also place it in a `.env` file in your working directory).*

### 4. Build Your Index

Run the `build_index` command pointing to your extracted `conversations.json`:

```bash
gpthistory build_index --file /path/to/conversations.json
```

What happens here:
- Parses every message turn and content block.
- Generates embeddings in batches of 100 to maximize throughput.
- Writes the index and vectors to `~/.gpthistory/chatindex.csv`.
- Subsequent runs will automatically skip conversations already in your index!

### 5. Search Your Conversations

Run the `search` command with your query:

```bash
gpthistory search "python asyncio task queue"
```

Sample output:
```text
2026-09-28 01:00:00 - INFO - Searching for keyword: python asyncio task queue
2026-09-28 01:00:01 - INFO - a1b2c3d4-e5f6-7890-abcd-ef1234567890: Building an async worker pool in Python with asyncio.Queue
2026-09-28 01:00:01 - INFO - ChatGPT Conversation link: https://chat.openai.com/c/a1b2c3d4-e5f6-7890-abcd-ef1234567890
--------------------------------------
```

---

## 🛠️ CLI Reference

| Command | Usage | Description |
|---|---|---|
| `build_index` | `gpthistory build_index --file <path>` | Extracts chats, generates embeddings, and saves/updates local index. |
| `search` | `gpthistory search "<query>"` | Computes query vector, calculates dot products, and prints top matching chats. |

---

## 🏗️ How It Works Under the Hood

1. **Extraction**: Reads `conversations.json` mapping tree and pulls textual message parts.
2. **Embedding**: Uses OpenAI's `text-embedding-ada-002` to turn conversation texts into dense vector representations.
3. **Storage**: Keeps embeddings in a pipe-delimited CSV (`~/.gpthistory/chatindex.csv`) for fast local reading without requiring a heavy vector database setup.
4. **Scoring**: When you search, your query is embedded on-the-fly, dot-product similarity is computed against all stored embeddings via NumPy, and top matches above the similarity threshold (>= 0.8) are returned in descending order.

---

## 👤 Author & Maintainer

**Kaustubh Srivastava**
- GitHub: [@kaustubh-28](https://github.com/kaustubh-28)
- Email: [kaustubh282.s@gmail.com](mailto:kaustubh282.s@gmail.com)

*Originally created by [Shrikar Archak](https://github.com/sarchak/gpthistory).*

---

## 📄 License

This project is licensed under the [MIT License](LICENSE.md).
