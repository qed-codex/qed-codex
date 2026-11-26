---
{
  "module": "OAI/Computability/VPVNP/DegreeRefreshEntries.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshEntries.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshEntries.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scalar entries in an actual degree-refresh branch

After the old and new incident indices have been fixed, the port first
tests its two diagonal ties. Passing these tests leaves the single
parameter list of the selected motif entry. The description uses only
the wire indices, and its polynomial can be evaluated at any solution
of the fixed equations.


### `expanderBranchGraph`

 The output network and its half-wires depend only on the branch's selected widths. 

### `refreshEntryIndices`

 The common scalar indices for one local kernel, after checking the two
diagonal segment equalities. The site is given in block and port coordinates. 

### `refreshEntryIndices_spec`

 Reading the common indices and multiplying the selected scalars gives
the actual kernel coefficient over any ring satisfying the equations. 

### `refreshEntryIndices_monomial`

 The integral entry polynomial is either zero or a monomial of coefficient
one and degree at most the number of copies used by this block. 

### `expanderKernelWitness`

 A kernel entry witness at an actual port. A failed list has no witnesses,
and a successful list gives one witness independently of the scalar values. 

### `expanderKernelWitness_exponents`

 For every surviving witness the total multiplicity is bounded linearly
in the maximum old width, uniformly over all networks of this fixed degree. 
