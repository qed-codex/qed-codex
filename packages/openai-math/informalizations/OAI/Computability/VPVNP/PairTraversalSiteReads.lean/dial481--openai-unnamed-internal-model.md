---
{
  "module": "OAI/Computability/VPVNP/PairTraversalSiteReads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalSiteReads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalSiteReads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External read addresses of a placement-fiber worker

The setup probes the count cell once. Every iteration reads its current
source identifier, then advances the source cursor by one. The translated
addresses and the two new header cells are written without being read.


### `scan_reads`

 In every successful loop derivation the sole read of an iteration is
at its current source address. 

### `native_reads`

 A successful native worker reads only its own count cell and its occupied
source row. The result applies to the report returned by the machine. 
