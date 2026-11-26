---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighIncidenceStream.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighIncidenceStream.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighIncidenceStream.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact disjoint conditioning and bounded-width accumulation on original variables.
The finite sums below specify the stream; they are not materialized by its program.
The source is the sparse-query proof in counting-k-sat.tex, lines 1636–1698. 

### `branchCount`

 Count over the complement, including every unused declared coordinate. 

### `length_carryAdd_of_lt`

 A binary carry does not enlarge a bounded word unless the numerical result overflows.
This also permits leading zeroes, so the existing actual adder needs no normalization. 
