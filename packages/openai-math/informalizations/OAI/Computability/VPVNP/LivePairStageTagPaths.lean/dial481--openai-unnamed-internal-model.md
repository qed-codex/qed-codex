---
{
  "module": "OAI/Computability/VPVNP/LivePairStageTagPaths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePairStageTagPaths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePairStageTagPaths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Full path semantics of the pair tag-address calculation

Computing the stage address on each fresh call uses only private ticks.
Removing these ticks is an equivalence of the capped native branch streams,
with exactly the same memory, continuing word and branch choices.


### `prefixReport`

 Prepend the five private ticks spent computing the pair tag address to a source call
report. 

### `pathEquiv`

 The branch strings are identical on both sides, and the predicate sees
the actually executed sequence of reports. 
