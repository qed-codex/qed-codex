---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorCallCredit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorCallCredit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorCallCredit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Starting a metered call

Before any instruction dispatch, restore the two unary credits from their
public tallies, save the current cost as the call start, reset the probe
ordinal to zero, and take the mandatory startup charge. A call can therefore
start with one remaining unit and complete without a probe.


### `startCall`

 Startup first prepares the per-call state, then charges its unit. 

### `resetTicks`

 Stack-step count for restoring call and instruction credits, saving the start cost and
resetting the probe ordinal, accounting for the lengths of their previous contents. 

### `followRight`

 In a sequenced routine a rejecting state of the second stage remains a
rejecting state, with no transition past the failure. 

### `firstCall`

 Initialize the binary allowance from the supplied cap and incoming cost
before starting the site's first live call. 

### `remaining_after_charge`

 After a permitted charge, the two binary counters continue to sum to
the cap, and the incremented cost fits the same word. 

### `ordinal_fits`

 A probe ordinal counts only the probes since startup. Its next value
therefore fits even if the probe takes the global cost exactly to the cap. 
