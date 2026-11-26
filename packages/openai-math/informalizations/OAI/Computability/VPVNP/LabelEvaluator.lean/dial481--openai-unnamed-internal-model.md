---
{
  "module": "OAI/Computability/VPVNP/LabelEvaluator.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LabelEvaluator.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LabelEvaluator.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Algebraic descent and the matrix-path identity for the label evaluator

For a satisfiable integer label system, Section 8.2 chooses one prime and one
finite algebra with normalized functional for all exponent inputs. In positive
characteristic the prime is the original characteristic. In characteristic
zero its bit length is bounded using the actual coefficient matrix. The
coordinate pins, slice field and monomial list have explicit bounds.
The counted branches below are the matrix-index paths of equation (8.2).


### `multiplierDegree`

 Bound on multiplier degrees in the effective polynomial-identity certificate for a system
in `t` variables of degree at most `d`. 

### `columnCountBound`

 Bound on the number of monomial columns used in the corresponding bounded-degree
coefficient system. 

### `pointCountBound`

 Uniform upper bound on the number of geometric points in the finite slice. 

### `Ground`

 Finite extension of the prime field chosen from the column-count bound to supply slice
coordinates. 

### `Ambient`

 Algebraic closure of the prime field in which the geometric zero set is taken. 

### `noncomputable local instance (p : Nat.Primes) (t d : ℕ) : Fintype (Ground p t d)`

 Finite enumeration of the label evaluator's slice ground field. 

### `noncomputable local instance (p : Nat.Primes) (t d : ℕ) : Algebra (Ground p t d) (Ambient p)`

 Regard the ambient algebraic closure as an algebra over the finite slice ground field via
its embedding. 

### `sliceIdeal`

 The affine ideal obtained by base change and pinning the selected coordinates. 

### `Model`

 The slice chosen for this system, including its ordered monomial basis. 

### `Model.pins`

 Coordinates fixed by affine equations when selecting this model's finite geometric slice. 

### `Model.values`

 Ground-field values assigned to the pinned coordinates of the slice. 

### `Model.presentation`

 Monomial basis presentation of the coordinate algebra of the finite slice, up to the
  point-count bound. 

### `Model.algebra`

 Reduced coordinate algebra of the slice defined by the original label equations and the
model's pinned coordinates. 

### `Model.labels`

 Elements of the coordinate algebra represented by the original label variables. 

### `Model.functional`

 Normalized prime-field linear functional used to evaluate products of the model's labels. 

### `Model.branchCount_mod`

 The count uses the same field, basis, labels and functional at every input width. 

### `model_of_geometric_solution`

 The slice field and ordered evaluator data exist from a geometric point in
the chosen prime characteristic, with the effective bound discharged. 

### `exists_model_positive`

 A solution in any field of positive characteristic gives the evaluator in
that same characteristic. 

### `exists_prime_solution`

 The chosen prime in characteristic zero admits a geometric solution of the
original integer equations. The effective multiplier bound is proved internally. 

### `exists_model_charZero`

 Characteristic-zero descent, with the prime-size bound independent of the
subsequent exponent width and processor program. 
