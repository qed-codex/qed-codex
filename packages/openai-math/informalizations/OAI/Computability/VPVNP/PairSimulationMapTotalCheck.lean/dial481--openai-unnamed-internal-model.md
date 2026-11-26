---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapTotalCheck.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapTotalCheck.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapTotalCheck.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Checking the entire supply width vector in private RAM

The fixed motif has one running total and one descriptor width for each
supply edge, including edges at other parties. A fixed sequence of guards
compares their resident word registers and branches to rejection on the
first discrepancy.


### `checkCode`

 The constant final guard is also the empty-edge exit. 

### `checkSteps`

 Number of comparisons executed up to the first mismatch or the final guard. 

### `checkCode_native`

 The fixed guards consume no guesses, perform no probes and preserve
all registers, private memory and the persistent word on both exits. 

### `totalCheck_native`

 Compare the full totals produced by an actual inner selector list with the
descriptor widths, even for a malformed descriptor. All tested natural values
must fit the word; all other cells and registers can be arbitrary. 
