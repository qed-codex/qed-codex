---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpKernelCorrectness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpKernelCorrectness.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpKernelCorrectness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Correctness of the executable r-group list kernel

The executable objects are actual lists of raw coefficient expressions.
Enumeration hypotheses assert duplicate-free, complete lists; expression
hypotheses identify each local group program, scalar weight, and outside
weight separately.  No hypothesis supplies a final jet or count.


### `buildBlocks`

 Assemble the actual list of outer blocks and independent inner lists. 

### `rawMomentValue_eq_finiteSum`

 Complete enumerations and local expression denotations identify the
kernel's raw polynomial value with the finite separated family sum. 

### `sum_exponentList_eq_sum_retained`

 The executable weak-composition list gives exactly the retained moment
sum, without enumerating a coordinate box. 

### `executeJet_eq_momentCoefficients`

 The concrete jet execution, with its verified weak-composition list,
expressed as a finite sum of canonical polynomial coefficient extractions. 

### `canonical_rawMomentValue_eq_separatedMoment`

 Local full-group expression denotations are sufficient: canonical
projection of the raw executed moment equals the separated symbolic moment.
Independence and factorization are pointwise facts about the input factors. 

### `executeJet_buildBlocks_eq_separatedJet`

 The actual list/dense/postfix jet kernel returns the coefficients of
the symbolic separated jet.  Every program-denotation premise is local to
one outside weight, one inner weight, or one group expression. 

### `executeJet_buildBlocks_eq_fullSum`

 Combining the executable bridge with the checked truncation/counting
semantics gives the coefficients of the full truncated input sum.  The
remaining algebraic premises are the local degree filtration and vanishing
of complete high-U coefficients after X substitution. 
