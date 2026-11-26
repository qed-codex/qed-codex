---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackNativeFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackNativeFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackNativeFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Physical Schur frame fields with native extension-field scalars

The query and loop registers use ordinary binary words. Accumulators and left
operands keep the low-degree-first stream of base-field limbs consumed by
the extension-field arithmetic. The direction takes one bit and the unused
left operand occupies an empty field.


### `Data`

 The ten bit-string fields of a live Schur frame or its corresponding ten history stacks. 

### `Key`

 A Schur query for an order-`n` matrix with coefficient degrees bounded by `U` and `Z`. 

### `F`

 A suspended Schur continuation whose accumulator and operands belong to the scalar ring
specified by `c`. 

### `scalar`

 Encode a scalar as its low-degree-first list of base-field coefficients, each in a `v`-bit
limb. 

### `fields`

 Assemble the ten live fields from the direction tag, six query words, remaining count,
accumulator, and saved left factor. 

### `nativeFrame`

 Encode a suspended continuation, saving the left scalar in a frame waiting for its right
child. 

### `history`

 Encode a list of suspended frames into parallel history stacks, with the top frame's
delimited fields first. 

### `store`

 The complete physical bank. The auxiliary port values depend on the
installed arithmetic routines and the persistent matrix description. 
