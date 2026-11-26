---
{
  "module": "OAI/Computability/VPVNP/RAMBuckets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMBuckets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMBuckets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Partitioning RAM calls by cumulative cost

In Lemma 10.1 of *VP and VNP differ over every field*, the site of a call is
determined by its starting cost. A call costs one plus its number of external
probes. The construction below preserves the full sequence of calls, so calls
with identical costs but different nondeterministic choices remain distinct.


### `cost`

 Cost of a contiguous sequence of calls. 

### `StartsBefore`

 All calls start before the boundary, including a last call that may finish
on or beyond the boundary. 

### `split`

 Split immediately before the first call that starts on or beyond the boundary. 

### `IsSplit`

 The site takes an initial segment. It can stop with work left only after
reaching its boundary. 

### `partition`

 Starting with site `v`, run the successive start-cost cutoffs. Sites after a
halt receive empty lists. 

### `Valid`

 The local cost checks on the successor chain. 

### `existsUnique_partition`

 There is exactly one contiguous grouping into the given number of sites
that recovers the original path and passes the local start/stop cost checks. 

### `StartsBefore.start_lt`

 Inspect the start cost of a specified call after a prefix of its block. 

### `call_site`

 Every call in a valid site block has exactly the site number prescribed by
the floor of its starting cost divided by the bucket size. 

### `next_bucket`

 A permitted call can only stay in its bucket or advance one bucket. 

### `site_cost_lt`

 The last call starts before the upper boundary and costs at most `H`. 

### `probeCount`

 One record is emitted per probe, independently of its kind and value. 

### `records_fit`

 The one initialization record and all probe records fit in the site's block. 

### `partition_block_bounds`

 With both of the paper's caps, the canonical site grouping satisfies the
local cost and record capacity bounds simultaneously. 

### `last_site_at_cap`

 If the final call consumes the entire cap, its start still belongs to
the last site. This applies equally to an accepting final call. 

### `final_unit_iff`

 At the last available unit, starting a call is possible exactly when
there are no subsequent probes in it. 

### `next_call_exceeds_cap`

 A running continuation at the cap cannot start even a probe-free call. 
