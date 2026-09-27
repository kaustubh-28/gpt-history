# gpthistory

A command-line tool to index and semantically search through your exported ChatGPT conversation history.

ChatGPT's sidebar makes it frustrating to locate older discussions, code snippets, or ideas. `gpthistory` parses your exported ChatGPT data dump, generates embeddings for each conversation using OpenAI's API, and saves them locally. You can then search your entire chat history semantically from the terminal and jump directly back to the original conversation via provided links.

---

## Features

- **Semantic Search**: Uses OpenAI embeddings (`text-embedding-ada-002`) to find conversations by context and meaning rather than strict keyword matching.
- **Incremental Indexing**: Skips already indexed conversations when you import newer data exports, saving time and API costs.
- **Direct Links**: Prints direct ChatGPT URLs (`https://chat.openai.com/c/<id>`) for matching conversations so you can reopen them in your browser.
- **Local Storage**: Keeps your index stored locally at `~/.gpthistory/chatindex.csv`.

---

## Installation

Clone the repository and install it in editable mode:

```bash
git clone git@github.com:kaustubh-28/gpt-history.git
cd gpt-history
pip install -e .
```

---

## Setup & Usage

### 1. Export your ChatGPT data

1. In ChatGPT, open **Settings** (bottom-left profile menu).
2. Go to **Data Controls** → **Export Data**.
3. Confirm the export and wait for the download link via email.
4. Download and unzip the archive to find `conversations.json`.

### 2. Configure your OpenAI API key

Set your OpenAI API key in your shell:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Or add it to a `.env` file in your working directory.

### 3. Build the index

Run `build_index` pointing to your `conversations.json` file:

```bash
gpthistory build_index --file /path/to/conversations.json
```

This extracts the text from each chat, generates embeddings in batches of 100, and writes the index to `~/.gpthistory/chatindex.csv`. Running this again with a newer export file will only embed new conversations.

### 4. Search

Run `search` followed by your query:

```bash
gpthistory search "python asyncio queue"
```

Example output:

```text
2026-09-28 01:00:00 - INFO - Searching for keyword: python asyncio queue
2026-09-28 01:00:01 - INFO - a1b2c3d4-e5f6-7890-abcd-ef1234567890: Building an async worker pool in Python with asyncio.Queue
2026-09-28 01:00:01 - INFO - ChatGPT Conversation link: https://chat.openai.com/c/a1b2c3d4-e5f6-7890-abcd-ef1234567890
--------------------------------------
```

---

## How It Works

1. **Extraction**: Iterates through the message mapping in `conversations.json` to pull out raw text content.
2. **Embeddings**: Passes batches of conversation texts to OpenAI's `text-embedding-ada-002` model.
3. **Index Cache**: Stores chat IDs, section IDs, text snippets, and embeddings into a pipe-delimited CSV (`~/.gpthistory/chatindex.csv`).
4. **Similarity Search**: When searching, generates an embedding for your query, computes the dot product across the stored vectors with NumPy, and prints matches meeting the similarity threshold (>= 0.8) ranked by relevance.

---

## Author

- **Kaustubh Srivastava** — [GitHub](https://github.com/kaustubh-28) · [Email](mailto:kaustubh282.s@gmail.com)

---

## License

This project is licensed under the [MIT License](LICENSE.md).
