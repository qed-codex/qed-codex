---
{
  "module": "OAI/Computability/VPVNP/CompressorLabelEvaluator.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorLabelEvaluator.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorLabelEvaluator.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A common finite algebra for the grammar and both compressor templates

At any small-circuit length, the grammar, the six-party block and the port
graph block satisfy their respective equations over the original field.
All three assignments descend together. The number of parties in the two
motifs can differ. The prime and the slice model are chosen before any input
exponent vector for the monomial evaluator.


### `compressorLabelCount`

 Numbered grammar labels followed, up to a permutation of coordinates,
by the fixed shrinking and degree-refresh map parameters. 

### `compressorEquations`

 The actual simultaneous equations. There is one grammar row per Boolean
input, and the fixed template rows retain their distinct parameter names. 

### `compressorDegree`

 The template contribution to the degree bound is constant across lengths. 

### `compressorHeight`

 A fixed bound for the absolute coefficients of both template families. 

### `compressorPrimeBits`

 Prime-size exponent in characteristic zero, fixed before the evaluator inputs. 

### `compressorSolution_iff`

 Read the original production coefficient equations and both templates
back out of the numbered simultaneous system in an arbitrary ring. 

### `exists_compressorModel_of_solution`

 Algebraic descent of the full joint system at every satisfiable length. 

### `exists_compressorSolution_of_circuit`

 A small circuit and the two compressor templates supply one simultaneous
solution to all the formal label equations. 

### `exists_compressorEvaluator`

 From an actual circuit at the indicated length, obtain one reduced
finite-algebra model for the entire compressor. In positive characteristic
the prime is the given characteristic, and in characteristic zero its bit
length is polynomially bounded. 

### `compressorEvaluator_readback`

 The same model specializes every path-count equation and the two fixed
wire identities. Its functional and all exponent-vector path counts come
from `LabelEvaluator.Model.functional_one` and `Model.branchCount_mod`. 
