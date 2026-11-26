---
{
  "module": "OAI/Computability/VPVNP/PairVertexLocatedBody.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexLocatedBody.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexLocatedBody.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Shared locator registers across stage-specific bodies

Register banks chosen by a matrix table need not have the same numerical ordering as the
child and hidden routines. Number the complement of the fourteen locator words separately.
Every stage then uses the shared prefix required by the finite stage dispatcher.


### `LocatedBody`

 A vertex segment together with an embedding of the fourteen registers needed to locate its
active level. 

### `LocatedBody.code`

 The executable segment of a body that shares a level locator. 

### `LocatedBody.locator`

 Identify the body's fourteen level-locator registers within its private register space. 

### `Tail`

 The body's private registers outside the image of its shared locator embedding. 

### `tailCount`

 Number of additional private registers required beyond the shared locator bank. 

### `order`

 Number the other registers separately and retain the order of the locator. 

### `normalized`

 Only the numerical operand placement changes. The PC and native opcode are identical. 

### `withChildren`

 Append fresh child registers after every register of the remaining routine. 

### `family`

 One finite image starts with the real level scan and selects the stage within the block. 
