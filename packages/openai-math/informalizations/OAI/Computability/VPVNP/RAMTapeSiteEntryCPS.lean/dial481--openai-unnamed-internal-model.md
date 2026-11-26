---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSiteEntryCPS.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteEntryCPS.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteEntryCPS.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The guarded site entry and its continuation

The two successor fields are checked before the global credit is initialized. On a
valid site the choice routine exhausts its unary budget and enters the continuation
once for each permitted bit stream. All such streams leave the same residual clock.


### `prepareEntry`

 Check the successor fields, initialize the global credit word, and generate the bounded
private choice string. 

### `entrySteps`

 Steps for the successor scan and guards, zero-word initialization, and the complete bounded
choice pass. 

### `entrySteps_le`

 Polynomial running time once the public width and bucket fit the physical input. 

### `prepare_count`

 Invalid successor fields reject. Each valid bounded word enters the continuation
on the bank containing that word and with exactly the requested residual fuel. 

### `prepare_allStops`

 The same clock covers all rejecting branches and leaves the same continuation fuel
on every valid branch. 
