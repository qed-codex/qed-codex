---
{
  "module": "OAI/Computability/VPVNP/PairShrinkCDReadBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCDReadBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCDReadBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Addresses read by the CD rank scan

The native expression tests every old arc in the second classified row for
the selected bundle. Each candidate read stays in the ID rectangle, each
rank read stays in the old-arc rank column, and the thickness test stays in
the old-site column. Both possible child addresses use the original
incidence columns and the full fixed-degree width prefix.


### `noncomputable local instance : DecidableEq X.Base`

 Classical equality on the input base vertices for tracing the CD row and incidence reads. 

### `ScanInputs`

 Readable source expressions for the row classifier and rank scan. 

### `scan`

 Confinement of all candidate and rank probes, including the candidates
whose ranks fail the test. 
