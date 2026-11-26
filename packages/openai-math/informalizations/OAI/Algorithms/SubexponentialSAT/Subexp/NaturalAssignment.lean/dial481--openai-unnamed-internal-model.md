---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/NaturalAssignment.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/NaturalAssignment.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/NaturalAssignment.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Conditional assignment by natural-number comparisons

The executable chooser and all of its scores use natural numbers. A rational
common-denominator identity is used only to prove that every comparison,
including ties, agrees with the previously verified conditional-expectation
algorithm. Score execution enumerates only the active local pair support.


### `chooseMinNat`

 Earliest minimum in an explicit nonempty list, using only natural scores. 

### `chooseMinNat_eq_chooseMin`

 The chooser depends only on the ordering of scores, including equality. 

### `assignNat`

 Sequential assignment with a natural-number evaluator. 

### `chooseWithCostNat`

 Instrumented natural chooser. The second component counts terminal calls
reported by the executed score evaluations. 

### `assignWithCostNat`

 Instrumented sequential natural search, retaining the same finite loops. 

### `completionCountCounted`

 Count successful completions and the leaf tests actually performed. 

### `commonNumeratorCounted`

 The natural common-numerator algorithm with its actual terminal-call
counter. Multiplications and list operations are separate cost obligations. 

### `numberedNaturalPairTerm`

 The natural zero/one collision test on numbered seed coordinates. 

### `numberedPairNumerator`

 A common natural numerator for the same local pairs as the verified
numbered evaluator. No rational arithmetic is executed by this definition. 

### `numberedPairNumerator_le_block_square`

 The common denominator is N² for a complete, duplicate-free word list. 

### `sequentialNumerator`

 Sequential candidate scores enumerate only the as-yet-unassigned numbered
coordinates read by each pair of input coordinates. 

### `sequentialNumerator_bitSize_le`

 Binary size of every actual sequential numerator used by the chooser. 

### `sequentialNumeratorLeaves`

 Materialize the same numerator as successful Boolean leaves, using dummy
choices to pad each pair's local support to 2(Δ+1) words. 

### `sequentialNumeratorLeaves_trueCount`

 The actual successful-leaf list is a unary representation of the score. 

### `sequentialEvaluator_eq_numerator`

 Exact common-denominator specification; this theorem does not execute
the rational evaluator inside the natural-number algorithm. 

### `sequentialEvaluator_le_iff_numerator_le`

 All compared sequential scores have the same positive denominator and
  constant offset, so natural comparisons preserve even ties exactly. 

### `naturalValues`

 The finite list of selected words. Every executed score is natural. 

### `naturalAssignment`

 The actual deterministic assignment, computed by bounded local natural
counts and comparisons. The representation agrees with computedAssignment. 

### `naturalAssignment_deviation_le`

 The already-proved deviation bound transfers to the executable natural
comparison program through equality of the complete assignments. 

### `sequentialNumeratorCounted`

 The concrete sequential numerator and its local collision-call counter. 

### `naturalAssignmentCounted`

 The natural assignment program instrumented through the actual recursion. 

### `naturalAssignmentCounted_calls_uniform`

 The natural-score implementation performs the same polynomially bounded
number of local collision evaluations. This is not a Turing-machine cost claim. 

### `enumeratedNaturalAssignment`

 Fully explicit word and seed enumerations for the natural-score program.
Only the input's vertex and factor lists remain as enumeration inputs. 
