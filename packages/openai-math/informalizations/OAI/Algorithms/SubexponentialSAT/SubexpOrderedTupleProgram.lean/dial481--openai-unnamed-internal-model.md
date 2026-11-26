---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpOrderedTupleProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpOrderedTupleProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpOrderedTupleProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-depth ordered tuple generation

The programs at depths two and four have fixed finite instruction tables.
Each Cartesian expansion is followed by the actual record reversal routine,
so the output order agrees exactly with QuarticSearch.vectors.


### `selected_runsIn`

 Exact source-vector order, rather than only a permutation of candidates. 
