# Fun Facts

A quirky fact fetcher for TRMNL — polls [uselessfacts.jsph.pl](https://uselessfacts.jsph.pl) for random, absurd, and occasionally useful trivia. No API key needed. Refreshes every 60 minutes.

![Demo](docs/demo.gif)

## How it works

**Settings** (`src/settings.yml`): Configures the polling endpoint and refresh interval (60 min).

**Transform** (`src/transform.py`): A small serverless step that keyword-matches each fact's text against a handful of topics (animal, ocean, space, food, body, history, science, nature) and tags it with a `category`, falling back to `general` when nothing matches.

**Templates**: Four Liquid layouts (`full`, `half_horizontal`, `half_vertical`, `quadrant`) render the fact text next to a small icon that matches its `category` — a reusable `fact_icon` partial in `src/shared.liquid`, sized to stay out of the text's way so long facts still have room to wrap.

**Data flow**: `text` → `{{ text }}`, `category` (added by the transform) → `{{ category }}` in the templates.

## Local Development

**Lint and preview:**
```bash
./bin/trmnlp lint
./bin/trmnlp serve
```

Open `http://localhost:4567` to cycle through all four layouts. 

*Note: The `serve` command uses Docker under the hood. If running non-interactively (e.g. in CI), omit the `-it` flag from your docker invocation — the container will still start.*

## Deployment

CI lints every PR. On merge to `main`, the `push` job automatically deploys to your TRMNL account using the `TRMNL_API_KEY` repo secret (already configured).

A separate `preview` job captures and commits an updated demo GIF on every push to `main`. The GIF will always show the latest random fact.
