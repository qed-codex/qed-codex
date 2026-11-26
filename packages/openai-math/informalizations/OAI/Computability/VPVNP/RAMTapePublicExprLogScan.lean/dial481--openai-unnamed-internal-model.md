---
{
  "module": "OAI/Computability/VPVNP/RAMTapePublicExprLogScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicExprLogScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicExprLogScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Finite scan for the highest set bit of a word

The scan reverses the input to inspect its most significant bit first. It emits a
unary mark for each position below the first one. For a ceiling logarithm it adds
a final mark exactly when some lower bit was set. Every consumed bit also allocates
a zero in the eventual result register.


### `Phase`

 States for reversing the input word, locating its highest set bit, counting lower
positions, and optionally rounding up. 

### `scan`

 Scan from the highest bit, emit logarithm marks, and allocate zero bits for the result. In
ceiling mode add a mark when a lower bit is set. 

### `scan_runs`

 The first scan produces the mathematical logarithm in unary and allocates
exactly the original number of zero result cells. 
