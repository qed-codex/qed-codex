---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateSelectedPrepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSelectedPrepare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSelectedPrepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Complete preparation of the two determinant queries

The evaluator's two public ordinals determine the source monomial and the
replacement row. The fixed label and Frobenius routines start with the same
advice. Their bounded executions supply the canonical input to each Schur
root for the live operation and pair of ordinals.


### `mode`

 Selects the Frobenius preparation routine on a Frobenius step and the label routine on a
label step. 

### `label`

 The zero-based variable index for a label step, with zero as the unary input for a
Frobenius step. 

### `local instance : DecidableEq (PrefixPort K)`

 Compares prefix-rank ports through the underlying Gram scan's register and auxiliary port
tags. 

### `local instance : DecidableEq (PrefixWorkspace.Aux (PrefixPort K))`

 Decides equality of the auxiliary ports used to call the prefix-rank machine. 

### `local instance : DecidableEq (Side K)`

 Distinguishes the word registers and auxiliary ports of the greedy selector workspace. 

### `local instance {J : Type} [DecidableEq J] : DecidableEq (SelectedMinor.Host K J)`

 Compares addresses in the row scan, column scan and direct entry reader of a selected
minor. 

### `local instance : DecidableEq (Den K)`

 Decides equality of the selected row word, selected column word and auxiliary addresses in
the denominator bank. 

### `local instance : DecidableEq (Parts K)`

 Compares ports of the determinant, ordinal and unary-label preparation components. 

### `local instance : DecidableEq (Advice K)`

 Compares an advice address by its component port or its Boolean scale selector. 

### `local instance : DecidableEq (Work K)`

 Distinguishes the writable component addresses from the shared temporary stack. 

### `local instance : DecidableEq (Prepare.Ports (Den K) (Raw K) (Side K))`

 Decides equality of public reader ports and their private advice or working addresses. 

### `machine`

 Prepares the determinant pair by reading the greedy row ordinal and staging the selected
target arguments for the given operation mode. 

### `numAt`

 Numerator bank for one live query, with the next coordinate as replacement row and the
current coordinate as source of the powered target. 

### `prepare_bounded`

 Runtime preparation from a reader for the original Macaulay relation
matrix. The returned host and the two original public ordinal words meet
the determinant caller's ABI. 
