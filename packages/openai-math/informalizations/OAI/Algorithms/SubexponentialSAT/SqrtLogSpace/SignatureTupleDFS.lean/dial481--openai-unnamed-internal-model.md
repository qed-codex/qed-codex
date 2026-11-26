---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleDFS.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleDFS.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleDFS.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Attained-signature DFS cardinalities and work

A level is indexed by its attained signatures, not its Boolean assignments or
an ambient rectangular range of raw row values. These finite types describe
visits mathematically; no family or product is materialized by these definitions.
The native encoded-frame traversal is a separate refinement obligation.


### `Prefix`

 Partial tuples indexing invocations of the generator at the next level. 

### `attainedTupleEquiv`

 A complete tuple of emitted representatives is in bijection with the
product of the actual attained full signatures. This records visit-once
semantics without choosing or enumerating independent matrix rows. 

### `prefixCount`

 Number of partial tuples at a specified depth. 

### `card_prefix`

 Exact cardinality of the partial-tuple domain. 

### `prefixCount_le`

 Empty heads contribute one key, so every factor is at least one. 

### `generatorWork`

 One full invocation cost for each earlier emitted partial tuple. The
cost includes reset, unsuccessful predecessor scans, and generator cleanup. 

### `generatorWork_eq_sum_invocations`

 The weighted number of generator invocations is precisely the sum over
all attained-key prefixes, with one invocation at each internal tree node. 

### `generatorWork_le`

 Uniform cost bound for all generator invocations in a DFS. 

### `generatorWork_le_four_pow`

 The extra predecessor rescans square each head's assignment count, but
never take the product of the assignment counts across different heads. 

### `groupRescans_le`

 The work of rescanning each group at each attained tuple. The Boolean
assignment factor is a sum over heads, never a product over heads. 

### `prefixCount_le_rank`

 Preserve the existing rational-rank charge for the attained-key product. 

### `totalWork_le`

 Charge both the generator traversal and a full group rescan at every
complete tuple. `leafCost` includes arithmetic and accumulator updates. 
