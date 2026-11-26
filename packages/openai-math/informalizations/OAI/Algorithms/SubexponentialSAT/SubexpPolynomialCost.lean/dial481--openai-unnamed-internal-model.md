---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPolynomialCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPolynomialCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPolynomialCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform polynomial and CRT costs with growing parameters

These bounds apply to the existing executable coefficient-list algorithms.
Their numerical constants and exponents are absolute: in particular, `Q`, `D`,
the path degree, the extension degree, and coefficient width are not fixed.
Scalar-operation counters and serialized bit lengths are distinguished from
the separate task of proving a Turing-machine simulation.


### `uniformCrtOps`

 A fixed polynomial bounding the actual dense CRT scalar-operation counter. 

### `uniformInverseOps`

 A fixed polynomial bounding the actual local-inverse counter. 

### `parameterSize`

 One size parameter containing every growing argument relevant here. 

### `scalarPowerWithCost`

 A finite scalar power loop, with one counted multiplication per step. 

### `constantInverseWithCost`

 Compute one local constant inverse from supplied pairwise inverses. 

### `crtFromDifferences`

 Cache the computed constant inverses in a finite vector before running
the dense CRT. Indexing the vector performs no hidden scalar inversion. 

### `denseCRT_cost_uniform`

 The existing executable loop has a uniform bound even when Q grows. 

### `inverse_working_buffers`

 Bounds the two stored polynomial arrays in the geometric-inverse loop.
This is a per-array bound, not an unproved peak-memory claim for recursive code. 

### `localInverse_spec`

 An actual executable local inverse, its algebraic certificate, its output
length, and its uniform scalar-operation bound in one statement. 

### `uniform_CRT_spec`

 The CRT algorithm is uniform in Q and D; inverse inputs are explicit and
the proof uses the genuine formal jets of H over a commutative ring. 

### `crtFromDifferences_spec`

 Pairwise inverse certificates suffice for the executable reconstruction;
all cofactor constant inverses are computed by the counted preprocessing loop. 

### `pathEval_cost`

 A path degree bound is charged as a growing numerical parameter. 

### `packCoefficients`

 Concatenate fixed-width coefficient encodings. The width and coefficient
count are external format data; no constant-time access is assumed. 

### `inputJets_bits`

 Encoding Q order-D jets requires at most Q*D coefficient slots. 

### `CRT_output_bits`

 A storage bound using an actual coefficient encoder of width h*(D+1)*b.
The logarithmic prime-width parameter b and extension degree h remain visible. 

### `CRT_output_bits_all_parameters`

 A fixed degree-five storage bound displaying every varying parameter. 

### `liftRing_CRT_output_bits`

 The concrete prime-power quotient encoder discharges the width premise.
This is a bit-length statement; it makes no claim about encoder runtime. 
