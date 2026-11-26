---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterChronology.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterChronology.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterChronology.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact coefficient count of chronological pair-counter tapes

The cursor visits the two input rectangles, then the sites in row-major order,
and finally all nominated histogram entries. A raw path has one list of branch
bits at every absolute cursor position. Recovering the shared choices at the
first-pass owners and the parse choices in the node slots is parsimonious.


### `Bits`

 An assignment to all internal primed bits shared by the two groups, including bits read at
several endpoints. 

### `PairTape`

 One private choice list per cursor slot across the two input passes, all site parses and
the final nomination comparisons. 

### `inputCalls`

 One singleton at each designated first-pass owner and an empty list at
every other first-pass position and every copy position. 

### `rowInput`

 Primed processor inputs, reindexed in the order of the parse loop. 

### `Accepts`

 Branch-tape condition tested by the input, site and comparison phases. 

### `pathEquiv`

 Extract the shared assignment and all local parses from a complete tape.
The inverse places each choice back at its absolute chronological position. 

### `count`

 The raw path count is the integer coefficient on the actual primed
inputs of both groups, including all internal bit assignments. 
