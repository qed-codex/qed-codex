---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkABSliceGroup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceGroup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceGroup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Complete AB packet group of the selected shrinking branch

The first scratch table holds the physical sorted widths and their starts.
The second table holds every AB interval record. The allocated block's end
bound suffices for both. The group uses the real shrinking numberings and
retains its exact external frame and resource bounds at its packet endpoint.


### `build_packets_trace`

 The source data come from the chosen geometry's current memory. Table
sizes, bundle indices and worker clocks are those of the compiled script. 

### `build_packets`

 Build the group, endpoint descriptors, external frame and costs of the
physical AB calendar on the admitted state. 

### `build_packets_of_run`

 Attach the AB report list already present in an ordered shrinking
construction. Its source clock and saved planner header may differ from
the online clock and header; their eight physical operands coincide. 
