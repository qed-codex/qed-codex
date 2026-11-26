---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Verification/Possible.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Verification/Possible.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Verification/Possible.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One small isolated system for generic matrix multiplication

The shared affine products come from a single accepting path.
The additional measurements lose at most the stated number of
independent output coordinates.



# Arithmetic verification with a public random seed

The seed distribution is input independent. Each outcome selects a
finite collection of accepting paths with a uniform bound on their
lengths. Accuracy is pointwise, allowing error on either answer.
Entropy uses natural logarithms in both the budget and its rate.


 # Cost of detecting single-entry errors in a proposed product 

### `detect`

 Every error must be detected on at least one third of the seed
mass. Count errors first on a finite subset, then take its mass to one. 

### `read_bound`

 This bound uses no restriction on support size or entropy. 


# Simulating an arithmetic tree by existential paths

Each path keeps the constraints accumulated on its branch.
A fresh register is uniquely determined by its instruction.
A failed division costs a single equality test.


### `simulate`

 Every finite tree has an existential path verifier of at most its depth. 


# Simulating division-free tests by witness-free decision trees

After a prefix of arithmetic operations, each available polynomial
can be read from a scalar, input, or register. Prepending this prefix
to any subsequent tree fixes all its initial registers and adds one
level per operation.


### `Test.tree`

 The deterministic tree needs no witness. Its depth counts one step
per arithmetic operation and one per final equality. 

 # Independent output combinations in a matrix product 

### `Projected`

 The linear combinations need not be individual output entries.
The closure here uses polynomials and decompositions over F itself. 

 # Selecting independent leading output cells 

### `pivots`

 Restriction to all possible leading indices is injective on the
row space. Use any requested number of them as normalized pivots. 

 # Degenerating an output projection to its leading cells 

### `Projected.cells`

 The additive weight of a cell is distinct for each pair of
indices. Negative powers cancel by the leading-index property. 

 # Descending projections by isolating their output cells 

### `Projected.descend`

 A leading-cell tensor descends to the ground field because its
coefficients are zeros and ones. No descent of the original
projection matrix is required. 

### `specialize_rank`

 Specialize entries integral at a place, allowing arbitrary poles
in the rank decomposition itself. 


# Specializing a projected quadratic term

Some terms separate only in the output index. Eliminate their
output vectors over the valuation ring before specializing. The
remaining projection has an identity minor and bounded border rank.


 # Inverting a Jacobian preserves the count of mixed products 

### `linearized_projection`

 Each quadratic term has two separated mixed derivatives.
Auxiliary measurements separate only in the output index. 


# Differentiating the deformed verification equations

A left and a right coordinate derivation lift to the generic point
of the curve, fixing the parameter. Their action commutes with
specialization at the chosen branch. Therefore the mixed derivative
of the output specializes to the matrix multiplication tensor.



# Independent projected outputs from equality-test verification

An isolated system at a generic input comes from just one accepting
path. A second family of independent constants gives the direction
of a simple deformation. Input derivations fix these new constants.
The mixed derivatives recover matrix multiplication upon specialization.


### `gap_projection`

 A strict gap on a finite set of seeds suffices. The rank bound
uses the maximum length of one path, independently of the seed count. 
