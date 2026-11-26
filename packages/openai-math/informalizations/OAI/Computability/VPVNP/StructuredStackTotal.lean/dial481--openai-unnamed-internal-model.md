---
{
  "module": "OAI/Computability/VPVNP/StructuredStackTotal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StructuredStackTotal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StructuredStackTotal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounding all branches of a structured stack program

The continuation receives the remaining fuel on each normal return. A direct
halt always finishes, including a rejecting halt. A binary choice satisfies
the bound exactly when both alternatives satisfy it.


### `AllStopsFrom`

 Every branch from the given local control halts or returns within the available fuel, with
each normal return satisfying the continuation at its remaining fuel and final stack bank. 

### `AllStops`

 The all-branches termination condition for a routine started at its entry label, with the
continuation checked on each normal return. 

### `Runs.allStops_iff`

 A deterministic successful run spends exactly its stated cost and hands every
remaining clock tick to the continuation. 
