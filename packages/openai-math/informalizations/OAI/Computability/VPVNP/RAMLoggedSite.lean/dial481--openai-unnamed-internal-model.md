---
{
  "module": "OAI/Computability/VPVNP/RAMLoggedSite.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMLoggedSite.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMLoggedSite.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Single-pass site loop with concrete private word work

A site starts every charged call with a fresh write log, records the call's
work in the same recursion that obtains its report, and uses its probe count
to advance the cut. The final loop check costs sixteen operations even when
no call can start.


### `Machine.loggedChargedCall`

 Charge startup against each remaining allowance before dispatching.
Every attempted call returns both the metered run and its word work. 

### `Machine.runLoggedSite`

 A single run returns the reports, unused suffix and total primitive work.
The sixteen control operations cover the cut tests, budget arithmetic and
collection of the returned reports. 

### `Machine.runLoggedSite_output`

 The logged interpreter follows exactly the reports and binary choices
used in the validator's path-counting theorem. 
