---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterGuessWord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterGuessWord.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterGuessWord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native binary-word choice subroutine

Three registers hold the partial value, the weight of the next bit, and zero.
Doubling the weight wraps to zero exactly after the last of the machine word's
bits. The eight-opcode fragment works at every word width, including zero, and
may be embedded at arbitrary program counters with an arbitrary continuation.


### `Prefix`

 A local prefix of genuine native steps. The relation records every consumed
branch bit and tick, and performs no external probe. 

### `Prefix.execute`

 A valid prefix composes with the genuine RAM interpreter on every
continuation, preserving the external memory and every unconsumed bit. 

### `Prefix.execute_short`

 A stream that stops before the last required binary choice rejects,
independently of the continuation and the available instruction fuel. 

### `instruction`

 Eight fixed instruction slots. Register zero is the result, register one
is the binary weight, and register two is zero. 

### `resize_instruction`

 The instantiated table embeds the same fragment in any larger program. 

### `Contains`

 The host machine implements the eight word-guess instructions at the specified labels and
registers with the specified continuation. 

### `value`

 Value of a little-endian bit string, independently of the RAM word modulus. 

### `events`

 Loop events for guessing the supplied little-endian bit sequence, including one choice per
bit and the final exit tick. 

### `loop`

 Execute the exact choices remaining at a loop entry. 

### `trace`

 The complete event list including the three register initializations. 

### `resultRegs`

 Exact register file at loop exit. Both temporary registers contain zero. 

### `native_exact`

 From its entry the native subroutine consumes exactly the canonical bits of
the output word, uses `4*w+4` private instructions, and returns to its chosen
continuation. Every external address and every other register is preserved. 

### `exists_wordBits`

 Every complete word-width string is the encoding of its unique output. 
