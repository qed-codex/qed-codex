---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketTupleProgramRepresentativeSemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketTupleProgramRepresentativeSemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BucketTupleProgramRepresentativeSemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A tuple's physically assembled baseline agrees with each chosen head's
representative on that head when the head masks are disjoint. 

### `assembled_on_head`

 Pointwise disjointness is enough; repeated occurrences of the same head
also preserve its representative, because they write the same value. 

### `representative_on_head`

 The actual output bit at any coordinate in a chosen head equals the first
stored assignment of that head's attained bucket. 

### `assembled_outside`

 Coordinates belonging to no head retain the supplied baseline bit; in the
native finalizer that bit is false from the paid shape-to-zero preparation. 
