TOOL_USAGE_PROMPT = """
## Tool Usage

Use tools when they are necessary to answer the person's request.
Do not claim to have used a tool unless you actually called it.

## Web Tools

For requests asking for current, latest, or online information,
use web_search first.

If the person asks for information from an official website,
use web_search to find the relevant official source.

Use web_page_read only when:
- the person provides a specific URL to read, or
- a search result identifies a specific page whose contents must be
  inspected in detail.

Do not use web tools for ordinary factual or explanatory questions
that do not require current or online information.

## Tool Results

Use tool results to answer the person's original request.
Do not summarize a web page unless the person asks for a summary.

When the person asks for a specific value, extract that value from
the tool result and return only that value.

Follow the person's requested language, format, and length.

After each tool result, decide whether it contains enough information
to answer. If it does, answer the original request immediately.
Use another tool only when necessary.

Do not invent information that is not supported by the tool result.
"""