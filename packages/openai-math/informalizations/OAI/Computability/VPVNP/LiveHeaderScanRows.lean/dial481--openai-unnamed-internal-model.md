---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderScanRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderScanRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderScanRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Field scans at the live header's scheduled addresses

The descriptor's two words supply the occupied interval. The scheduled row
supplies the destination and capacity. The processor sites precede scratch,
so an active copy preserves the remaining source bits and descriptor words.


### `operands`

 The first sixteen words of the scan row, before its wrapper appends the capacity. 

### `execute_scan`

 A scheduled scan call executes the bounded field table with its exact public row. 

### `copy_run`

 The complete native scan copies exactly the occupied field to its scheduled
destination. Every successful report preserves the linker's tag on replay. 

### `padding_run`

 A zero padding interval accepts after its scheduled calls and leaves
every scratch cell and every packed processor word intact. 

### `padding_sound`

 Arbitrary choice strings and an arbitrary source fuel cannot skip a
nonzero occupied padding bit on an accepting row execution. 

### `short_call`

 A complete call must execute the three guard instructions and a terminal instruction. 

### `padding_sound_any`

 Soundness for every total fuel, including attempts to stop during the guard. 

### `padding_call_frame`

 On every successful call of the scheduled padding row, its event log leaves
every replay address intact. This includes returning calls before an eventual
failure and the closing call. No descriptor validity is required. 
