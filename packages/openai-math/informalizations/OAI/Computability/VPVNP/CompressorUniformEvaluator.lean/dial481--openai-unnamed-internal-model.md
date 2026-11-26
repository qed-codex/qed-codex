---
{
  "module": "OAI/Computability/VPVNP/CompressorUniformEvaluator.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorUniformEvaluator.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorUniformEvaluator.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform compilation of the joint label evaluator

The scalar-query implementation provides its two fixed tables and a polynomial
length envelope for their physical inputs. This theorem composes that interface
with algebraic descent, the canonical monomial basis, nondeterministic
evaluation and the literal two-tape compiler. Its exponent and threshold are
chosen before the input length, prime, solution, exponent width or processor.


### `uniformEvaluatorFintype`

 Finite enumeration of the ground field used by the uniform joint evaluator. 

### `uniformEvaluatorDecidableEq`

 Classical equality decision for the ground-field coefficients used by the uniform
evaluator. 

### `uniformEvaluatorAmbientAlgebra`

 Algebra structure on the ambient field induced by the slice-field embedding. 

### `uniform_evaluator_of_coordinate_readers`

 The uniform fixed-code evaluator conclusion, with its physical reader
interface left explicit for assembly of the deterministic Cramer routines. 

### `exists_reader_envelope`

 Per-component size bounds on concrete initialized readers yield the common
length envelope needed for uniform compilation, even if the advised prime and
slice vary across lengths. 
