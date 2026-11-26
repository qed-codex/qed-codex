---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorInitialize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorInitialize.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorInitialize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Initial and final words of an evaluator group

At the midpoint the input tape starts at its leftmost input bit, and the
second tape is blank. In the head-relative field the first input bit goes
at cell `M`. A fixed native RAM call reads one packed input bit and stores
its tape symbol. Cells outside the raw input retain their initial zeroes.
The last group's required accepting configuration has state one and zero
in every tape field.


### `bitSymbol`

 A raw bit is nonblank, including a zero input bit. 

### `inputCell`

 At cell `i` the head-relative input offset is `i - M`. 

### `initial_state`

 The state word is one for the empty table and two for a nonempty
machine, even if it rejects on its first transition. 

### `rawInput_at_field`

 Address a field bit by the exact length of all preceding port fields. 

### `inputWord`

 Pack the raw stream in little-endian words. Bits in the last incomplete
word and all words beyond the stream use zero padding. 

### `copyBit`

 Public words give the radius, destination state base, packed raw input
base and word width, in that order. The persistent state is the input bit
number. Register 29 returns the next bit number. 

### `putState`

 Store the canonical state word into an otherwise blank bank. The same
native call with tag one prepares the required output at the final group. 

### `sourceAddress`

 The address of the packed input word containing the specified input bit. 

### `targetAddress`

 The first-tape cell receiving an input bit, counting forward from the head in the
serialized configuration. 

### `copyBit_native`

 Native code emits exactly one initialized input symbol with a single
read and write, advancing its persistent cursor. 

### `putState_native`

 One native write prepares the state field. The full halt-bank contents
are canonical if its tape fields are in zero-default memory. 
