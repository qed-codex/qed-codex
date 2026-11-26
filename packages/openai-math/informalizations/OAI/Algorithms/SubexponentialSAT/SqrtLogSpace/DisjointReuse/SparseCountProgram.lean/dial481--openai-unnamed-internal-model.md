---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseCountProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseCountProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseCountProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Appendix A: the mathematical depth-first transition and its count invariant.

The transition below specifies a leaf operation by its exact count. It is not a
primitive implementation of that operation, and no bit-time bound is asserted.
The pending list retains the current node and one sibling per branch on the
active path; completed leaves are discarded immediately.


### `Transition`

 The count/frontier invariant does not depend on tie breaking. A physical
selector must separately certify sparsity and the sharp priority conditions. 

### `Descendant`

 Every pending node has an actual sequence of selected disjoint branches.
This relation is proof evidence; it is not a stored history. 

### `exists_finished`

 A termination bound for the semantic transition. This coarse bound does
not assert the draft's sharp running time or implement the leaf operation. 

### `Derivation`

 A proof-only tree records which concrete branches the selector makes.
The running state contains no such tree. 

### `Derivation.run_steps`

 The macro transition visits each derivation node once, consumes its
frontier entry, and adds its exact count to the existing accumulator. 

### `PriorityDerivation`

 The physical serialized search may use any fixed tie order satisfying the
source priority. This proof-only tree imposes no runtime storage obligation. 

### `exists_finished_visit_bound`

 This bounds the number of macro visits. Charging each visit's searches,
leaf computation, and primitive storage is a separate obligation. 

### `Ordered`

 After the current node, sibling depths decrease strictly. 

### `pending_length_le`

 This uses a path-depth bound, rather than the total number of visited nodes. 

### `formulaBound`

 A width-`k` set of clauses has polynomial-size explicit syntax. 

### `encodeBody`

 This is the actual callback body encoding, in its retained raw clause order. 

### `encodeFrontier`

 Pending bodies are stored once in a framed LIFO list; no count table or
completed-leaf list occurs in this representation. 

### `encodeState_run_length_le`

 This bounds serialized semantic state, not the transient storage of a
primitive refinement of the transition. 
