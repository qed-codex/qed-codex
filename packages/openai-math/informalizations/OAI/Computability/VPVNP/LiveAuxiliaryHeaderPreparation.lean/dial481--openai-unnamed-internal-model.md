---
{
  "module": "OAI/Computability/VPVNP/LiveAuxiliaryHeaderPreparation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveAuxiliaryHeaderPreparation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveAuxiliaryHeaderPreparation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing a live group's sparse auxiliary RAM header

One native call reads the two exterior lengths and constructs the seven
descriptors. A sequence of native copy calls then writes the header the
auxiliary pair computation will see. The initialization phase has an accepting
exit, allowing the enclosing live stage linker to start the copy cursor at zero.


### `initTable`

 Normal acceptance after the twenty-one descriptor words have been written. 

### `initData`

 The length-array base is the first of the seven source bases. 

### `Areas`

 Physical address bounds used by the two stages. Table words, source words
and auxiliary destinations can be placed in distinct live scratch regions. 

### `prepare_native`

 Both stages execute on the original live memory, including the true label
nominations. Every virtual address in the reserved zero-initialized region
returns the exact word of the §11 auxiliary header. 
