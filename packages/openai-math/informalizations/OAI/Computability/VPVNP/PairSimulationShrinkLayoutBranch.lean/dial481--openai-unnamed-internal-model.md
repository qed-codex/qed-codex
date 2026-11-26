---
{
  "module": "OAI/Computability/VPVNP/PairSimulationShrinkLayoutBranch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkLayoutBranch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkLayoutBranch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selecting the resident shrinking layout

The old level's field at offset 38 holds the chosen layout bit. The
vertex reader doubles the five-bit literal 19 to obtain that offset,
reads the published field and enters the matching gather continuation.


### `code`

 Compute the layout field's address, read it, and branch on its word. 

### `Linked`

 Installation of the five instructions at their relocatable labels. 

### `events`

 Chronological events on the external memory supplied to the vertex call. 

### `native`

 The physical field selects its designated continuation. The scratch
register receives the read word. Every other register and both kinds of
caller state survive the branch. 
