---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/AttainedSignatures.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/AttainedSignatures.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/AttainedSignatures.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# First occurrences of attained keys

The subtype below is a specification of emissions, not a stored family.
The executable scan checks a candidate against its predecessors one at a time.
The key may be an entire integer row-signature; no coordinate projection occurs.


### `assignmentEquiv`

 Increasing numeric order of little-endian words, equivalently lexicographic
order after reversing the words. The empty head has its unique empty word. 

### `integerKey`

 All stored constraint rows occur in this key, with integer arithmetic. 

### `duplicateScan`

 The mutable duplicate latch has this proof-level recurrence. The actual
program implements it with a bounded word and one Boolean register. 

### `rescan_comparisons_le`

 Both candidate and predecessor scans are charged even when a key loses.
This is a bound on scan counts, not an implementation cost theorem. 
