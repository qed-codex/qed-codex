---
{
  "module": "OAI/Computability/VPVNP/RAMSiteBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSiteBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSiteBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Processor strings and counters at large lengths

The logarithmic address and quartic word width can be fixed before selecting
a successful circuit length. The shared messages fit in the processor input
under the live bucket's strictly sublinear growth. The same word width holds
every counter bounded by a fixed polynomial in the input length.


### `eventually_polynomial_lt_wordModulus`

 Any fixed power eventually fits a word, uniformly in all address
widths at least `log₂ n`. 

### `eventually_polylog_le_rpow`

 Any fixed log-polynomial factor fits inside an arbitrarily small
positive power. This handles the overhead from words, stages and field tags. 

### `site_length_bound`

 A whole site uses only a fixed log-polynomial overhead per bucket
entry. Here `L` is the program-prefix length. 

### `eventually_processorInputFits`

 Section 10's live processor layout fits all its fields in `n` input
bits, for any fixed `δ > 0`, prefix, and logarithmic address multiplier. 
