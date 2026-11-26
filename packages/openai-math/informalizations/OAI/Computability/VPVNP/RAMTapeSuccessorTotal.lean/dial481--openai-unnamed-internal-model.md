---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorTotal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorTotal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorTotal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Return and rejection of the successor guard on shared words

The two checked fields decide whether the continuation is reached. On a valid site the
reader takes its exact scan cost and the guard takes two further instructions. One extra
instruction in the all-branch budget lets the explicit rejecting halt execute when the
incoming verdict is false.


### `shared_verdicts_iff`

 The verdict stacks at the end of this physical scan test precisely the two local predicates. 

### `checked_shared_runs`

 On a canonical pair the exact run preserves the typed output stacks for the next pass. 

### `checked_shared_allStops`

 With three guard ticks every malformed pair has stopped. A canonical pair must satisfy
its continuation with the one unused guard tick and the physical output of the scan. 
