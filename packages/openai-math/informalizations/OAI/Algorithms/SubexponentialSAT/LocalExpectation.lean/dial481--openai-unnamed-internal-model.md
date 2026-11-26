---
{
  "module": "OAI/Algorithms/SubexponentialSAT/LocalExpectation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/LocalExpectation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/LocalExpectation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Conditional expectations of local objectives

A local term is evaluated only on the still-unassigned coordinates in its
support. The resulting evaluator is proved equal to exhaustive conditional
expectation. Instrumentation counts calls to local terms, separately from
arithmetic and data-structure costs.


### `DependsOn`

 A term reads only the coordinates in `support`. 

### `wordExpectation`

 Exhaustive conditional average on an explicit list of remaining indices. 

### `active`

 Indices still free and actually read by a local term. 

### `wordExpectation_filter`

 Removing unread free indices leaves the exact conditional average. 

### `objective`

 A sum of local terms with a constant offset, including the collision form
of the sum of squared type-count deviations. 

### `localEvaluator`

 Efficient local conditional evaluation: a separate small enumeration for
each local term, with unrelated random words omitted. 

### `active_length_le`

 A repetition-free remaining-index list has at most `support.card` active
indices. No bound on the total number of remaining indices is needed. 

### `wordExpectationCounted`

 Exact instrumentation of exhaustive averaging over its supplied indices.
One count unit is one invocation of the local terminal function `f`. 

### `localEvaluatorCounted`

 The implementation computes each local result once and sums its value
and terminal-call count. 

### `localEvaluatorCounted_calls_le`

 With fixed alphabet and fixed support bound, this is linear in the number
of local terms, regardless of the number of globally unassigned variables. 

### `decode`

 Decode the reverse list of chosen values into numbered word variables. 

### `sequentialEvaluator`

 Polynomially many local evaluations per sequential candidate when term
supports are bounded. Numbered coordinates start at `fixed.length`. 

### `sequentialEvaluator_eq`

 Exact equality of the fast local evaluator and the original conditional
mean on lists of word choices. 

### `localAssign`

 Actual sequential search using only the local evaluator. 

### `indexCode`

 Numbering through an explicit enumeration, using the supplied decidable
equality uniformly across generic and concrete index types. 

### `reindexTerm`

 Pull a local term back to numbered coordinates. 

### `initialEvaluator_reindex_eq`

 Explicit `idxOf` numbering preserves the initial conditional mean. 

### `initialEvaluator_reindex_uniform`

 Full explicit enumerations turn the initial local evaluator into the
ordinary uniform mean on all independent word assignments. 

### `chooseWithCost`

 Instrumented finite search with a cost returned by each score evaluation.
Each comparison evaluates the two compared scores exactly once. 

### `assignWithCost`

 Sequential assignment with the evaluator's terminal-call counts composed. 

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
