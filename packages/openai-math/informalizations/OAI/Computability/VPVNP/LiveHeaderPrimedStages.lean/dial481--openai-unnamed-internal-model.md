---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderPrimedStages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPrimedStages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPrimedStages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native primed index stages in the live header program

The setup stage initializes the borrow and both low bits. The following
bounded stage reads one unpacked group digit per call and writes the shifted
digits of the two primed indices. The all-zero low digits of the last group
are included in the same execution, with the borrow still set at the end.


### `operands`

 The four addresses of the original group digits, the two primed digit arrays, and the
shared borrow cell. 

### `layout_of_fit`

 The three operands addressed by a digit are disjoint, fit in word memory,
and all input digits are outside the two output buffers and borrow cell. 

### `init_run`

 The accepting setup call has exactly three writes and initializes the
three scalar cells before the enclosing linker advances the stage tag. 

### `Ready`

 Values supplied by the primed initialization stage. 

### `active_digits`

 Prefix of the bounded source stage, including each active call's choices
and probes and preservation of the linker's tag at every returned cursor. 

### `Output`

 Readback at the actual scheduled addresses. Every entry is one RAM word
containing one low-endian digit. The borrow distinguishes the last group.
All scratch words outside those three output regions retain their values. 

### `digits_run`

 The complete bounded stage on an arbitrary physical group, including
the last all-zero scanned index. It accepts after precisely one closing
call, having used exactly five probes and zero choice bits per active digit. 

### `handoff_ready`

 The initialization-to-digit handoff preserves the copied input and
the three freshly initialized words. 

### `Output.values`

 For every group whose doubled index fits, the arrays decode to the
two primed indices. This includes the whole first half, where they are used. 

### `Output.last_group`

 In the last group the mathematical even primed index is the next power
of two. Its low buffer is zero, its predecessor buffer is all ones, and
the scalar retains the final borrow. 

### `Output.auxiliary_group_bits`

 The first-half buffers are precisely the two group fields queried in
the auxiliary input. Address arithmetic is the RAM's modular addition;
the scratch layout ensures that these additions do not wrap. 

### `primed_prefix`

 Execute and link the two primed stages in their actual positions. The
frame in the returned output includes the final handoff at the reserved
stage tag. Every preceding width, flag, physical header and input digit
outside the writable regions retains its value. 
