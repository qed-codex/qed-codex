---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapScanAcceptance.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapScanAcceptance.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapScanAcceptance.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Acceptance of a finite row of deterministic resident maps

Even though each successful map changes the scratch passed to the next,
the scan's success bit depends only on the acceptance predicate of each
occurrence when that predicate holds for all starting scratch values.


### `scan_ofFn_iff`

 Once each occurrence's success bit is determined by its typed input,
the whole scratch-dependent loop succeeds exactly when every occurrence does. 

### `scan_ofFn_add`

 On a successful scan, any coordinate updated additively by each
occurrence receives the sum of the actual updates in row order. 
