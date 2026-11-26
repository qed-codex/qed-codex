---
{
  "module": "OAI/Computability/VPVNP/PairSimulationPrivateFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationPrivateFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationPrivateFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Private bit fields in a final-site call

A guess writes each consumed branch bit to one private word. A copy uses the
same storage order and takes each bit from an existing private slice. The two
fragments accept arbitrary program labels and leave the external memory and
the registers of the enclosing traversal available to their continuation.


### `Mode`

 Source of the bits written to a private field. Guess mode consumes branch bits and copy
mode loads an existing private slice. 

### `bitValue`

 Each private cell holds the word zero or one. 

### `instruction`

 Registers are source cursor, exclusive destination end, destination
cursor, one and temporary. Only the two cursors and the temporary are written. 

### `Linked`

 The machine contains the seven instructions of the selected guess or copy loop at the
specified labels, with the given registers and continuation. 

### `storeBits`

 A private-memory slice in increasing physical-address order. 

### `events`

 The exact local trace, including the final range test. 

### `iteration`

 Exact state transition for one bit. The copy reads its value before
either cursor advances. 

### `Result`

 The frame and exit data shared by guessing and copying. 

### `guess_prefix`

 One fresh binary branch for each field bit, in address order. 

### `copy_prefix`

 A private-to-private forward slice copy. The permitted overlap includes
the identical slice and moving the slice toward lower addresses. 

### `bitField_encode`

 The abstract reader serializes the bits in exactly the native store order. 

### `execute_guess`

 Exact suffix, fuel, stored bits and frame when reading one field of a
compression kernel. The enclosing vertex may immediately read its next field. 

### `execute_copy`

 A copy has no branch bits or external probes and takes five local
steps per bit plus the final test. 

### `guess_short`

 The RAM rejects a short field independently of the linked continuation. 

### `guess_accepts_iff`

 With an accepting continuation, complete native paths are in bijection
with the independent assignments of the declared field bits. 
