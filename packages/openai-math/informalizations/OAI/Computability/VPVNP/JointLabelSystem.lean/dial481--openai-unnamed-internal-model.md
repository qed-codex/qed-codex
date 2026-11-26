---
{
  "module": "OAI/Computability/VPVNP/JointLabelSystem.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointLabelSystem.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointLabelSystem.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The joint integer label equations of Section 8.1

The grammar labels and the entries of the fixed motif maps are disjoint sets
of variables. Enumerating their union gives one finite list of variables for
the field-descent and Macaulay constructions. Every solution specializes the
two systems simultaneously, over any commutative coefficient ring.


### `leftIndex`

 Index of a variable from the first system in the joint coordinate list. 

### `rightIndex`

 Index of a variable from the second system in the joint coordinate list. 

### `unionEquations`

 Place the two lists of integer equations in one ring on numbered variables. 

### `unionEquations_solution_iff`

 Pulling a joint assignment back along the two coordinate embeddings yields
exactly the simultaneous solutions of the original systems. 

### `joinAssignment`

 Combine two label assignments into the common list of numbered coordinates. 

### `Production`

 Production labels at the width used for a size `n^c` circuit. 

### `grammarEquation`

 The integer equation `Bₓ - Uₙ(x) = 0` at the designated start state. 

### `equations`

 The full integer polynomial system for the production labels and the motif
matrix entries, in the finite coordinate format of Section 8.2. 

### `equation_count`

 There is one equation per Boolean input in addition to the fixed output
coordinates of the motif data. 

### `variable_count_le`

 The variable count of the joint system grows polynomially at each fixed
circuit exponent and fixed motif data. 

### `solution_iff`

 A solution in any commutative ring gives the path counts for every input
word and specializes the integral motif identities in the same ring. 

### `exists_solution`

 An actual small circuit and a solution of the fixed local motif equations
give a joint solution in the circuit's coefficient ring. 
