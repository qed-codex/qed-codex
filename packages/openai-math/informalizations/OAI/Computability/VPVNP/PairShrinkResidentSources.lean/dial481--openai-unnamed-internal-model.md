---
{
  "module": "OAI/Computability/VPVNP/PairShrinkResidentSources.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkResidentSources.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkResidentSources.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Source records of a selected shrinking level

The input incidence, old-port lists, sorted ranks, dense demand pairs, term
words, resident directories, slice banks and ordered-slot rectangles occupy
the producing level. The copied successor incidence occupies its own
canonical bank. All components here describe one selected branch at one
chronological level and one memory snapshot.


### `Data`

 Typed data consumed by resident-party handlers after the native
shrinking pass and its successor-incidence copy. 

### `Data.transfer`

 Transfer all typed inputs to the memory of a later parser call. Only
the producing level and the successor's pointer and incidence bank are
used, so writes to its scalar header and workspace are allowed. 
