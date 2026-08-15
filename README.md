# Fun Facts

A quirky fact fetcher for TRMNL — polls [uselessfacts.jsph.pl](https://uselessfacts.jsph.pl) for random, absurd, and occasionally useful trivia. No API key needed. Refreshes every 60 minutes.

![Demo](docs/demo.gif)

## How it works

**Settings** (`src/settings.yml`): Configures the polling endpoint and refresh interval (60 min).

**Templates**: Four Liquid layouts (`full`, `half_horizontal`, `half_vertical`, `quadrant`) render the fact text next to a small illustrated dog, defined once as a reusable `dog_icon` partial in `src/shared.liquid` and rendered at a size suited to each layout. No transform step needed — the API response fields map straight to template variables.

**Data flow**: `text` → `{{ text }}` in the templates.

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
