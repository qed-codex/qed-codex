---
{
  "module": "OAI/Computability/VPVNP/MotifPowerExpansion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifPowerExpansion.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifPowerExpansion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The repeated motif identity as an ordinary sum over total widths

After copying a fixed base identity, choices of its summands form selector
lists. The supply edge payloads are grouped by their total width vector.
The selector and validity checks in the local maps count each admissible
list exactly once, as required by Theorem 6.1.


### `baseTerm`

 The contribution of one selected base map after contracting its supply wires. 

### `groupedMap_contraction`

 Each compressed term counts precisely the lists with its total width vector. 

### `power_expansion`

 The repeated ordinary sum, grouped by admitted total payload widths.
Every successful selector list has exactly one outer index. 
