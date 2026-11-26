---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpRowArithmeticRelocation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpRowArithmeticRelocation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpRowArithmeticRelocation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Source-row arithmetic without overwriting the source caches

Native convolution uses stacks 128--204, while the source caches occupy
128--137. A fixed permutation moves those ten arithmetic slots to 214--223.
Relocation changes no operand widths or numerical parameters and introduces
only the final halt of the installed command.


### `relocated`

 Install a command at permuted physical stack ports. 
