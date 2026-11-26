---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkBundleWalk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkBundleWalk.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkBundleWalk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native sources for dense shrinking visits

Each stage indexes its worker in the block planner. The first ten stages
replay the placement, rank and width reports from the physical shrinking
run, starting in the memory left by the two greedy assignments.


### `Stage`

 The eleven dense bundle worker stages, from preliminary placement and rank preparation to
AB pieces and absolute identifiers. 

### `Stage.index`

 Number a bundle stage from zero for placement to ten for the final absolute-ID pass. 

### `preparationOrder`

 The first ten bundle stages that prepare the sorted widths, both prefix tables and AB
pieces. 

### `order`

 The full bundle-stage sequence, ending with the absolute-ID scan after preparation. 

### `Stage.visit`

 Select the planned catalog visit corresponding to a bundle stage at the specified level and
arena. 

### `Stage.arity`

 Number of public operands required by the local worker for this bundle stage. 

### `Stage.limit`

 Exclusive cursor bound for the stage, determined by its scan over sites, ports, bucket
counts or bundle fields. 

### `Stage.bank`

 The stage-specific public operand words assembled from the input incidence directory,
preliminary placement and rank and width arenas. 

### `Source`

 The checked segment for a worker from the planner, with its physical bank
and one empty choice tape per cursor value. 

### `preparationReports`

 Concatenate the physical reports of the first ten preparation scans in their execution
order through AB piece construction. 

### `preparation_sources`

 All ten deterministic report lists in their native chronological order. 
