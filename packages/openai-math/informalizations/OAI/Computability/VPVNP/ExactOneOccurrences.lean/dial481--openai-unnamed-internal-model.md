---
{
  "module": "OAI/Computability/VPVNP/ExactOneOccurrences.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExactOneOccurrences.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExactOneOccurrences.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Flattening exact-one literal occurrences for the graph reductions

The graph for Hamiltonian cycles and the graph for cycle covers have one indexed
occurrence per literal position. Each occurrence retains its variable, clause,
and polarity. Multiple occurrences of the same literal stay distinct.


### `occurrenceIndex`

 The graph may number occurrences by any bijection. 

### `occurrences`

 The variable, clause and satisfying bit of occurrence `j`. 

### `holds_iff_unique_occurrence`

 Exact-one satisfaction is equivalent to one true numbered occurrence in each clause. 

### `not_holds_of_nil_mem`

 Any family member containing an empty clause has zero satisfying assignments. 

### `length_le_literalCount_of_nil_notMem`

 Without empty clauses the graph's number of clause vertices is at most the literal count. 
