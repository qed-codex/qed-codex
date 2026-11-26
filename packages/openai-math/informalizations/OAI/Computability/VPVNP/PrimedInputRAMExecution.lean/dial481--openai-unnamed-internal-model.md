---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Complete native execution of the cursor-controlled input program

Every accepting native path performs the entire public schedule followed by one
halt call. Its only private branch bits are those at the scheduled choice positions.
Conversely, every such assignment determines all reads, writes and reports uniquely.
The prefix theorem allows replacing the terminal call with the grammar parser.


### `scheduledMemory`

 Final memory obtained by executing the indicated cursor items. 

### `Aligned`

 The remaining cells form the consecutive suffix beginning at cursor k and ending at the
exclusive schedule bound. 

### `splice_scheduledPrefix`

 Stitch this input stage to any following program with the same data calls. At cursor
`M` its continuation can start the grammar parser; the prefix fixes its memory and leaves
its private choice streams untouched. 

### `scheduled_prefix`

 Execute the data calls and supply an arbitrary continuation from the terminal cursor. 

### `run_generated`

 Every scheduled assignment yields its complete native report list. 

### `run_accepted_iff`

 The native accepting paths consist of the scheduled owner choices, with empty
private streams for the remaining calls and the terminal halt. 
