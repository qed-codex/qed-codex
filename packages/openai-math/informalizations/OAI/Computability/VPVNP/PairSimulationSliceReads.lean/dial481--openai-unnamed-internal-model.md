---
{
  "module": "OAI/Computability/VPVNP/PairSimulationSliceReads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationSliceReads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationSliceReads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External cells read by operand setup and private slice transfers

The native setup reads only the cells reached by its evaluated load expressions.
The slice header always reads its length and reads its offsets only for a nonempty
intersection. The private bit loop adds no external reads.


### `execute_setup_trace_reads`

 The actual continuation trace of a linked setup reads only the cells visited by
its evaluated load expressions, including nested loads that compute later addresses. 

### `PrivateFields.events_reads`

 Guesses and copies within the private bit loop read no external cell. 

### `PrivateSlices.frameEvents_reads_iff`

 The physical frame reads its length on every branch. Its offsets are needed
only if that length is nonzero, even when the external cells contain stale values. 
