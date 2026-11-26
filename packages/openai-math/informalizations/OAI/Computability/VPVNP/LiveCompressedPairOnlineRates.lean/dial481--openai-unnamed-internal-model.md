---
{
  "module": "OAI/Computability/VPVNP/LiveCompressedPairOnlineRates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairOnlineRates.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairOnlineRates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Online report budgets from chronological work bounds

A single length threshold covers every report sequence whose total probes are
linear in the input positions times a fixed power of the binary logarithm,
and whose individual bursts have polylogarithmic length. The estimates apply
directly to the concatenated chronological runs, including repeated visits
to the same abstract level.


### `eventually_online_of_local_rates`

 Total probes take at most one sixty-fourth of the live group, and each
report fits both the burst and private clock with the enclosing link costs. 
