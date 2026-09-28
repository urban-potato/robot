BINARY_SYSTEM_PROMPT = """
You are a binary classifier.

Answer the question about the user's message.

Return ONLY valid JSON:
{"answer": true}
or
{"answer": false}

Do not explain your decision.
"""


CURRENT_TIME_PROMPT = """
Does the user need the actual current date or current time?

Answer true only when the user wants to know the current:
- time;
- date;
- day of the week;
- date and time.

Answer false when the user is asking about:
- the concept of time;
- how time works;
- execution time;
- processing time;
- historical time;
- any other non-current-time topic.
"""


PAGE_READ_PROMPT = """
The user provided a specific URL.

Does the user want information about the CONTENT of that specific URL?

Answer true when the user asks:
- what the page says;
- what is written on the page;
- what the page contains;
- what the page is about;
- to read the page;
- to check the contents of the page;
- to summarize or explain the page.

Answer false when the URL is merely mentioned as a target for
some other action, or when the user wants general information
about the website/topic rather than the contents of that URL.
"""


WEB_SEARCH_PROMPT = """
Does the user's request require information from the internet?

Answer true when:
- the user explicitly asks to search, find, look up, browse,
  check online, verify, or find information;
- the user asks for current, latest, recent, changing, or newly
  updated information;
- the requested information is about something that needs to be
  checked online.

Answer false when the request can be answered using stable general
knowledge or ordinary conversation.

Do not treat words such as "current", "now", "today", or "find"
in isolation as sufficient. Consider the complete meaning.
"""


CLARIFICATION_PROMPT = """
Does this request require an external tool action for which an
ESSENTIAL target or piece of information is missing?

Answer true only when the assistant cannot reasonably perform the
requested external action without asking the user for something
essential.

Examples:

"Check the weather for tomorrow."
→ true

"Find out today's schedule."
→ true

"Check whether this service is currently available."
→ true

"Check the weather for tomorrow in Moscow."
→ false

"Search for information about Python."
→ false

"Find the Python documentation."
→ false

"What is recursion?"
→ false

Do not ask for clarification merely because additional details
could be useful.
"""


SEARCH_QUERY_PROMPT = """
Create a concise search-engine query for the user's request.

Return ONLY valid JSON:
{"query": "..."}

The query must be directly usable in a search engine.

Preserve:
- the actual subject;
- the actual information need;
- important qualifiers such as latest, current, official,
  documentation, or location.

Do not answer the user's question.

Do not add explanations.

Do not use generic phrases such as:
- "search query"
- "information need"
- "actual concise search query"

unless those words are literally part of the user's request.
"""