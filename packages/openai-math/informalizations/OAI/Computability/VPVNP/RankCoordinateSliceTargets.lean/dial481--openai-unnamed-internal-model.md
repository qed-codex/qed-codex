---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateSliceTargets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSliceTargets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSliceTargets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The powered target in the live numerator bank

The ordinary matrix reader and the target reader have disjoint auxiliary
ports. The latter compares the indexed current monomial with the requested
column, returning the native polynomial-basis encoding of zero or one.


### `targetTemplate`

 Powered-monomial scan template with the slice arity and its two degree bounds fixed, and
the dynamic arguments initialized to zero. 

### `targetArgs`

 Installs the current basis monomial, operation scale and variable mark in the target
template. 

### `Direct`

 Disjoint auxiliary ports for the ordinary matrix reader and the powered-target reader. 

### `directReady`

 Requires the base reader to be ready on its own ports and the powered reader to hold its
target arguments on the other ports. 

### `ordinary`

 Runs the ordinary scalar entry reader using the left auxiliary bank of the direct reader. 

### `powered`

 Runs the powered-monomial entry reader using the right auxiliary bank of the direct reader. 

### `target_flag`

 The exact field encoding of the current powered target at one column. 

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

### `native_reads`

 Only the scalar entries of the original relation matrix are an input
contract. The target and both pivot scans execute physical finite code.
The common time and space bounds apply to every choice of basis ordinals. 
