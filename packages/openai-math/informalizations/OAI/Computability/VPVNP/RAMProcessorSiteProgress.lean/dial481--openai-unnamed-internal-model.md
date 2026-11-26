---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorSiteProgress.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorSiteProgress.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorSiteProgress.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# State and record accounting between bucket calls

The loop invariant retains the public template parameters and target cut,
the exact native continuation, the unconsumed guess suffix, and the full
list of records already emitted by the physical graph.


### `Progress`

 Relate two call boundaries across a sequence of reports. The reports advance the cut, debit
the site credit and append exactly their timestamped probe records, with the specified
choice suffix. 

### `nativeCall`

 Run one charged call of the instantiated program from the snapshot's persistent state using
its public fuel and remaining global and site credit. 

### `nativeLoop`

 Run the native site loop with the supplied iteration bound, starting at the snapshot's cut
with its site credit and remaining choices. 

### `BoundaryInvariant`

 Type of a predicate on a site snapshot and the chronological word records accumulated at a
call boundary. 

### `LoopRun`

 A complete graph run either reaches its next public label with the
indicated records and exact report stream, or reaches an actual rejecting row. 
