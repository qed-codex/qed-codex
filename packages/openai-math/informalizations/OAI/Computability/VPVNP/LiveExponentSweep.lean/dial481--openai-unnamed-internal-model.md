---
{
  "module": "OAI/Computability/VPVNP/LiveExponentSweep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveExponentSweep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveExponentSweep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing a row of the first-half exponent check

Each digit runs in a fresh private workspace. The only shared cell changed
by an entire row is that label's increment word. Its final value on success
is zero. The input and output bit buffers may be read at any disjoint
addresses computed by the stage.


### `atPos`

 Convert a natural exponent-sweep cursor to its persistent machine word. 

### `RowCells`

 The read-only and writable cells used by a nonempty suffix of one row.
The final digit test is taken exactly at the end of the row. 

### `rowReports`

 Expected digit reports, even if a check would stop the actual run.
They determine the only possible complete transcript. 

### `run_row`

 Execute the digit calls of one row with any continuation. An incorrect
output bit, overflow, or any extra binary choice rejects the call sequence. 
