---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/CandidateScoreRefinement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/CandidateScoreRefinement.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/CandidateScoreRefinement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Candidate-array and generated-score refinement

The concrete temporary array has the same values as the search decoder after
one candidate is prepended. Generated collision streams may be permuted;
their successful-leaf counts still equal the exact natural evaluator.


### `currentArray_set_candidate`

 The preserving array writer's indexed replacement has exactly the
candidate decoder used by sequentialNumerator. 

### `encoded_candidate_array`

 Direct split-array form for CandidateArrayProgram's temporary copy. 

### `generated_counts_sum`

 An arbitrary explicit ordering of all vertex pairs yields the same
natural score. Only permutation, not a particular enumeration order, is used. 

### `scorerContext`

 Exact concrete inputs for the fixed pair scorer. 

### `selectedPairPlans`

 The selected plans consumed by one actual pair-score callback. 

### `score_eq_sequentialNumerator`

 The actual pair aggregator computes precisely the evaluator used by
chooseMinNat, with no required order beyond a permutation of all ordered pairs. 

### `scorer_program_run`

 Actual halting execution plus the exact natural unary score on port 18. 

### `generated_pair_payloads`

 Depth-two tuple generation on framed vertex plans produces exactly the
pair payload expected by PairScoreProgram, retaining every multiplicity. 
