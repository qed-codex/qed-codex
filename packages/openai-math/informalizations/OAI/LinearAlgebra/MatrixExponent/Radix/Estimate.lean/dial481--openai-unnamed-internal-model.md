---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Radix/Estimate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Radix/Estimate.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Radix/Estimate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# From wide records to logarithmic-width tagged permutations

If the wide-record threshold at overhead exponent 1/2 is w^A, set
t = 1/A. Use s = floor(w^t) bits per digit and 2^s records per pack.
Each local call has height 2s+3 and each global call has width at
least 2^s. Both calls cost at most O(w^(t/2)) per payload bit. There
are O(w^(1-t)) passes, yielding the exponent 2-t/2.

