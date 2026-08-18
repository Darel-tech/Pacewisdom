# Advanced Google Search Cheat Sheet for Backend Developers

A quick-reference for cutting through noise and finding precise technical answers fast.

---

## Core Operators

| Operator | Syntax | What It Does | Backend Example |
|---|---|---|---|
| **Site restrict** | `site:domain.com` | Limits results to one domain — great for pinning searches to official docs or a trusted Q&A site instead of SEO blogspam. | `site:stackoverflow.com "connection pool exhausted" postgres` |
| **File type** | `filetype:ext` | Restricts results to a specific file extension, useful for finding config examples, slide decks, or reference PDFs. | `filetype:yaml kubernetes readinessProbe example` |
| **Exact phrase** | `"exact phrase"` | Forces Google to match the words in that exact order — essential for error messages, since it stops Google from "helpfully" reinterpreting your query. | `"django.db.utils.OperationalError: FATAL: too many connections"` |
| **Exclude term** | `-word` | Removes results containing that word, handy for filtering out noise like ads, beginner content, or a language you don't want. | `redis eviction policy -tutorial -"getting started"` |
| **OR / logical or** | `term1 OR term2` | Returns results matching either term — useful when a bug could be described two different ways (e.g. two exception names for the same root cause). | `"ECONNRESET" OR "socket hang up" node.js https agent` |
| **Wildcard** | `*` | Acts as a placeholder for unknown word(s) inside a phrase — useful when you remember part of an error but not the exact wording or a variable value. | `"TypeError: Cannot read propert* of undefined" express middleware` |

**Bonus combos:**
- `site:` + `-` together restrict to a domain while cutting low-value pages, e.g. `site:github.com "panic: runtime error" -example -demo`
- Wrapping multiple `OR` terms in parentheses groups them: `(timeout OR "connection refused") site:docs.aws.amazon.com`

---

## Three Real Debugging Searches

**Scenario:** A Python service intermittently throws `psycopg2.OperationalError: connection to server was lost` under load.

### 1. Verbatim error, scoped to Stack Overflow
```
site:stackoverflow.com "psycopg2.OperationalError: connection to server was lost"
```
**Why it works:** The exact-phrase quotes stop Google from splitting the error into loosely related keywords, so you get pages where someone hit *this specific* error rather than generic psycopg2 chatter. Scoping to Stack Overflow surfaces threads with real fixes and accepted answers instead of scraped tutorial sites.

### 2. Official docs only, excluding beginner content
```
site:postgresql.org connection lost timeout server -tutorial
```
**Why it works:** Once you suspect the root cause (a server-side timeout dropping idle connections), pivoting to the official Postgres docs gets you authoritative config details (like `tcp_keepalives_idle` or `statement_timeout`) instead of a third party's possibly-outdated interpretation. `-tutorial` filters out "intro to Postgres" content that would bury the actual parameter reference.

### 3. Broaden with OR to catch differently-worded reports of the same bug
```
"connection to server was lost" OR "server closed the connection unexpectedly" psycopg2 pooling
```
**Why it works:** Different users and library versions phrase the same underlying connection-drop differently. Using `OR` between the two known variants doubles your chances of finding someone who diagnosed the same root cause (often connection pooling or keepalive misconfiguration) even if their exact error text differs slightly from yours.

---

### General Debugging Strategy
1. Start **narrow** — exact phrase of the error, no site restriction — to see how common the problem is.
2. Narrow further with `site:` once you know if you want official docs (root cause / config) or Stack Overflow (real-world fixes).
3. Use `-` and `OR` to cut noise and cover wording variants once you have a working hypothesis.
