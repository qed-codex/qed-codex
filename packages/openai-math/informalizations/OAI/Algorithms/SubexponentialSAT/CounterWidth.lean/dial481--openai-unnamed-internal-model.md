---
{
  "module": "OAI/Algorithms/SubexponentialSAT/CounterWidth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/CounterWidth.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/CounterWidth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Width preservation below a binary overflow boundary

The input word may contain high zero bits. This lemma applies to actual ripple
increment results and does not assume a canonical binary representation.


### `increment_length_le_of_lt`

 Increment stays within an n-bit word when its new value is below 2^n. 
