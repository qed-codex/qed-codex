---
{
  "module": "OAI/Computability/VPVNP/RAMFinite.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMFinite.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMFinite.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite path counts for burst RAMs

The fuel bound makes the event history of an individual call finite. The
charge for starting a call also bounds the number of calls in an accepting
execution. These two bounds suffice even when the set of private machine
configurations is infinite. Fixing all shared bits leaves an independent
choice of a valid report list at each site.


### `BoundedReports`

 A report list with boundedly many calls, each of which fits its instruction fuel. 

### `localSegment_event_bound`

 Every locally replayed call obeys its own instruction bound. 

### `boundedReports_of_localSegment`

 The cost cap bounds the total number of calls, including calls without probes. 

### `siteWitnessEquiv`

 Pairing a shared assignment with separate local witnesses enforces precisely
all the local checks on the pair. 

### `card_siteWitnesses`

 Counting independent local witnesses after fixing the shared assignment
turns the number of transcripts into a sum of products. 
