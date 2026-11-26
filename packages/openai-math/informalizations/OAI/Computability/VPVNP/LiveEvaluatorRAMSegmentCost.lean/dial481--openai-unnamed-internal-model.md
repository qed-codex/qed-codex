---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorRAMSegmentCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMSegmentCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMSegmentCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native evaluator-group costs in the transcript model

One cost unit pays for each call and one for each external probe. The first
call costs eight units for an accepting carry and ten for a running source.
Each of the two tape scans costs seven units per cell.


### `segmentResources`

 Exact total cost and call count, with a constant clock and probe cap on
every report returned by an accepting native evaluator segment. 

### `segmentWithinCaps`

 The native group lies within the successor-chain caps used in Lemma 10.1. 

### `capPathEquiv`

 Imposing the native transcript caps preserves each accepting branch path. 
