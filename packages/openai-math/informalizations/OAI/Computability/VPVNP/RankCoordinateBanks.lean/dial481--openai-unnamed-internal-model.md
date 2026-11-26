---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateBanks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateBanks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateBanks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Installing ordinal and scalar readers in disjoint auxiliary banks

The public address and result ports are shared with the caller. An injective
map places only the reader's auxiliary stacks in a selected part of the host
bank. A call updates that part in place and preserves every exterior stack,
including the data used by the other coordinate readers.


### `BoundedRun.framed_exterior`

 A framed call needs a separate input-size bound only on the exterior
ports. The callee's bounded run already covers every port in its image. 

### `auxPorts`

 Rename the auxiliary ports while retaining the ordinal and result words. 

### `onAux`

 Mount an ordinal reader on a new auxiliary bank while retaining its public input and result
ports. 

### `auxPorts`

 The row and column words and the result stay at their original public ports. 

### `onAux`

 Mount a Macaulay entry reader on a new auxiliary bank while retaining its row, column, and
result ports. 

### `Host`

 A disjoint union of three auxiliary stack banks allows the readers to keep their own
working data. 

### `left`

 Place a port in the first of the three disjoint banks. 

### `middle`

 Place a port in the second bank, separated from the first and third reader workspaces. 

### `right`

 Place a port in the third of the three disjoint banks. 

### `Ready`

 Independent readiness of the two selectors and the scalar reader. 

### `length_le`

 A common component cap bounds every exterior stack of each mounted call. 
