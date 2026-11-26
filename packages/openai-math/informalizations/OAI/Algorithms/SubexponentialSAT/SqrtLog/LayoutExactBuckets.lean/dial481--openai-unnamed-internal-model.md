---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutExactBuckets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutExactBuckets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutExactBuckets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact integer signatures survive every coefficient-ring reduction

The assignments in this module are integer vectors. In the counting
application they are Boolean vectors or differences of Boolean vectors.
Equality of signatures is an equality in `ℤ`, before any reduction.
No claim about the kernel of a matrix reduced modulo a prime is used.


### `value_eq_on_pulled_bucket`

 A concrete copy row remains exactly constant on the pulled-back buckets.
This is literal incidence duplication, with no inverse or field hypothesis. 

### `RationalRowSpan`

 The selected rows rationally span every original integer row. This
condition can be verified over `ℚ`; it is never asserted after reduction. 

### `killsIntegerKernel_of_rational_span`

 Selecting actual independent integer rows is safe for exact integer
buckets in every commutative target ring, including prime-power rings. 
