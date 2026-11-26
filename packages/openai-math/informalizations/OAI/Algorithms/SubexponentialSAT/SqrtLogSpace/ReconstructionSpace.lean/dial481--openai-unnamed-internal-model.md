---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/ReconstructionSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/ReconstructionSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/ReconstructionSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete CRT reconstruction and full-word modular readback. The same actual
native traces satisfy correctness, polynomial local time, and every-prefix
bounds on all source stacks, including the persistent caller frame. 

### `reconstruct_run_space`

 Correct Hasse jets give the actual residue output, with all-prefix local
workspace bounded by the fixed-degree polynomial native runtime. 

### `readback_budget_le`

 Modular reduction and extraction remain polynomial even when the residue
vector contains noncanonical representatives. 

### `readback_run_space`

 The actual reader produces a complete little-endian count word; its Boolean
head is not used as a satisfiability answer. The caller later normalizes this
word and computes positivity on the separate answer stack. 

### `normalizationPorts`

 The normalizer uses the count port and two empty low scratch ports.
Modulus and width remain in their existing high ports. 

### `canonicalReadback`

 A fixed reader followed by the actual unsigned normalizer. Zero has the
canonical one-bit output `[false]`, and positive counts retain all their bits. 

### `canonical_readback_run_space`

 Native reconstruction readback returns precisely the frozen binary word.
The same trace has polynomial local time and bounds every source stack at
every prefix, including modulus, width, and normalization scratch. 

### `canonicalReadbackCall`

 Only the eight explicitly assigned ports participate in the reader call.
The enclosing streaming machine may keep its tuple and signature frame on any
other ports, independently of the number of calls. 

### `canonicalQueryReadCommand`

 The existing query ABI is retained: reconstructed coefficients enter on
261, the canonical count leaves on 323, and 324 is the transfer scratch. 
