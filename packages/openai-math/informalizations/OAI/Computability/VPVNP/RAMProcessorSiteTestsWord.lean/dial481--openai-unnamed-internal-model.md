---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorSiteTestsWord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorSiteTestsWord.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorSiteTestsWord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Read-only word comparisons in the outer site processor

The cumulative charge, its bounds, and the incoming or outgoing persistent
state are full-width words. Two operand copies are compared by a fixed table;
a comparison preserves both source words and returns its decision in one bit.


### `WordField`

 Full-width site fields for the bucket bounds, cumulative cost, global cap, persistent state
and the target cut's cost and state. 

### `BitField`

 Flags indicating whether the incoming cut is running, whether a target cut is present and
whether that target is running. 

### `Port`

 Stack ports for decoded site fields, unused choices and verdict bits, together with the
operand and scratch stacks for read-only comparisons. 

### `Snapshot`

 Decoded site data on which entry, iteration and final checks operate, comprising
fixed-width words, status flags and the remaining choices. 

### `Snapshot.words`

 Fixed-width cost, bound and state words indexed by their role in the site checks. 

### `Snapshot.flags`

 Boolean values of the running and target-status fields used to interpret the cut words. 

### `Snapshot.choices`

 Unconsumed private choice stream tested for exact exhaustion when the site closes. 

### `Snapshot.bank`

 Encode each word as its bit string and each flag as a singleton stack, install the choices
and initialize the verdict and comparison scratch stacks to empty. 

### `compare`

 Return one test bit in the left scratch stack. Both source words remain
available, including when they name the same field. 
