---
{
  "module": "OAI/Computability/VPVNP/RAMSortFieldIndex.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortFieldIndex.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortFieldIndex.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sorting stages and the physical exchange fields

In Lemma 10.1 of *VP and VNP differ over every field*, the stride exponent
determines whether a comparison needs an exchange. Every such stage has its
own field at each site, and its addressed record partner is precisely the
site partner designated by that field.


### `crossStageEquiv`

 The physical fields index exactly the stages with stride at least the
site block width. Physical steps increase as the stride decreases. 

### `crossStage_partner`

 The record address in a nonlocal comparator, decoded from its field,
has the same offset at the designated peer site. 

### `sourceSite_eq_physical`

 The sender read during local replay is the peer specified by the physical field. 

### `phases_nodup`

 Phases one through `a` visit each of their stages exactly once. 

### `mem_fullPhases`

 The full physical schedule includes every allowed `(phase, stride)`. 
