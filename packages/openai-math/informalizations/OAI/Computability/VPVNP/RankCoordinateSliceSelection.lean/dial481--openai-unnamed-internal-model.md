---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateSliceSelection.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSliceSelection.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSliceSelection.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Greedy minor readers for a live finite-slice query

The two pivot templates depend only on the base relation matrix. The
numerator has a separate direct reader bank for the currently staged
powered monomial and the replacement row. Both physical readers use the
same clock and stack cap expected by the paired determinant machine.


### `local instance : DecidableEq (PrefixPort K)`

 Compares the ports of a prefix-rank call using the underlying Gram-scan address type. 

### `local instance : DecidableEq (PrefixWorkspace.Aux (PrefixPort K))`

 Decides equality of auxiliary addresses in the greedy prefix scanner. 

### `local instance : DecidableEq (Select.Side K)`

 Compares the register and auxiliary addresses of a row or column selector. 

### `local instance {J : Type} [DecidableEq J] : DecidableEq (SelectedMinor.Host K J)`

 Distinguishes the two selector banks and the direct entry reader inside a selected minor. 

### `local instance {J : Type} [DecidableEq J] : DecidableEq (SelectedMinor.Work K J)`

 Compares the selected row word, column word and remaining selected-minor workspace
addresses. 

### `height`

 Row count of the appended matrix, comprising equation multiples and monomials up to the
point bound. 

### `width`

 Column count of the slice matrix, given by the number of monomials up to its column degree. 

### `selectedTime`

 Time bound for a selected entry, covering the slower of the ordinary and powered readers
and the row-replacement overhead. 

### `selectedSpace`

 Peak stack height for a selected entry, including the workspace needed to test the
replacement row. 

### `selected_reads`

 Physical readers for the exact two matrices in the finite-slice Cramer
quotient. The three direct scalar programs may use different predicates and
banks from the immutable pivot matrix reader. 
