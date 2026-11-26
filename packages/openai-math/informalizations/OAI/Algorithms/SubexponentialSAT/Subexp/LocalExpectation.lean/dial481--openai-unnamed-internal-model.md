---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/LocalExpectation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/LocalExpectation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/LocalExpectation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform multi-color conditional expectation

All parameters remain visible. The local evaluator enumerates only each pair's
read support, and its total evaluation bound is a fixed polynomial in the
number of chunks and universal types. Natural completion counts also give a
common-denominator representation for the rational conditional scores.


### `completionCount`

 Unnormalized finite completion count. Its terminal function can be a local
zero/one collision indicator. 

### `wordExpectation_eq_completionCount`

 Exact numerator and denominator for an exhaustive local average. 

### `scaledCount`

 A local numerator scaled to a common power of the word alphabet size. 

### `commonNumerator`

 Natural common numerator for a sum of bounded-support local indicators. 

### `localEvaluator_eq_commonNumerator`

 The common numerator represents the actual rational local evaluator,
including its constant offset. 

### `pairObjective`

 The squared type-count potential from Section 5.4. 

### `pairEvaluator`

 The actual local-pair evaluator on the manuscript's factor/head/padding
word variables. Only the union of the two read supports is enumerated. 

### `pairEvaluator_calls_le`

 The evaluator makes at most `D² q^(2(Δ+1))` local collision calls for a
vertex enumeration of length `D`. This bound is uniform over partial assignments. 

### `numberedPairSupport`

 Numbered local support from an explicit list of independent word indices. 

### `computedAssignment`

 A concrete, terminating deterministic word assignment using the efficient
local-pair conditional evaluator at every choice. 

### `computedAssignment_deviation_le`

 The executable local-pair construction satisfies the manuscript's
deviation bound. All enumerations are explicit algorithm inputs. 

### `computedAssignment_consistent`

 A shared factor receives one word at all of its incidences in the computed
assignment, so the derandomization preserves the required slot consistency. 

### `computedAssignmentCounted`

 The same concrete assignment, instrumented to count local collision calls. 

### `computedAssignmentCounted_calls_le`

 Whole-search bound: the actual instrumented program makes at most
`M * 2(q-1) * D² * q^(2(Δ+1))` local collision evaluations. 

### `indices_length_le`

 The explicit seed representation includes factor words, heads, and all
padding slots. Its length is still linear in the number of chunks. 

### `computedAssignmentCounted_calls_polynomial`

 A polynomial bound in the input chunk count for the fully instrumented
local-pair search. The leading factor depends only on the fixed alphabet and Δ.
Arithmetic bit costs and list-processing costs are not asserted to be unit cost. 

### `alphabet_pair_power`

 The support-completion power is exactly the square of the universal block
size, even when every displayed parameter grows. 

### `computedAssignmentCounted_calls_uniform`

 Uniform fixed-degree polynomial bound for the whole local-word search.
In particular no exponent of D or N depends on r,Q,Δ, or k. 

### `naturalPairTerm`

 The local collision as a natural zero/one function. 

### `pairNumerator`

 A bounded natural common numerator for all pair terms of the conditional
objective. Its common denominator is N². 

### `pairEvaluator_eq_numerator`

 Every conditional score has the same displayed denominator, and the
numerator above is bounded by D²N². 

### `pairEvaluator_le_iff_numerator_le`

 Comparing conditional scores requires only comparing bounded natural
numerators. The offset and positive common denominator cancel exactly. 

### `pairNumerator_bitSize_le`

 Explicit logarithmic bit-size bound on every natural score numerator. 
