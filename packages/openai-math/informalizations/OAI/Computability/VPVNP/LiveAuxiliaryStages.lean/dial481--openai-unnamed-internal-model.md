---
{
  "module": "OAI/Computability/VPVNP/LiveAuxiliaryStages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveAuxiliaryStages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveAuxiliaryStages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Stage tables for nomination and auxiliary header preparation

The nomination stage accepts when the cursor reaches the public production-label
count. The descriptor initializer accepts after one call. The copy stage uses the
seventh descriptor's cumulative end, read from live scratch on each call. Both
boundary checks have deterministic accepting exits on an empty choice stream.


### `nomination`

 Run the nomination worker under a public production-label bound, accepting at the end of
the label scan. 

### `«initialize»`

 The one-call stage that creates the auxiliary header descriptor table. 

### `copy`

 The counted sparse-copy stage whose stopping bound is read from the last auxiliary
descriptor. 

### `nominationData`

 The nomination worker's public data extended with the label count used by its stage guard. 

### `copyData`

 The final packed end is field zero of the seventh descriptor. 

### `headerSources`

 The output ranges produced by the preceding header recovery and nomination stages. 

### `initializeData`

 The initializer's public input uses capacities and addresses only. The two
exterior lengths that depend on the group are read from the first source array. 

### `nomination_active`

 The component template and the cursor guard together consume the specified
bits, preserving the stored value and the one-probe bound. 

### `nomination_closed`

 The last nomination call transfers to descriptor initialization, including
when the production-label count is zero. 

### `copy_active`

 The copy wrapper performs one extra read of the cumulative end, then the
dispatcher copies the selected word. 

### `copy_closed`

 The cursor at the end of the populated header accepts without touching
the sparse virtual destinations. 
