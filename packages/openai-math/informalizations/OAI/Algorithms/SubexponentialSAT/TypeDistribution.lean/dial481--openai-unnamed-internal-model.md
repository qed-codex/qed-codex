---
{
  "module": "OAI/Algorithms/SubexponentialSAT/TypeDistribution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/TypeDistribution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/TypeDistribution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform words induce uniform local types

The outcome space consists of all assignments of words to distinct factor,
head, and padding indices. Local read maps are injective. Read maps at
distinct coordinates sharing no factor have disjoint ranges. Finite product
counting then supplies the actual marginals and pair moments needed by
SubexponentialSAT.Variance; these probabilistic properties are conclusions, not hypotheses.


### `Unread`

 Coordinates outside the image of an injective read map. 

### `splitReads`

 Split a global assignment into the read coordinates and all remaining ones. 

### `mean_restrict`

 Restricting independent uniform coordinates along an injection is uniform. 

### `jointReads`

 Combine two disjoint injective sets of reads into a single injection. 

### `mean_restrict_mul`

 Functions of disjoint sets of independent uniform coordinates have
factorizing pair moments. 

### `list_mean_eq_uniform`

 An explicit duplicate-free complete alphabet has the uniform finite mean. 

### `resampleEquiv`

 Swap an assignment coordinate with one fresh word. This is a permutation
of the full product outcome space, including the old coordinate value. 

### `mean_resample`

 Resampling any single word preserves the uniform mean. 

### `recursive_word_mean_eq_uniform`

 Bridge from a recursively enumerated word expectation to the uniform
finite mean. Completeness of the coordinate list suffices: repeated resampling
of a coordinate also preserves the uniform distribution. The recursion
equations are explicit hypotheses so this applies to independently implemented
finite evaluators without introducing a second algorithm definition. 

### `sum_fiberCount_sq`

 Squared fiber counts count ordered pairs in the same fiber. 

### `squared_deviation_eq_collisions`

 The global squared-deviation potential is a sum of local pair-collision
indicators minus a constant. This is the efficient-evaluation interface. 

### `SeedIndex`

 Each factor, head, and padding slot has a distinct independent word. 

### `Assignment`

 A complete assignment of all independent random words. 

### `LocalCoord`

 A head position and one position for every slot. 

### `LocalParts`

 The same local positions, distinguishing used and unused slots. 

### `reads`

 Every local type coordinate reads a different underlying word. 

### `wordTypeEquiv`

 Functions on the local read positions are precisely universal types. 

### `assignmentType`

 Types induced by one full assignment of independent words. 

### `assignmentType_eq_typeFromWords`

 This read-map presentation is the actual slot assignment of Section 5.4. 

### `rawRead_ne`

 Distinct chunks without a common factor have disjoint raw read indices. 

### `readSupport`

 The exact finite set of source words read by one coordinate. 

### `pairSupport`

 Shared factors are counted only once in the union of two read supports. 

### `pairCollision`

 Rational indicator that two coordinate types coincide. 

### `assignment_deviation_eq_collisions`

 The exact potential used for derandomization is a sum of local pair terms. 

### `mean_assignmentType`

 The full law of a coordinate type is uniform, derived from its read injection. 

### `mean_assignmentType_mul`

 Types at distinct coordinates sharing no factor have factorizing moments. 

### `assignmentType_marginal`

 The single-coordinate indicator moment required by the variance theorem. 

### `assignmentType_independent`

 The independent pair moment required by the variance theorem.
Adjacent chunks need not satisfy this conclusion and are not assumed to. 

### `mean_squared_deviation_le`

 Expected squared type-count deviation for the actual independent word
assignment, with the manuscript's conservative dependency-degree bound. 

### `exists_assignment_deviation_le`

 A concrete global word assignment satisfying (5.8) exists.
This uses the finite averaging theorem; the sequential computable minimizer
is supplied separately in ConditionalExpectation. 

### `exists_consistent_types_deviation_le`

 Direct layout interface: one global word per factor and a consistent
coordinate type assignment, with the full squared-deviation guarantee. 
