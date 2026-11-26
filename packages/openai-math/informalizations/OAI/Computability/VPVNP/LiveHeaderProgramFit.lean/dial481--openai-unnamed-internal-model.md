---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderProgramFit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderProgramFit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderProgramFit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scratch geometry of the linked live-header program

The native stages use one contiguous scratch allocation after the packed
processor headers. Its end gives a single word-size bound for all occupied
cells. Distinct copied fields have disjoint destinations, so later scans
preserve earlier decoded fields and the fixed scratch prefix.


### `scalarFit_of_limit`

 All scalar fit requirements follow from the end of the scratch allocation. 

### `field_capacity_lt`

 Field capacities fit even when an empty buffer starts exactly at the
exclusive end of memory. 

### `cut_width_le_capacity`

 Bound the live cut width before selecting a field. 

### `dest_bounds`

 Payload buffers start after the descriptor words and the unpacked
index/advice fields and end before the next component's allocation. 

### `dest_disjoint`

 Distinct allocated destinations occupy disjoint half-open ranges. 

### `scan_public`

 The row of public scan operands gives the constant cursor zero and
the two allocated descriptor words. 

### `scan_sizes`

 The scan sizes require only the physical source extent and the allocation
bound. Its cursor starts at zero for every stage. 

### `scan_copyLayout`

 A full copy-stage layout at the exact public operands. For a zero-length
field the descriptor writes offset zero, including if the unused destination
address wraps at the exclusive end of memory. 

### `scan_fit_of_shape`

 All scan operands for a descriptor computed on an incident cut. 

### `preserve_copied_field`

 A later copy retains every bit of an earlier, distinct payload field. 

### `fieldCopy_prefix`

 Copying a payload preserves the packed sites, descriptor words and all
unpacked index and advice words before the payload area. 
