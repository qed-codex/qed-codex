---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorAction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Successful live evaluator instructions

The preparing call chooses an instruction and publishes five words. A carried
accept uses one all-zero-motion instruction. The two scheduled tape scans
check the proposed target. Together these checks characterize exactly the
nonrejecting successors of the bounded evaluator.


### `carry`

 The five scratch fields written when carrying an accepting halt. 

### `pick`

 A selected native table slot. Canonical padding on a carried halt takes
choice zero and malformed choices have no successful slot. 

### `branchBits`

 The native call consumes a branch bit exactly on a two-slot running row. 

### `pick_bit_unique`

 Accepted slots with identical native bit strings have the same padded
witness bit. This also covers the zero-bit native accepting carry. 

### `first`

 The first tape's finite cell window extracted from an encoded evaluator configuration. 

### `second`

 The second tape's finite cell window extracted from an encoded evaluator configuration. 

### `tapeCheck`

 At an accepting target the comparison scans the zero tape fields. At a
continuing target it scans the shift, write and clipped endpoints. 

### `checks`

 The successful-transition test requiring a positive matching target state and the proposed
write and motion on both tape windows. 

### `pick_checks_iff`

 This equivalence preserves the specified choice bit, even for distinct
slots whose five published words coincide. 
