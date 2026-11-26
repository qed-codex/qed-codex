---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSitePostLink.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSitePostLink.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSitePostLink.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preserving the physical post-pass inputs through the call controller

The guarded frame retains the literal sorting suffix and two endpoint
records while private calls run. Writing a completed call bank into that
frame replaces the sorting input block by the controller's serialized
output. No machine parameter depends on the record sequence or edge bits.


### `edges`

 Received and sent boundary records decoded from the site’s actual successor scan. 

### `postBank`

 Physical post-pass bank with the completed block, remaining incident bits, and encoded
predecessor and sent records. 

### `PostReady`

 Certificate that the post-pass ports contain the two decoded boundary records and the
required bank before call output is installed. 

### `PostReady.previous`

 Optional predecessor record retained from the guard for the final boundary scan. 

### `PostReady.sent`

 Optional outgoing record retained from the guard for the final boundary scan. 

### `PostReady.ofGuarded`

 The actual guard supplies canonical predecessor words and the untouched
sorting suffix. Sorting scratch is blank at this point. 

### `PostReady.complete`

 At the returned call bank the physical continuation computes the exact
memory predicate on the emitted reports, regardless of sorting success. 
