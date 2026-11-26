---
{
  "module": "OAI/Computability/VPVNP/CompressorNativePassRates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorNativePassRates.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorNativePassRates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Communication rates of the installed pass program

All source calls and probes are charged at their actual multiplicity. The
online controller charges a fixed amount per source call and a fixed recipe
overhead per source packet. The latter is bounded by the number of visits
in the single hardwired block. Neither charge uses the private burst clock.


### `nativePassRate`

 Charge per position when the raw source workers use at most `raw`
units per position in the pass. 

### `commonRawRate`

 Uniform source-rate bound taking the maximum over all shrink indices and the refresh rate. 

### `rawPassRate`

 Source rate for a particular scheduled pass, selected from the indexed shrink rates or the
single refresh rate. 

### `passCharges_le`

 The full source cost for a shrinking substep or a refresh yields the
same uniform bound for the three physical parts used in the pass runner.
The absolute ordinal equation gives the number of actual worker visits. 

### `timeline_rate`

 Total of the uniform per-pass bounds in the actual chronological tree,
followed by the calendar's terminal cost of four. 
