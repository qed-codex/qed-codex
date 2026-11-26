---
{
  "module": "OAI/Computability/VPVNP/LiveExponentRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveExponentRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveExponentRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The complete first-half exponent phase

After the chosen pair path has supplied all grammar and gadget increments,
the deterministic stage scans the labels in address order. It succeeds
exactly when the outgoing cut contains their sum with the incoming cut.
There is one terminal call and one constant-probe call per encoded bit.


### `clearCounters`

 Clearing the consumed increment words in address order. 

### `rowsReports`

 Exact report sequence of all data calls. 

### `run_rows`

 Exact native execution of all data calls, with any succeeding call sequence.
The first stage cursor is zero and the final one equals the total digit count. 

### `run_stage`

 All data calls followed by the unique accepting end call. 
