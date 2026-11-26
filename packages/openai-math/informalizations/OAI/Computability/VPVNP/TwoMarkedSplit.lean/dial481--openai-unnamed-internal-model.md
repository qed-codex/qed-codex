---
{
  "module": "OAI/Computability/VPVNP/TwoMarkedSplit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TwoMarkedSplit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TwoMarkedSplit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tensor nodes in the endpoint-coupling split

Appendix A.3 splits the first marked index while retaining the second.
The exterior column and row become background indices at the fixed endpoints,
so that a child is again a two-marked table with both marks free to move.


### `TwoMarkedNode`

 A coefficient table with two movable indices and a finite background
basis at each party. The background may grow at successive splits. 

### `TwoMarkedNode.Basis`

 Finite background basis at each party, separate from the two movable indices of the node. 

### `TwoMarkedNode.coeff`

 Tensor coefficients indexed by a background basis assignment and the two independently
  marked indices. 

### `place`

 Place the two indices without moving any background index. 

### `wire`

 The root table is the identity on a pair of marked indices. 

### `child`

 Contract the old first index against the last argument of the operator.
Its column lives at `a₀`, its row at `a₁`, and the new first index can be
placed anywhere. 

### `exteriorOperator`

 `true` chooses contraction after creation. The intermediate level is
one higher on that branch and one lower on the `false` branch. 

### `exteriorChild`

 One exterior split in the binary tree of Appendix A.3. 

### `value_exterior_split`

 At each placement the sum of the two child arrays represents the parent
times the identity wire on the exterior level. 
