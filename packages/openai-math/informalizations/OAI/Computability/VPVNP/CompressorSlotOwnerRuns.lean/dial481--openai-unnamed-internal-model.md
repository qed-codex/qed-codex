---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotOwnerRuns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOwnerRuns.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOwnerRuns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The two native endpoint-owner scans

The genuine scan reads the role, the chosen site, the CD indicator, and the
subdivision count. The padding scan reads the cyclic successor of a site.
Disjointness of those inputs from the output interval suffices to compute
both scans from the original descriptor memory.


### `genuineInputs`

 The four external addresses consulted by the genuine worker. The second
read depends on the role word returned by the first. 

### `FilledRun`

 A complete worker scan starts at cursor zero and fills its output cells
in address order. The frame covers arbitrary external addresses. 

### `filled_run`

 Start a sequential output worker at zero and package its interval and frame. 

### `genuine_run`

 Read four input words and write one genuine-field owner at each cursor. 

### `dummy_run`

 Read one cyclic successor and write one dummy-field owner at each cursor. 

### `owner_runs`

 Execute the genuine and dummy workers in sequence, resetting the cursor
between phases. The final table gives each endpoint the owner computed from
the original descriptor memory. The two calls-plus-probes costs add exactly. 

### `genuine_inputs_ranges`

 The four read addresses stay in the original-arc records, the eight role
entries, and the four subdivision counts, respectively. 

### `genuine_inputs_before`

 Placing the three input arrays below the output suffices for every genuine
read. The role words are offsets in the three-site part of each four-word record. 

### `dummy_input_range`

 Both endpoints of a dummy arc probe its original site in the cyclic successor array. 

### `dummy_input_before`

 A cyclic-successor array of one word per site suffices for both sides of
each dummy arc, including all copies of a padding slot. 

### `template_opcode_work`

 Straight-line templates use registers and external memory, so an
instruction never scans the private write log. This holds at every program
counter, for every allowance and stream of read bits. 

### `genuine_opcode_work`

 A genuine-owner call dispatches at most 49 instructions. 

### `dummy_opcode_work`

 A dummy-owner call dispatches at most 20 instructions. 
