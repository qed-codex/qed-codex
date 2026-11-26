---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackAlias.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackAlias.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackAlias.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Register aliases between the determinant engine and its arithmetic bank

Schur instructions read the six live query fields directly. Child instructions
also read the saved loop index. Output registers and temporary word stacks
belong to the auxiliary bank. The routine preserves the entire live frame and
history, as well as every auxiliary port outside the register bank.


### `R`

 Register count for the aliased dispatcher, including eight input words, six outputs and the
scratch bank. 

### `Small`

 Register-machine ports for the dispatcher with no public-word inputs. 

### `Reg`

 Indices of the dispatcher's physical registers. 

### `liveSlot`

 Identify the six query inputs and, when enabled, the count input with their corresponding
live-frame slots. 

### `ports`

 Route aliased inputs to the live frame and the remaining dispatcher ports through the
supplied auxiliary bank. 

### `pub`

 Empty public-word bank of the aliased dispatcher. 

### `Ready`

 Width-sized auxiliary register words, including a zero dummy counter and
the row dimension. The scratch registers may contain arbitrary words. 

### `routine`

 Install one compiled dispatch operation with its query registers aliased to the live frame. 

### `LiveInput`

 The fields actually read from the caller's frame. 

### `run`

 Execute the dispatcher directly on the engine's frame. Replacing the
auxiliary scratch state never changes the live query, history, or result. 
