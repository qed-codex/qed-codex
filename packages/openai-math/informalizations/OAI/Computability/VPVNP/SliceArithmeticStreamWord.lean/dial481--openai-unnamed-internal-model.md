---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticStreamWord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticStreamWord.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticStreamWord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word transfers for the streamed extension-field evaluator

Each architectural register has the common word width. During a load, popping
the old register provides one iteration per input bit. A single scratch stack
then restores the loaded word to least-significant-bit-first order. A store
uses the same scratch space to prepend the register to a packed output stream.


### `load`

 Replace the register by one word from the front of the stream. 

### `store`

 Prepend the register to the stream and restore the register. 

### `storeReverse`

 Emit the register in the reverse bit order used by a backward output scan. 

### `load_runs`

 The width comes from the old register. Other stacks retain their contents,
the input tail is untouched, and the scratch stack returns empty. 

### `store_runs`

 Copy a register onto the output stream in its native bit order. 

### `storeReverse_runs`

 A reversed store stages a copy of the register, then transfers its bits to
the stream. Both temporary stacks return empty. 
