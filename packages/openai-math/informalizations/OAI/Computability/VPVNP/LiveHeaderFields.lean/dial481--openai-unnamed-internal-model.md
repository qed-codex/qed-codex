---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Copying payload and validating zero padding in a live cut

An incoming or outgoing cut bit resides in the packed header of the processor
at its cut offset. The offset of a payload field can depend on the distributed
group index. A descriptor word supplies that offset. The destination array is
fixed across groups, including for the two exponent buffers and tail configurations.
Each call checks or copies one bit and advances its persistent cursor.


### `locateCell`

 Public slots are the phase's first cursor, the address of the source
offset descriptor, and the fixed base of the destination array. Register 4
holds the absolute cursor, register 5 the position within this field. 

### `copyFieldCell`

 Copy one bit to the same offset in the designated unpacked field. 

### `checkPaddingCell`

 Reject a nonzero padding bit. This same guard checks all nonmode bits
of an incident cut in unit mode. 

### `sourceSite`

 The packed-header source address found by adding the current field-relative cursor to the
offset read from the descriptor. 

### `checkPaddingCell_native_iff`

 For the real packed header at the computed site, the padding microcall
has a successful native return exactly when the designated field bit is zero. 
