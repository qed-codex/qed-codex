---
{
  "module": "OAI/Computability/VPVNP/NetworkMonomials.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/NetworkMonomials.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/NetworkMonomials.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The monomials of an expanded contraction

In equation (12.2) of *VP and VNP differ over every field*, each path records
the old half-wire indices, a local witness for each kernel entry, and an
accepting path at each original site. Products add parameter exponents.
The choice sets are specified independently of the parameter values.


### `MonomialWitness`

 An entry specified by finite witnesses, each contributing a parameter
monomial. The empty witness set represents a failed local check. 

### `MonomialWitness.Choice`

 Finite index type of the monomials in the witnessed sum, retaining repeated summands as
  separate choices. 

### `MonomialWitness.exponents`

 Exponent of each label in the monomial selected by a given witness choice. 

### `changeValue`

 Change only the proved value of an expansion, preserving the choice
type and exponent function by definition. 

### `paths`

 All accepting local paths have unit weight before kernel substitution. 

### `oneMonomial`

 A single successful local monomial. Its witness persists under every
parameter specialization, including one sending the monomial to zero. 

### `checked`

 A map entry that fails its syntactic checks has no witnesses. Passing
the checks contributes its monomial even if that monomial evaluates to zero. 

### `sum`

 Disjointly enumerate a finite sum of local choices. 

### `prod`

 Independent local choices multiply. Exponents accumulate coordinatewise. 

### `mul`

 Combine witnesses of two successive factors of the path weight. 

### `Layout.kernelWitness`

 Expand the hidden sums over absorbed fields in the local layout kernel.
The local entry witnesses include the syntactic map-entry checks and their
monomials. 

### `Term.pushWitness`

 Expand a single new vertex factor. Its choice records the old half-wires
and witnesses only at old sites assigned to this vertex, together with the
chosen witness for the new local kernel. 

### `Term.pushChoice`

 Unpack a local history node into its hidden old indices, the independent
children assigned to this vertex, and its own kernel witness. 

### `Term.pushChoice_exponents`

 Exponents at a local history node accumulate over precisely its own
children and its kernel entry. 

### `KernelWitnesses`

 Finite local witnesses for every kernel that occurs in this history.
A branch can have different sites, hidden fields and templates. 

### `expandedWitness`

 Complete finite witnesses for a network contraction. First select all
terms along the branch. After choosing one common value for each final edge,
each final site expands its own local history independently. 

### `stopChoice`

 At a terminal branch choose the final edge payloads once, and one local
history at each final vertex. 

### `branchChoice`

 At a branch, the selector chooses the new network and the rest of the
choice belongs to that network's continuation. 

### `natCast_contract`

 Natural path counts can be transported to any commutative coefficient
ring before expanding the kernels. 

### `History.expandedCount`

 Equation (12.2) for a compressed network of local path counts. Its left
side enumerates local paths explicitly, including distinct paths that have
the same exponent vector. 
